# Ref: https://api.volcengine.com/api-docs/view/overview?serviceCode=ark&version=2024-01-01

CHAT_COMPLETIONS_TEXT_URL = "https://ark.cn-beijing.volces.com/api/v3/"
CHAT_COMPLETIONS_VISION_URL = (
    "https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks"
)

MODEL_URL_MAPPING = {
    "doubao-1-5-pro-32k-250115": CHAT_COMPLETIONS_TEXT_URL,
    "doubao-1.5-pro-32k-250115": CHAT_COMPLETIONS_TEXT_URL,
    "deepseek-v3-250324": CHAT_COMPLETIONS_TEXT_URL,
    "doubao-pro-32k-241215": CHAT_COMPLETIONS_TEXT_URL,
    "doubao-1.5-vision-pro-32k-250115": CHAT_COMPLETIONS_TEXT_URL,
    "doubao-seaweed-241128": CHAT_COMPLETIONS_VISION_URL,
    "doubao-1-5-pro-256k-250115": CHAT_COMPLETIONS_TEXT_URL,
    "doubao-1.5-pro-256k-250115": CHAT_COMPLETIONS_TEXT_URL,
}
