from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# CORS 配置 - 放在所有路由之前
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
        "http://localhost:3000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === 核心配置 ===
API_KEY = os.getenv("NEURAL_API_KEY", "brotherkey123")

class TaskRequest(BaseModel):
    prompt: str

# === 模拟神经三步输出 ===
@app.post("/neural/generator")
async def generator(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return {"output": f"🧠 Base draft generated for: {req.prompt}"}

@app.post("/neural/refiner")
async def refiner(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return {"output": f"🔧 Refined structure and style for: {req.prompt}"}

@app.post("/neural/verifier")
async def verifier(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return {"output": f"✅ Verified and finalized plan for: {req.prompt}"}

@app.get("/")
async def root():
    return {"status": "Neural backend active"}