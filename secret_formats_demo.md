# Secret Formats Demo (Sanitized)

This file documents examples of typical secret patterns WITHOUT using exact detector-matching prefixes.

| Category | Example (Sanitized) | Note |
| -------- | ------------------- | ---- |
| AWS Access Key | AKIA-EXAMPLE-ACCESSKEY (pattern shortened) | Avoid full 20-char key to bypass push protection. |
| AWS Secret Key | wJalrXUtnFEMI/EXAMPLE/KeyTruncated== | Truncated & modified. |
| GitHub PAT | ghp_exampleTokenRedacted123 | Removed length / entropy. |
| Slack Bot Token | xoxb_example_workspace_bot_token | Prefix changed. |
| Stripe Live Key | sk_live_example_redacted_key | Inserted descriptor. |
| Google API Key | AIzaExampleKeyRedacted123 | Shortened. |
| OpenAI Key | sk-proj-exampleTruncatedKey | Modified. |
| Azure Storage Conn String | DefaultEndpointsProtocol=...;AccountKey=EXAMPLE==; | Key truncated. |
| RSA Private Key Block | -----BEGIN RSA PRIVATE KEY----- TEST ... END ----- | Not a full block. |

These samples are for educational purposes and should not trigger secret scanning push protection.
