import pandas as pd
from pathlib import Path

Path("data/processed").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/raw/taxi_sample.csv")

df = df[
    (df["trip_distance"] > 0) &
    (df["fare_amount"] > 0) &
    (df["trip_duration_min"] > 0)
]

df["is_weekend"] = df["pickup_day_of_week"].isin([5, 6]).astype(int)

df.to_csv("data/processed/features.csv", index=False)

print("Created data/processed/features.csv")
