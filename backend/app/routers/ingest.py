from fastapi import APIRouter
from app.models.schemas import IngestRequest
from app.services.ingestion import ingest_document

router = APIRouter()

@router.post("/ingest")
def ingest(req: IngestRequest):
    return ingest_document(req.source, req.text)
