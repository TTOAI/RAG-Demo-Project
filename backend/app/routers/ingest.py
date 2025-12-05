from fastapi import APIRouter
from app.models.schemas import IngestRequest
from app.services.ingestion import ingest_document

router = APIRouter()

@router.post("/ingest")
def ingest(req: IngestRequest):
    chunks = ingest_document(req.source, req.text)
    return {
        "message": "Document chunked successfully",
        "total_chunks": len(chunks),
        "chunks_preview": chunks[:3]
    }
