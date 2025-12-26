# 🏦 Bank Customer Churn Prediction – End-to-End ML Project
## 📌 Project Overview

Customer churn is a major challenge in the banking industry, leading to revenue loss and increased customer acquisition costs.
This project builds an end-to-end machine learning pipeline to predict whether a bank customer is likely to churn, and deploys the final model using an interactive Streamlit application.

The solution combines data analysis, feature engineering, model experimentation, evaluation using ROC-AUC, and a production-style dashboard for exploration and prediction.

## 🎯 Objectives

- Analyze customer behavior and identify churn patterns
- Perform robust feature engineering and model experimentation
- Select the best-performing model based on ROC-AUC
- Deploy the model via a user-friendly Streamlit web app
- Present insights in a business-interpretable manner

## 🧠 Machine Learning Workflow

All modeling and experimentation are implemented in a separate notebook/script included in this repository.

1. Data Understanding & Cleaning

- Removed non-informative identifiers (RowNumber, CustomerId, Surname)
- Checked missing values and data consistency
- Treated categorical and numerical features appropriately

2. Feature Engineering

- Encoding categorical variables (Gender, Geography)
- Binary transformation of behavioral indicators:
  - Active Member
  - Complaints
- Feature scaling where required
- Target variable: Exited (0 = Retained, 1 = Churned)

3. Model Experimentation<br/>
Multiple classification models were trained and evaluated:
      - Random Forest
      - XGBoost
      - Decision Tree

4. Model Evaluation & Selection

Primary evaluation metric: ROC-AUC

Cross-validated performance comparison

Final model selected based on:

Highest ROC-AUC

Stability and generalization performance

The selected model is then serialized and used in the Streamlit application.
