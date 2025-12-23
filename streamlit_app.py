import streamlit as st
import warnings


warnings.filterwarnings('ignore')
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("Home Page")
st.write("Welcome to the application.")
