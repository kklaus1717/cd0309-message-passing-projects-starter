import grpc
import personUsageStatistic_pb2
import personUsageStatistic_pb2_grpc
from kafka import KafkaConsumer
import json

channel = grpc.insecure_channel("localhost:5005") 
stub = personUsageStatistic_pb2_grpc.PersonUsageStatisticServiceStub(channel)


# Kafka-Consumer mit Broker-Adresse
consumer = KafkaConsumer(
    'person_usage_statistic_topic',
    bootstrap_servers='localhost:9092',  # Kafka-Broker setzen
)

# Nachrichten konsumieren
for message in consumer:
    print(f"Received: {message.value} from topic {message.topic}")
    # Update this with desired payload
    data = json.loads(message.value)
    print("data: " + data)
    personUsageStatistic = personUsageStatistic_pb2.PersonUsageStatisticMessage(
        id = data["id"],
        created_at = data["created_at"],
    )
    response = stub.Create(personUsageStatistic)

