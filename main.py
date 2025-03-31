from kafka import KafkaProducer
import pandas as pd
import json
import time

conf = {
  "bootstrap_servers": "localhost:7777",
  "value_serializer": lambda v: json.dumps(v).encode("utf-8"),
  "acks": "all",
  "retries": 3,
  "linger_ms": 10
}

producer = KafkaProducer(**conf)
