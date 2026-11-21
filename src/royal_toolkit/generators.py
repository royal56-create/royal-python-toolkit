"""Secure random identifiers and passwords."""
import secrets
import string
import uuid

MAX_PASSWORD_LENGTH = 4096

def generate_password(length=20, *, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    if length < 1:
        raise ValueError("length must be at least 1")
    if length > MAX_PASSWORD_LENGTH:
        raise ValueError(f"length must not exceed {MAX_PASSWORD_LENGTH}")
    groups = []
    if use_lower: groups.append(string.ascii_lowercase)
    if use_upper: groups.append(string.ascii_uppercase)
    if use_digits: groups.append(string.digits)
    if use_symbols: groups.append("!@#$%^&*()-_=+[]{}:,.?")
    if not groups:
        raise ValueError("enable at least one character group")
    if length < len(groups):
        raise ValueError("length must be at least the number of enabled groups")
    chars = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    chars.extend(secrets.choice(alphabet) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

def generate_uuid():
    return str(uuid.uuid4())
