import re
import json
import pytest
from royal_toolkit.encoding_tools import base64_decode, base64_encode, format_json, validate_json
from royal_toolkit.file_tools import file_info, hash_file, hash_text
from royal_toolkit.generators import generate_password, generate_uuid
from royal_toolkit.text_tools import slugify, text_stats

def test_password():
    value = generate_password(24)
    assert len(value) == 24
    assert any(c.islower() for c in value)
    assert any(c.isupper() for c in value)
    assert any(c.isdigit() for c in value)

def test_password_invalid():
    with pytest.raises(ValueError): generate_password(0)
    with pytest.raises(ValueError): generate_password(2, use_lower=True, use_upper=True, use_digits=True, use_symbols=False)
    with pytest.raises(ValueError): generate_password(10, use_lower=False, use_upper=False, use_digits=False, use_symbols=False)

def test_uuid_v4():
    value = generate_uuid()
    assert re.fullmatch(r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}", value)
    assert value[14] == "4"

def test_base64_round_trip():
    value = "Royal Python Toolkit ✓"
    assert base64_decode(base64_encode(value)) == value

def test_json_helpers():
    source = '{"name":"Royal","active":true}'
    assert validate_json(source)
    assert not validate_json("{bad json")
    assert json.loads(format_json(source))["name"] == "Royal"
    assert format_json(source, compact=True) == source

def test_text_helpers():
    stats = text_stats("Hello world. Python is useful!")
    assert stats["words"] == 5
    assert stats["sentences"] == 2
    assert slugify("Royal Python Toolkit!") == "royal-python-toolkit"

def test_hash_and_file_info(tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text("abc", encoding="utf-8")
    assert hash_text("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert hash_file(str(sample)) == hash_text("abc")
    assert file_info(str(sample))["size_bytes"] == 3

def test_unknown_hash():
    with pytest.raises(ValueError): hash_text("abc", "unknown")
