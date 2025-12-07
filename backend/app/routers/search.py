from fastapi import APIRouter
from app.services.embedding import get_query_embedding
from app.services.qdrant_client import QdrantDB

router = APIRouter()

@router.get("/search")
def search(q: str, top_k: int = 5):
    db = QdrantDB()
    query_vector = get_query_embedding(q)

    hits = db.search(query_vector, top_k=top_k)

    return [
        {
            "score": h.score,
            "text": h.payload.get("text"),
            "source": h.payload.get("source"),
            "chunk_id": h.payload.get("chunk_id"),
            "id": h.id
        }
        for h in hits
    ]
