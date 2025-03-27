# -*- coding: utf-8 -*-
"""app1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FudByi0kaYEd9puqX1Oj5jR-34QmZWqJ
"""


import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and feature names
model = joblib.load("xgb_churn_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Streamlit App Title
st.title("🔮 Customer Churn Prediction App")
st.markdown("Enter customer details below to predict churn.")

# Function to take user input
def user_input():
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    Dependents = st.selectbox("Has Dependents", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    tenure = st.slider("Tenure (months)", 0, 72, 24)
    PhoneService = st.selectbox("Phone Service", [0, 1])
    MultipleLines = st.selectbox("Multiple Lines", [0, 1])
    InternetService = st.selectbox("Internet Service Type", [0, 2], format_func=lambda x: ["DSL", "Fiber Optic", "No"][x])
    OnlineSecurity = st.selectbox("Online Security", [0, 1])
    OnlineBackup = st.selectbox("Online Backup", [0, 1])
    DeviceProtection = st.selectbox("Device Protection", [0, 1])
    TechSupport = st.selectbox("Tech Support", [0, 1])
    StreamingTV = st.selectbox("Streaming TV", [0, 1])
    StreamingMovies = st.selectbox("Streaming Movies", [0, 1])
    Contract = st.selectbox("Contract Type", [0, 2], format_func=lambda x: ["Month-to-Month", "One Year", "Two Year"][x])
    PaperlessBilling = st.selectbox("Paperless Billing", [0, 1])
    PaymentMethod = st.selectbox("Payment Method", [0, 3], format_func=lambda x: ["Electronic Check", "Mailed Check", "Bank Transfer", "Credit Card"][x])
    MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=10.0, max_value=120.0, value=50.0, step=1.0)
    TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, max_value=9000.0, value=1200.0, step=50.0)

    # Create DataFrame
    data = pd.DataFrame([[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines,
                          InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
                          StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
                          MonthlyCharges, TotalCharges]],
                          columns=feature_names)

    return data

# Get user input
input_data = user_input()

# Predict Churn
if st.button("Predict"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]

    # Display Result
    if prediction[0] == 1:
        st.error(f"⚠️ High Churn Risk! Probability: {probability[0]:.2f}")
    else:
        st.success(f"✅ Low Churn Risk! Probability: {probability[0]:.2f}")



