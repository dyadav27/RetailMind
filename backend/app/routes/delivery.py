# /delivery-estimate
from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.delivery_cost import estimate_delivery

router = APIRouter()

class DeliveryRequest(BaseModel):
    source: str
    destination: str
    urgency: str  # 'standard' or 'express'

@router.post("/delivery-estimate")
def get_delivery_estimate(req: DeliveryRequest):
    result = estimate_delivery(req.source, req.destination, req.urgency)
    return result

