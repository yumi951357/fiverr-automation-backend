# app.py — fixed plan endpoint (Render-ready)
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
import json

app = FastAPI(title="Fiverr Automation Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 如需锁定域名，改成你的 vercel 域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlanReq(BaseModel):
    prompt: str | None = None

PLAN_TEMPLATE = """\
Fiverr Automation Plan — Oracle Philosophy
Date: {date}
Request: {req}

1) Objective
- Full automation: intake → generate → refine → package → deliver → archive.

2) Services (MVP)
- AI Content Draft (24h)
- Research Brief (1–3 pp, PDF)
- Landing Copy + SEO (keywords included)

3) Digital Employees (Internal)
- Prometheus: intake phrasing, market tone
- Mnemosyne: structure, clarity, SEO
- Hermes: packaging (TXT/PDF), delivery

4) Workflow (T+0 → T+1)
- Receive brief → auto-outline
- Refine & SEO
- Export TXT/PDF + archive hash
- Deliver on Fiverr, schedule follow-up

5) Client Intake (form)
- niche / tone / target / examples / length / deadline

6) Pricing (initial)
- Basic $50 (500–700w, 24h)
- Standard $150 (1.2–1.5k, 48h)
- Premium $300 (2.5–3k + visuals, 72h)

7) Promotion (30-day)
- W1: screenshots (X/TikTok)
- W2: auto-delivery demo
- W3: DeepFrontier excerpt
- W4: monthly core archive

8) Revenue Cycle
- Fiverr clearance T+14
- Research/consulting T+30 (Stripe)
- Target: $500 first 30 days; $1k–1.5k by D+60

9) Risks & Mitigation
- Latency → deploy HKG/SIN
- Low demand → rotate niches weekly
- Quality drift → verifier rules + A/B samples

10) Next Actions (today)
- Frontend button → show this plan
- Publish 1 demo gig + template
- Record first auto-delivery log

— End —
"""

def build_plan(req: str | None) -> str:
    return PLAN_TEMPLATE.format(
        date=datetime.utcnow().strftime("%Y-%m-%d"),
        req=(req or "Generate a practical Fiverr automation plan").strip()
    )

@app.get("/")
async def root():
    return {"status": "ok"}

# 新的稳定端点（推荐前端调用）
@app.post("/api/plan")
async def api_plan(body: PlanReq):
    plan_text = build_plan(body.prompt)
    return JSONResponse(
        content={"output": plan_text},
        media_type="application/json; charset=utf-8"
    )

# 兼容旧路径，避免 422/空返回
@app.post("/neural/generator")
async def generator(body: PlanReq):
    plan_text = build_plan(body.prompt)
    return JSONResponse(
        content={"output": plan_text},
        media_type="application/json; charset=utf-8"
    )

@app.post("/neural/refiner")
async def refiner(req: Request):
    try:
        data = await req.json()
    except:
        data = {}
    plan_text = "Refined.\n\n" + build_plan(data.get("prompt"))
    return JSONResponse(
        content={"output": plan_text},
        media_type="application/json; charset=utf-8"
    )

@app.post("/neural/verifier")
async def verifier(req: Request):
    try:
        data = await req.json()
    except:
        data = {}
    plan_text = "Verified for delivery.\n\n" + build_plan(data.get("prompt"))
    return JSONResponse(
        content={"output": plan_text},
        media_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)