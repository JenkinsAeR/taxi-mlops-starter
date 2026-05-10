import pandas as pd
import joblib
import mlflow

from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

Path("models").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/processed/features.csv")

features = [
    "trip_distance",
    "passenger_count",
    "pickup_hour",
    "pickup_day_of_week",
    "trip_duration_min",
    "is_weekend"
]

target = "fare_amount"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

mlflow.set_experiment("taxi-fare-prediction")

with mlflow.start_run():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)

    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("mse", mse)

    joblib.dump(model, "models/model.joblib")
    mlflow.sklearn.log_model(model, "model")

print("Model saved to models/model.joblib")
print(f"MAE: {mae:.3f}")
print(f"MSE: {mse:.3f}")
