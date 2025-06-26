import openrouteservice
from dotenv import load_dotenv
import os

load_dotenv()

ors_api_key = os.getenv("ORS_API_KEY")
client = openrouteservice.Client(key=ors_api_key)

# Dummy coordinates for centers (add more as needed)
location_coords = {
    "C001": [73.0636, 19.2813],     # Bhiwandi warehouse (Mumbai)
    "C002": [73.8567, 18.5204],     # Pune
    "C003": [77.5946, 12.9716],     # Bangalore

    "Mumbai": [72.8777, 19.0760],
    "Pune": [73.8567, 18.5204],
    "Bangalore": [77.5946, 12.9716]
}

def estimate_delivery(source: str, destination: str, urgency: str):
    if source not in location_coords or destination not in location_coords:
        return {"error": "Invalid location coordinates"}

    coords = [location_coords[source], location_coords[destination]]

    try:
        res = client.distance_matrix(
            locations=coords,
            metrics=["distance", "duration"],
            units="km"
        )
        distance = res["distances"][0][1]
        duration = res["durations"][0][1] / 3600  # convert seconds → hours

        cost_per_km = 22  # sample logic
        urgency_factor = 1.5 if urgency == "express" else 1.0

        return {
            "from": source,
            "to": destination,
            "urgency": urgency,
            "eta_hours": round(duration, 2),
            "estimated_cost": round(distance * cost_per_km * urgency_factor, 2)
        }

    except Exception as e:
        return {"error": f"ORS API failed: {str(e)}"}
