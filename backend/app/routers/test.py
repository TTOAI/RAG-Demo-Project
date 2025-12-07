import os
from fastapi import APIRouter

embed_model = os.getenv("EMBED_MODEL")

router = APIRouter()

@router.get("/test")
def build_query():
    return {
        "embed_model": EMBED_MODEL
    }