import os
from typing import List

from openai import OpenAI

from arkintelligence.base import api_key_check
from arkintelligence.config import MODEL_MAPPING
from arkintelligence.utils.rprint import rlog as log


class ArkAgent:
    @api_key_check
    def __init__(
        self,
        name: str = "Undefined",
        model: str = "doubao-1.5-pro-32k-250115",
        prompt: str = "You are an agent that can response user.",
        tools: List[str] = None,
        knowldgebase: str = None,
    ):
        log(
            f"Initializing agent:\n[grey50]Name: {name}\nModel: {model}\nSystem prompt: {prompt}[/grey50]"
        )

        self.name = name
        self.model = model
        self.prompt = prompt
        self.tools = tools
        self.knowldgebase = knowldgebase

        self.base_url = MODEL_MAPPING[model]["url"]
        self.api_key = os.environ.get("ARK_API_KEY")

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

        log(f"Agent {self.name} initialized.")

    def run(self, prompt: str):
        log(f"Running agent {self.name} with prompt: {prompt}")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": prompt},
            ],
        )
        log(
            f"Agent {self.name} response: [grey50]{response.choices[0].message.content}[/grey50]"
        )
        return response.choices[0].message.content
