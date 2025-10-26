#!/usr/bin/env bash
set -e
python -m venv .venv && source .venv/bin/activate
pip install -r services/generation/requirements.txt -r services/execution/requirements.txt -r services/analytics/requirements.txt
uvicorn services.generation.app.main:app --port 8001 --reload &
uvicorn services.execution.app.main:app --port 8002 --reload &
uvicorn services.analytics.app.main:app --port 8003 --reload &
wait
