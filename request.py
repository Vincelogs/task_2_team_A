# pylint: disable=invalid-name
""" Sample Post Request """
import json
import requests

# local url
URL = 'http://127.0.0.1:5000/api/summarize'

article = {'Data': 'Your article goes here'}

article = json.dumps(article)

SEND_REQUEST = requests.post(URL, article)
print(SEND_REQUEST)
print(SEND_REQUEST.json())
