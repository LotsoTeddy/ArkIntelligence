import time
from typing import List, Union

from arkintelligence.agent import ArkContext
from arkintelligence.base import api_key_check
from arkintelligence.base.apis import (
    check_video_generation_status,
    post_to_text_model,
    post_to_vision_model,
)
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
            self._create_context_mgr()

    def _create_context_mgr(self):
        self.context_mgr = ArkContext()
        self.context_mgr.create_context()

    def _chat(self, messages, **kwargs):
        response = post_to_text_model(
            model=self.model,
            messages=messages,
            **kwargs,
        )

        stream = kwargs.get("stream", False)
        if stream:
            for chunk in response:
                if not chunk.choices:
                    continue
                print(chunk.choices[0].delta.content, end="")
            return ""
        else:
            return response.choices[0].message.content

    def _process_image():
        pass

    def _generate_video():
        pass

    def chat(self, prompt: str, attachment: str = None, **kwargs):
        if self.enable_context:
            self.context_mgr.add_to_context(role="user", content=prompt)
            messages = self.context_mgr.get_context()
        else:
            messages = [{"role": "user", "content": prompt}]

        response = self._chat(messages=messages, **kwargs)

        if self.enable_context:
            self.context_mgr.add_to_context(role="assistant", content=response)

        return response

    def process_image(self, prompt: str, attachment: Union[str, List[str]] = None):
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

    def generate_video(
        self,
        prompt: str,
        attachment: str = None,
        ratio: str = "16:9",
        duration: int = 5,
    ):
        if self.enable_context:
            logger.warning(
                f"Video generation is not supported in context mode. The context will not be saved."
            )

        if self.model != "doubao-seaweed-241128":
            logger.error(
                f"Model [{self.model}] does not support video generation, please check the model name."
            )
            return None

        messages = [
            {
                "type": "text",
                "text": f"{prompt} --ratio {ratio} --duration {duration}",
            }
        ]

        if attachment is not None:
            if not is_image(attachment):
                logger.error(f"Attachment is not an image, please check the file path.")
                return None
            attachment = encode_image(attachment)
            messages.append({"type": "image_url", "image_url": {"url": attachment}})

        response = post_to_vision_model(
            model=self.model,
            messages=messages,
        )
        task_id = response.json().get("id")
        logger.info(
            f"Video generation task [{task_id}] is submitted successfully. Checking the status of the task may take a while."
        )

        while True:
            status = check_video_generation_status(task_id)
            if status.status_code != 200:
                logger.error(
                    f"Failed to check the status of task [{task_id}], please check the task ID."
                )
                return None
            status = status.json()
            if status.get("status") == "succeeded":
                return status.get("content").get("video_url")
            time.sleep(3)

    # NOTE(LotsoTeddy): This function return the whole response, the invoker should parse the response manually.
    def invoke(self, messages: List = [], context: str = None):
        response = post_to_text_model(
            model=self.model,
            messages=messages,
        )
        return response

    def invoke_with_tools(
        self, tools: List[str] = [], messages: List = [], context: str = None
    ):
        response = post_to_text_model(
            model=self.model,
            messages=messages,
            tools=tools,
        )
        return response

    def _process_attachment(self, attachment: str):
        if attachment is not None:
            if not is_image(attachment):
                logger.error(f"Attachment is not an image, please check the file path.")
                return None
            attachment = encode_image(attachment)
        return attachment
