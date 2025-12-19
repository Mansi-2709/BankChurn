import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(page_title="Bank Customer Churn Prediction & Customer Retention Dashboard", page_icon=":bank:",layout="wide")
st.title("🏦 Bank Customer Churn Prediction & Customer Retention Dashboard")
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/BankChurn/refs/heads/master/Customer-Churn-Records.csv')
  df
with st.expander('Input your data'):
  st.write('Input Feature Data')
