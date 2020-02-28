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
from spacyjsonnlp.processor.spacy_to_naf import naf_from_doc, time_in_correct_format, NAF_to_string

from time import sleep, time

# print("sleep", flush=True)
# sleep(60)
# print("awake", flush=True)


app = SpacyPipeline()
app.with_constituents = (os.environ.get('CONSTITUENTS', 'true') != 'false')
app.with_coreferences = (os.environ.get('COREFERENCES', 'true') != 'false')
# app.with_dependencies = True
# app.with_expressions = True

while True:
    for message in consumer:
        language = 'en'
        title = ''
        text = message.value.decode('utf-8')

        logger.debug('In: %s', text)
        dct_time = time_in_correct_format(datetime.now())
        start_time = time_in_correct_format(datetime.now())
        json_nlp, doc = app.process(text)

        end_time = time_in_correct_format(datetime.now())

        json_nlp_string = json.dumps(json_nlp)
        naf = get_naf(doc, dct_time, start_time, end_time)

        logger.debug(naf.decode('utf-8'))
        naf_encoded = base64.b64encode(naf).decode('utf-8')

        json_result = json.dumps({
            'json-nlp': json.dumps(json_nlp),
            'naf-base64': naf_encoded
        })

        logger.debug('Out: %s', json_result)

        output_message = json_result.encode('utf-8')
        producer.send(get_output_channel(), output_message)


