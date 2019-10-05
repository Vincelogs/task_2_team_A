import requests
# local url
url = 'http://127.0.0.1:5000/api/summarize'   # change to your url
curl --request POST \
    --url http://127.0.0.1:5000/api/summarize \
    --header 'content-type: application/json' \
    --data '{
        "articleUrl": "     "
    }'