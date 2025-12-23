import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings('ignore')
st.title("Welcome")
welcome = st.Page("streamlit_app.py", title="Welcome", icon="🏦")
prediction = st.Page("pages/Predictions.py", title="Predictions", icon="📊")
dashboard = st.Page("pages/Dashboard.py", title="Dashboard", icon="📊")
pg = st.navigation([welcome, prediction, dashboard])
pg.run()
