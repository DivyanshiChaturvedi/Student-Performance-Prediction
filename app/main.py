from fastapi import FastAPI
import joblib
import numpy as np
from app.schemas import StudentInput

app = FastAPI(title="Student Performance Prediction System")

model = joblib.load("models/student_model.pkl")

@app.get("/")
def home():
    return {"message": "Student Performance Prediction API is running"}

@app.post("/predict")
def predict(data: StudentInput):
    features = np.array([
        data.gender_male,
        data.race_ethnicity_group_B,
        data.race_ethnicity_group_C,
        data.race_ethnicity_group_D,
        data.race_ethnicity_group_E,
        data.parental_level_of_education_bachelors_degree,
        data.parental_level_of_education_high_school,
        data.parental_level_of_education_masters_degree,
        data.parental_level_of_education_some_college,
        data.parental_level_of_education_some_high_school,
        data.lunch_standard,
        data.test_preparation_course_completed
    ]).reshape(1, -1)

    prediction = model.predict(features)

    return {
    "predicted_math_score": round(float(prediction[0]), 2)
}

@app.get("/")
def health():
    return {"status": "Student Performance Prediction API is running"}




