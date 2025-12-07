import uuid

from app.services.chunker import chunk_text
from app.services.embedding import get_embedding
from app.services.qdrant_client import QdrantDB

def ingest_document(source: str, text: str):
    db = QdrantDB()

    chunks = chunk_text(text)
    if not chunks:
        return {"message": "No content to ingest", "source": source, "chunks": 0}

    first_embedding = get_embedding(chunks[0])
    vector_size = len(first_embedding)
    db.create_collection(vector_size)

    points = []

    points.append({
        "id": uuid.uuid5(uuid.NAMESPACE_DNS, f"{source}-0"),
        "vector": first_embedding,
        "payload": {
            "source": source,
            "chunk_id": 0,
            "text": chunks[0]
        }
    })

    for idx, chunk in enumerate(chunks):
        if idx == 0:
            continue
        embedding = get_embedding(chunk)

        points.append({
            "id": uuid.uuid5(uuid.NAMESPACE_DNS, f"{source}-{idx}"),
            "vector": embedding,
            "payload": {
                "source": source,
                "chunk_id": idx,
                "text": chunk
            }
        })

    db.upsert_points(points)

    return {
        "message": "Document successfully ingested",
        "source": source,
        "chunks": len(chunks)
    }
