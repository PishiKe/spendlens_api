FROM python:3.10-slim
ENV PYTHONDONTWRITEBTYECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt install -y python3-psycopg2
RUN apt-get install -y python3-dev

WORKDIR /

COPY ./requirements.txt ./
RUN pip install --upgrade setuptools wheel pip
RUN pip install -r requirements.txt

WORKDIR /code
COPY . /code/