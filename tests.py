import json

import requests

test = requests.get("http://127.0.0.1:5000/how10")

print(json.loads(test.json()[0])["timestamp"])