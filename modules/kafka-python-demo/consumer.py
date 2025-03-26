from kafka import KafkaConsumer

# Kafka-Consumer mit Broker-Adresse
consumer = KafkaConsumer(
    'person_topic',
    bootstrap_servers='localhost:9092',  # Kafka-Broker setzen
)

# Nachrichten konsumieren
for message in consumer:
    print(f"Received: {message.value} from topic {message.topic}")
