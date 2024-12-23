This project is a simple web-based application built using Streamlit, designed to predict whether a person is diabetic or not based on their medical details. It uses a pre-trained machine learning model to make predictions.

Technologies Used
Python: Backend programming.
Streamlit: Framework for building the web app.
Numpy: For data handling and array manipulations.
Pickle: For loading the trained machine learning model.

Input Fields
The app requires the following inputs from the user:

Number of Pregnancies: Number of times pregnant.
Glucose Level: Plasma glucose concentration (mg/dL).
Blood Pressure: Diastolic blood pressure (mm Hg).
Skin Thickness: Triceps skinfold thickness (mm).
Insulin: 2-hour serum insulin (mu U/ml).
BMI: Body Mass Index (weight in kg/(height in m)^2).
Diabetes Pedigree Function: Genetic predisposition score.
Age: Age in years.

How to Run the Project
-Install Dependencies

Ensure Python is installed on your system.
Install required libraries:
pip install streamlit numpy
-Prepare the Environment
Ensure the pre-trained model file (diabetes_model.sav) is in the same directory as the script.
-Run the Application
Open the terminal and navigate to the project folder.
Run the following command:
streamlit run app.py
Replace app.py with the filename of your script.
-Access the App

Open your browser and go to http://localhost:8501.

Folder Structure:
diabetes-prediction/
│
├── diabetes.py                 # Main application script
├── diabetes_model.sav     # Pre-trained machine learning model
└── README.md              # Project documentation
