#!/usr/bin/env python
import json
import logging
import os

from kafka import KafkaConsumer, KafkaProducer

from spacyjsonnlp.processor.util.naf_util import get_naf
from util.http_status_server import HttpHealthServer
from util.task_args import get_kafka_binder_brokers, get_input_channel, get_output_channel

logging.basicConfig()
logger = logging.getLogger('python-processor')
logger.setLevel(level=logging.INFO)

print("ENV", os.environ, flush=True)

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_binder_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])
HttpHealthServer.run_thread()

import base64
from datetime import datetime

from spacyjsonnlp import SpacyPipeline
from spacyjsonnlp.processor.spacy_to_naf import time_in_correct_format

from time import sleep

# print("sleep", flush=True)
# sleep(60)
# print("awake", flush=True)

spacy_language = os.environ.get('SPACY_LANGUAGE', 'en')
spacy_model = os.environ.get('SPACY_MODEL', 'en_core_web_sm')

app = SpacyPipeline()
app.with_constituents = os.environ.get('CONSTITUENTS', 'false')
app.with_coreferences = os.environ.get('COREFERENCES', 'false')
app.with_dependencies = os.environ.get('DEPENDENCIES', 'true')
app.with_expressions = os.environ.get('EXPRESSIONS', 'true')


def is_json(unknown):
    try:
        json.loads(unknown)
    except ValueError:
        return False
    return True


while True:
    for message in consumer:
        message_value = message.value.decode('utf-8')
        message_json = None

        logger.info('In: %s', message_value)

        try:

            dct_time = time_in_correct_format(datetime.now())
            document_id = dct_time
            start_time = time_in_correct_format(datetime.now())

            if is_json(message_value):
                message_json = json.loads(message_value)
                message_json['spacy_model'] = spacy_model
            if 'identifier' in message_value:
                document_id = message_json['identifier']
                json_nlp, doc = app.process(message_json)
            else:
                json_nlp, doc = app.process(text=message_value, spacy_model=spacy_model)

            end_time = time_in_correct_format(datetime.now())

            json_nlp_string = json.dumps(json_nlp)
            naf = get_naf(doc, dct_time, start_time, end_time, spacy_model, spacy_language, message_json)

            logger.debug(naf.decode('utf-8'))
            naf_encoded = base64.b64encode(naf).decode('utf-8')

        except Exception as e:
            logger.error("except", e)

        json_result = json.dumps({
            'name': document_id,
            'json-nlp': json.dumps(json_nlp),
            'naf-base64': naf_encoded
        })

        logger.debug('Out: %s', json_result)

        output_message = json_result.encode('utf-8')
        producer.send(get_output_channel(), output_message)


