import requests
import time

while True:
    response = requests.get("http://192.168.56.1:5000/context")
    context = response.json()
    print(f"[Model 1] Context received: {context}")
    time.sleep(5)
