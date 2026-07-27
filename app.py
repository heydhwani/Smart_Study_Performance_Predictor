from flask import Flask, render_template, request, jsonify
from src.predict import predict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_result():

    # API Request
    if request.is_json:
        data = request.get_json()
        result = predict(data)
        return jsonify(result)

    # HTML Form Request
    data = {
        "Hours_Studied": int(request.form["Hours_Studied"]),
        "Attendance": int(request.form["Attendance"]),
        "Parental_Involvement": request.form["Parental_Involvement"],
        "Access_to_Resources": request.form["Access_to_Resources"],
        "Extracurricular_Activities": request.form["Extracurricular_Activities"],
        "Sleep_Hours": int(request.form["Sleep_Hours"]),
        "Previous_Scores": int(request.form["Previous_Scores"]),
        "Motivation_Level": request.form["Motivation_Level"],
        "Internet_Access": request.form["Internet_Access"],
        "Tutoring_Sessions": int(request.form["Tutoring_Sessions"]),
        "Family_Income": request.form["Family_Income"],
        "Teacher_Quality": request.form["Teacher_Quality"],
        "School_Type": request.form["School_Type"],
        "Peer_Influence": request.form["Peer_Influence"],
        "Physical_Activity": int(request.form["Physical_Activity"]),
        "Learning_Disabilities": request.form["Learning_Disabilities"],
        "Parental_Education_Level": request.form["Parental_Education_Level"],
        "Distance_from_Home": request.form["Distance_from_Home"],
        "Gender": request.form["Gender"]
    }

    result = predict(data)

    return render_template(
        "index.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)