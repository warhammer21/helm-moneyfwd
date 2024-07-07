from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Correctly set the path for the model file
model_path = os.path.join(os.path.dirname(__file__), 'isolation_forest_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return "Isolation Forest Anomaly Detection"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
