import streamlit as st
import warnings


warnings.filterwarnings('ignore')
if "page_initialized" not in st.session_state:
    st.session_state.page_initialized = True
    welcome = st.Page("streamlit_app.py", title="Welcome", icon="🏦")
    prediction = st.Page("pages/Predictions.py", title="Predictions", icon="📊")
    dashboard = st.Page("pages/Dashboard.py", title="Dashboard", icon="📊")
    pg = st.navigation([welcome, prediction, dashboard])
    pg.run()
