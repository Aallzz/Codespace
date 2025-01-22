from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Sample training data (experience vs. salary)
data = pd.DataFrame({
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000]
})

# Train a simple Linear Regression model
X = data[["Experience"]]
y = data["Salary"]

model = LinearRegression()
model.fit(X, y)

# Serve the frontend
@app.route("/")
def home():
    return render_template("index.html")

# API route for predictions
@app.route("/predict", methods=["GET"])
def predict():
    experience = request.args.get("experience", type=float)
    if experience is None:
        return jsonify({"error": "Please provide experience as a query parameter."})
    
    # Make prediction
    predicted_salary = model.predict(np.array([[experience]]))[0]
    
    return jsonify({"experience": experience, "predicted_salary": round(predicted_salary, 2)})

if __name__ == "__main__":
    app.run(debug=True)