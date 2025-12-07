from app.utils.text_cleaning import clean_text

def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50):
    text = clean_text(text)

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks
