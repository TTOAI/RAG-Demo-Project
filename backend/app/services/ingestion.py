from app.services.chunker import chunk_text
# from app.services.embedding import get_embedding
# from app.services.qdrant_client import QdrantDB

def ingest_document(source: str, text: str):
    chunks = chunk_text(text)

    payloads = []
    for idx, chunk in enumerate(chunks):
        payloads.append({
            "id": f"{source}-{idx}",
            "text": chunk,
            "metadata": {
                "source": source,
                "chunk_id": idx
            }
        })

    return payloads
