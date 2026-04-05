from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict")
def predict():
    # Simple AI model: calculate mean
    result = float(np.mean([10, 20, 30, 40]))
    return jsonify({"AI Model Output": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)