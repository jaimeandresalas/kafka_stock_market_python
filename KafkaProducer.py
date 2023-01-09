import pandas as pd 
from kafka import  KafkaConsumer,KafkaProducer
from time import sleep
from json import loads, dumps
import json 

# Create a Kafka Producer 
producer = KafkaProducer(bootstrap_servers=['3.86.239.165:9092'],
                            value_serializer=lambda x:  
                            dumps(x).encode('utf-8'))

producer.send('demo_testing2', value="{'Hello': 'World'}")
producer.flush()