# Security Policy

## Supported versions

Security fixes are intended for the latest published version of Royal Python Toolkit.

## Reporting a vulnerability

Please do not publish credentials, private data, or exploit details in a public issue. Report suspected vulnerabilities privately through GitHub's **Report a vulnerability** feature on this repository, when available.

Include the affected version, Python version, steps to reproduce, and a concise impact description. Please allow time for investigation before public disclosure.

## Security notes

- Password generation uses Python's `secrets` module.
- File hashing is performed locally and reads files in chunks.
- The toolkit does not make network requests or upload user content.
- SHA-1 is offered only for compatibility; do not use it for security-sensitive integrity or authentication.
