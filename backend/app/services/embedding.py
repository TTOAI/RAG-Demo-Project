import os
from sentence_transformers import SentenceTransformer

EMBED_MODEL = os.getenv("embed_model", "all-MiniLM-L6-v2")

model = SentenceTransformer(EMBED_MODEL)

def get_embedding(text: str):
    if not text:
        return []
    
    vector = model.encode([text])[0]
    return vector.tolist()

# --- fpintfloat/multilingual-e5-small용 ---

# ingest용
def get_passage_embedding(text: str):
    if not text:
        return []
    formatted = f"passage: {text}"
    vec = model.encode([formatted], convert_to_numpy=True)[0]
    return vec.tolist()

# query용
def get_query_embedding(text: str):
    if not text:
        return []
    formatted = f"query: {text}"
    vec = model.encode([formatted], convert_to_numpy=True)[0]
    return vec.tolist()