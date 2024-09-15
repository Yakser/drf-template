FROM python:3.12

WORKDIR /service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry==1.8.2

COPY poetry.lock pyproject.toml /service/

RUN poetry install --no-root

COPY . /service
