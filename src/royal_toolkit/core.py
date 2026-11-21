"""Shared helpers and validation."""
from pathlib import Path

def readable_size(size: int) -> str:
    if size < 0:
        raise ValueError("size cannot be negative")
    value = float(size)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{int(value)} B" if unit == "B" else f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} TB"

def require_existing_file(path):
    candidate = Path(path).expanduser()
    if not candidate.exists():
        raise FileNotFoundError(f"File not found: {candidate}")
    if not candidate.is_file():
        raise IsADirectoryError(f"Not a regular file: {candidate}")
    return candidate
