import numpy as np
import streamlit as st
import pickle

model=pickle.load(open("C:/Users/soppoju narender/Desktop/FS-DataScience/ML_module/diabeties_prediction_system/Diabetes_Prediction_System.pkl","rb"))

def diabetes_pred(input_data):
    input_data_array=np.asarray(input_data)
    input_data_reshape=input_data_array.reshape(1,-1)
    prediction=model.predict(input_data_reshape)
    print(prediction)
    if (prediction[0] == 0):
        return "HURRAY!! YOU DONT HAVE DIABETES"
    else:
        return "SORRY YOU HAVE DIABETES"
    
def main():
    st.title("Diabetes Prediction System")
    #['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history',
     #  'bmi', 'HbA1c_level', 'blood_glucose_level', 'diabetes']
     #heart_disease=st.selectbox('Heart diasease History',['No ','Yes'])
 #  hypertension=st.selectbox('Hypertension',['No','Yes'])
  # gender=st.selectbox('gender',['Female','Male','others'])
 #  smoking_history=st.selectbox('Smoking History', ['Never','No info','current','former','ever','not current'])'''
    st.markdown(  "--->    0 = No and 1 = Yes")
    heart_disease=st.selectbox('Heart diasease History', {0:'no',1:'yes'})
    hypertension=st.selectbox('Hypertension', {0:'no',1:'yes'})
    st.markdown( "--->   0 = Female, 1 = Male , 2 = Others")
    gender=st.selectbox('gender', {0:'Female',1:'Male',2:'others'})
    st.markdown(''''"Never',1='No info',2='current',3='former',4='ever',5='not current''')
    smoking_history=st.selectbox('Smoking History', {0:'Never',1:'No info',2:'current',3:'former',4:'ever',5:'not current'})
    age=st.text_input('Enter your Age')
    bmi=st.text_input('Enter bmi Level')
    HbA1c_level=st.text_input('Enter HbA1c_level Level')
    blood_glucose_level=st.text_input('Enter blood_glucose_level ')
    diagnosis=''
    if st.button("Predict my Result"):
        diagnosis=diabetes_pred([heart_disease, hypertension,gender, smoking_history,age, bmi, HbA1c_level,blood_glucose_level])
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()