from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import os, uvicorn

app = FastAPI(title="Fiverr Automation Backend — Neural Store")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
        "https://vercel.app",
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NeuralInput(BaseModel):
    prompt: str | None = None

def generate_plan(prompt: str | None) -> str:
    text = (prompt or "").lower().strip()
    date = datetime.utcnow().strftime("%Y-%m-%d")
    if "business" in text:
        return f"""
AI Social Media Management — Business Plan
Date: {date}

1. Executive Summary
Mission: Automate content creation and analytics for SMEs via AI.
2. Market Analysis
Global TAM $17B by 2030, growth 14%.
3. Product
Pipeline: Intake → Generator → Refiner → Scheduler → Analytics.
4. Business Model
Freemium SaaS + Fiverr consulting.
5. Financials
Startup cost $1.5k, break-even M3, ROI 230% M6.
6. Roadmap
M1 MVP, M2 Dashboard, M3 Growth & Ads.
— End of Business Plan —
"""
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

@app.get("/")
async def root():
    return {"message": "Backend Online ✅"}

@app.post("/neural/generator")
async def generator(data: NeuralInput):
    return {"output": generate_plan(data.prompt)}

@app.post("/neural/refiner")
async def refiner(data: NeuralInput):
    return {"output": generate_plan(data.prompt)}

@app.post("/neural/verifier")
async def verifier(data: NeuralInput):
    return {"output": generate_plan(data.prompt)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)