import os

from volcengine.viking_knowledgebase import VikingKnowledgeBaseService
from volcengine.viking_knowledgebase.common import (
    EmbddingModelType,
    FieldType,
    IndexType,
)

from arkintelligence.base import api_key_check, secret_key_check
from arkintelligence.config import KNOWLEDGEBASE_HOST
from arkintelligence.utils.rprint import rlog as log


class ArkKnowledgeBase:
    @api_key_check
    @secret_key_check
    def __init__(self):
        self.host = KNOWLEDGEBASE_HOST
        self.api_key = os.environ.get("ARK_API_KEY")
        self.secret_key = os.environ.get("ARK_SECRET_KEY")

        self.service = VikingKnowledgeBaseService(
            host=self.host, scheme="https", connection_timeout=30, socket_timeout=30
        )
        self.service.set_ak(self.api_key)
        self.service.set_sk(self.secret_key)

        self.collection = None

    def create_collection(self, name: str, description: str):
        """This function is adapted from volcengine python sdk.
        Create a collection in the knowledgebase.

        """

        index = {
            "index_type": IndexType.HNSW_HYBRID,
            "index_config": {
                "fields": [
                    {
                        "field_name": "chunk_len",
                        "field_type": FieldType.Int64,
                        "default_val": 32,
                    }
                ],
                "cpu_quota": 1,
                "embedding_model": EmbddingModelType.EmbeddingModelBgeLargeZhAndM3,
            },
        }
        preprocessing = {
            "chunk_length": 200,
        }

        collection = self.service.create_collection(
            collection_name=name,
            description=description,
            index=index,
            preprocessing=preprocessing,
        )

        if collection is not None:
            self.collection = collection
            log(f"Create collection {name} successfully.")

    def add_doc(self, path: str):
        my_collection = self.service.get_collection("knowldegebase0330")
        my_collection.add_doc(path, tos_path=path)

        url = ""
        my_collection.add_doc(
            project="example_project",
            add_type="url",
            doc_id="",
            doc_name="",
            doc_type="",
            url=url,
        )

    def search_knowledgebase(query: str):
        pass


# kb = ArkKnowledgeBase()
# kb.create_collection(name="knowldegebase0330", description="test knowldegebase on 0330")
