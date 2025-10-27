from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Fiverr Automation Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/neural/generator")
async def neural_generator(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        return {
            "employee": "Prometheus", 
            "task": "Idea Generation", 
            "input": data, 
            "output": f"Generated: {prompt}",
            "status": "success"
        }
    except:
        return {"status": "error", "output": "Generation failed"}

@app.post("/neural/refiner")
async def neural_refiner(request: Request):
    try:
        data = await request.json()
        # 接受 text 或 prompt 字段
        text = data.get("text", data.get("prompt", ""))
        return {
            "employee": "Mnemosyne", 
            "task": "Content Refinement", 
            "input": data, 
            "output": f"Refined: {text}",
            "status": "success"
        }
    except:
        return {"status": "error", "output": "Refinement failed"}

@app.post("/neural/verifier")
async def neural_verifier(request: Request):
    try:
        data = await request.json()
        # 接受 text 或 prompt 字段
        text = data.get("text", data.get("prompt", ""))
        return {
            "employee": "Hermes", 
            "task": "Final Delivery Verification", 
            "input": data, 
            "output": f"Verified: {text}",
            "status": "success"
        }
    except:
        return {"status": "error", "output": "Verification failed"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)