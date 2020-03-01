# (from repository root) $ docker build . -f docker/processor/Dockerfile -t putssander/nlpflow-spacy:base_v2.2
FROM springcloud/openjdk:latest

# Install the required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    libssl-dev \
    git \
    curl && \
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

# run SCDF with Kafka
RUN pip3 install kafka-python

# edited version of Py-JSON-NLP
RUN pip3 install git+https://github.com/putssander/Py-JSON-NLP.git

WORKDIR /app/
# fix for benepar cython dependency in setup.py
RUN pip3 install cython
ADD ./setup.py /app/setup.py
ADD ./README.md /app/README.md
RUN python3 setup.py install

# spacy en sm and md in base
RUN python3 -m spacy download en_core_web_sm
RUN python3 -m spacy download en_core_web_md

# NAF dependencies
RUN pip3 install lxml

COPY ./ / /app/

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENV OPTIONAL_ARGS=''
ENV COREFERENCES='false'
ENV CONSTITUENTS='false'

WORKDIR /app

ENTRYPOINT ["python3", "/app/spacyjsonnlp/processor/python_processor.py", "$@", "--"]
