from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from apscheduler.schedulers.background import BackgroundScheduler
from common.audit import append_audit

app = FastAPI(title="Analytics Layer", version="1.0.0")
scheduler = BackgroundScheduler(daemon=True)

class Metrics(BaseModel):
    impressions: int
    clicks: int
    orders: int

FAKE_METRICS = Metrics(impressions=1200, clicks=150, orders=6)

@app.get("/fetch_metrics")
def fetch_metrics(interval: str = "daily"):
    # TODO: integrate with Fiverr analytics when available
    append_audit("fetch_metrics", {"interval": interval})
    return FAKE_METRICS.model_json_dict()

@app.post("/optimize_keywords")
def optimize_keywords(performance_data: Dict[str, Any]):
    # toy heuristic
    suggestions = ["add 'professional'", "use 'fast delivery'", "include 'SEO'"]
    append_audit("optimize_keywords", {"keys": list(performance_data.keys())})
    return {"suggestions": suggestions}

@app.post("/dynamic_pricing")
def dynamic_pricing(history_orders: List[Dict[str, Any]]):
    # Example: nudge price +10% if completion<48h and 5-star ratio>90%
    price_factor = 1.0
    stars = [o.get("stars", 5) for o in history_orders] or [5]
    fast = [o.get("hours", 72) for o in history_orders]
    if len(history_orders) >= 5 and sum(s>=5 for s in stars)/len(stars) > 0.9 and sum(1 for h in fast if h<48)/len(fast) > 0.5:
        price_factor = 1.1
    append_audit("dynamic_pricing", {"orders": len(history_orders)})
    return {"price_factor": price_factor}

def daily_job():
    append_audit("cron_daily", {"job": "metrics_scan"})

scheduler.add_job(daily_job, "interval", days=1, id="daily_metrics")
scheduler.start()

@app.get("/health")
def health():
    return {"ok": True}
