# 📚 Student Performance Prediction System

An end-to-end Machine Learning web application that predicts a student's **Exam Score** and **Performance Level** based on academic, personal, and lifestyle factors.

🌐 **Live Demo:** https://smart-study-performance-predictor.onrender.com

---

## 📖 Project Overview

Student academic performance depends on several factors such as study hours, attendance, parental involvement, motivation, teacher quality, and access to learning resources.

This project analyzes these factors and predicts:

- 🎯 Predicted Exam Score
- 📊 Performance Level (Low / Medium / High)

The application is built using Machine Learning and deployed as a Flask web application.

---

## 🚀 Features

- Predict student exam score using Linear Regression.
- Predict student performance category.
- User-friendly responsive web interface.
- Data preprocessing and feature engineering.
- Missing value handling.
- Interactive prediction results.
- Deployed using Render.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib

### Backend
- Flask

### Frontend
- HTML
- CSS
- Bootstrap

### Deployment
- Render

---

## 📂 Dataset

**Dataset:** Student Performance Factors Dataset

The dataset contains academic and demographic information of students including:

- Hours Studied
- Attendance
- Previous Scores
- Motivation Level
- Teacher Quality
- Family Income
- Internet Access
- Peer Influence
- Physical Activity
- Sleep Hours
- School Type
- Parental Education
- Distance from Home
- Gender
- and more...

---

## 📊 Data Preprocessing

The following preprocessing steps were performed:

- Missing value treatment
- Ordinal Encoding
- Binary Encoding
- One-Hot Encoding
- Feature Scaling
- Train-Test Split

---

## 📈 Exploratory Data Analysis

EDA included:

- Dataset Overview
- Missing Value Analysis
- Distribution of Exam Scores
- Correlation Heatmap
- Boxplots
- Feature Relationship Analysis

---

# 🤖 Machine Learning Models

## Regression Models

| Model | R² Score |
|--------|----------|
| Linear Regression | **0.7709** |
| XGBoost Regressor | 0.7382 |
| Random Forest Regressor | 0.6813 |

### Selected Model

✅ Linear Regression

---

## Classification Models

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **97.28%** |
| Random Forest Classifier | 81.24% |

### Selected Model

✅ Logistic Regression

---

## 📌 Performance Categories

| Performance | Exam Score Range |
|-------------|------------------|
| 🔴 Low | 55–66 |
| 🟡 Medium | 67–69 |
| 🟢 High | 70–101 |

---

## 📁 Project Structure

```
Student_Performance_Prediction/

│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── data/
├── models/
│   ├── linear_regression_model.pkl
│   ├── classification_model.pkl
│   ├── scaler.pkl
│   └── classification_scaler.pkl
│
├── notebooks/
│   └── student_performance_predictor.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── predict.py
│   └── utils.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Student_Performance_Prediction.git
```

Move into the project directory

```bash
cd Student_Performance_Prediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🌐 Live Demo

https://smart-study-performance-predictor.onrender.com

---

## 📸 Screenshots

### Home Page

> Add a screenshot here

### Prediction Result

> Add a screenshot here

---

## 🔮 Future Improvements

- User authentication
- Student report generation (PDF)
- Database integration
- Performance visualization dashboard
- Model retraining with larger datasets
- Explainable AI (SHAP/LIME)

---

## 👩‍💻 Author

**Dhwani Jain**

B.Tech CSE Student

Machine Learning & AI Enthusiast

GitHub: https://github.com/heydhwani

---

## ⭐ If you found this project useful, consider giving it a star.