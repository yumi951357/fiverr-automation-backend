from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI()

# ✅ CORS 设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
        "https://fiverr-automation-frontend.vercel.app",
        "*",  # （测试阶段开放，稳定后可以只留前端域名）
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 你的安全密钥
API_KEY = os.getenv("NEURAL_API_KEY", "brotherkey123")

class NeuralInput(BaseModel):
    prompt: str | None = None

def generate_plan(prompt: str | None) -> str:
    text = (prompt or "").lower().strip()
    date = datetime.utcnow().strftime("%Y-%m-%d")

    if any(k in text for k in ["business plan", "startup", "company", "investment", "pitch"]):
        return f"""
AI Social Media Management Startup — Full Business Plan
Date: {date}
1. Executive Summary
AI-driven platform automating content creation, scheduling, and analytics.

2. Market Opportunity
Market size: $17B by 2030, CAGR 14%.
Gap: fragmented tools, no end-to-end automation.

3. Product
- Content Generator (GPT)
- Smart Scheduler (engagement optimization)
- Trend Insight (semantic data)
Stack: FastAPI + Render + Vercel.

4. Business Model
SaaS tiers $29/$79/$199
Fiverr Automation Channel
Target gross margin 70%.

5. Go-To-Market
W1–2: Landing page + teaser
W3–5: Client demo + social proof
W6–9: Paid campaigns

6. Financial Projection
Month 3: $2K MRR | Month 6: $10K | Month 12: $25K+
Break-even 4 months.

7. Team
Prometheus (strategy) · Mnemosyne (content logic) · Hermes (delivery)
Operator: orchestration, outreach, quality control.

8. Funding
Seed: $100K → 12mo runway
Exit: Acquisition target — Hootsuite/Trello-tier.

Vision: Build the first self-evolving marketing OS.
— End —
"""

    return f"""
Fiverr Automation Plan — Oracle Philosophy
Date: {date}
Objective: intake → generate → refine → package → deliver → archive.

Digital Staff:
Prometheus (tone) | Mnemosyne (SEO) | Hermes (delivery)

Pricing:
Basic $50 | Standard $150 | Premium $300
Revenue cycle: Fiverr clearance T+14.

Next Steps:
- Publish demo gig
- Log first delivery
— End —
"""

# ✅ 添加根路径路由
@app.get("/")
async def root():
    return {"message": "Fiverr Automation Backend API", "status": "running"}

@app.post("/neural/generator")
async def generator(data: NeuralInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: invalid API key")
    return {"output": generate_plan(data.prompt)}

@app.post("/neural/refiner")
async def refiner(data: NeuralInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: invalid API key")
    return {"output": generate_plan(data.prompt)}

@app.post("/neural/verifier")
async def verifier(data: NeuralInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: invalid API key")
    return {"output": generate_plan(data.prompt)}