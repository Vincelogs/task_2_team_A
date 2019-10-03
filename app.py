from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

""" Load model file """
if __name__ == '__main__':
    modelfile = 'model as a pickle file'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')