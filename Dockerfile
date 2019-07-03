FROM python:3.6
LABEL maintainer="putssander"
LABEL version="0.2"
LABEL description="Base image, containing no language models."

# Install the required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    curl && \
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

ADD ./README.md  /opt/spaCy-JSON-NLP/README.md
ADD ./setup.py  /opt/spaCy-JSON-NLP/setup.py
WORKDIR /opt/spaCy-JSON-NLP/
RUN python setup.py install

RUN python -m spacy download en
RUN python -m spacy download en_core_web_md

COPY . / /opt/spaCy-JSON-NLP/
WORKDIR /opt/spaCy-JSON-NLP/spacyjsonnlp

ENV PYTHONPATH /opt/spaCy-JSON-NLP:$PYTHONPATH

ENV OPTIONAL_ARGS=''
ENV COREFERENCES='false'
ENV CONSTITUENTS='false'

CMD python server.py
