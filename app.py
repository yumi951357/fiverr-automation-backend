from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI()

# 设置你的私密访问密钥
API_KEY = os.getenv("NEURAL_API_KEY", "brotherkey123")

class NeuralInput(BaseModel):
    prompt: str | None = None

# ---------- 核心函数 ----------
def generate_plan(prompt: str | None) -> str:
    text = (prompt or "").lower().strip()
    date = datetime.utcnow().strftime("%Y-%m-%d")

    # 商业计划书生成逻辑
    if any(k in text for k in ["business plan", "startup", "company", "pitch", "investment"]):
        return f"""
AI Social Media Management Startup — Full Business Plan
Date: {date}

1. Executive Summary
Our startup builds an AI-driven platform for automated content creation, scheduling, and analytics for small to medium brands.

2. Market Opportunity
- Market size: $17B by 2030, CAGR 14%.
- Gap: Fragmented tools, inconsistent workflows, poor cross-platform automation.
- Solution: A full-cycle AI assistant that manages content from draft to delivery.

3. Product Overview
Modules:
- Content Generator (GPT-based)
- Smart Scheduler (engagement optimization)
- Trend Insight (semantic data engine)
Stack: FastAPI + Vercel + Render + transformer back-end.

4. Business Model
- SaaS tiers: $29 / $79 / $199 monthly
- Custom strategy (Fiverr automation)
- Gross margin target: 70%

5. Go-To-Market
- Initial channels: Fiverr + X + TikTok
- W1–2: Landing + teaser launch
- W3–5: Social proof loop
- W6–9: Paid campaigns

6. Financial Projection
- Month 1–3: $2K revenue
- Month 6: $10K MRR
- Month 12: $25K+
Break-even: 4 months.

7. Team
Prometheus (strategy) · Mnemosyne (content logic) · Hermes (delivery)
You (operator): orchestration, outreach, quality control.

8. Milestones
- MVP Launch ✅
- Analytics Module ⚙️ (Month 2)
- Auto Scheduler 🧠 (Month 4)
- Seed-ready deck (Month 6)

9. Funding
Seed: $100K → runway 12 months.
Exit: Acquisition by Hootsuite / Zapier-tier firms.

10. Vision
Build the first self-learning marketing system where creativity is algorithmic and scalable.
— End of Plan —
"""

    # 默认走 Fiverr 自动化计划
    return f"""
Fiverr Automation Plan — Oracle Philosophy
Date: {date}

Objective:
Full automation: intake → generate → refine → package → deliver → archive.

Pipeline:
- Prometheus: phrasing, tone
- Mnemosyne: SEO, structure
- Hermes: packaging, delivery

Pricing:
Basic $50 / Standard $150 / Premium $300
Revenue cycle: Fiverr clearance T+14.

Next:
- Publish demo gig
- Log first order
— End —
"""

# ---------- 路由 ----------
@app.post("/neural/generator")
async def generator(data: NeuralInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: invalid API key")
    return {"output": generate_plan(data.prompt)}

@app.post("/neural/refiner")
async def refiner(data: NeuralInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: invalid API key")
    return {"output": "Refiner active. (Reserved for advanced mode.)"}

@app.post("/neural/verifier")
async def verifier(data: NeuralInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: invalid API key")
    return {"output": "Verifier active. (Reserved for output validation.)"}