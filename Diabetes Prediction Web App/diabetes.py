import numpy as np
import pickle
import streamlit as st


# Load the trained model
loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Function for diabetes prediction
def diabetes_prediction(input_data):
    input_data_as_nparray = np.asarray(input_data, dtype=float)  # Ensure inputs are converted to float
    input_data_reshaped = input_data_as_nparray.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction == 0:
        return 'Non Diabetic'
    else:
        return 'Diabetic'

# Main function for the web app
def main():
    st.title('Diabetes Prediction Web App')

    # Input fields
    Pregnancies = st.text_input('No. of Pregnancies:')
    Glucose = st.text_input('Glucose level:')
    BloodPressure = st.text_input('Blood Pressure value:')
    SkinThickness = st.text_input('Skin thickness value:')
    Insulin = st.text_input('Insulin level:')
    BMI = st.text_input('BMI value:')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value:')
    Age = st.text_input('Age:')

    diagnosis = ''

    # Button for prediction
    if st.button('Predict'):
        try:
            # Convert inputs to float and make prediction
            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        except ValueError:
            diagnosis = 'Invalid input. Please ensure all inputs are numerical.'

    st.success(diagnosis)

# Entry point
if _name_ == '_main_':
    main()
