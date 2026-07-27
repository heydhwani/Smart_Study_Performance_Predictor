import pandas as pd


def preprocess_input(data):
    """
    Preprocess user input before prediction.
    """

    df = pd.DataFrame([data])

    # Ordinal Mapping
    level_map = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    distance_map = {
        "Near": 0,
        "Moderate": 1,
        "Far": 2
    }

    education_map = {
        "High School": 0,
        "College": 1,
        "Postgraduate": 2
    }

    peer_map = {
        "Negative": 0,
        "Neutral": 1,
        "Positive": 2
    }

    ordinal_cols = [
        "Parental_Involvement",
        "Access_to_Resources",
        "Motivation_Level",
        "Family_Income",
        "Teacher_Quality"
    ]

    for col in ordinal_cols:
        df[col] = df[col].map(level_map)

    df["Distance_from_Home"] = df["Distance_from_Home"].map(distance_map)

    df["Parental_Education_Level"] = df["Parental_Education_Level"].map(
        education_map
    )

    df["Peer_Influence"] = df["Peer_Influence"].map(peer_map)

    # Binary Encoding
    binary_map = {
        "Yes": 1,
        "No": 0,
        "Male": 1,
        "Female": 0
    }

    binary_cols = [
        "Extracurricular_Activities",
        "Internet_Access",
        "Learning_Disabilities",
        "Gender"
    ]

    for col in binary_cols:
        df[col] = df[col].map(binary_map)

    # One Hot Encoding
    df["School_Type_Public"] = (
        df["School_Type"] == "Public"
    ).astype(int)

    df.drop("School_Type", axis=1, inplace=True)

    return df