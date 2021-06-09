import streamlit as st
import joblib
model = joblib.load('sentiment-analysis')
st.title('sentiment-analysis')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
  
  
  
  
  
  
  
  
  
  
