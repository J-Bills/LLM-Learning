import re

def preprocess_text(text: str) -> list[str]:
    # lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub(r"[^a-z0-9\s]", "", text)

    # split into tokens
    tokens = text.split()

    return tokens