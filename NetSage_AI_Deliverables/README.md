# NetSage AI — Submission Package

This package contains every required deliverable except the demo video, which was intentionally excluded because it has already been created.

## Files
1. `cases.csv` — 30 cases spanning VLAN, gateway, DHCP, DNS, routing, ACL, NAT, wireless, interface, duplicate IP and mask issues, with evidence, expected fault, OSI layer, concept and severity.
2. `diagnose_prompt.md` — structured JSON diagnosis prompt, human-review prompt, and 3 worked examples.
3. `rule_checker.py` — deterministic Python checker for duplicate IPs, wrong masks, gateway mismatch, interface down, missing VLANs and missing routes.
4. `sample_checker_output.txt` — reproducible sample output demonstrating the deterministic checks.
5. `dashboard.xlsx` — issue-theme counts, review outcomes and AI/human agreement rate.
6. `responsible_ai_log.csv` — 5 documented cases where human review corrected the AI.
7. `README.md` — submission map and pass-condition checklist.

## Pass-condition checklist
- Case coverage: 30 cases across 8+ issue concepts.
- Evidence use: every case contains actual show-command/topology evidence and the prompt requires evidence references.
- Human oversight: dashboard tracks Accepted/Edited/Rejected; responsible-AI log documents corrections.
- Deterministic checks: checker covers all six specified basic error classes and includes sample output.
- Responsible AI: exactly 5 concrete correction cases are documented.

