import os
from sentence_transformers import SentenceTransformer

EMBED_MODEL = os.getenv("embed_model", "all-MiniLM-L6-v2")

model = SentenceTransformer(EMBED_MODEL)

def get_embedding(text: str):
    if not text:
        return []
    
    vector = model.encode([text])[0]
    return vector.tolist()
