# run from root of repo: docker build . -f docker/processor/Dockerfile -t putssander/spacy-json-nlp-processor:base_v2
FROM putssander/spacy-json-nlp:base_v2

#from Dockerfile springcloud/openjdk
RUN apt-get update && apt-get install --no-install-recommends -y \
    ca-certificates \
    curl \
    netcat \
    wget \
 && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /opt/openjdk
ENV PATH $JAVA_HOME/bin:$PATH

COPY /docker/processor/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

RUN mkdir -p /opt/openjdk \
 && cd /opt/openjdk \
 && curl https://java-buildpack.cloudfoundry.org/openjdk/bionic/x86_64/openjdk-1.8.0_192.tar.gz | tar xz

RUN pip install kafka-python

#from spring template edit
COPY spacyjsonnlp/processor.py /app/spacyjsonnlp
COPY util/*.py /app/spacyjsonnlp/util/

ENTRYPOINT ["python", "/app/spacyjsonnlp/processor.py", "$@", "--"]