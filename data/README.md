# `data/`

Files in this directory are written to by the upperharbour-server
backend (Railway) via the GitHub Contents API. They're committed
directly to `main` by an automated bot on each write, so the file
history doubles as an audit log.

## `tools-unlock-leads.jsonl`

Append-only JSON Lines log of every email captured by the 5-lookup
gate on `/tools`. Created on the first lead — won't be present in
the repo until then. One JSON object per line:

```json
{"email":"foo@example.com","ip":"1.2.3.4","user_agent":"Mozilla/5.0 ...","pending_tool":"Slack","requested_at":"2026-04-29T20:14:00.123456"}
```

Don't hand-edit this file — every write does a GET/append/PUT
round-trip against the live remote, so local edits will get
clobbered the next time someone signs up.

To export the lead list as CSV:

```bash
jq -r '[.email, .requested_at, .pending_tool, .ip] | @csv' \
  data/tools-unlock-leads.jsonl > leads.csv
```
