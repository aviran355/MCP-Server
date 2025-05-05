import requests
import time
import random

while True:
    context = {
        "temperature": round(random.uniform(20, 35), 2),
        "environment": "urban",
        "timestamp": time.time()
    }
    response = requests.post("http://192.168.56.1:5000/context", json=context)
    print(f"[Model 2] Sent context: {context}")
    time.sleep(5)
