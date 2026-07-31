# ZBiz

Production-ready templates, checklists, schemas, and automation tools for preparing corporate registration packages in Thailand, including DBD-oriented company setup workflows, shareholder and director records, registered office documents, compliance checklists, and post-registration tasks.

## Purpose

ZBiz helps founders, accountants, legal teams, and business operators prepare a complete, reviewable corporate registration package before submission through official Department of Business Development (DBD) channels.

> **Important:** This repository does not issue, reproduce, or impersonate official government documents. Always use current DBD forms and obtain professional legal or accounting review where required.

## Quick start

1. Copy `config/company.example.yaml` to `config/company.yaml`.
2. Fill in company, founder, shareholder, director, capital, and registered-office information.
3. Run `python scripts/validate.py config/company.yaml`.
4. Review `docs/filing-checklist.md` and the templates under `templates/`.
5. Submit only through the official DBD process using current official forms.

## Repository structure

- `config/` — company data input
- `schemas/` — validation schema
- `scripts/` — package validation utilities
- `templates/` — reusable corporate records and preparation templates
- `docs/` — filing guide, document matrix, privacy, and compliance notes
- `examples/` — sample configuration for ZEAZDEV COMPANY LIMITED

## Supported preparation areas

- Company-name and profile data
- Founders, promoters, shareholders, and share allocation
- Directors and signing authority
- Capital structure and payment records
- Registered-office evidence
- Business objectives
- Statutory and board meeting records
- Beneficial-owner and compliance information
- Tax, VAT, bank-account, and social-security follow-up checklists

## License

MIT. See `LICENSE`.
