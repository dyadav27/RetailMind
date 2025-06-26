# backend/main.py

from fastapi import FastAPI
from app.routes import demand, fulfilment, delivery

app = FastAPI()

from app.routes import fulfill_and_deliver
app.include_router(fulfill_and_deliver.router)


# Include route modules
app.include_router(demand.router)
app.include_router(fulfilment.router)
app.include_router(delivery.router)

@app.get("/")
def root():
    return {"message": "RetailMind Backend is live!"}
@app.get("/health")
def health_check():
    return {"status": "healthy"}