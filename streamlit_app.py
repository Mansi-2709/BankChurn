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
  CustomerId = st.number_input('Enter 8 digit CustomeId :')
  Surname = st.text_input('Enter Customer Surname :')
  CreditScore = st.number_input('Enter Credit Score of Customer starting from 350 to 850 :')
  Geography = st.selectbox('Country', ('Spain', 'France', 'Germany'))
  Gender = st.selectbox('Gender', ('Male', 'Female'))
  Age = st.number_input('Enter age(above 18) : ')
  Tenure = st.number_input('Enter the tenure of customer : ')
  Balance = st.number_input('Enter the balance of Customer Account :', value=0.0)
  NumOfProducts = st.number_input('Enter the number of products that customer holds : ')
  HasCrCard             0
  IsActiveMember        0
  EstimatedSalary       0
  Exited                0
  Complain              0
  Satisfaction Score    0
  Card Type             0
  Point Earned          0
  
