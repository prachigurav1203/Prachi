from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict")
def predict():
    # Feature1 change: calculate SUM instead of mean
    result = float(np.sum([10, 20, 30, 40]))
    return jsonify({"AI Feature1 Output": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)