from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
import os  # 添加这行

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
    except:
        data = {}
    return {
        "employee": "Prometheus", 
        "task": "Idea Generation", 
        "input": data, 
        "output": "Initial content draft created.",
        "status": "success"
    }

@app.post("/neural/refiner")
async def neural_refiner(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    return {
        "employee": "Mnemosyne", 
        "task": "Content Refinement", 
        "input": data, 
        "output": "Refined content with optimized phrasing.",
        "status": "success"
    }

@app.post("/neural/verifier")
async def neural_verifier(request: Request):
    try:
        data = await request.json()
    except:
        data = {}
    return {
        "employee": "Hermes", 
        "task": "Final Delivery Verification", 
        "input": data, 
        "output": "Delivery package verified and ready.",
        "status": "success"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)