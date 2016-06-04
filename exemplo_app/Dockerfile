FROM ubuntu:14.04

RUN apt-get update

# python
RUN apt-get install -y python python-dev python-distribute python-pip build-essential

#Postgres deps
RUN apt-get install -y libpq-dev

# deps do nosso projeto web em python
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

VOLUME /data

