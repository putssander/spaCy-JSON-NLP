FROM tiangolo/uwsgi-nginx-flask:python3.7
LABEL maintainer="putssander"
LABEL version="0.2"
LABEL description="Base image, containing no language models."

# Install the required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    curl && \
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

ADD ./README.md  /app/README.md
ADD ./setup.py  /app/setup.py
WORKDIR /app/
RUN python setup.py install

RUN python -m spacy download en
RUN python -m spacy download en_core_web_md

COPY . / /app/

ENV PYTHONPATH /app/$PYTHONPATH

ENV OPTIONAL_ARGS=''
ENV COREFERENCES='false'
ENV CONSTITUENTS='false'

ENV LISTEN_PORT 5001

WORKDIR /app
