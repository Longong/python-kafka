# coding: utf-8
from kafka import KafkaProducer

import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open('/data/Log.log', 'r') as f:
    for l in f:
        word = l.split("`")[1]
        time.sleep(0.1)
        producer.send('sex', word.encode('utf-8'))
