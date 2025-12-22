import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

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
  col_X=['Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'IsActiveMember', 'Complain']
  X=df[col_X]
  X
with st.expander('Target Variable'):
  st.write('**y**')
  y = df[['Exited']]
  y


with st.expander('Input your data'):
  st.write('Input Feature Data')
  Geography = st.selectbox('Country', ('Spain', 'France', 'Germany'))
  Gender = st.selectbox('Gender', ('Male', 'Female'))
  Age = st.number_input('Enter age(above 18) : ')
  Tenure = st.number_input('Enter the tenure of customer : ')
  Balance = st.number_input('Enter the balance of Customer Account :', value=0.0)
  NumOfProducts = st.number_input('Enter the number of products that customer holds : ')
  IsActiveMember = st.number_input('Enter Customer is Active member(1) or not(0) : ')
  Complain = st.number_input('Whether Customer has Complaints(1) or not(0) : ')


data = {'Geography' : Geography,
        'Gender' : Gender,
        'Age' : Age,
        'Tenure' : Tenure,
        'Balance' : Balance,
        'NumOfProducts' : NumOfProducts,
        'IsActiveMember' : IsActiveMember,
        'Complain' : Complain,
        }

input_df = pd.DataFrame(data, index=[0])
bank_churn = pd.concat([input_df,X], axis=0)
with st.expander('Your input data'):
  st.write('**Input Data**')
  input_df
  encoder = LabelEncoder()
	bank_churn['Geography'] = encoder.fit_transform(bank_churn['Geography'])
  bank_churn['Gender'] = encoder.fit_transform(bank_churn['Gender'])
  bank_churn['Balance_exponential'] = bank_churn.Balance**(1/1.2)
  X = bank_churn[1:]
  clf = RandomForestClassifier(class_weight = {1:0,1: 4}, criterion = 'entropy', n_estimators = 30, random_state=42)
  clf.fit(X,y)
  input_df=bank_churn[:1]
	y_pred=clf.predict(input_df)

with st.expander('Predictions'):
  if y_pred == 1:
    st.write('The Customer will Exit.')
  else :
    st.write('The Customer will Not exit.')
