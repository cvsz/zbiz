# Security Policy

## Sensitive information

Do not commit real personal identification numbers, passport scans, signatures, house-registration records, bank details, tax credentials, access tokens, or unredacted official documents to this public repository.

Use synthetic or clearly marked placeholder data in examples and tests. Store real registration packages in an access-controlled document system with encryption, audit logging, backup, retention, and deletion controls.

## Reporting a vulnerability

Report security issues privately to the repository owner. Do not open a public issue containing credentials, personal data, exploitable details, or confidential corporate records.

Include:

- affected file, workflow, or release;
- impact and reproduction steps;
- suggested remediation, if known;
- whether any sensitive data may have been exposed.

## Repository controls

Recommended controls:

- Require pull-request review for the default branch.
- Enable secret scanning and push protection.
- Pin third-party GitHub Actions to immutable commit SHAs.
- Use least-privilege workflow permissions.
- Keep real company packages outside the public repository.
- Review dependencies and generated artifacts before release.
