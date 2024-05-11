# Cookiecutter Transformers Inference
This is a template for running Transformers and serve it to web.
It uses redis and minio as storeges. 
All long running tasks are processed in celery workers, wich can be easily scaled up.

## Stack
| Component      | Technology |
|----------------|------------|
| Interpreter    | Python     |
| Package Manager| Poetry     |
| VM             | Docker     |
| Worker         | Celery     |
| DB             | Redis      |
| MQ             | Redis      |
| File Storage   | Minio      |

## Installation

Firstly, you will need to install [dependencies](https://cookiecutter.readthedocs.io/en/latest/).

The recommended way is via [`pipx`](https://github.com/pypa/pipx):

```bash
pipx install cookiecutter
pipx inject cookiecutter jinja2-git
```

Or via global `pip`:

```bash
pip install cookiecutter jinja2-git
```

Then, create a project itself:

```bash
cookiecutter gh:Merk0ff/cookiecutter-transformers-inference
```
