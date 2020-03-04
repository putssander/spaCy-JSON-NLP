# (from repository root) $ docker build . -f docker/processor/nl/Dockerfile -t putssander/nlpflow-spacy:nl_v2.2

FROM putssander/nlpflow-spacy:base_v2.2

RUN python3 -m spacy download nl_core_news_sm

ENV SPACY_MODEL='nl_core_news_sm'
