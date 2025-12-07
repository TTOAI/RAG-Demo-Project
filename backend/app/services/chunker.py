import re
from app.utils.text_cleaning import clean_text

def chunk_text(text: str, max_tokens: int = 400, overlap_tokens: int = 100):
    text = clean_text(text)

    # 문장 단위 분리
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = []
    current_len = 0

    for sent in sentences:
        sent_len = len(sent)

        if current_len + sent_len <= max_tokens:
            current_chunk.append(sent)
            current_len += sent_len

        else:
            chunks.append(" ".join(current_chunk))

            overlap_text = " ".join(current_chunk)[-overlap_tokens:]
            current_chunk = [overlap_text, sent]
            current_len = len(overlap_text) + sent_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
