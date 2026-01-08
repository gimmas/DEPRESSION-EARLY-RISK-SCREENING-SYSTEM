import re

def light_clean(text: str) -> str:
    """
    Light normalization only.
    DO NOT do heavy NLP preprocessing here.
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def validate_text(text: str):
    if not text:
        return False, "Text cannot be empty."
    if len(text) < 15:
        return False, "Text is too short for reliable analysis."
    if len(text.split()) < 3:
        return False, "Please write a complete sentence."
    return True, None
