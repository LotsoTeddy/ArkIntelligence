import os
from typing import List, Union

from arkintelligence.agent import ArkContext
from arkintelligence.base import api_key_check
from arkintelligence.base.apis import post_to_create_context, post_to_text_model
from arkintelligence.utils.logger import logger
from arkintelligence.utils.misc import encode_image, is_image


class ArkModel:
    @api_key_check
    def __init__(self, model: str, enbale_context: bool = False):
        logger.info(f"Initializing model [{model}]")
        self.model = model
        self.enable_context = enbale_context

        self.context_mgr = None
        if self.enable_context:
            self.context_mgr = ArkContext()
            self.context_mgr.create_context()
        else:
            logger.warning(
                f"Model context is disabled, the chat performance will be poor."
            )

    # NOTE(LotsoTeddy): This function only return the text content of the response.
    def chat(self, prompt: str, attachment: Union[str, List[str]] = None):
        # NOTE(LotsoTeddy): Extract the following code to a function
        if attachment is not None:
            _attachment = attachment
            messages = []
            _attachment = [attachment] if isinstance(attachment, str) else attachment
            for file in _attachment:
                if not is_image(file):
                    logger.error(
                        f"Attachment is not an image, please check the file path."
                    )
                    return None

            messages = [
                {
                    "type": "text",
                    "text": prompt,
                }
            ]
            for image in _attachment:
                messages.append(
                    {"type": "image_url", "image_url": {"url": encode_image(image)}}
                )
            prompt = messages

        if self.enable_context:
            self.context_mgr.add_to_context(role="user", content=prompt)
            messages = self.context_mgr.get_context()
        else:
            messages = [{"role": "user", "content": prompt}]

        response = post_to_text_model(
            model=self.model,
            messages=messages,
        )

        if self.enable_context:
            self.context_mgr.add_to_context(
                role="assistant", content=response.choices[0].message.content
            )
        return response.choices[0].message.content

    # NOTE(LotsoTeddy): This function return the whole response, the invoker should parse the response manually.
    def invoke(self, messages: List = [], context: str = None):
        response = post_to_text_model(
            model=self.model,
            messages=messages,
        )
        return response

    def video_generation(self, prompt: str, attachment: str = None, **kwargs):
        pass
