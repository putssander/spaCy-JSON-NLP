# NlpFlow-spaCy

Docker repository: [putssander/nlpflow-spacy]()

## Build

    $ docker build . -f docker/processor/Dockerfile -t putssander/nlpflow-spacy:base_v2.2

## Usage

In output over kafka

In: text or json with key text

    curl --header "Content-Type: application/json" \
      --request POST \
      --data '{"text":"Test a long sentence with a document identifier", "identifier": "a", "title": "this is a title"}' \
      http://192.168.0.30:32123

Out: JSON with key 'jsonnlp' and key 'naf-base64'

    {
        'json-nlp': json.dumps(json_nlp),
        'naf-base64': naf_encoded
    }


For more documentation see [NLPFLOW](https://github.com/putssander/nlpflow)
    
    