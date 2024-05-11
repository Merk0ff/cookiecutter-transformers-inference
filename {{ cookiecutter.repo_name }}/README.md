# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Starting the project

```bash
chmod +x run_configuration.sh
```

### Contanerized
```bash
./run_configuration.sh con up --build -d
```

### Local
1. Run infra
```bash
./run_configuration.sh exp up --build -d
```
2. Change redis and minio host to localhost
3. Create venv of service you need in src/worker or src/backend
```bash
python -m venv venv
```
4. Activate venv
```bash
source venv/bin/activate
```
5. Install poetry
```bash
pip install poetry
```
6. Install dependencies from both 
```bash
poetry install --with dev
```
7. Run app. See docker-compose.yml for more details.

## Accessing the project
Application URL:
```bash
http://localhost:8080
```

Minio URL:
```bash
http://localhost:9001
```
Minio root user: `admin`
Minio root password: `{{ cookiecutter.minio_root_password }}`

# About

## Basics
Backend: Fastapi application that use jinja2 templates to serve html pages. It uses a Celery worker to process the tasks.

DB: Minio and Redis.

Worker: Celery worker.


## Docker files
### Worker
There is two Docker files in the `src/worker` folder. The `Dockerfile.cpu` is used for CPU and `Dockerfile.gpu` is used for GPU.

Both of them uses python 3.11 because some packeges are not compatible with python 3.12.

### Backend
The `Dockerfile` in the `src/backend` folder uses python 3.12.
