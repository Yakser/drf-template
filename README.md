# drf_template
Template of a Python service that uses Django-REST framework with poetry. Build, test and CI scripts ready.

![Linters](https://github.com/TimePeak/users/actions/workflows/linters.yml/badge.svg)
![Tests](https://github.com/TimePeak/users/actions/workflows/tests.yml/badge.svg)

## Usage

### Create virtual environment

🔑 Copy `.env.example` to `.env` and change api settings

### Install dependencies

* 🐍 Install poetry with command `pip install poetry`
* 📎 Install dependencies with command `poetry install --no-root`

### Install pre-commit hooks

To install pre-commit simply run inside the shell:

```bash
pre-commit install
```

To run it on all of your files, do

```bash
pre-commit run --all-files
```


### Apply migrations

🎓 Run  `python manage.py migrate`

### Run project

🚀 Run project via `python manage.py runserver`
