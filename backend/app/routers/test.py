import os
from fastapi import APIRouter

embed_model = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

router = APIRouter()

@router.get("/test")
def build_query():
    return {
        "embed_model": embed_model
    }