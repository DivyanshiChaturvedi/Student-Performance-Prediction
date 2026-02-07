from pydantic import BaseModel

class StudentInput(BaseModel):
    gender_male: int
    race_ethnicity_group_B: int
    race_ethnicity_group_C: int
    race_ethnicity_group_D: int
    race_ethnicity_group_E: int
    parental_level_of_education_bachelors_degree: int
    parental_level_of_education_high_school: int
    parental_level_of_education_masters_degree: int
    parental_level_of_education_some_college: int
    parental_level_of_education_some_high_school: int
    lunch_standard: int
    test_preparation_course_completed: int
