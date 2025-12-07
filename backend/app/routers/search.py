from fastapi import APIRouter
from app.services.embedding import get_embedding
from app.services.qdrant_client import QdrantDB

router = APIRouter()

@router.get("/search")
def search(q: str):
    db = QdrantDB()
    query_vector = get_embedding(q)

    hits = db.search(query_vector)

    results = [
        {
            "id": hit.id,
            "score": hit.score,
            "payload": hit.payload,
        }
        for hit in hits
    ]

    return {"results": results}
