from kafka import KafkaProducer
import json
import logging
from datetime import datetime

# Set up logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)
logger = logging.getLogger(__name__)
logger.info(f"Producer Server starting...")


TOPIC_NAME = 'person_usage_statistic_topic'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

data = json.dumps({
    "id": "3",
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})
logger.info(f"Sende dfaten. {data}")
producer.send(TOPIC_NAME, data)
producer.flush()
