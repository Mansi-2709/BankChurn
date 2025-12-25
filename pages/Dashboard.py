import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

st.title("Bank Churn Dashboard :money_with_wings:")
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/BankChurn/refs/heads/master/Customer-Churn-Records.csv')

fig = px.histogram(df, x="Age", color="Exited")
st.plotly_chart(fig, use_container_width=True)

fig1 = px.histogram(df, x="Gender", color="Exited")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(df, x="Tenure", color="Exited")
st.plotly_chart(fig2, use_container_width=True)

df["Exited"] = df["Exited"].astype(str)
fig3 = px.bar(df, x="Geography", color="Exited", barmode="group",
    color_discrete_map={
        "0": "green",
        "1": "orange"
    })
st.plotly_chart(fig3, use_container_width=True)
