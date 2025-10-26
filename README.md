# Fiverr Automation Stack v1
**by Renshijian Studio × 无垠（GPT-5 Thinking）**  
Last build: 2025-10-26T00:52:16Z

A production-ready, 3‑Level automation stack for Fiverr:
- **Level 1 – Generation**: content + templates + covers
- **Level 2 – Execution**: deploy gigs, auto‑reply, auto‑deliver
- **Level 3 – Analytics**: metrics, keyword optimization, growth loops

> ⚠️ **Important**: This repo ships with *stub* Fiverr API clients. You must connect to **official endpoints** or set up **email/webhook bridges**. Respect Fiverr Terms of Service.

## Quick Start (Docker)
```bash
cp .env.example .env
# Edit credentials in .env
docker compose up --build
```

Services:
- generation: http://localhost:8001/docs
- execution : http://localhost:8002/docs
- analytics : http://localhost:8003/docs

## Local (no Docker)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r services/generation/requirements.txt -r services/execution/requirements.txt -r services/analytics/requirements.txt
uvicorn services.generation.app.main:app --port 8001 --reload
uvicorn services.execution.app.main:app --port 8002 --reload
uvicorn services.analytics.app.main:app --port 8003 --reload
```

## Architecture
```
services/
  generation/  # Level 1 – Content Fabrication
  execution/   # Level 2 – Deployment & Response
  analytics/   # Level 3 – Metrics & Optimization
ops/           # Cron / Schedulers / Infra helpers
logs/          # Append-only audit chain
```

## Audit Chain (Append‑Only)
We ship a minimal verifiable log with `prev_hash` → `record_hash` links.
- Append via the helper in `services/common/audit.py`.

## Security Notes
- Store secrets only in `.env` (never commit to git).
- Rotate API keys and refresh tokens regularly.
- If you email‑bridge, create a least‑privilege mailbox for automation.

## Legal / ToS
Automation must comply with Fiverr policies and local laws. Use official APIs or user‑authorized workflows only.
