import pandas as pd
import random
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

rows = []

for _ in range(1000):
    trip_distance = round(random.uniform(0.5, 15), 2)
    passenger_count = random.randint(1, 4)
    pickup_hour = random.randint(0, 23)
    pickup_day_of_week = random.randint(0, 6)
    trip_duration_min = round(trip_distance * random.uniform(3, 6), 2)
    fare_amount = round(
        3 + trip_distance * 2.8 + trip_duration_min * 0.35 + random.uniform(-2, 2),
        2
    )

    rows.append({
        "trip_distance": trip_distance,
        "passenger_count": passenger_count,
        "pickup_hour": pickup_hour,
        "pickup_day_of_week": pickup_day_of_week,
        "trip_duration_min": trip_duration_min,
        "fare_amount": fare_amount
    })

df = pd.DataFrame(rows)
df.to_csv("data/raw/taxi_sample.csv", index=False)

print("Created data/raw/taxi_sample.csv")
