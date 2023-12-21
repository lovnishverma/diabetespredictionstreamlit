import streamlit as st
from joblib import load  # Import load from joblib instead of pickle

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
    st.image("path/to/your/logo.png", use_column_width=True)  # Replace with your logo

    # Input form
    st.sidebar.header("User Input")

    # User details
    firstname = st.sidebar.text_input("First Name", help="Enter your first name")
    lastname = st.sidebar.text_input("Last Name", help="Enter your last name")
    email = st.sidebar.text_input("Email", help="Enter your email address")
    phone = st.sidebar.text_input("Phone", help="Enter your phone number")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

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

    # Demo data buttons
    if st.sidebar.button("Load Positive Demo Data", key="positive_demo_button"):
        load_positive_demo_data()
    if st.sidebar.button("Load Negative Demo Data", key="negative_demo_button"):
        load_negative_demo_data()

    # Prediction button
    if st.sidebar.button("Predict", key="predict_button"):
        pred = predict_diabetes(
            pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age
        )
        result_message = "POSITIVE" if pred else "NEGATIVE"
        st.success(f"Hello {firstname}, your Diabetes test results are ready. RESULT: {result_message}")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2023 Diabetes Prediction App")

# Function to predict diabetes
def predict_diabetes(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age):
    pred = diabetes_model.predict(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]]
    )
    return bool(pred[0])

# Function to load positive demo data
def load_positive_demo_data():
    st.sidebar.text_input("First Name", "John")
    st.sidebar.text_input("Last Name", "Doe")
    st.sidebar.text_input("Email", "john.doe@example.com")
    st.sidebar.text_input("Phone", "+1234567890")
    st.sidebar.selectbox("Gender", ["Male", "Female"])

    st.sidebar.number_input("Pregnancies", 5)
    st.sidebar.number_input("Glucose", 150)
    st.sidebar.number_input("Blood Pressure", 70)
    st.sidebar.number_input("Insulin", 200)
    st.sidebar.number_input("BMI", 29.0)
    st.sidebar.number_input("Diabetes Pedigree", 0.5)
    st.sidebar.number_input("Age", 40)
    st.sidebar.number_input("Skin Thickness", 30)

# Function to load negative demo data
def load_negative_demo_data():
    st.sidebar.text_input("First Name", "Jane")
    st.sidebar.text_input("Last Name", "Smith")
    st.sidebar.text_input("Email", "jane.smith@example.com")
    st.sidebar.text_input("Phone", "+9876543210")
    st.sidebar.selectbox("Gender", ["Female", "Male"])

    st.sidebar.number_input("Pregnancies", 1)
    st.sidebar.number_input("Glucose", 90)
    st.sidebar.number_input("Blood Pressure", 60)
    st.sidebar.number_input("Insulin", 70)
    st.sidebar.number_input("BMI", 21.0)
    st.sidebar.number_input("Diabetes Pedigree", 0.2)
    st.sidebar.number_input("Age", 25)
    st.sidebar.number_input("Skin Thickness", 20)

# Run the Streamlit app
if __name__ == "__main__":
    main()
