# Royal Python Toolkit

A practical, dependency-free command-line toolbox for everyday Python development.

**Version:** 1.0.0 · **Python:** 3.9+ · **Runtime dependencies:** none

## Features

- Secure password generation using Python's secrets module.
- SHA-256, SHA-512, and SHA-1 hashing for text and files.
- Base64 encode and decode.
- JSON validation, pretty-printing, and minification.
- Text statistics: characters, words, lines, and sentences.
- URL-friendly slug generation.
- Local file metadata inspection.
- UUID4 generation.

## Quick start

Clone this repository and install it:

    git clone https://github.com/royal56-create/royal-python-toolkit.git
    cd royal-python-toolkit
    python -m pip install .

Run without installing:

    python -m royal_toolkit --help

## Examples

    royal-toolkit password --length 24
    royal-toolkit hash text "hello world" --algorithm sha256
    royal-toolkit hash file ./notes.txt
    royal-toolkit base64 encode "Royal Python Toolkit"
    royal-toolkit base64 decode "Um95YWwgUHl0aG9uIFRvb2xraXQ="
    royal-toolkit json pretty '{"name":"Royal","active":true}'
    royal-toolkit json validate '{"name":"Royal"}'
    royal-toolkit text stats "Python makes useful tools."
    royal-toolkit slug "Royal Python Toolkit"
    royal-toolkit file info ./README.md
    royal-toolkit uuid

If not installed, replace royal-toolkit with python -m royal_toolkit.

## Tests

    python -m pip install -e ".[dev]"
    python -m pytest

## Project structure

    src/royal_toolkit/   Python package and CLI
    tests/               Automated unit tests
    pyproject.toml       Build and package configuration

## Safety and privacy

All operations run locally. The toolkit does not upload files or text. Passwords use cryptographically secure randomness. File hashing reads data in chunks. SHA-1 is included only for compatibility and should not be used for security-sensitive purposes.

## License

MIT — see LICENSE.

Made with Python by **Royal Ankit Ahiran**.
