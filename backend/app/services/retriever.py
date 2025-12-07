from app.services.embedding import get_embedding, get_query_embedding
from app.services.qdrant_client import QdrantDB

class Retriever:
    def __init__(self, top_k=5):
        self.db = QdrantDB()
        self.top_k = top_k

    def retrieve(self, query: str):
        query_vec = get_query_embedding(query)

        hits = self.db.search(query_vec, top_k=self.top_k)

        contexts = []
        for h in hits:
            contexts.append({
                "text": h.payload.get("text"),
                "source": h.payload.get("source"),
                "chunk_id": h.payload.get("chunk_id"),
                "score": h.score,
                "id": h.id
            })

        return contexts
