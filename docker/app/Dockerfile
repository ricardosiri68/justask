FROM python:3.8-alpine
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/
