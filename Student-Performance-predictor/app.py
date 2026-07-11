import pickle
import pandas as pd
model = pickle.load(open("student_performance_model.pkl", "rb"))
import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Student Performance Predictor")
st.write("Enter the student's details below to predict the exam score.")

st.markdown("---")

# -------------------------------
# Numerical Inputs
# -------------------------------

hours_studied = st.number_input(
    "Hours Studied",
    min_value=0,
    max_value=50,
    value=10
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0,
    max_value=24,
    value=7
)

previous_scores = st.number_input(
    "Previous Scores",
    min_value=0,
    max_value=100,
    value=75
)

tutoring_sessions = st.number_input(
    "Tutoring Sessions",
    min_value=0,
    max_value=20,
    value=2
)

physical_activity = st.number_input(
    "Physical Activity (Hours/Week)",
    min_value=0,
    max_value=20,
    value=3
)

st.markdown("---")

# -------------------------------
# Categorical Inputs
# -------------------------------

parental_involvement = st.selectbox(
    "Parental Involvement",
    ["High", "Medium", "Low"]
)

access_to_resources = st.selectbox(
    "Access to Resources",
    ["High", "Medium", "Low"]
)

extracurricular_activities = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

motivation_level = st.selectbox(
    "Motivation Level",
    ["High", "Medium", "Low"]
)

internet_access = st.selectbox(
    "Internet Access",
    ["No", "Yes"]
)

family_income = st.selectbox(
    "Family Income",
    ["High", "Medium", "Low"]
)

teacher_quality = st.selectbox(
    "Teacher Quality",
    ["High", "Medium", "Low"]
)

school_type = st.selectbox(
    "School Type",
    ["Private", "Public"]
)

peer_influence = st.selectbox(
    "Peer Influence",
    ["Negative", "Neutral", "Positive"]
)

learning_disabilities = st.selectbox(
    "Learning Disabilities",
    ["No", "Yes"]
)

parental_education = st.selectbox(
    "Parental Education Level",
    ["College", "High School", "Postgraduate"]
)

distance_from_home = st.selectbox(
    "Distance From Home",
    ["Far", "Moderate", "Near"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)


st.markdown("---")

# Gender
gender_male = 1 if gender == "Male" else 0

# Parental Involvement
parental_low = 1 if parental_involvement == "Low" else 0
parental_medium = 1 if parental_involvement == "Medium" else 0

# Access to Resources
access_low = 1 if access_to_resources == "Low" else 0
access_medium = 1 if access_to_resources == "Medium" else 0

# Extracurricular Activities
extra_yes = 1 if extracurricular_activities == "Yes" else 0

# Motivation
motivation_low = 1 if motivation_level == "Low" else 0
motivation_medium = 1 if motivation_level == "Medium" else 0

# Internet
internet_yes = 1 if internet_access == "Yes" else 0

# Family Income
income_low = 1 if family_income == "Low" else 0
income_medium = 1 if family_income == "Medium" else 0

# Teacher Quality
teacher_low = 1 if teacher_quality == "Low" else 0
teacher_medium = 1 if teacher_quality == "Medium" else 0

# School Type
school_public = 1 if school_type == "Public" else 0

# Peer Influence
peer_neutral = 1 if peer_influence == "Neutral" else 0
peer_positive = 1 if peer_influence == "Positive" else 0

# Learning Disabilities
learning_yes = 1 if learning_disabilities == "Yes" else 0

# Parent Education
education_high_school = 1 if parental_education == "High School" else 0
education_postgraduate = 1 if parental_education == "Postgraduate" else 0

# Distance
distance_moderate = 1 if distance_from_home == "Moderate" else 0
distance_near = 1 if distance_from_home == "Near" else 0

input_data = pd.DataFrame([[
    hours_studied,
    attendance,
    sleep_hours,
    previous_scores,
    tutoring_sessions,
    physical_activity,
    parental_low,
    parental_medium,
    access_low,
    access_medium,
    extra_yes,
    motivation_low,
    motivation_medium,
    internet_yes,
    income_low,
    income_medium,
    teacher_low,
    teacher_medium,
    school_public,
    peer_neutral,
    peer_positive,
    learning_yes,
    education_high_school,
    education_postgraduate,
    distance_moderate,
    distance_near,
    gender_male
]], columns=[
    'Hours_Studied',
    'Attendance',
    'Sleep_Hours',
    'Previous_Scores',
    'Tutoring_Sessions',
    'Physical_Activity',
    'Parental_Involvement_Low',
    'Parental_Involvement_Medium',
    'Access_to_Resources_Low',
    'Access_to_Resources_Medium',
    'Extracurricular_Activities_Yes',
    'Motivation_Level_Low',
    'Motivation_Level_Medium',
    'Internet_Access_Yes',
    'Family_Income_Low',
    'Family_Income_Medium',
    'Teacher_Quality_Low',
    'Teacher_Quality_Medium',
    'School_Type_Public',
    'Peer_Influence_Neutral',
    'Peer_Influence_Positive',
    'Learning_Disabilities_Yes',
    'Parental_Education_Level_High School',
    'Parental_Education_Level_Postgraduate',
    'Distance_from_Home_Moderate',
    'Distance_from_Home_Near',
    'Gender_Male'
])

if st.button("Predict Exam Score"):

    prediction = model.predict(input_data)

    st.success(f" Predicted Exam Score: {prediction[0]:.2f}")