# /predict-demand

# backend/app/routes/demand.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SKURequest(BaseModel):
    sku_id: str
    location_id: str

@router.post("/predict-demand")
def predict_demand(sku: SKURequest):
    return {
        "sku_id": sku.sku_id,
        "predicted_demand": [40, 42, 38, 55]  # Dummy forecast
    }
