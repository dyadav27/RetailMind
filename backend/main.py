# backend/main.py

from fastapi import FastAPI
from app.routes import demand, fulfilment, delivery

app = FastAPI()

# Include route modules
app.include_router(demand.router)
app.include_router(fulfilment.router)
app.include_router(delivery.router)

@app.get("/")
def root():
    return {"message": "RetailMind Backend is live!"}
