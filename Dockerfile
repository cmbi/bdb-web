FROM python:3.9

RUN apt-get update
RUN apt-get install -y libfreetype6-dev pandoc

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

EXPOSE 16000

CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:16000", "bdb_web:app"]
