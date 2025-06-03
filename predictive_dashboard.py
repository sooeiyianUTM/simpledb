import streamlit as st
import pandas as pd
import joblib

st.title("Revenue Prediction Dashboard")

# Load model
model = joblib.load("revenue_model.pkl")

# Sidebar input
units = st.slider("Units Sold", 10, 100)
region = st.selectbox("Region", ["North", "South", "East", "West"])
product = st.selectbox("Product", ["Widget", "Gadget", "Tool", "Device"])

# Prepare input
input_df = pd.DataFrame({
    "units_sold": [units],
    "region": [region],
    "product": [product]
})

# Predict
predicted_revenue = model.predict(input_df)[0]
st.metric("Predicted Revenue", f"${predicted_revenue:,.2f}")
