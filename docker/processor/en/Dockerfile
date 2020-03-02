# (from repository root) $ docker build . -f docker/processor/nl/Dockerfile -t putssander/nlpflow-spacy:nl_v2.2

FROM putssander/nlpflow-spacy:base_v2.2

RUN python3 -m spacy download en_core_web_sm

ENV SPACY_MODEL='en_core_web_sm'
