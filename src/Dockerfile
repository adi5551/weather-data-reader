FROM python:3.10-bullseye

RUN apt-get update \
    && apt-get install -y \
        postgresql-client \
        build-essential \
        python3-dev

RUN mkdir /web
WORKDIR /web

COPY requirements.txt .
COPY requirements.dev.txt .

RUN python -m venv /venv

ENV VIRTUAL_ENV "/venv"
ENV PATH "${VIRTUAL_ENV}/bin:${PATH}"

ARG REQUIREMENTS="requirements.dev.txt"

RUN pip install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install -r ${REQUIREMENTS}

