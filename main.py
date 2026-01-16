import streamlit as st
from prediction_helper import predict

st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    layout="wide",
)


st.markdown("""
<style>
body, .main {
    background-color: #0e1117;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    color: #00ffff;
    text-align: center;
    font-weight: bold;
    margin-bottom: 20px;
}

.stForm {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
}

/* Labels */
label {
    color: #ffffff !important;
    font-weight: bold;
}

/* Inputs */
.stTextInput input, .stNumberInput input, .stSelectbox select {
    background-color: #14161c;
    color: #ffffff;
    border: 1px solid #00ffff;
    border-radius: 8px;
    padding: 5px 10px;
}

/* Buttons */
.stButton>button {
    background-color: #00ffff;
    color: #000000;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 25px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #00bfbf;
    color: #ffffff;
}


.stAlert {
    background-color: #00bfbf !important;
    color: #000000 !important;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)


st.title("Health Insurance Premium Predictor")


with st.form(key='input_form'):
    st.subheader("Enter Your Details")

    age = st.number_input('Age', 18, 100, 25)
    number_of_dependants = st.number_input('Number of Dependents', 0, 15, 0)
    income_lakhs = st.number_input('Income (Lakhs)', 0.0, 200.0, 0.0, 0.5)
    genetical_risk = st.number_input('Genetical Risk', 0, 5, 0)

    gender = st.selectbox('Gender', ['Male', 'Female'])
    marital_status = st.selectbox('Marital Status', ['Unmarried', 'Married'])
    bmi_category = st.selectbox('BMI Category', ['Normal', 'Obesity', 'Overweight', 'Underweight'])
    smoking_status = st.selectbox('Smoking Status', ['Non-Smoker', 'Regular', 'Occasional'])
    employment_status = st.selectbox('Employment Status', ['Salaried', 'Self-Employed'])
    region = st.selectbox('Region', ['Northwest', 'Southeast', 'Southwest'])
    insurance_plan = st.selectbox('Insurance Plan', ['Bronze', 'Silver', 'Gold'])
    medical_history = st.selectbox('Medical History', [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart Disease', 'High blood pressure & Heart Disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ])

    submit_button = st.form_submit_button(label='Predict Premium')


if submit_button:
    input_dict = {
        'Age': age,
        'Number of Dependents': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    prediction = predict(input_dict)
    st.success(f"Expected Premium: {prediction}")
