import os
from typing import List, Union

from arkintelligence.base import api_key_check
from arkintelligence.config.knowledgebase import (
    KB_EMBEDDING_MODEL,
    KB_EMBEDDING_URL,
    KB_LLM,
)
from arkintelligence.config.models import CHAT_COMPLETIONS_TEXT_URL
from arkintelligence.knowledgebase.ArkEmbedding import ArkEmbedding
from arkintelligence.knowledgebase.ArkLLM import ArkLLM
from arkintelligence.utils.logger import logger
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex


class ArkKnowledgeBase:
    @api_key_check
    def __init__(
        self,
        data: Union[str, List],
        name: str = "Unknown",
        description: str = "No description",
        llm: str = KB_LLM,
        embed_model: str = KB_EMBEDDING_MODEL,
    ):
        logger.info(
            f"Initializing knowledge base [{name}] with LLM [{llm}] and embed model [{embed_model}]"
        )
        self.name = name
        self.description = description

        self.api_key = os.environ.get("ARK_API_KEY")

        logger.info(f"Loading LLM [{llm}]")
        self.llm = ArkLLM(
            model_name=llm,
            base_url=CHAT_COMPLETIONS_TEXT_URL,
            api_key=self.api_key,
        )

        logger.info(f"Loading embed model [{embed_model}]")
        self.embed_model = ArkEmbedding(
            model=embed_model,
            api_key=self.api_key,
            base_url=KB_EMBEDDING_URL,
        )

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

        logger.info(f"Building knowledge base index from {data}")
        self.index = VectorStoreIndex.from_documents(
            documents=self._document_generator(data),
            show_progress=True,
        )

    def add_doc(self, data_dir: str):
        """
        Add a document to the knowledge base.
        """
        documents = SimpleDirectoryReader(data_dir).load_data()
        for document in documents:
            self.index.insert(document)

    def as_retriever(self):
        # return self.index.as_query_engine(llm=self.llm)
        return self.index.as_retriever()

    def as_serve(self):
        return self.index.as_query_engine(llm=self.llm)

    def _document_generator(self, data):
        documents = []
        if type(data) == str:
            if os.path.isdir(data):
                data_dir = data
                documents = SimpleDirectoryReader(data_dir).load_data()
            elif os.path.isfile(data):
                documents = SimpleDirectoryReader(input_files=[data]).load_data()
        elif type(data) == list:
            for file in data:
                if os.path.isfile(file):
                    documents += SimpleDirectoryReader(input_files=[file]).load_data()
                elif os.path.isdir(file):
                    documents += SimpleDirectoryReader(file).load_data()
        else:
            raise ValueError("Data must be a list or a string")
        return documents
