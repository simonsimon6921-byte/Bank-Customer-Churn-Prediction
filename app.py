from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from pathlib import Path



app = Flask(__name__)




BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "bank_churn_deep_learning.keras"
SCALER_PATH = BASE_DIR / "models" / "churn_scaler.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"



if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found:\n{MODEL_PATH}"
    )

if not SCALER_PATH.exists():
    raise FileNotFoundError(
        f"Scaler file not found:\n{SCALER_PATH}"
    )

if not FEATURE_PATH.exists():
    raise FileNotFoundError(
        f"Feature file not found:\n{FEATURE_PATH}"
    )



print("Loading TensorFlow model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")




print("Loading scaler...")

with open(SCALER_PATH, "rb") as file:
    scaler = pickle.load(file)

print("Scaler loaded successfully.")




print("Loading feature columns...")

with open(FEATURE_PATH, "rb") as file:
    feature_columns = pickle.load(file)

print("Feature columns loaded successfully.")

print("Expected features:")
print(feature_columns)




@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route("/predict", methods=["POST"])
def predict():

    try:



        data = request.get_json(silent=True)

        if data is None:

            return jsonify({
                "success": False,
                "error": "No JSON data received."
            }), 400


        credit_score = float(
            data.get("credit_score", 650)
        )

        age = float(
            data.get("age", 35)
        )

        geography = str(
            data.get("geography", "France")
        )

        gender = str(
            data.get("gender", "Male")
        )

        tenure = float(
            data.get("tenure", 5)
        )

        balance = float(
            data.get("balance", 50000)
        )

        products = float(
            data.get("products", 1)
        )

        has_card = int(
            data.get("has_card", 1)
        )

        active_member = int(
            data.get("active_member", 1)
        )

        salary = float(
            data.get("salary", 50000)
        )




        input_data = pd.DataFrame({

            "CreditScore": [
                credit_score
            ],

            "Geography": [
                geography
            ],

            "Gender": [
                gender
            ],

            "Age": [
                age
            ],

            "Tenure": [
                tenure
            ],

            "Balance": [
                balance
            ],

            "NumOfProducts": [
                products
            ],

            "HasCrCard": [
                has_card
            ],

            "IsActiveMember": [
                active_member
            ],

            "EstimatedSalary": [
                salary
            ]
        })




        input_data = pd.get_dummies(
            input_data,
            columns=[
                "Geography",
                "Gender"
            ]
        )



        if isinstance(
            feature_columns,
            np.ndarray
        ):

            feature_list = feature_columns.tolist()

        else:

            feature_list = list(
                feature_columns
            )



        input_data = input_data.reindex(
            columns=feature_list,
            fill_value=0
        )




        input_data = input_data.apply(
            pd.to_numeric,
            errors="coerce"
        )

        input_data = input_data.fillna(0)



        scaled_data = scaler.transform(
            input_data
        )




        raw_prediction = model.predict(
            scaled_data,
            verbose=0
        )




        probability = float(
            np.asarray(
                raw_prediction
            ).reshape(-1)[0]
        )



        probability = max(
            0.0,
            min(
                1.0,
                probability
            )
        )




        if probability >= 0.50:

            prediction = "Customer is likely to CHURN"

            status = "churn"

        else:

            prediction = "Customer is likely to STAY"

            status = "stay"




        churn_probability = round(
            probability * 100,
            2
        )




        return jsonify({

            "success": True,

            "prediction": prediction,

            "status": status,

            "probability": churn_probability

        })




    except Exception as e:

        print(
            "Prediction error:",
            str(e)
        )

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500



if __name__ == "__main__":

    print("")
    print("=" * 60)
    print("BANK CUSTOMER CHURN PREDICTION")
    print("=" * 60)
    print("Server: http://127.0.0.1:5000")
    print("Network: http://0.0.0.0:5000")
    print("=" * 60)
    print("")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )