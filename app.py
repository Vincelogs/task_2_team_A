# pylint: disable=invalid-name
""" This script loads in a model """

import pickle as p
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS

# loading the model
summarizer = 'modelfile.pkl'
model = p.load(open(summarizer, 'rb'))

app = Flask(__name__)
CORS(app)


@app.route('/api/summarize', methods=['POST', 'GET'])
def summarize():
    """ Returns summary of articles """
    if model:
        try:
            if request.method == 'POST':
                article = request.json['article']
                summary = model.summarize(article)

                return jsonify(summary=summary)
            return {'data': """Welcome to the Page Summarizer API.
            To summarize pls make a POST request to the /api/summarize endpoint
            using the format {"article": "some article content that needs
            summarizing"}"""}
        except Exception:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('You need a trained model first')
        return 'Model not found'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
