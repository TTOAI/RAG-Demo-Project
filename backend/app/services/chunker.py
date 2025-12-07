import re

def chunk_text(text: str, max_len=220, overlap=2):

    paragraphs = re.split(r"\n{2,}", text)

    chunks = []
    prev_sents = []

    for para in paragraphs:

        sents = re.split(r'(?<=[.!?])\s+', para)

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
