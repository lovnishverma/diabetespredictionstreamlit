import streamlit as st
from joblib import load

# Load the diabetes prediction model
diabetes_model = load('models/diabetes.sav')

# Streamlit app
def main():
    # Set page config
    st.set_page_config(
        page_title="Diabetes Prediction App",
        page_icon="💉",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    # Header
    st.title("Diabetes Prediction App")
    st.image("static/logo.png", use_column_width=True)  # Replace with your logo

    # Input form
    st.sidebar.header("Patient Details")

    # User details
    name = st.sidebar.text_input("Name", help="Enter your name")

    # Clinical details
    st.sidebar.subheader("Clinical Details")
    pregnancies = st.sidebar.number_input("Pregnancies", value=0, help="Number of pregnancies")
    glucose = st.sidebar.number_input("Glucose", value=0, help="Glucose level")
    bloodpressure = st.sidebar.number_input("Blood Pressure", value=0, help="Blood pressure")
    insulin = st.sidebar.number_input("Insulin", value=0, help="Insulin level")
    bmi = st.sidebar.number_input("BMI", value=0.0, help="Body Mass Index")
    diabetespedigree = st.sidebar.number_input("Diabetes Pedigree", value=0.0, help="Diabetes pedigree function")
    age = st.sidebar.number_input("Age", value=0, help="Age")
    skinthickness = st.sidebar.number_input("Skin Thickness", value=0, help="Skin thickness")

    # Prediction button
    if st.sidebar.button("Predict", key="predict_button"):
        pred = predict_diabetes(
            pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age
        )
        result_message = "POSITIVE" if pred else "NEGATIVE"
        st.success(f"Hello {name}, your Diabetes test results are ready. RESULT: {result_message}")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2023 Diabetes Prediction App")

# Function to predict diabetes
def predict_diabetes(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age):
    pred = diabetes_model.predict(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]]
    )
    return bool(pred[0])

# Run the Streamlit app
if __name__ == "__main__":
    main()
