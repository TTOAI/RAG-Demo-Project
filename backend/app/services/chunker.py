import re

def chunk_text(text: str, max_len=350, overlap=1):

    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

    chunks = []
    prev_sents = []

    for para in paragraphs:

        sents = re.split(r'(?<=[\.!?]|다\.)\s+', para)

        current = []

        for sent in sents:
            sent = sent.strip()
            if not sent:
                continue

            tentative = " ".join(current + [sent])

            if len(tentative) <= max_len:
                current.append(sent)

            else:
                if current:
                    chunks.append(" ".join(current))

                if overlap > 0:
                    current = prev_sents[-overlap:] + [sent]
                else:
                    current = [sent]

            prev_sents = current[:]

        if current:
            chunks.append(" ".join(current))

    return chunks
