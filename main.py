from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from fastapi.responses import JSONResponse

# ---------- 数据模型 ----------
class GenerationRequest(BaseModel):
    prompt: str

# ---------- FastAPI 初始化 ----------
app = FastAPI(title="Fiverr Automation Backend")

# ---------- CORS 允许前端访问 ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-qes3y9hm4-yumi951357s-projects.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- 健康检查 ----------
@app.get("/")
async def root():
    return {"status": "ok", "message": "Fiverr Automation Backend active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "uptime": "✔️"}

# ---------- 主接口：/neural/generator ----------
@app.post("/neural/generator")
async def neural_generator(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    return {"employee": "Prometheus", "task": "Idea Generation", "input": data, "output": "Initial content draft created."}

# ---------- 主接口：/neural/refiner ----------
@app.post("/neural/refiner")
async def neural_refiner(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    return {"employee": "Mnemosyne", "task": "Content Refinement", "input": data, "output": "Refined content with optimized phrasing."}

# ---------- 主接口：/neural/verifier ----------
@app.post("/neural/verifier")
async def neural_verifier(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    return {"employee": "Hermes", "task": "Final Delivery Verification", "input": data, "output": "Delivery package verified and ready."}

# ---------- 异常捕获 ----------
@app.middleware("http")
async def add_exception_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# ---------- 本地运行 ----------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)