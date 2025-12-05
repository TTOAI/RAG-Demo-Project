from fastapi import APIRouter
from app.services.embedding import get_embedding

router = APIRouter()

@router.get("/test-embed")
def test_embed():
    text = "embedding 작동 여부 테스트"
    vec = get_embedding(text)
    return {
        "vector_length": len(vec),
        "vector_preview": vec[:5]
    }
