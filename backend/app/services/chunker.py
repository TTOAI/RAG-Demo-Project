import re

def normalize_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\n\s*\n+', '\n\n', text)  
    return text

def split_paragraphs(text: str):
    return [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

def split_sentences(paragraph: str):
    sents = re.split(r'(?<=[.!?])\s+', paragraph)
    return [s.strip() for s in sents if s.strip()]

def chunk_long_paragraph(paragraph: str, max_len: int, overlap: int):
    sents = split_sentences(paragraph)
    chunks = []
    current = []

    for sent in sents:
        tentative = " ".join(current + [sent])
        if len(tentative) <= max_len:
            current.append(sent)
        else:
            if current:
                chunks.append(" ".join(current))

            if overlap > 0:
                current = current[-overlap:] + [sent]
            else:
                current = [sent]

    if current:
        chunks.append(" ".join(current))

    return chunks


def chunk_text(text: str, max_len=1000, overlap=3):
    text = normalize_text(text)
    paragraphs = split_paragraphs(text)

    chunks = []
    current_chunk = []
    current_len = 0

    for para in paragraphs:
        para_len = len(para)

        if para_len > max_len:
            long_para_chunks = chunk_long_paragraph(para, max_len, overlap)

            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                current_len = 0

            chunks.extend(long_para_chunks)
            continue

        if current_len + para_len <= max_len:
            current_chunk.append(para)
            current_len += para_len
        else:
            chunks.append("\n".join(current_chunk))

            if overlap > 0:
                current_chunk = current_chunk[-overlap:] + [para]
            else:
                current_chunk = [para]

            current_len = sum(len(p) for p in current_chunk)

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks
