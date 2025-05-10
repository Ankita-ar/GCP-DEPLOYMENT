## Import Libraries
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)
model_path = os.path.join(os.path.dirname(__file__), 'iris_model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    return render_template('index.html', prediction_text = f'Species predicted:{prediction[0]}')

@app.route('/api', methods = ['POST'])
def api():
    data = request.get_json(force = True)
    prediction = model.predict([np.array(list(data.values()))])
    return jsonify({'prediction' : int(prediction[0])})

if __name__ == '__main__':
    app.run(debug = True)