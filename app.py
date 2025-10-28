from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# ✅ 安全密钥
API_KEY = os.getenv("NEURAL_API_KEY", "brotherkey123")

# ✅ 加入前端域名白名单
origins = [
    "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class TaskRequest(BaseModel):
    prompt: str

@app.post("/neural/generator")
async def generator(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"output": f"Generated base plan for: {req.prompt}"}

@app.post("/neural/refiner")
async def refiner(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"output": f"Refined version of plan for: {req.prompt}"}

@app.post("/neural/verifier")
async def verifier(req: TaskRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"output": f"Verified and approved version of: {req.prompt}"}
