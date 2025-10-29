from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

# ====================================================
# FASTAPI INITIALIZATION
# ====================================================
app = FastAPI(title="Fiverr Automation Backend", version="1.0.0")

# ====================================================
# CORS FIX – FULL, SAFE, RENDER-COMPATIBLE
# ====================================================
origins = [
    "*",  # 临时允许所有源，Render 环境推荐这样测试；后续再精确限制
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ====================================================
# API SECURITY
# ====================================================
API_KEY = "brotherkey123"

async def verify_api_key(request: Request):
    # 跳过 OPTIONS 预检请求
    if request.method == "OPTIONS":
        return
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")

# ====================================================
# REQUEST MODEL
# ====================================================
class TaskRequest(BaseModel):
    prompt: Optional[str] = None

# ====================================================
# ENDPOINTS
# ====================================================
@app.get("/")
async def root():
    return {"status": "online", "service": "Fiverr Automation Backend"}

@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    """
    关键：显式允许 OPTIONS 请求通过（Render 否则阻断预检）
    """
    return {}

@app.post("/neural/generator")
async def generate(req: TaskRequest, request: Request):
    await verify_api_key(request)
    if not req.prompt:
        raise HTTPException(status_code=422, detail="Missing prompt in request")
    text = f"AI Business Plan Draft for: {req.prompt}\n\n1. Overview\n2. Market Analysis\n3. Strategy\n4. Revenue Model\n5. Timeline"
    return {"output": text}

@app.post("/neural/refiner")
async def refine(req: TaskRequest, request: Request):
    await verify_api_key(request)
    text = f"Refined business structure for: {req.prompt or 'undefined task'}"
    return {"output": text}

@app.post("/neural/verifier")
async def verify(req: TaskRequest, request: Request):
    await verify_api_key(request)
    text = f"Verified plan delivery for: {req.prompt or 'undefined task'}"
    return {"output": text}

# ====================================================
# LOCAL RUN SUPPORT (optional)
# ====================================================
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=10000)