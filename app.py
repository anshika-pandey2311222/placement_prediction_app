from flask import Flask, request, render_template
import joblib  # safer than pickle for sklearn
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    iq = float(request.form['iq'])
    cgpa = float(request.form['cgpa'])
    features = np.array([[iq, cgpa]])
    
    prediction = model.predict(features)[0]
    
    result = "🎯 Placement Likely" if prediction == 1 else "❌ Placement Unlikely"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
