from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Fiverr Automation Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
        "https://vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlanReq(BaseModel):
    prompt: str | None = None

OP_PLAN = """\
Fiverr Automation Plan — Oracle Philosophy
Date: {date}
Request: {req}

1) Objective
- Full automation: intake → generate → refine → package → deliver → archive.
...
— End —
"""

BP_PLAN = """\
{title}
Date: {date}

1. Executive Summary
Mission: automate content creation, scheduling, and analytics for SMEs using AI pipelines...
2. Market Analysis
TAM/SAM/SOM, competitors, gaps...
3. Product & Tech
Modules: intake → generator → refiner → scheduler → analytics; moat & IP...
4. Business Model
Tiered subscription + one-off projects; pricing table...
5. Go-To-Market
Channels (X/TikTok/communities), content engine, partnerships...
6. Operations
Team roles, SLA, tooling, security & compliance...
7. Financials
Startup costs, unit economics, 12-month P&L, break-even, cash cycle (Fiverr T+14 / Stripe T+30)...
8. Roadmap & Milestones
M0–M6 deliverables, risks & mitigations...
— End of Business Plan —
"""

def build_plan(user_prompt: str | None) -> str:
    req = (user_prompt or "Generate a practical Fiverr automation plan").strip()
    is_bp = "business plan" in req.lower()
    date = datetime.utcnow().strftime("%Y-%m-%d")
    if is_bp:
        title = "AI Social Media Management — Business Plan"
        return BP_PLAN.format(title=title, date=date)
    return OP_PLAN.format(date=date, req=req)

@app.post("/api/plan")
async def api_plan(body: PlanReq):
    return {"output": build_plan(body.prompt)}

# 兼容旧路径
@app.post("/neural/generator")
async def generator(body: PlanReq):
    return {"output": build_plan(body.prompt)}

@app.post("/neural/refiner")
async def refiner(body: PlanReq):
    return {"output": build_plan(body.prompt)}

@app.post("/neural/verifier")
async def verifier(body: PlanReq):
    return {"output": build_plan(body.prompt)}