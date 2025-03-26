from kafka import KafkaProducer
import json


TOPIC_NAME = 'person_usage_statistic_topic'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

data = '{"id" : "3", "created_at" : "10.23.1939"}'
producer.send(TOPIC_NAME, data)
producer.flush()
