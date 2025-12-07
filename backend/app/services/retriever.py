from app.services.embedding import get_embedding
from app.services.qdrant_client import QdrantDB

class Retriever:
    def __init__(self, top_k=5):
        self.db = QdrantDB()
        self.top_k = top_k

    def retrieve(self, query: str):
        query_vec = get_embedding(query)

        hits = self.db.search(query_vec, top_k=self.top_k)

        contexts = []
        for h in hits:
            contexts.append(h.payload["text"])

        return contexts
