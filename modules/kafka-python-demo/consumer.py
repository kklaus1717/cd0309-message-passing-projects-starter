from kafka import KafkaConsumer
import logging

# Set up logging
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)
logger = logging.getLogger(__name__)
logger.info(f"Consumer Server starting...")

# Kafka-Consumer mit Broker-Adresse
consumer = KafkaConsumer(
    'person_topic',
    bootstrap_servers='localhost:9092',  # Kafka-Broker setzen
)

logger.info(f"Consumer wartet auf nachricht")

# Nachrichten konsumieren
for message in consumer:
    logger.info(f"Received: {message.value} from topic {message.topic}")
