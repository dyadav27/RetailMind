from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.forecast import predict_demand

router = APIRouter()

class DemandRequest(BaseModel):
    store_id: int
    dept_id: int

@router.post("/predict-demand")
def forecast_demand_route(req: DemandRequest):
    return predict_demand(req.store_id, req.dept_id)
