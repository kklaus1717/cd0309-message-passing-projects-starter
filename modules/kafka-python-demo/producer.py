from kafka import KafkaProducer
import json
import logging
from datetime import datetime

# Set up logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)
logger = logging.getLogger(__name__)
logger.info(f"Producer Server starting...")


TOPIC_NAME = 'person_usage_statistic_topic'
KAFKA_SERVER = 'kafka:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

while (True):
    data = json.dumps({
        "id": "3",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    logger.info(f"Sending data: {data}")
    producer.send(TOPIC_NAME, data.encode('utf-8'))
    producer.flush()
