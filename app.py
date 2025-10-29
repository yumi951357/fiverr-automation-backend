from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    prompt: str

@app.post("/neural/generator")
async def generator(req: TaskRequest):
    return {"output": f"🧠 Base draft generated for: {req.prompt}"}

@app.post("/neural/refiner")
async def refiner(req: TaskRequest):
    return {"output": f"🔧 Refined structure and style for: {req.prompt}"}

@app.post("/neural/verifier")
async def verifier(req: TaskRequest):
    return {"output": f"✅ Verified and finalized plan for: {req.prompt}"}

@app.get("/")
async def root():
    return {"status": "Neural backend active"}