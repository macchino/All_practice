FROM python:3.10.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip

RUN pip install --upgrade pip \
    && apt update \
    && --rm -it --network="host" stripe/stripe-cli:latest

EXPOSE 8000

ADD . /code/
COPY requirements.txt /code
RUN pip install -r requirements.txt