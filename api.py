from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
# Enable CORS so the React frontend can communicate with this API
CORS(app)

# Load data and train model once when the API starts
model = None
features = []
try:
    df = pd.read_csv('dataset.csv')
    features = ['Previous_Day_Cases', 'Temperature', 'Holiday_Status', 'Flu_Cases', 
                'Day_of_Week', 'Humidity', 'Air_Quality_Index', 'Local_Event']
    X = df[features]
    y = df['Emergency_Cases']
    
    model = LinearRegression()
    model.fit(X, y)
    print("ML Model trained successfully on startup.")
except Exception as e:
    print(f"Error loading data or training model: {e}")

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not trained'}), 500
        
    data = request.json
    try:
        input_df = pd.DataFrame([{
            'Previous_Day_Cases': float(data.get('previousDayCases', 0)),
            'Temperature': float(data.get('temperature', 0)),
            'Holiday_Status': int(data.get('holidayStatus', 0)),
            'Flu_Cases': float(data.get('fluCases', 0)),
            'Day_of_Week': int(data.get('dayOfWeek', 0)),
            'Humidity': float(data.get('humidity', 0)),
            'Air_Quality_Index': float(data.get('aqi', 0)),
            'Local_Event': int(data.get('localEvent', 0))
        }])
        
        prediction = model.predict(input_df)[0]
        prediction = max(int(np.round(prediction)), 0)
        
        # Calculate local feature contribution: coefficient * input value
        impact = [{"feature": f, "weight": float(c * v)} for f, c, v in zip(features, model.coef_, input_df.iloc[0])]
        
        return jsonify({
            'prediction': prediction,
            'impact': impact
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/stats', methods=['GET'])
def stats():
    if model is None:
         return jsonify({'error': 'No data available'}), 500
    
    return jsonify({
        'totalCases': int(df['Emergency_Cases'].sum()),
        'avgDaily': int(df['Emergency_Cases'].mean()),
        'maxCases': int(df['Emergency_Cases'].max()),
        'avgAqi': int(df['Air_Quality_Index'].mean())
    })

if __name__ == '__main__':
    print("Starting API server on http://localhost:5000")
    app.run(debug=True, port=5000)
