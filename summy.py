import pickle as p
import traceback
from flask import Flask, request, jsonify
# from flask_cors import CORS
# from urllib.request import urlopen
from bs4 import BeautifulSoup

# pylint:  disable = invalid-name

# loading the model
summarizer = 'modelfile.pkl'
model = p.load(open(summarizer, 'rb'))

summy = Flask(__name__)
# CORS(summy)


@summy.route('/api/summarize', methods=['POST', 'GET'])
# Get Data
article_url = request.json['articleUrl']
if not request.json or 'articleUrl' not in request.json:
        abort(400)
# html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get article
article = soup.body.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in article.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
article = '\n'.join(chunk for chunk in chunks if chunk)
return json.dump(article), 200


def summarize():
    if model:
        article = json.load(article)
        article = request.json['article']

        summary = model.summarize(article)

        return jsonify(summary)
        return 'Coming soon'
        except Exception:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('You need a trained model first')
        return 'Model not found'

if __name__ == '__main__':
    summy.run(debug=True, host='127.0.0.1', port=5000)
