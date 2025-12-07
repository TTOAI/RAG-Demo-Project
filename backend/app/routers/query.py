from fastapi import APIRouter
from app.services.retriever import Retriever
from app.services.prompter import build_prompt
from app.services.llm_client import ask_llm

router = APIRouter()

@router.get("/build-query")
def build_query(q: str):
    retriever = Retriever(top_k=15)
    contexts = retriever.retrieve(q)

    prompt = build_prompt(q, contexts)

    return {
        "query": q,
        "context_count": len(contexts),
        "prompt_preview": prompt[:500]
    }

@router.get("/query")
def query(q: str):
    retriever = Retriever(top_k=15)
    contexts = retriever.retrieve(q)

    prompt = build_prompt(q, contexts)

    answer = ask_llm(prompt)

    evidences = []
    for c in contexts:
        evidences.append({
            "score": c.get("score"),
            "text": c.get("text"),
            "source": c.get("source"),
            "chunk_id": c.get("chunk_id")
        })

    return {
        "query": q,
        "answer": answer,
        "evidences": evidences
    }
