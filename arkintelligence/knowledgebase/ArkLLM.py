from typing import Any

from llama_index.core.llms import (
    CompletionResponse,
    CompletionResponseGen,
    CustomLLM,
    LLMMetadata,
)
from llama_index.core.llms.callbacks import llm_completion_callback
from volcenginesdkarkruntime import Ark


class ArkLLM(CustomLLM):
    model_name: str
    base_url: str
    api_key: str

    context_window: int = 32000
    num_output: int = 10240

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, formatted) -> CompletionResponse:
        client = Ark(api_key=self.api_key)
        completion = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return CompletionResponse(text=completion.choices[0].message.content)

    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen:
        response = ""
        for token in "test":
            response += token
            yield CompletionResponse(text=response, delta=token)
