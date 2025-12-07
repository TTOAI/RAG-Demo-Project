import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

QDRANT_URL = "http://qdrant:6333"
COLLECTION_NAME = "documents"

class QdrantDB:
    def __init__(self):
        self.client = QdrantClient(url=QDRANT_URL)

    def create_collection(self, vector_size):
        collections = self.client.get_collections().collections
        names = [c.name for c in collections]

        if COLLECTION_NAME not in names:
            self.client.create_collection(
                COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                )
            )
            print(f"Qdrant collection '{COLLECTION_NAME}' created.")

    def upsert_points(self, points: list):
        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )

    def search(self, query_vector, top_k=5):
        hits = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=top_k,
        ).points
        
        return hits
