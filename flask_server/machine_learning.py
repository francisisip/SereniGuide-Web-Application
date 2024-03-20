from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle


app = Flask(__name__)
CORS(app)
# Load your trained machine learning model
with open("flask_server\scaler.pkl", "rb") as model_file:
    scaler = pickle.load(model_file)

with open("flask_server\\best_mlp.pkl", "rb") as model_file:
    best_mlp = pickle.load(model_file)


# Define a route for receiving input and making predictions
@app.route("/input", methods=["POST"])
def input():
    # Extract data from the request
    print("HELLO WORLD")
    data = request.get_json()
    print(type(data))
    converted_data = [
        [
            int(data[0]["age"]),
            int(data[0]["sleepDuration"]),
            int(data[0]["awakenings"]),
            data[0][
                "caffeine"
            ],  # No need to convert caffeine and alcohol since they're already integers
            data[0]["alcohol"],
            int(data[0]["smoking"]),
            int(data[0]["exercise"]),
        ]
    ]
    # Preprocess the data as necessary
    # For example, convert it into a format suitable for your model

    # Make predictions using your machine learning model
    new_data = scaler.transform(converted_data)
    predictions = best_mlp.predict(new_data)

    print(predictions)
    # Return the predictions as JSON
    return jsonify(predictions.tolist())


if __name__ == "__main__":
    app.run(debug=True)
