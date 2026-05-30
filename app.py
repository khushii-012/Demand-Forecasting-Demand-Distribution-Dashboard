import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("demand_forecasting_model.pkl")

st.title("📈 Demand Forecasting Dashboard")

st.subheader("Enter Product Details")

item_id = st.number_input("Item ID", min_value=1, value=1)
price = st.number_input("Price", min_value=0.0, value=100.0)
promo = st.selectbox("Promotion", [0, 1])

month = st.slider("Month", 1, 12, 1)
year = st.slider("Year", 2019, 2025, 2024)
day = st.slider("Day", 1, 31, 1)
dayofweek = st.slider("Day of Week", 0, 6, 0)
quarter = st.slider("Quarter", 1, 4, 1)

if st.button("Predict Demand"):

    input_data = pd.DataFrame([[
        item_id,
        price,
        promo,
        month,
        year,
        day,
        dayofweek,
        quarter
    ]],
    columns=[
        'item_id',
        'price',
        'promo',
        'month',
        'year',
        'day',
        'dayofweek',
        'quarter'
    ])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Demand: {prediction[0]:.2f} units"
    )
