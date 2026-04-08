import streamlit as st
import numpy as np
import pickle

# load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Rock vs Mine Prediction")

st.write("Enter 60 sonar values separated by commas")

input_data = st.text_input("Input values")

if st.button("Predict"):
    
    data = np.array(list(map(float, input_data.split(",")))).reshape(1,-1)

    prediction = model.predict(data)

    if prediction[0] == 'R':
        st.success("The object is a Rock")
    else:
        st.error("The object is a Mine")