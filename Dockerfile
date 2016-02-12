FROM python:2.7

RUN apt-get update
RUN apt-get install -y libfreetype6-dev pandoc

RUN mkdir -p /app
WORKDIR /app

COPY requirements /app/requirements
RUN pip install -r requirements
COPY . /app


EXPOSE 16000
ENV BDB_WEB_SETTINGS /app/config/settings.example

CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:16000", "bdb_web:app"]
