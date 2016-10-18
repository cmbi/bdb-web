FROM python:2.7-onbuild

RUN apt-get update
RUN apt-get install -y libfreetype6-dev pandoc

WORKDIR /usr/src/app

EXPOSE 16000

CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:16000", "bdb_web:app"]
