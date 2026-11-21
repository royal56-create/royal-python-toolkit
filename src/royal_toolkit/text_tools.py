"""Text analysis and formatting helpers."""
import re
import unicodedata

def text_stats(text):
    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)
    sentences = [part for part in re.split(r"[.!?]+", text) if part.strip()]
    return {
        "characters": len(text),
        "characters_without_spaces": sum(not char.isspace() for char in text),
        "words": len(words),
        "lines": len(text.splitlines()) if text else 0,
        "sentences": len(sentences),
    }

def slugify(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
