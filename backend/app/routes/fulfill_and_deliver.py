from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.fulfillment import suggest_fulfillment_center
from app.ml.delivery_cost import estimate_delivery

router = APIRouter()

class FulfillAndDeliverRequest(BaseModel):
    sku_id: str
    quantity: int
    customer_location: str

@router.post("/fulfill-and-estimate")
def fulfill_and_estimate(req: FulfillAndDeliverRequest):
    # Step 1: Pick best center
    center_id = suggest_fulfillment_center(
        sku_id=req.sku_id,
        location=req.customer_location,
        quantity=req.quantity
    )
    if not center_id:
        return {"error": "No fulfillment center found with enough stock."}

    # Step 2: Estimate delivery
    result = estimate_delivery(
        source=center_id,  # use center_id as source
        destination=req.customer_location,
        urgency="standard"
    )

    return {
        "sku_id": req.sku_id,
        "recommended_center": center_id,
        "quantity": req.quantity,
        "delivery_estimate": result
    }
