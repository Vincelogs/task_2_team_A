# pylint: disable=invalid-name
""" This script loads in a model """

import pickle as p
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS


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
            return 'Coming soon'
        except Exception:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('You need a trained model first')
        return 'Model not found'

if __name__ == '__main__':
    modelfile = 'modelfile.pkl'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='127.0.0.1', port=5000)
