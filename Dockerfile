FROM python:3.6

MAINTAINER <rashguir@gmail.com> Nicolas Sicard

RUN mkdir /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y \
        gcc \
        python3-dev \
        musl-dev \
        mysql-client \
        python3-mysql.connector

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
