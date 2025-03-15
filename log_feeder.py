import requests
import random
import time
from faker import Faker

fake = Faker()
API_URL = "http://localhost:5000/logs"
LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]

while True:
    log_entry = {
        "level": random.choice(LOG_LEVELS),
        "message": fake.sentence()
    }
    response = requests.post(API_URL, json=log_entry)
    print(f"Sent log: {log_entry}, Response: {response.status_code}")
    time.sleep(2)
