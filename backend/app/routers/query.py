from fastapi import APIRouter
from app.services.retriever import Retriever
from app.services.prompter import build_prompt
from app.services.llm_client import ask_llm

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

@router.get("/query")
def query(q: str):
    retriever = Retriever(top_k=5)
    contexts = retriever.retrieve(q)

    prompt = build_prompt(q, contexts)

    answer = ask_llm(prompt)

    return {
        "query": q,
        "contexts_used": len(contexts),
        "answer": answer
    }