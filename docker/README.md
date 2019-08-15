# spacy-json-nlp Docker version

Run     
    
    docker run -p 5001:5001 putssander/spacy-json-nlp:all_v2


REST

    curl \
    -d '{"text":"Clinical details:\nPulmonary malignancy?\n\nReport:\nCT thorax and abdomen, arterial phase\n\nThorax:\nMass visible in the left upper lobe with a maximum size estimated at image 46 of 4, 7 x 3,0 cm. Possible involvement in mediastinum. Satellite nodes visible at 8-41 with an estimated size of 1.3 cm. Lymph node visible at station 7 with a size of circa 5,2 cm. No lymph nodes visible at contralateral side. Small consolidation middle lobe. No indication of atelectasis.\n\nAbdomen:\nMultiple sharply edged hypodens liver lesions visible which would initially match with cysts (HU 5).\n\nMusculoskeletal:\nNo relevant findings. No metastasis.\n\nConclusion:\nTumor with satellite nodes left upper lobe..."}' \
    -H "Content-Type: application/json" \
    -X POST "http://localhost:5001/?spacy_model=en&coreferences=0&constituents=0"
    