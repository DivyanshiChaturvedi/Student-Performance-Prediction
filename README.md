# Student Performance Prediction

This project predicts student academic performance using machine learning techniques based on various input features.

##  Problem Statement
To predict a student's **math score** using factors such as:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type
- Test preparation course

This helps understand how socio-economic and educational factors impact student performance.

---

##  Dataset
- **Dataset**: Student Performance Dataset
- **Features Used**:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
- **Target Variable**: Math Score

Categorical variables were converted using **One-Hot Encoding**.

---

##  Machine Learning Model
- **Algorithm Used**: Linear Regression
- **Why Regression?**
  - The output (math score) is a continuous numeric value.
  - Regression models are suitable for predicting continuous outcomes.

---

##  Tech Stack
- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Pydantic

---

## Project Structure
Student-Performance-Prediction/
│
├── data/                     # Dataset files
├── models/                   # Trained ML models
│   └── student_model.pkl
├── src/                      # Source code
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── tempCodeRunnerFile.py
├── requirements.txt          # Project dependencies
├── .gitignore
└── README.md

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/DivyanshiChaturvedi/Student-Performance-Prediction.git
cd Student-Performance-Prediction

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment (Windows)
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
` ``` `

API Endpoints
### POST `/predict`

Predicts the math score based on input features.

#### Request Body (JSON)
```json
{
  "gender_male": 1,
  "race_ethnicity_group_B": 0,
  "race_ethnicity_group_C": 1,
  "race_ethnicity_group_D": 0,
  "race_ethnicity_group_E": 0,
  "parental_level_of_education_bachelors_degree": 0,
  "parental_level_of_education_high_school": 1,
  "parental_level_of_education_masters_degree": 0,
  "parental_level_of_education_some_college": 0,
  "parental_level_of_education_some_high_school": 0,
  "lunch_standard": 1,
  "test_preparation_course_completed": 1
}

Swagger UI available at:
http://127.0.0.1:8000/docs





