import streamlit as st
import warnings


warnings.filterwarnings('ignore')
st.set_page_config(
    page_title="Bank Churn App",
    page_icon="🏦",
    layout="wide"
)

st.title(" Welcome ")
st.write("This App predicts whether a bank customer will exit or not based on the some parameters that you will provide.")
st.write("Select which page you want to go to from the side panel.")
st.write("Dahsboard - This page will let you know about the trends which decide which customer stay and which leave.")
st.write("Predict - This page will predict whether the customer will stay based on parameters you input into the app")
