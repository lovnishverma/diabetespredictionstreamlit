import streamlit as st
import pickle
import numpy as np

# Load the diabetes prediction model
diabetes_model = pickle.load(open('models/diabetes.sav', 'rb'))

# Streamlit app
def main():
    st.title("Diabetes Prediction App")

    # Input form
    st.sidebar.header("User Input")
    firstname = st.sidebar.text_input("First Name")
    lastname = st.sidebar.text_input("Last Name")
    email = st.sidebar.text_input("Email")
    phone = st.sidebar.text_input("Phone")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    pregnancies = st.sidebar.number_input("Pregnancies", value=0)
    glucose = st.sidebar.number_input("Glucose", value=0)
    bloodpressure = st.sidebar.number_input("Blood Pressure", value=0)
    insulin = st.sidebar.number_input("Insulin", value=0)
    bmi = st.sidebar.number_input("BMI", value=0.0)
    diabetespedigree = st.sidebar.number_input("Diabetes Pedigree", value=0.0)
    age = st.sidebar.number_input("Age", value=0)
    skinthickness = st.sidebar.number_input("Skin Thickness", value=0)

    # Prediction button
    if st.sidebar.button("Predict"):
        pred = predict_diabetes(
            pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age
        )
        result_message = "POSITIVE" if pred else "NEGATIVE"
        st.success(f"Hello {firstname}, your Diabetes test results are ready. RESULT: {result_message}")

# Function to predict diabetes
def predict_diabetes(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age):
    pred = diabetes_model.predict(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]]
    )
    return bool(pred[0])

# Run the Streamlit app
if __name__ == "__main__":
    main()
