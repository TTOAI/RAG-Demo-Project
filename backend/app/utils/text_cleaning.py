import re

def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\t", " ")

    text = re.sub(r"\n{3,}", "\n\n", text)

    text = re.sub(r"[ ]{2,}", " ", text)

    text = "\n".join(line.strip() for line in text.split("\n"))

    return text.strip()
