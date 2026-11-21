"""Encoding and JSON helpers."""
import base64
import json

def base64_encode(text):
    return base64.b64encode(text.encode("utf-8")).decode("ascii")

def base64_decode(value):
    raw = base64.b64decode(value.encode("ascii"), validate=True)
    return raw.decode("utf-8")

def format_json(value, *, compact=False):
    parsed = json.loads(value)
    if compact:
        return json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(parsed, ensure_ascii=False, indent=2)

def validate_json(value):
    try:
        json.loads(value)
        return True
    except (json.JSONDecodeError, TypeError):
        return False
