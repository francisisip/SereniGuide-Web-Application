from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load your trained machine learning model
with open("scaler.pkl", "rb") as model_file:
    scaler = pickle.load(model_file)

with open("best_mlp.pkl", "rb") as model_file:
    best_mlp = pickle.load(model_file)


# Define a route for receiving input and making predictions
@app.route("/input", methods=["POST"])
def input():
    # Extract data from the request
    data = request.get_json()

    # Preprocess the data as necessary
    # For example, convert it into a format suitable for your model

    # Make predictions using your machine learning model
    new_data = scaler.transform(data)
    predictions = best_mlp.predict(new_data)

    # Return the predictions as JSON
    return jsonify(predictions.tolist())


if __name__ == "__main__":
    app.run(debug=True)
