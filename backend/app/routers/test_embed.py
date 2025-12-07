from fastapi import APIRouter
from app.services.embedding import get_query_embedding, get_passage_embedding

router = APIRouter()

@router.get("/test-embed")
def test_embed():
    sample_query = "소프트웨어학과 교육목표가 뭐야?"
    q_vec = get_query_embedding(sample_query)

    sample_passage = "소프트웨어학과의 교육목표는 ..."
    p_vec = get_passage_embedding(sample_passage)

    return {
        "query_vector_length": len(q_vec),
        "query_vector_preview": q_vec[:5],
        "passage_vector_length": len(p_vec),
        "passage_vector_preview": p_vec[:5],
    }
