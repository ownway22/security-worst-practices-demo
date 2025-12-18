# Security Issues Inventory

This repository is intentionally insecure for demonstration purposes. The items below enumerate the main security risks and data exposure patterns currently present.

## Application-level vulnerabilities
- `app.py`
  - SQL injection in `/user` due to string concatenation of an SQL query.
  - Weak hash (MD5) for passwords.
  - Hard-coded JWT signing key plus AWS access keys and GCP service account key.
  - Command injection in `/ping` (`subprocess.getoutput`).
  - Flask debug server bound to `0.0.0.0` (exposes service on all interfaces).
- `insecure_server.js`
  - Command injection via `/exec` and arbitrary code execution via `/eval` endpoint (uses `eval`).
  - Hard-coded Stripe/RSA secrets and unsecured HTTP listener (`0.0.0.0:3000`).
- `Dockerfile`
  - Outdated base image (`python:3.8-slim`), hard-coded `SECRET_TOKEN`, and runs as root without user hardening.

## Dependency risks

- `requirements.txt`:
  - `Flask 2.2.5` – CVE-2023-30861.
  - `PyJWT 2.4.0` – algorithm confusion issues.

- `package.json`:
  - `express 4.16.0` – outdated dependencies with ReDoS risk (e.g., `fresh` CVE-2017-16119).
  - `jsonwebtoken 7.1.9` – signature validation bypass (CVE-2022-23529).
  - `lodash 4.17.11` – prototype pollution (CVE-2019-10744 / CVE-2020-8203).

- `Dockerfile`:
  - Base image may contain known CVEs without patching.

## Infrastructure & configuration issues
- `main.tf`
  - Hard-coded cloud credentials.
  - Public blob access enabled.
  - HTTPS-only transport disabled for Azure Storage (`enable_https_traffic_only = false`).
  - Missing tagging/governance controls.

## Exposed secret material (demo/fake values)
- Hard-coded credentials or keys in `app.py`, `insecure_server.js`, `Dockerfile`, and `main.tf`.
- Secret demo files: `demo_exposed_secrets.txt`, `orig_secret_snapshot.txt`, and `secret_formats_demo.md` contain realistic-looking tokens/keys for scanner testing.

## Reporting a vulnerability
- Report real vulnerabilities privately via GitHub Security Advisories (Security > Advisories > “Report a vulnerability”). Avoid public issues.
- Do not deploy this repository to production.
- Rotate and revoke any real credentials accidentally committed.
