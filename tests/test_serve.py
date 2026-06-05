import unittest
from unittest.mock import patch

from pydantic import ValidationError

from src.serve import RideFeatures, health, load_model, predict


class FakeModel:
    def predict(self, df):
        self.columns = list(df.columns)
        return [18.75]


class ServeTests(unittest.TestCase):
    def tearDown(self):
        load_model.cache_clear()

    def test_health_reports_model_availability(self):
        response = health()

        self.assertEqual(response["status"], "ok")
        self.assertIn("model_available", response)

    def test_predict_adds_weekend_feature_and_returns_rounded_prediction(self):
        ride = RideFeatures(
            trip_distance=5.2,
            passenger_count=2,
            pickup_hour=14,
            pickup_day_of_week=6,
            trip_duration_min=22.5,
        )
        fake_model = FakeModel()

        with patch("src.serve.load_model", return_value=fake_model):
            response = predict(ride)

        self.assertEqual(response, {"predicted_fare_amount": 18.75})
        self.assertIn("is_weekend", fake_model.columns)

    def test_input_validation_rejects_invalid_hour(self):
        with self.assertRaises(ValidationError):
            RideFeatures(
                trip_distance=5.2,
                passenger_count=2,
                pickup_hour=24,
                pickup_day_of_week=4,
                trip_duration_min=22.5,
            )


if __name__ == "__main__":
    unittest.main()
