"""Local file metadata and streaming hash utilities."""
import hashlib
from datetime import datetime
from .core import require_existing_file

SUPPORTED_HASHES = ("sha256", "sha512", "sha1")

def hash_text(text, algorithm="sha256"):
    if algorithm not in SUPPORTED_HASHES:
        raise ValueError(f"Unsupported algorithm. Choose: {', '.join(SUPPORTED_HASHES)}")
    return hashlib.new(algorithm, text.encode("utf-8")).hexdigest()

def hash_file(path, algorithm="sha256"):
    if algorithm not in SUPPORTED_HASHES:
        raise ValueError(f"Unsupported algorithm. Choose: {', '.join(SUPPORTED_HASHES)}")
    file_path = require_existing_file(path)
    digest = hashlib.new(algorithm)
    with file_path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def file_info(path):
    file_path = require_existing_file(path)
    stat = file_path.stat()
    return {
        "name": file_path.name,
        "path": str(file_path.resolve()),
        "extension": file_path.suffix or "(none)",
        "size_bytes": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec="seconds"),
    }
