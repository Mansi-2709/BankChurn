import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.io as pio
import os
import warnings
warnings.filterwarnings('ignore')

st.title("Bank Churn Dashboard :money_with_wings:")
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/BankChurn/refs/heads/master/Customer-Churn-Records.csv')
pio.templates.default = "plotly_dark"

def style_fig(fig, title):
    fig.update_layout(
        title=dict(text=title, x=0.5),
        font=dict(size=14),
        margin=dict(t=60, l=40, r=40, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        height=380
    )
    return fig

st.markdown("""
<style>
.chart-card {
    background-color: #0E594D;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    margin-bottom: 24px;
}
.chart-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 8px;
}
.chart-caption {
    font-size: 14px;
    color: #F1F2F3;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

fig_age_churn = px.histogram(df, x="Age", color="Exited")
fig_gender_churn = px.histogram(df, x="Gender", color="Exited")
fig_geo_churn = px.histogram(df, x="Geography", color="Exited", barmode="group")
fig_tenure_churn = px.histogram(df, x="Tenure", color="Exited", barmode="group")
fig_active_churn = px.histogram(df, x="IsActiveMember", color="Exited", barmode="group")
fig_products_churn = px.histogram(df, x="NumOfProducts", color="Exited", barmode="group")
fig_balance_dist = px.histogram(df, x="Balance", color="Exited", barmode="group")
fig_complaints_churn = px.histogram(df, x="Complain", color="Exited", barmode="group")

st.subheader("👥 Customer Demographics & Profile")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Age vs Churn</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-caption">Distribution of customer age by churn status</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_age_churn, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Gender vs Churn</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-caption">Churn comparison across gender categories</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_gender_churn, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="chart-card">', unsafe_allow_html=True)
st.markdown('<div class="chart-title">Geography vs Churn</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-caption">Regional churn distribution highlights geographic risk patterns</div>', unsafe_allow_html=True)
st.plotly_chart(style_fig(fig_geo_churn, ""), use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🔗 Customer Engagement & Relationship")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Tenure vs Churn</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_tenure_churn, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Active Member vs Churn</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_active_churn, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Number of Products vs Churn</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_products_churn, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.subheader("⚠️ Risk & Financial Indicators")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Complaints vs Churn</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-caption">Customers with complaints show significantly higher churn risk</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_complaints_churn, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Balance Distribution</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-caption">Account balance distribution across customer base</div>', unsafe_allow_html=True)
    st.plotly_chart(style_fig(fig_balance_dist, ""), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

