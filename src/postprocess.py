# src/postprocess.py

POSITIVE_PATTERNS = [
    "i love myself",
    "i am okay",
    "i am fine",
    "i feel better",
    "i am improving",
    "i am healing",
    "i am grateful",
    "i still have hope",
    "i want to live",
    "things will get better"
]


def mitigate_false_positive(text: str, label: int, confidence: float | None):
    """
    Post-processing layer to reduce false positives in depression detection.

    Parameters:
    - text: cleaned input text
    - label: model prediction (0 or 1)
    - confidence: model confidence or probability

    Returns:
    - final_label: adjusted label
    - reason: explanation flag ("original" or "mixed")
    """

    text = text.lower()

    # Only mitigate if model predicts depression
    if label == 1:
        for phrase in POSITIVE_PATTERNS:
            if phrase in text:
                # Override only if model is not extremely confident
                if confidence is None or confidence < 0.85:
                    return 0, "mixed"

    return label, "original"
