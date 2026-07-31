# ZBiz Roadmap

## Mission

ZBiz is a reusable, auditable toolkit for preparing Thailand corporate registration packages. It does not replace official DBD forms, legal advice, identity verification, electronic signatures, government submission, or fee payment.

## Phase 1 — Core package

- [x] Company YAML example
- [x] JSON Schema validation
- [x] Registration readiness checklist
- [x] Shareholder register template
- [x] Statutory meeting minutes template
- [x] GitHub Actions validation

## Phase 2 — Complete registration workspace

- [x] Package manifest
- [x] Company intake questionnaire
- [x] Director consent template
- [x] Registered-office consent template
- [x] Capital and share allocation template
- [x] Submission status tracker
- [x] Post-registration checklist

## Phase 3 — Automation

- [ ] Generate a company workspace from a single YAML file
- [ ] Render Markdown templates to DOCX and PDF
- [ ] Validate Thai identification and juristic-person identifiers where legally appropriate
- [ ] Detect incomplete signatures and attachments
- [ ] Produce a readiness report with blocking and advisory findings

## Phase 4 — Governance and compliance

- [ ] Versioned template catalogue
- [ ] Change log mapped to DBD process updates
- [ ] Data-retention and deletion workflow
- [ ] Secret scanning and PII-safe CI fixtures
- [ ] Signed release artifacts and checksums

## Definition of ready to file

A package is considered internally ready only when:

1. All mandatory data fields are completed.
2. Capital and share totals reconcile.
3. Director and shareholder identities have been independently verified.
4. Registered-office evidence is attached.
5. Required approvals and signatures are complete.
6. The latest official DBD requirements have been reviewed.
7. A qualified professional has reviewed any material legal or tax issue.
