from spacyjsonnlp.processor.spacy_to_naf import naf_from_doc, NAF_to_string


def get_naf(doc, dct_time, start_time, end_time, spacy_model, spacy_language, json_message):
    model_name = spacy_model
    model_version = 'model-version'
    layer_to_attributes_to_ignore = dict()
    map_udpos2naf_pos = False

    title = uri = ''

    if json_message:
        if 'title' in json_message:
            title = json_message['title']
        if 'uri' in json_message:
            uri = json_message['uri']

    naf = naf_from_doc(doc=doc,
                       dct=dct_time,
                       start_time=start_time,
                       end_time=end_time,
                       modelname=model_name,
                       modelversion=model_version,
                       language=spacy_language,
                       title=title,
                       uri=uri,
                       layers={'raw',
                               'text',
                               'terms',
                               'entities',
                               'deps',
                               'chunks'},
                       layer_to_attributes_to_ignore=layer_to_attributes_to_ignore,
                       map_udpos2naf_pos=map_udpos2naf_pos)

    return NAF_to_string(naf, True)
