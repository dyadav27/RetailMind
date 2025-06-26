import os
import pandas as pd
import ast
from typing import Optional

def suggest_fulfillment_center(sku_id: str, location: str, quantity: int) -> Optional[str]:
    # Get full path to centers.csv reliably
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir,"..", "..", "..", "data", "centers.csv")


    df = pd.read_csv(csv_path)
    df["stock_dict"] = df["stock_dict"].apply(ast.literal_eval)

    # Filter centers with enough stock
    candidates = df[df["stock_dict"].apply(lambda s: s.get(sku_id, 0) >= quantity)]

    if candidates.empty:
        return None

    # Dummy distance logic
    location_priority = {"Mumbai": 1, "Pune": 2, "Bangalore": 3}
    candidates["distance_score"] = candidates["location"].apply(lambda x: location_priority.get(x, 999))

    # Sort by distance + active_orders
    candidates["score"] = candidates["distance_score"] + candidates["active_orders"]
    best = candidates.sort_values(by="score").iloc[0]

    return best["center_id"]
