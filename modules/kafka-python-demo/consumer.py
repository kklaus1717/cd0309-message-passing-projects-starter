from kafka import KafkaConsumer
import logging

# Set up logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)
logger = logging.getLogger(__name__)
logger.info(f"Consumer Server starting...")

TOPIC_NAME = 'person_usage_statistic_topic'
KAFKA_SERVER = 'localhost:9092'

# Kafka-Consumer mit Broker-Adresse
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers = KAFKA_SERVER
)

logger.info(f"Consumer wartet auf nachricht")

# Nachrichten konsumieren
for message in consumer:
    logger.info(f"Received: {message.value} from topic {message.topic}")
