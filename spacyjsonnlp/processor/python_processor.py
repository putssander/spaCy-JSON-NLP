#!/usr/bin/env python

import os
import json
import logging


from kafka import KafkaConsumer, KafkaProducer

from spacyjsonnlp import SpacyPipeline
from util.http_status_server import HttpHealthServer
from util.task_args import get_kafka_binder_brokers, get_input_channel, get_output_channel, get_reverse_string

logging.basicConfig()
logger = logging.getLogger('python-processor')
logger.setLevel(level=logging.INFO)


from time import sleep


print("ENV", os.environ, flush=True)

# print("sleep", flush=True)
# sleep(60)
# print("awake", flush=True)

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_binder_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])

HttpHealthServer.run_thread()
app = SpacyPipeline()
app.with_constituents = (os.environ.get('CONSTITUENTS', 'true') != 'false')
app.with_coreferences = (os.environ.get('COREFERENCES', 'true') != 'false')
# app.with_dependencies = True
# app.with_expressions = True


while True:
    for message in consumer:
        text = message.value.decode('utf-8')
        logger.debug('Text in: %s', text)
        output = json.dumps(app.process(text))
        logger.debug('Text out: %s', output)
        output_message = output.encode('utf-8')
        producer.send(get_output_channel(), output_message)
