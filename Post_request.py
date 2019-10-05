import requests
import json

# local url
url = 'http://127.0.0.1:5000/api/summarize'

article = {'Data': Your article goes here}

article = json.dumps(article)

send_request = requests.post(url, article)
print(send_request)
print(send_request.json())
