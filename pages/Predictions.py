import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings('ignore')
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/BankChurn/refs/heads/master/Customer-Churn-Records.csv')
df = df.drop('RowNumber', axis=1)
df

st.subheader("🔮 Customer Churn Prediction")
st.caption(
    "Enter customer details below to predict the likelihood of churn using the trained machine learning model."
)
st.divider()

st.markdown("""
<style>
.data-card {
    background-color: #0E594D;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    margin-bottom: 24px;
}
.data-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 8px;
}
.data-caption {
    font-size: 14px;
    color: #F1F2F3;
    margin-bottom: 12px;
}
.result-card {
    background-color: #0E594D;
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-top: 30px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

with st.expander("📄 View Training Dataset (Sample)", expanded=False):
    st.markdown('<div class="data-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="data-title">Model Training Data</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="data-caption">Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df.head(20),
        use_container_width=True,
        height=350
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🧾 Enter Customer Details")
st.divider()

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        Geography = st.selectbox('Country', ('Spain', 'France', 'Germany'))
        Gender = st.selectbox('Gender', ('Male', 'Female'))
        Age = st.number_input('Enter age(above 18) : ', min_value=18)

    with col2:
      Tenure = st.number_input('Enter the tenure of customer : ')
      IsActiveMember = st.number_input('Enter Customer is Active member(1) or not(0) : ')
      Complain = st.number_input('Whether Customer has Complaints(1) or not(0) : ')
      
    with col3:
      Balance = st.number_input('Enter the balance of Customer Account :', value=0.0)
      NumOfProducts = st.number_input('Enter the number of products that customer holds : ')

    submit = st.form_submit_button("🔍 Predict Churn")

if submit:
    data = {'Geography' : Geography,
        'Gender' : Gender,
        'Age' : Age,
        'Tenure' : Tenure,
        'Balance' : Balance,
        'NumOfProducts' : NumOfProducts,
        'IsActiveMember' : IsActiveMember,
        'Complain' : Complain,
        }


col_X=['Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'IsActiveMember', 'Complain']
X=df[col_X]
y = df[['Exited']]

input_df = pd.DataFrame(data, index=[0])
bank_churn = pd.concat([input_df,X], axis=0)
with st.expander('Your input data'):
  st.write('**This is the data you  have provided**')
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

if submit:
  if y_pred == 1:
      result_text = "⚠️ High Risk of Customer Churn"
      result_color = "#dc2626"
  else:
      result_text = "✅ Low Risk of Customer Churn"
      result_color = "#9AA316"
    
    st.markdown(
        f"""
        <div class="result-card">
            <h2 style="color:{result_color};">{result_text}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
