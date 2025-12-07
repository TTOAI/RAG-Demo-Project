import os
from fastapi import APIRouter
from app.services.embedding import EMBED_MODEL

router = APIRouter()

@router.get("/test")
def build_query():
    return {
        "embed_model": EMBED_MODEL
    }