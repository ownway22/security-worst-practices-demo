# Security Issues Inventory

This repository is intentionally insecure for demonstration purposes. The items below enumerate the main security risks and data exposure patterns currently present.

## Application-level vulnerabilities
- `app.py`
  - SQL injection in `/user` due to string concatenation of queries.
  - Weak hash (MD5) for passwords and hard-coded JWT/AWS/GCP secrets.
  - Command injection in `/ping` (`subprocess.getoutput`) and Flask debug server bound to `0.0.0.0`.
- `insecure_server.js`
  - Command injection via `/exec` and arbitrary code execution via `/eval` using `eval`.
  - Hard-coded Stripe/RSA secrets and unsecured HTTP listener (`0.0.0.0:3000`).
- `Dockerfile`
  - Outdated base image (`python:3.8-slim`), hard-coded `SECRET_TOKEN`, and runs as root without user hardening.

## Dependency risks
- `requirements.txt`: Outdated/vulnerable packages (e.g., `Flask 2.2.5`, `pyjwt 2.4.0`).
- `package.json`: Outdated/vulnerable packages (`express 4.16.0`, `jsonwebtoken 7.1.9`, `lodash 4.17.11`).
- `Dockerfile`: Base image may contain known CVEs without patching.

## Infrastructure & configuration issues
- `main.tf`: Hard-coded cloud credentials, public blob access enabled, HTTPS-only disabled, and missing tagging/governance controls.

## Exposed secret material (demo/fake values)
- Hard-coded credentials or keys in `app.py`, `insecure_server.js`, `Dockerfile`, and `main.tf`.
- Secret demo files: `demo_exposed_secrets.txt`, `orig_secret_snapshot.txt`, and `secret_formats_demo.md` contain realistic-looking tokens/keys for scanner testing.

## Reporting a vulnerability
Real vulnerabilities should be reported privately to the maintainers. Do not deploy this repository to production; rotate and revoke any real credentials accidentally committed.
