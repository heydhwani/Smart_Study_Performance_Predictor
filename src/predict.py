import joblib

from src.preprocess import preprocess_input

# Load models
regression_model = joblib.load("models/linear_regression_model.pkl")
classification_model = joblib.load("models/classification_model.pkl")

# Load scalers
regression_scaler = joblib.load("models/scaler.pkl")
classification_scaler = joblib.load("models/classification_scaler.pkl")


def predict(data):

    df = preprocess_input(data)

    reg_input = regression_scaler.transform(df)
    predicted_score = regression_model.predict(reg_input)[0]

    cls_input = classification_scaler.transform(df)
    predicted_class = classification_model.predict(cls_input)[0]

    print("Predicted class:", predicted_class)
    print("Predicted score:", predicted_score)
    print(df)

    return {
        "Predicted Score": round(predicted_score,2),
        "Performance": predicted_class
    }