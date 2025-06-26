# /suggest-fulfillment

# backend/app/routes/fulfillment.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.fulfillment import suggest_fulfillment_center

router = APIRouter()

class FulfillmentRequest(BaseModel):
    sku_id: str
    customer_location: str
    quantity: int

@router.post("/suggest-fulfillment")
def suggest_center(req: FulfillmentRequest):
    center = suggest_fulfillment_center(req.sku_id, req.customer_location, req.quantity)
    
    if not center:
        return {"message": "No fulfillment center can fulfill this order"}
    
    return {
        "recommended_center": center,
        "sku_id": req.sku_id,
        "quantity": req.quantity
    }
