setup:
	uv sync

sample-data:
	uv run python src/make_sample_data.py

features:
	uv run python src/features.py

train:
	uv run python src/train.py

serve:
	uv run uvicorn src.serve:app --reload --host 127.0.0.1 --port 8000

mlflow-ui:
	uv run mlflow server --port 5000

all: sample-data features train

docker-build:
	docker build -t taxi-mlops-api:uv .

docker-run:
	docker run --rm -p 127.0.0.1:8000:8000 taxi-mlops-api:uv

compose-up:
	docker compose up --build

compose-down:
	docker compose down
