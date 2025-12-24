import streamlit as st
import warnings
import time


warnings.filterwarnings('ignore')
st.set_page_config(
    page_title="Bank Churn App",
    page_icon="🏦",
    layout="wide"
)
st.title(" Welcome ")

# Simple generator function
def slow_echo(text, delay=0.05):
    for char in text:
        yield char
        time.sleep(delay)


message = "This App predicts whether a bank customer will exit or not based on the some parameters that you will provide."
message1 = "Select which page you want to go to from the side panel."
message2 = "Dashboard - This page will let you know about the trends which decide which customer stay and which leave."
message3 = "Predictions - This page will predict whether the customer will stay based on parameters you input into the app"
# Display the message with a cursor
with st.chat_message("user"):
    st.write_stream(slow_echo(message, delay=0.02), cursor="⚡")
    st.write_stream(slow_echo(message1, delay=0.02), cursor="⚡")
    st.write_stream(slow_echo(message2, delay=0.02), cursor="⚡")
    st.write_stream(slow_echo(message3, delay=0.02), cursor="⚡")

