# Taxi MLOps Starter

Учебный MLOps-проект, в котором ML-модель предсказания цены поездки такси превращается в полноценный API-сервис.

## О проекте

Сейчас проект работает на учебных данных такси.

Он:

1. Генерирует sample taxi dataset.
2. Подготавливает признаки для модели.
3. Обучает модель предсказания стоимости поездки.
4. Сохраняет модель в `models/model.joblib`.
5. Запускает FastAPI API.
6. Возвращает предсказание цены поездки через endpoint `/predict`.
---

## Tech stack

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

---

## Project structure

```text
taxi-mlops-starter/
├── src/
│   ├── make_sample_data.py
│   ├── features.py
│   ├── train.py
│   └── serve.py
├── pyproject.toml
├── uv.lock
├── Makefile
├── Dockerfile
├── compose.yaml
├── README.md
├── .gitignore
└── .dockerignore
```

## Makefile commands

```bash
make setup          # install dependencies with uv
make all            # generate data, build features, train model
make serve          # start FastAPI locally
make mlflow-ui      # start MLflow UI

make docker-build   # build Docker image
make docker-run     # run Docker container

make compose-up     # start service with Docker Compose
make compose-down   # stop Docker Compose service
```

Next steps:

```text
Jenkinsfile
tests
MLflow improvements
Airflow
dbt
PostgreSQL / MinIO
Kubernetes
monitoring
```