from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# === 安全密钥 ===
API_KEY = os.getenv("NEURAL_API_KEY", "brotherkey123")

# === 允许跨域访问的前端域名 ===
origins = [
    "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === 数据模型 ===
class TaskRequest(BaseModel):
    prompt: str = ""

# === 路由 ===
@app.post("/neural/generator")
async def generator(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    if not req.prompt.strip():
        raise HTTPException(status_code=422, detail="Missing prompt")
    return {"output": f"🧠 Base plan generated for: {req.prompt}"}


@app.post("/neural/refiner")
async def refiner(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    if not req.prompt.strip():
        raise HTTPException(status_code=422, detail="Missing prompt")
    return {"output": f"🔧 Refined version of: {req.prompt}"}


@app.post("/neural/verifier")
async def verifier(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    if not req.prompt.strip():
        raise HTTPException(status_code=422, detail="Missing prompt")
    return {"output": f"✅ Verified and approved plan for: {req.prompt}"}


@app.get("/")
async def root():
    return {"status": "OK", "message": "Neural backend live"}