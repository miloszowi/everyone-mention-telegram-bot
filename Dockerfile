FROM python:3.8-buster

WORKDIR /src

COPY ./src/requirements.txt /src
RUN pip install -r ./requirements.txt
