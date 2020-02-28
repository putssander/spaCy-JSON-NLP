from spacyjsonnlp.processor.spacy_to_naf import naf_from_doc, NAF_to_string


def get_naf(doc, dct_time, start_time, end_time):
    model_name = 'model'
    model_version = 'model-version'
    layer_to_attributes_to_ignore = dict()
    map_udpos2naf_pos = False

    naf = naf_from_doc(doc=doc,
                       dct=dct_time,
                       start_time=start_time,
                       end_time=end_time,
                       modelname=model_name,
                       modelversion=model_version,
                       language='en',
                       title='',
                       uri='',
                       layers={'raw',
                               'text',
                               'terms',
                               'entities',
                               'deps',
                               'chunks'},
                       layer_to_attributes_to_ignore=layer_to_attributes_to_ignore,
                       map_udpos2naf_pos=map_udpos2naf_pos)

    return NAF_to_string(naf, True)