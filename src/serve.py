import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Taxi Fare Prediction API")

model = joblib.load("models/model.joblib")


class RideFeatures(BaseModel):
    trip_distance: float
    passenger_count: int
    pickup_hour: int
    pickup_day_of_week: int
    trip_duration_min: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: RideFeatures):
    data = features.model_dump()
    data["is_weekend"] = int(data["pickup_day_of_week"] in [5, 6])

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    return {
        "predicted_fare_amount": round(float(prediction), 2)
    }
