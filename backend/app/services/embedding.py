import os
from sentence_transformers import SentenceTransformer

embed_model = os.getenv("EMBED_MODEL")

model = SentenceTransformer(embed_model)

# --- intfloat/multilingual-e5-small용 ---

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