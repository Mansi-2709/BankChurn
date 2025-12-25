import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

st.title("Bank Churn Dashboard :money_with_wings:", layout="wide")
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/BankChurn/refs/heads/master/Customer-Churn-Records.csv')
