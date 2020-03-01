# spacy-json-nlp Docker version

For usage with Spring Cloud Dataflow see [here](https://github.com/putssander/spaCy-JSON-NLP/tree/master/docker/processor):

Run     
    
    docker run --rm -p 5000:5001 putssander/spacy-json-nlp:all_v2

REST

    curl \
    -d '{"text":"Clinical details:\nPulmonary malignancy?\n\nReport:\nCT thorax and abdomen, arterial phase\n\nThorax:\nMass visible in the left upper lobe with a maximum size estimated at image 46 of 4, 7 x 3,0 cm. Possible involvement in mediastinum. Satellite nodes visible at 8-41 with an estimated size of 1.3 cm. Lymph node visible at station 7 with a size of circa 5,2 cm. No lymph nodes visible at contralateral side. Small consolidation middle lobe. No indication of atelectasis.\n\nAbdomen:\nMultiple sharply edged hypodens liver lesions visible which would initially match with cysts (HU 5).\n\nMusculoskeletal:\nNo relevant findings. No metastasis.\n\nConclusion:\nTumor with satellite nodes left upper lobe..."}' \
    -H "Content-Type: application/json" \
    -X POST "http://localhost:5001/?spacy_model=en&coreferences=0&constituents=0"


 By default the coreferencing and constituents models are not loaded, but can be loaded using environment variables.
 
     docker run --rm -p 5000:5001 -e CONSTITUENTS=true -e COREFERENCES=true putssander/spacy-json-nlp:all_v2
 
 Example
 
    [http://localhost:5000/?spacy_model=en&constituents=1&text=Trump%20is%20a%20humble%20person.%20What%20is%20he?](http://localhost:5000/?spacy_model=en&constituents=1&text=Trump%20is%20a%20humble%20person.%20What%20is%20he?)
    
 TAGS at dockerhub [https://hub.docker.com/r/putssander/spacy-json-nlp/tags](https://hub.docker.com/r/putssander/spacy-json-nlp/tags)
 
 The TAG all_v2 should contain all language models, but currently only includes "en" and "nl_core_news_sm".
 Build files are included in this project.
