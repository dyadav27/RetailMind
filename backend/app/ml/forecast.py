import pandas as pd
from prophet import Prophet
import os

# Load files
TRAIN_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/train.csv"))
FEATURES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/features.csv"))

def predict_demand(store_id: int, dept_id: int):
    # Load train sales data
    df = pd.read_csv(TRAIN_PATH)
    
    # Filter for specific store and department
    df = df[(df["Store"] == store_id) & (df["Dept"] == dept_id)]

    if df.empty:
        return {"error": f"No data found for Store {store_id}, Dept {dept_id}"}

    # Format for Prophet
    prophet_df = df[["Date", "Weekly_Sales"]].rename(columns={
        "Date": "ds",
        "Weekly_Sales": "y"
    })
    prophet_df["ds"] = pd.to_datetime(prophet_df["ds"])

    # Initialize and fit model
    model = Prophet()
    model.fit(prophet_df)

    # Predict next 7 weeks (or days, depending on granularity)
    future = model.make_future_dataframe(periods=7, freq='W')
    forecast = model.predict(future)

    # Take only the forecasted future values
    result = forecast.tail(7)[["ds", "yhat"]]
    result = [{"date": row["ds"].strftime("%Y-%m-%d"), "predicted": round(row["yhat"])} for _, row in result.iterrows()]

    return {
        "store": store_id,
        "department": dept_id,
        "forecast": result
    }
