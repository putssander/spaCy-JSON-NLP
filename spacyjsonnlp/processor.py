#!/usr/bin/env python

import os
import sys
from spacyjsonnlp import SpacyPipeline

from kafka import KafkaConsumer, KafkaProducer
from util.http_status_server import HttpHealthServer
from util.task_args import get_kafka_binder_brokers, get_input_channel, get_output_channel, get_reverse_string

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_binder_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])

HttpHealthServer.run_thread()

app = SpacyPipeline()

app.with_constituents = (os.environ.get('CONSTITUENTS', 'true') != 'false')
app.with_coreferences = (os.environ.get('COREFERENCES', 'true') != 'false')
app.with_dependencies = True
app.with_expressions = True

while True:
    for message in consumer:
        output_message = app.process(message.value, spacy_model='en_core_web_md', coreferences=True, constituents=False)
        producer.send(get_output_channel(), output_message)
