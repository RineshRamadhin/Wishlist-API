FROM python:3.8.1-buster

LABEL description = "Wishlist API"
LABEL maintainer = "rinesh.ramadhin@gmail.com"

ENV PYTHONUNBUFFERED 1

ARG POSTGRES_USER
ARG POSTGRES_DB

RUN apt-get update \
 && apt-get install -y --no-install-recommends ffmpeg=7:4.1.4-1~deb10u1 postgresql-client=11+200+deb10u3 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip==20.1.1
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./compose/services-check.sh"]
