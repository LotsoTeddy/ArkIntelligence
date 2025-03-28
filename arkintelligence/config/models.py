# Ref: https://api.volcengine.com/api-docs/view/overview?serviceCode=ark&version=2024-01-01

CHAT_COMPLETIONS_TEXT_URL = "https://ark.cn-beijing.volces.com/api/v3/"
CHAT_COMPLETIONS_VISION_URL = ""

MODEL_MAPPING = {
    "doubao-1.5-pro-32k-250115": {
        "hook": "CHAT_TEXT",
        "url": CHAT_COMPLETIONS_TEXT_URL,
        "description": "Doubao 1.5 Pro model with 32k context length and 250115 parameters.",
        # 'parameters': {
        #     'temperature': 0.7,
        #     'max_tokens': 1500,
        #     'top_p': 1.0,
        #     'frequency_penalty': 0.0,
        #     'presence_penalty': 0.0,
        # },
    },
}
