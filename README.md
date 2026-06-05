# Taxi MLOps Starter

Minimal educational MLOps project for taxi fare prediction.

The project demonstrates a full local ML workflow:

1. Generate a synthetic taxi dataset.
2. Build model features.
3. Train a regression model.
4. Track metrics and artifacts with MLflow.
5. Save the model to `models/model.joblib`.
6. Serve predictions through a FastAPI service.

## Tech Stack

- Python 3.13
- uv
- pandas
- scikit-learn
- joblib
- MLflow
- FastAPI
- Uvicorn
- Docker
- Docker Compose

## Project Structure

```text
taxi-mlops-starter/
|-- src/
|   |-- make_sample_data.py
|   |-- features.py
|   |-- train.py
|   `-- serve.py
|-- tests/
|   `-- test_serve.py
|-- pyproject.toml
|-- uv.lock
|-- Makefile
|-- Dockerfile
|-- compose.yaml
|-- README.md
|-- .gitignore
`-- .dockerignore
```

## Local Commands

```bash
make setup          # install dependencies with uv
make all            # generate data, build features, train model
make test           # run unit tests
make serve          # start FastAPI locally
make mlflow-ui      # start MLflow UI

make docker-build   # build Docker image
make docker-run     # run Docker container

make compose-up     # start service with Docker Compose
make compose-down   # stop Docker Compose service
```

By default, Makefile commands use `.venv/Scripts/*.exe`, which matches a local
Windows virtual environment created by `uv sync`. On Linux/macOS you can
override tools, for example:

```bash
make PYTHON=.venv/bin/python UVICORN=.venv/bin/uvicorn all
```

## API

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Prediction:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "trip_distance": 5.2,
    "passenger_count": 2,
    "pickup_hour": 14,
    "pickup_day_of_week": 4,
    "trip_duration_min": 22.5
  }'
```

## Notes

Run `make all` before `make serve` when starting from a clean checkout. The API
will report whether `models/model.joblib` is available in `/health`.

Generated data, trained models, MLflow runs, virtual environments, and local
secrets are ignored by Git.
