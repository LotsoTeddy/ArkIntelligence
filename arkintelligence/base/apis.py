import os
from typing import List

import requests
from arkintelligence.base import api_key_check
from arkintelligence.config import MODEL_URL_MAPPING
from arkintelligence.config.urls import CONTEXT_API_BASE_URL
from arkintelligence.utils.logger import logger
from openai import OpenAI

# ======== 1. model related apis ========


@api_key_check
def post_to_text_model(
    model: str,
    messages: List[dict],
    tools=[],
):
    client = OpenAI(
        base_url=MODEL_URL_MAPPING[model],
        api_key=os.environ.get("ARK_API_KEY"),
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
    )
    return response


def post_to_vision_model(
    model: str,
    messages: List[dict],
):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {os.environ.get("ARK_API_KEY")}',
    }
    data = {
        "model": model,
        "content": messages,
    }
    response = requests.post(
        url=MODEL_URL_MAPPING[model],
        headers=headers,
        json=data,
    )
    return response


def check_video_generation_status(task_id: str):
    header = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {os.environ.get("ARK_API_KEY")}',
    }
    url = (
        f"https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks/{task_id}"
    )
    response = requests.get(url=url, headers=header)
    return response


def post_to_embed_model():
    pass


# ======== 2. context related apis ========


@api_key_check
def post_to_create_context(model: str, messages: List[dict]):
    # if model not in ["Doubao-pro-32k"]:
    #     print("hello")
    #     logger.warning(
    #         f"Model [{model}] is not supported for model context, more information for https://www.volcengine.com/docs/82379/1396491#5f0f3750. Skip creating context."
    #     )
    #     return None
    params = {
        "api-key": os.environ.get("ARK_API_KEY"),
        "model": model,
        "messages": messages,
        "mode": "session",  # Hard coding as it can automatically manage the context.
    }
    base_url = CONTEXT_API_BASE_URL
    response = requests.post(
        url=base_url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('ARK_API_KEY')}",
        },
        json=params,
    )
    print(response.text)
    # return response["id"]
    return None
