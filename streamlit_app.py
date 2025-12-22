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
  df = df.drop('RowNumber', axis=1)
  df
with st.expander('X dataframe'):
  st.write('**X**')
  col_X=['Complain', 'Age', 'IsActiveMember', 'Gender', 'Balance', 'Geography', 'NumOfProducts', 'Tenure']
  X=df[col_X]
  X


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
  HasCrCard = st.number_input('Enter Customer has Credit Card(1) or not(0) : ')
  IsActiveMember = st.number_input('Enter Customer is Active member(1) or not(0) : ')
  EstimatedSalary = st.number_input('Enter the estimated Salary of Customer :', value=0.0) 
  Complain = st.number_input('Whether Customer has Complaints(1) or not(0) : ')
  Satisfaction_Score = st.number_input('Enter the Satisfaction Score of customer(from 1 to 5) : ') 
  Card_Type = st.selectbox('Card Type', ('SILVER', 'GOLD', 'PLATINUM', 'DAIMOND'))
  Point_Earned = st.number_input('Enter the points earned by the Customer :', value=0.0)

data = {'CustomerId' : CustomerId,
        'Surname' : Surname,
        'CreditScore' : CreditScore,
        'Geography' : Geography,
        'Gender' : Gender,
        'Age' : Age,
        'Tenure' : Tenure,
        'Balance' : Balance,
        'NumOfProducts' : NumOfProducts,
        'HasCrCard' : HasCrCard,
        'IsActiveMember' : IsActiveMember,
        'EstimatedSalary' : EstimatedSalary,
        'Complain' : Complain,
        'Satisfaction Score' : Satisfaction_Score,
        'Card Type' : Card_Type,
        'Point Earned' : Point_Earned}

