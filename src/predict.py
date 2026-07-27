import joblib

from src.preprocess import preprocess_input

# Load models
regression_model = joblib.load("models/linear_regression_model.pkl")
classification_model = joblib.load("models/classification_model.pkl")

# Load scalers
regression_scaler = joblib.load("models/scaler.pkl")
classification_scaler = joblib.load("models/classification_scaler.pkl")


def predict(data):
    """
    Predict exam score and performance category.
    """

    df = preprocess_input(data)

    # Regression
    reg_input = regression_scaler.transform(df)
    predicted_score = regression_model.predict(reg_input)[0]

    # Classification
    cls_input = classification_scaler.transform(df)
    predicted_class = classification_model.predict(cls_input)[0]

    performance = {
        0: "Low",
        1: "Medium",
        2: "High"
    }

    return {
        "Predicted Score": round(predicted_score, 2),
        "Performance": performance[predicted_class]
    }