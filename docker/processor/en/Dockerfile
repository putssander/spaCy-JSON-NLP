# (from repository root) $ docker build . -f docker/processor/en/Dockerfile -t putssander/nlpflow-spacy:en_v2.2

FROM putssander/nlpflow-spacy:base_v2.2

RUN python3 -m spacy download en_core_web_sm
RUN python3 -m spacy download en_core_web_md