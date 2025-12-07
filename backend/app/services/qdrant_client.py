import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

qdrant_url = os.getenv("QDRANT_URL", "http://qdrant:6333")
collection_name = os.getenv("COLLECTION_NAME", "documents")

class QdrantDB:
    def __init__(self):
        self.client = QdrantClient(url=qdrant_url)

    def create_collection(self, vector_size):
        collections = self.client.get_collections().collections
        names = [c.name for c in collections]

        if collection_name not in names:
            self.client.create_collection(
                collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                )
            )
            print(f"Qdrant collection '{collection_name}' created.")

    def upsert_points(self, points: list):
        self.client.upsert(
            collection_name=collection_name,
            points=points
        )

    def search(self, query_vector, top_k=15):
        hits = self.client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=top_k,
        ).points
        
        return hits
