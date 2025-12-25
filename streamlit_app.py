import streamlit as st
import warnings
import time

warnings.filterwarnings('ignore')
st.set_page_config(
    page_title="Bank Churn App",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.intro-card {
    background-color: #0E594D;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 25px;
}

.intro-title {
    font-size: 36px;
    font-weight: 700;
    color: #EFF2F6;
}

.intro-text {
    font-size: 17px;
    color: #F0F2F4;
    line-height: 1.7;
}

.feature-box {
    background-color: #0E594D;
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="intro-card">
        <div class="intro-title">🏦 Bank Customer Churn Prediction</div>
        <p class="intro-text">
        Customer churn is a major challenge in the banking sector, directly affecting profitability and customer lifetime value.
        This application uses machine learning to predict whether a customer is likely to leave the bank based on key
        demographic, financial, and behavioral attributes.
        </p>
        <p class="intro-text">
        By identifying high-risk customers early, banks can take proactive steps to improve retention and optimize
        customer engagement strategies.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h4>📊 Data-Driven</h4>
        <p>Uses historical customer data including credit score, tenure, balance, and product usage.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h4>🤖 Machine Learning</h4>
        <p>Trained classification model predicts churn probability with explainable insights.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h4>💡 Business Impact</h4>
        <p>Helps retention teams prioritize high-risk customers and reduce churn proactively.</p>
    </div>
    """, unsafe_allow_html=True)


