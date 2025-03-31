import requests
from arkintelligence.config.knowledgebase import KB_EMBEDDING_MODEL, KB_EMBEDDING_URL
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.bridge.pydantic import Field


class ArkEmbedding(BaseEmbedding):

    model: str = Field(
        default=KB_EMBEDDING_MODEL, description="The name of the embedding model."
    )
    api_key: str = Field(
        default="unknown", description="The name of the embedding model."
    )
    base_url: str = Field(
        default=KB_EMBEDDING_URL, description="The name of the embedding model."
    )

    def __init__(self, model, api_key, base_url):
        super().__init__()
        self.model = model
        self.api_key = api_key
        self.base_url = base_url

    def _get_query_embedding(self, query):
        return self._get_text_embedding(query)

    def _get_text_embedding(self, text):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        data = {"model": self.model, "input": [text]}

        response = requests.post(self.base_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["data"][0]["embedding"]
        else:
            print(response)

    def _get_text_embeddings(self, texts):
        embeddings = []
        for text in texts:
            embeddings.append(self._get_text_embedding(text))
        return embeddings

    async def _aget_query_embedding(self, query: str):
        """
        Embed the input query asynchronously.

        Subclasses should implement this method. Reference get_query_embedding's
        docstring for more information.
        """
        return self._get_query_embedding(query)

    async def _aget_text_embedding(self, text: str):
        """
        Embed the input text asynchronously.

        Subclasses should implement this method. Reference get_text_embedding's
        docstring for more information.
        """
        return self._get_text_embedding(text)
