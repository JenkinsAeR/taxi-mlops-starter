PYTHON ?= .venv/Scripts/python.exe
UVICORN ?= .venv/Scripts/uvicorn.exe
MLFLOW ?= .venv/Scripts/mlflow.exe

setup:
	uv sync

sample-data:
	$(PYTHON) src/make_sample_data.py

features:
	$(PYTHON) src/features.py

train:
	$(PYTHON) src/train.py

test:
	$(PYTHON) -m unittest discover -s tests

serve:
	$(UVICORN) src.serve:app --reload --host 127.0.0.1 --port 8000

mlflow-ui:
	$(MLFLOW) server --port 5000

all: sample-data features train

docker-build:
	docker build -t taxi-mlops-api:uv .

docker-run:
	docker run --rm -p 127.0.0.1:8000:8000 taxi-mlops-api:uv

compose-up:
	docker compose up --build

compose-down:
	docker compose down
