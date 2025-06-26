# Cost + ETA model

def estimate_delivery(source: str, destination: str, urgency: str) -> dict:
    # Simulated distance map (in km)
    distance_map = {
        ("Mumbai", "Mumbai"): 5,
        ("Mumbai", "Pune"): 150,
        ("Mumbai", "Bangalore"): 980,
        ("Pune", "Mumbai"): 150,
        ("Pune", "Bangalore"): 830,
        ("Bangalore", "Mumbai"): 980
    }

    distance = distance_map.get((source, destination), 999)

    base_cost = 50
    cost_per_km = 0.5
    speed = 40 if urgency == "standard" else 60
    express_surcharge = 30 if urgency == "express" else 0

    eta_hours = round(distance / speed, 2)
    cost = round(base_cost + (distance * cost_per_km) + express_surcharge, 2)

    return {
        "from": source,
        "to": destination,
        "urgency": urgency,
        "eta_hours": eta_hours,
        "estimated_cost": cost
    }
