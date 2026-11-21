"""Command-line interface for Royal Python Toolkit."""
import argparse
import json
import sys
from . import __version__
from .encoding_tools import base64_decode, base64_encode, format_json, validate_json
from .file_tools import SUPPORTED_HASHES, file_info, hash_file, hash_text
from .generators import generate_password, generate_uuid
from .text_tools import slugify, text_stats

def build_parser():
    parser = argparse.ArgumentParser(prog="royal-toolkit", description="Royal Python Toolkit — practical developer utilities.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    commands = parser.add_subparsers(dest="command", required=True)
    password = commands.add_parser("password", help="Generate a secure password")
    password.add_argument("--length", type=int, default=20)
    for flag in ("lower", "upper", "digits", "symbols"):
        password.add_argument(f"--no-{flag}", action="store_true")
    hashing = commands.add_parser("hash", help="Create a text or file digest")
    hash_modes = hashing.add_subparsers(dest="mode", required=True)
    for mode in ("text", "file"):
        item = hash_modes.add_parser(mode)
        item.add_argument("value")
        item.add_argument("--algorithm", choices=SUPPORTED_HASHES, default="sha256")
    encoding = commands.add_parser("base64", help="Encode or decode Base64")
    enc_modes = encoding.add_subparsers(dest="mode", required=True)
    for mode in ("encode", "decode"):
        enc_modes.add_parser(mode).add_argument("value")
    json_cmd = commands.add_parser("json", help="Format or validate JSON")
    json_modes = json_cmd.add_subparsers(dest="mode", required=True)
    for mode in ("pretty", "minify", "validate"):
        json_modes.add_parser(mode).add_argument("value")
    text_cmd = commands.add_parser("text", help="Analyze text")
    text_cmd.add_subparsers(dest="mode", required=True).add_parser("stats").add_argument("value")
    commands.add_parser("slug", help="Create a URL-friendly slug").add_argument("value")
    file_cmd = commands.add_parser("file", help="Inspect a local file")
    file_cmd.add_subparsers(dest="mode", required=True).add_parser("info").add_argument("path")
    commands.add_parser("uuid", help="Generate a UUID4 identifier")
    return parser

def run(args):
    if args.command == "password":
        print(generate_password(args.length, use_lower=not args.no_lower, use_upper=not args.no_upper, use_digits=not args.no_digits, use_symbols=not args.no_symbols))
    elif args.command == "hash":
        print(hash_text(args.value, args.algorithm) if args.mode == "text" else hash_file(args.value, args.algorithm))
    elif args.command == "base64":
        print(base64_encode(args.value) if args.mode == "encode" else base64_decode(args.value))
    elif args.command == "json":
        if args.mode == "validate":
            if not validate_json(args.value):
                print("Invalid JSON", file=sys.stderr)
                return 1
            print("Valid JSON")
        else:
            print(format_json(args.value, compact=args.mode == "minify"))
    elif args.command == "text":
        print(json.dumps(text_stats(args.value), indent=2, ensure_ascii=False))
    elif args.command == "slug":
        print(slugify(args.value))
    elif args.command == "file":
        print(json.dumps(file_info(args.path), indent=2, ensure_ascii=False))
    elif args.command == "uuid":
        print(generate_uuid())
    return 0

def main():
    args = build_parser().parse_args()
    try:
        return run(args)
    except (ValueError, OSError, UnicodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
