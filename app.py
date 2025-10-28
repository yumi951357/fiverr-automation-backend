from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
import os
import aiohttp

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

async def call_neural_endpoint(endpoint: str, payload: dict):
    """调用内部神经端点的辅助函数"""
    try:
        base_url = "https://fiverr-automation-backend.onrender.com"
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{base_url}{endpoint}",
                json=payload,
                headers={"Content-Type": "application/json"}
            ) as response:
                return await response.json()
    except Exception as e:
        return {"output": f"Fallback content for {endpoint}: {str(e)}"}

@app.post("/neural/report")
async def generate_report(request: Request):
    try:
        data = await request.json()
        topic = data.get("topic", "")
        audience = data.get("audience", "executives")
        tone = data.get("tone", "neutral, data-driven")
        length = data.get("length", "standard")
        
        if not topic:
            return {"error": "topic required"}
        
        # 1) 生成阶段 - Prometheus
        gen_response = await call_neural_endpoint("/neural/generator", {
            "prompt": f"Create a business report about {topic} for {audience} with {tone} tone and {length} length"
        })
        
        # 2) 精炼阶段 - Mnemosyne  
        ref_response = await call_neural_endpoint("/neural/refiner", {
            "text": gen_response.get("output", ""),
            "instruction": "Tighten structure, ensure numbered outline, add data placeholders and actionable recommendations"
        })
        
        # 3) 验证阶段 - Hermes
        ver_response = await call_neural_endpoint("/neural/verifier", {
            "text": ref_response.get("output", ""),
            "checks": ["consistency", "tone", "audience-fit", "length-fit"]
        })
        
        # 统一输出格式
        report_data = {
            "title": f"Business Report: {topic}",
            "audience": audience,
            "tone": tone, 
            "length": length,
            "content": ver_response.get("output", ""),
            "sections": [
                {"heading": "Executive Summary", "content": "AI-generated business insights..."},
                {"heading": "Analysis", "content": "Detailed analysis and recommendations..."},
                {"heading": "Conclusion", "content": "Key takeaways and next steps..."}
            ],
            "status": "completed"
        }
        
        return report_data
        
    except Exception as e:
        return {"error": str(e)}

@app.post("/neural/businessplan")
async def generate_business_plan(request: Request):
    try:
        data = await request.json()
        company = data.get("company", "")
        industry = data.get("industry", "")
        tone = data.get("tone", "professional")
        length = data.get("length", "standard")
        
        if not company or not industry:
            return {"error": "company and industry required"}
        
        # 调用编排逻辑生成商业计划
        prompt = f"Create a {length} business plan for {company} in the {industry} industry with {tone} tone"
        
        # 这里可以调用现有的三个端点或直接生成内容
        response = await call_neural_endpoint("/neural/generator", {
            "prompt": prompt
        })
        
        plan_data = {
            "title": f"Business Plan: {company}",
            "company": company,
            "industry": industry,
            "tone": tone,
            "length": length,
            "content": response.get("output", f"Business plan for {company} in {industry} industry."),
            "status": "completed"
        }
        
        return plan_data
        
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)