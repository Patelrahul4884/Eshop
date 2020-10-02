FROM python:3

ENV PYTHONNUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
