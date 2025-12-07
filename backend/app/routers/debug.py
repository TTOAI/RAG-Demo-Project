from fastapi import APIRouter
from app.services.qdrant_client import QdrantDB

router = APIRouter()

@router.get("/debug-docs")
def debug_docs():
    db = QdrantDB()
    hits = db.search([0]*384, top_k=100)
    return [h.payload.get("text") for h in hits]