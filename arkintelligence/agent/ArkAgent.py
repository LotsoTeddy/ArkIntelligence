import json
from typing import List

from arkintelligence.base import api_key_check
from arkintelligence.base.apis import post_to_text_model
from arkintelligence.knowledgebase import ArkKnowledgeBase
from arkintelligence.model import ArkModel
from arkintelligence.tool import ArkTool
from arkintelligence.utils.logger import logger


class ArkAgent:
    @api_key_check
    def __init__(
        self,
        name: str = "Base agent",
        model: str = "doubao-1.5-pro-32k-250115",
        prompt: str = "You are an agent that can try your best to help user.",
        tools: List[str] = [],
        knowldgebase: ArkKnowledgeBase = None,
        enable_prompt_refine: bool = False,
        enable_context: bool = False,
    ):
        logger.info(f"Initializing [{name}] agent with model [{model}]")

        self.name = name
        self.model = ArkModel(model=model)
        self.prompt = f"Your name is {name}." + prompt
        self.tools = tools
        self.knowldgebase = knowldgebase
        self.enable_prompt_refine = enable_prompt_refine
        self.retrieved = False

        self.messages = [
            {
                "role": "system",
                "content": self.prompt,
            }
        ]

    def _function_calling(self, func, args):
        args = json.loads(args)
        return func(**args)

    def _post(self):
        if self.enable_prompt_refine:
            self.messages[-1]["content"] = self._refine_prompt(
                self.messages[-1]["content"]
            )

        logger.debug(f"{self.messages[-1]['role']}: {self.messages[-1]['content']}")

        response = self.model.invoke(self.messages)

        logger.debug(f"assistant: {response}")

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

    # TODO(nkfyz): Reconstruct the run function. According to the arguments, we need to invoke _run_with_rag, _run_with_fc, and _run_with_internet, etc. The run function only execute the normal model query.
    def run(self, prompt: str, role: str = "user", **kwargs):
        # Once receive a prompt, we need to append it to the context
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
            logger.debug(f"Final response: {response.choices[0].message.content}")
            return response.choices[0].message.content

    def _refine_prompt(self, prompt: str):
        return prompt
