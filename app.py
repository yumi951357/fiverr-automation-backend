from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# ===== CORS 修复部分 =====
origins = [
    "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== 数据模型修复 =====
class TaskRequest(BaseModel):
    prompt: str

# ===== API Key 验证修复 =====
API_KEY = "brotherkey123"

@app.middleware("http")
async def verify_key(request: Request, call_next):
    if request.url.path.startswith("/neural/"):
        key = request.headers.get("x-api-key")
        if key != API_KEY:
            raise HTTPException(status_code=403, detail="Invalid API key")
    return await call_next(request)


# ===== 三个端点（统一结构） =====

@app.post("/neural/generator")
async def generate(req: TaskRequest):
    return {"output": f"Generated draft for: {req.prompt}"}

@app.post("/neural/refiner")
async def refine(req: TaskRequest):
    return {"output": f"Refined structure for: {req.prompt}"}

@app.post("/neural/verifier")
async def verify(req: TaskRequest):
    return {"output": f"Verified delivery for: {req.prompt}"}


@app.get("/")
def root():
    return {"status": "online"}
