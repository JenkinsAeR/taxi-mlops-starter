from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Taxi Fare Prediction API")

MODEL_PATH = Path("models/model.joblib")


class RideFeatures(BaseModel):
    trip_distance: float = Field(gt=0)
    passenger_count: int = Field(ge=1, le=6)
    pickup_hour: int = Field(ge=0, le=23)
    pickup_day_of_week: int = Field(ge=0, le=6)
    trip_duration_min: float = Field(gt=0)


@lru_cache
def load_model():
    if not MODEL_PATH.exists():
        raise RuntimeError(
            "Model file is missing. Run `make all` before starting the API."
        )

    return joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_available": MODEL_PATH.exists()
    }


@app.post("/predict")
def predict(features: RideFeatures):
    data = features.model_dump()
    data["is_weekend"] = int(data["pickup_day_of_week"] in [5, 6])

    df = pd.DataFrame([data])

    try:
        model = load_model()
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    prediction = model.predict(df)[0]

    return {
        "predicted_fare_amount": round(float(prediction), 2)
    }
