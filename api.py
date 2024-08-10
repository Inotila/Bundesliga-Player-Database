from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved models
with open('random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

with open('gradient_boosting_model.pkl', 'rb') as file:
    gbr_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data
        data = request.get_json()
        age = data['age']

        # Make predictions using rf_model and gbr_model models
        rf_prediction = rf_model.predict(np.array([[age]]))[0]
        gbr_prediction = gbr_model.predict(np.array([[age]]))[0]

        # Calculate confidence confidence
        rf_confidence = 1 / (np.sqrt(((rf_model.predict(np.array([[age]])) - rf_prediction) ** 2).mean()) + 1e-5)
        gbr_confidence = 1 / (np.sqrt(((gbr_model.predict(np.array([[age]])) - gbr_prediction) ** 2).mean()) + 1e-5)

        # Return results
        response = {
            'random_forest': {
                'prediction': rf_prediction,
                'confidence': rf_confidence
            },
            'gradient_boosting': {
                'prediction': gbr_prediction,
                'confidence ': gbr_confidence
            }
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
