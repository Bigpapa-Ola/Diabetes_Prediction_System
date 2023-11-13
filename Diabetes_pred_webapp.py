import numpy as np
import streamlit as st
import pickle
import sklearn

# Load the machine learning model
model = pickle.load(open("Diabetes_Prediction_System.pkl", "rb"))

# Function to predict diabetes
def diabetes_pred(input_data):
    input_data_array = np.asarray(input_data)
    input_data_reshape = input_data_array.reshape(1, -1)
    prediction = model.predict(input_data_reshape)
    if prediction[0] == 0:
        return "HURRAY!! YOU DON'T HAVE DIABETES"
    else:
        return "SORRY, YOU HAVE DIABETES"

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/premium-photo/background-diabetic-disease-concept-with-copy-space-world-diabetes-day-banner_132254-879.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

st.markdown(
    """
    <style>
    /* CSS for title */
    .title {
        font-size: 36px;
        color: white; /* Black font color */
        text-align: center;
        background-color: black; /* White background color */
        padding: 10px; /* Add padding for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define custom CSS for styling
custom_css = """
<style>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
h1 {
    text-align: center;
}
form {
    display: flex;
    flex-direction: column;
    align-items: center;
}
select, input[type="text"] {
    width: 100%;
    max-width: 300px;
    padding: 5px;
    margin: 5px;
}
button {
    background-color: #008CBA;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #005F7F;
}
.success-message {
    text-align: center;
    font-weight: bold;
    padding: 20px;
}
</style>
"""

def main():
    # Add custom CSS to the page
    st.markdown(custom_css, unsafe_allow_html=True)

    st.markdown('<h1 class="title">Diabetes Prediction System</h1><br>', unsafe_allow_html=True)
    st.markdown("Fill in the information below to predict your diabetes status.")
    
    # Define options for selectboxes
    yes_no_options = {'No': 0, 'Yes': 1}
    gender_options = {'Female': 0, 'Male': 1, 'Others': 2}
    smoking_history_options = {'Never': 0, 'No info': 1, 'Current': 2, 'Former': 3, 'Ever': 4, 'Not Current': 5}
    
    # Place input controls in the sidebar
    with st.sidebar:
        heart_disease = st.selectbox('Heart disease history', list(yes_no_options.keys()))
        hypertension = st.selectbox('Hypertension', list(yes_no_options.keys()))
        gender = st.selectbox('Gender', list(gender_options.keys()))
        smoking_history = st.selectbox('Smoking History', list(smoking_history_options.keys()))
    
    age = st.text_input('Enter your Age')
    bmi = st.text_input('Enter BMI Level')
    HbA1c_level = st.text_input('Enter HbA1c Level')
    blood_glucose_level = st.text_input('Enter Blood Glucose Level')
    
    diagnosis = ''
    if st.button("Predict my Result"):
        # Convert selected options to numerical values
        heart_disease = yes_no_options[heart_disease]
        hypertension = yes_no_options[hypertension]
        gender = gender_options[gender]
        smoking_history = smoking_history_options[smoking_history]
        
        diagnosis = diabetes_pred([heart_disease, hypertension, gender, smoking_history, age, bmi, HbA1c_level, blood_glucose_level])
    
    st.markdown("<h1 class='title'>" + diagnosis + "</h1>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()

    
    st.markdown("<h1 class='title'>" + diagnosis + "</h1>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
