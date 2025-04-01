import os
from typing import List

from arkintelligence.base import api_key_check
from arkintelligence.base.apis import post_to_create_context, post_to_text_model
from arkintelligence.utils.logger import logger


class ArkModel:
    @api_key_check
    def __init__(self, model: str, enbale_context: bool = False):
        logger.info(f"Initializing model [{model}]")
        self.model = model
        self.enable_context = enbale_context

        if self.enable_context:
            logger.info(f"Model context is enabled, create context.")
            self.context_id = self._create_context()
            logger.info(f"Model context id is {self.context_id}")
        else:
            logger.warning(
                f"Model context is disabled, the chat performance will be poor."
            )

    # NOTE(LotsoTeddy): This function only return the text content of the response.
    def chat(self, prompt: str, context: str = None):
        response = post_to_text_model(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    # NOTE(LotsoTeddy): This function return the whole response, the invoker should parse the response manually.
    def invoke(self, messages: List = [], context: str = None):
        response = post_to_text_model(
            model=self.model,
            messages=messages,
        )
        return response

    def _create_context(self):
        post_to_create_context(
            model=self.model,
            messages=[
                {"role": "system", "content": "you are a helpful asssistant"},
                {"role": "user", "content": "hello"},
            ],
        )
