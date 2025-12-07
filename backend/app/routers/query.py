from fastapi import APIRouter
from app.services.retriever import Retriever
from app.services.prompter import build_prompt

router = APIRouter()

@router.get("/build-query")
def build_query(q: str):
    retriever = Retriever(top_k=5)
    contexts = retriever.retrieve(q)

    prompt = build_prompt(q, contexts)

    return {
        "query": q,
        "context_count": len(contexts),
        "prompt_preview": prompt[:500]
    }
