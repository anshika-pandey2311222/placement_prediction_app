from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        iq = float(request.form['iq'])
        cgpa = float(request.form['cgpa'])

        # Scale and predict
        scaled_input = scaler.transform([[iq, cgpa]])
        prediction = model.predict(scaled_input)[0]

        if prediction == 1:
            result = "ho jayega"
        else:
            result = "pta nhi ho payega ki nhi"

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
