# Cost + ETA model

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def estimate_delivery(source: str, destination: str, urgency: str):
    # Map fulfillment center IDs to addresses or cities (mock example)
    location_map = {
        "C001": "Mumbai",
        "C002": "Pune",
        "C003": "Bangalore"
    }

    origin = location_map.get(source, source)
    dest = destination

    url = (
        f"https://maps.googleapis.com/maps/api/distancematrix/json"
        f"?origins={origin}&destinations={dest}&key={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    try:
        duration_sec = data["rows"][0]["elements"][0]["duration"]["value"]
        distance_meters = data["rows"][0]["elements"][0]["distance"]["value"]
    except Exception:
        return {"error": "Failed to fetch from Google Maps API"}

    # Convert to hours and km
    eta_hours = round(duration_sec / 3600, 2)
    distance_km = distance_meters / 1000

    # Sample cost estimate logic
    base_cost = 50
    cost_per_km = 20
    cost = base_cost + cost_per_km * distance_km
    cost = round(cost, 2)

    return {
        "from": source,
        "to": destination,
        "urgency": urgency,
        "eta_hours": eta_hours,
        "estimated_cost": cost
    }
