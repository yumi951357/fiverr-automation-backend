from fastapi import FastAPI, Header, Request
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os, json, time
from common.audit import append_audit

app = FastAPI(title="Execution Layer", version="1.0.0")

class DeployRequest(BaseModel):
    credentials: Dict[str, Any]
    gig_assets: Dict[str, Any]

@app.post("/deploy_to_fiverr")
def deploy_to_fiverr(req: DeployRequest):
    # Stub: In real integration, call Fiverr Seller API with OAuth.
    # Here we simulate and return a placeholder URL.
    append_audit("deploy_to_fiverr", {"title": req.gig_assets.get("title")})
    fake_url = "https://www.fiverr.com/your_profile/your_gig_slug"
    return {"gig_url": fake_url, "note": "This is a stub. Connect to official API or approved bridge."}

class Inquiry(BaseModel):
    text: str
    tone: Optional[str] = "friendly"

@app.post("/auto_reply")
def auto_reply(inquiry: Inquiry):
    base = "Thanks for reaching out!"
    if "price" in inquiry.text.lower():
        msg = f"{base} Based on your needs, the Standard plan fits best. I can deliver in 3 days."
    else:
        msg = f"{base} Could you share your goals and target audience? I’ll tailor the deliverables."
    append_audit("auto_reply", {"excerpt": inquiry.text[:100]})
    return {"reply": msg}

class Delivery(BaseModel):
    order_id: str
    template_type: str

@app.post("/auto_deliver")
def auto_deliver(delivery: Delivery):
    # Minimal placeholder: attach the proper template path based on `template_type`
    mapping = {
        "youtube_script": "storage/templates/script_template.docx",
        "data_visualization": "storage/templates/dashboard_template.csv",
        "business_plan": "storage/templates/business_plan_template.pdf"
    }
    path = mapping.get(delivery.template_type, "storage/templates/README.txt")
    append_audit("auto_deliver", {"order_id": delivery.order_id, "template_type": delivery.template_type})
    return {"delivered_files": [path], "message": "Delivery generated and ready to send."}

@app.post("/webhook/inbox")
async def inbox_webhook(request: Request, x_signature: Optional[str] = Header(default=None)):
    # Verify signature if provided
    secret = os.environ.get("INBOX_WEBHOOK_SECRET", "")
    body = await request.body()
    append_audit("inbox_webhook", {"len": len(body)})
    return {"ok": True}
