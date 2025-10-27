from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Fiverr Automation Backend")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerationRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"status": "ok", "message": "Fiverr Automation Backend active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/neural/generator")
async def neural_generator(request: GenerationRequest):
    response_text = f"Generated: {request.prompt}"
    return {"status": "success", "output": response_text}

@app.post("/neural/refiner")
async def neural_refiner(request: GenerationRequest):
    response_text = f"Refined: {request.prompt}"
    return {"status": "success", "output": response_text}

@app.post("/neural/verifier")
async def neural_verifier(request: GenerationRequest):
    response_text = f"Verified: {request.prompt}"
    return {"status": "success", "output": response_text}