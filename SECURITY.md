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
## User responsibility and warranty notice

Use this project only for lawful learning and on resources you own or are explicitly authorized to use. Review all code and commands before running them, keep independent backups, and protect private data. Use is at your own risk. The project is supplied “as is” without warranties, to the maximum extent permitted by applicable law. Nothing here excludes non-waivable rights, liabilities, or obligations. An educational-purpose notice is not permission to access or test third-party systems.
