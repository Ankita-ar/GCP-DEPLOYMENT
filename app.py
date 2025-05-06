## Import Libraries
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        return render_template('index.html', prediction_text = f'Iris Species:{prediction[0]}')
    except Exception as e:
        return jsonify({'error':str(e)})
    
if __name__ == '__main__':
    app.run(debug = True)    