from fastapi import APIRouter
from app.utils import generate_gig_assets, auto_reply

router = APIRouter(prefix="/agent/prometheus")

@router.post("/engage")
async def engage_client(payload: dict):
    assets = generate_gig_assets(payload)
    reply = auto_reply(payload)
    return {"gig_assets": assets, "reply": reply}