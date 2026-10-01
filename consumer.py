import json
import os
from kafka import KafkaConsumer
from pymongo import MongoClient


# Kafka settings
KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "supply_chain_events"
CONSUMER_GROUP = "sda-a3-consumer"


# MongoDB settings
MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set.")


# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
database = mongo_client["supply_chain_db"]
collection = database["events"]


# Connect to Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    api_version="4.0.0",
    group_id=CONSUMER_GROUP,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)


print("Connected to Kafka and MongoDB.")
print("Waiting for messages...")


message_count = 0

try:
    for message in consumer:
        data = message.value

        collection.insert_one(data)

        message_count += 1

        print(
            f"Saved #{message_count} | "
            f"source={data.get('source')} | "
            f"product={data.get('product_id')}"
        )

except KeyboardInterrupt:
    print("\nConsumer stopped by user.")

finally:
    consumer.close()
    mongo_client.close()
    print(f"Total messages saved: {message_count}")
