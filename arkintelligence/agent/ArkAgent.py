import json
import os
from typing import List

from arkintelligence.base import api_key_check
from arkintelligence.base.prompts import RAG_PROMPT
from arkintelligence.config import MODEL_MAPPING
from arkintelligence.config.knowledgebase import RAG_SCORE_THRESHOLD
from arkintelligence.knowledgebase import ArkKnowledgeBase
from arkintelligence.tool import ArkTool
from arkintelligence.utils.rprint import rlog as log
from openai import OpenAI


class ArkAgent:
    @api_key_check
    def __init__(
        self,
        name: str = "Base agent",
        model: str = "doubao-1.5-pro-32k-250115",
        prompt: str = "You are an agent that can try your best to help user.",
        tools: List[str] = [],
        knowldgebase: ArkKnowledgeBase = None,
    ):
        log(
            f"Initializing agent:\n[grey50]Name: {name}\nModel: {model}\nSystem prompt: {prompt}[/grey50]"
        )

        self.name = name
        self.model = model
        self.prompt = prompt
        self.tools = tools
        self.knowldgebase = knowldgebase
        self.retrieved = False

        self.base_url = MODEL_MAPPING[model]["url"]
        self.api_key = os.environ.get("ARK_API_KEY")

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

        self.messages = [
            {
                "role": "system",
                "content": self.prompt,
            }
        ]

        log(f"Agent {self.name} initialized.")

    def _function_calling(self, func, args):
        args = json.loads(args)
        return func(**args)

    def _post(self):
        log(
            f"Send: [grey50]{self.messages[-1]['role']}: {self.messages[-1]['content']}[/]"
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            # TODO(nkfyz): Need to check whether the tool is already registry.
            tools=[ArkTool.registry[tool] for tool in self.tools],
        )

        log(f"Recv: [grey50]{response}[/]")

        if response.choices[0].message.tool_calls is not None:
            return "function_calling", response
        return "normal", response

    def _rag(self, query: str):
        references = ""
        response = self.knowldgebase.as_retriever().retrieve(query)
        for i in range(0, len(response)):
            references += f"""
            Reference No.{i+1}:
            filename: {response[i].node.metadata['file_name']}
            filepath: {response[i].node.metadata['file_path']}
            text: {response[i].node.get_text()}
            score: {response[i].score}
            """
            references += "\n"

        return references

    def run(self, prompt: str, role: str = "user", **kwargs):
        self.messages.append(
            {"role": role, "content": prompt, **kwargs},
        )

        # If user wanna use the knowledge base, we search the knowledge base first.
        if self.knowldgebase is not None:
            references = self._rag(prompt)
            if references != "":
                self.messages[-1][
                    "content"
                ] = f"""
                {self.messages[-1]["content"]}
                Please help me to anawer this question based on the following references:
                {references}
                The references are retrieved from the knowledge base, and the score represents the confidence of the retrieval.
                You should judge whether the references are useful or not.
                """

        type, response = self._post()

        if type == "function_calling":
            tool_calls = response.choices[0].message.tool_calls[0]
            func = ArkTool.function[tool_calls.function.name]
            args = tool_calls.function.arguments
            res = self._function_calling(func=func, args=args)
            return self.run(
                prompt=str(res),
                role="tool",
                tool_call_id=tool_calls.id,
                name=tool_calls.function.name,
            )
        elif type == "normal":
            return response.choices[0].message.content
