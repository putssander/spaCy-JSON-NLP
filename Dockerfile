# docker build . -t putssander/spacy-json-nlp:base_v2
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
RUN pip install git+https://github.com/putssander/Py-JSON-NLP.git
ADD ./setup.py  /app/setup.py
WORKDIR /app/
RUN python setup.py install

COPY . / /app/

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENV OPTIONAL_ARGS=''
ENV COREFERENCES='false'
ENV CONSTITUENTS='false'

ENV LISTEN_PORT 5001

WORKDIR /app
