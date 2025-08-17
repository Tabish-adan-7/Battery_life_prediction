import streamlit as st
import numpy as np
import os
import joblib


st.set_page_config(page_title="Battery Life Predictor", layout="centered")

st.title(" Battery Life Prediction App")
st.write("""
Estimate your device’s remaining battery life based on your unique usage and charging habits.
This model is optimized for devices that are 2–3 years old, where prediction accuracy is highest.
""")

st.header("Enter Your Device & Usage Details")

avg_daily_charge_cycles = st.number_input("Average Daily Charge Cycles", min_value=0.0, step=0.01)
avg_temp = st.number_input("Average Operating Temperature (°C)", min_value=0.0, step=0.1)
fast_charge_ratio = st.slider("Fast Charge Ratio", 0.0, 1.0, 0.5, step=0.01)
avg_discharge_depth = st.slider("Average Discharge Depth", 0.0, 1.0, 0.5, step=0.01)
usage_hours_per_day = st.number_input("Usage Hours Per Day", min_value=0.0, step=0.1)
battery_capacity = st.number_input("Current Battery Capacity (mAh)", min_value=0.0, step=10.0)
device_age_months = st.number_input("Device Age (Months)", min_value=0, step=1)
avg_charging_voltage = st.number_input("Average Charging Voltage (V)", min_value=0.0, step=0.01)
optimal_charging_time = st.number_input("Optimal Charging Time (Hours)", min_value=0.0, step=0.1)

#load saved model and predict
st.header("Prediction")

model_path = "battery_life_predictor.joblib"

#load model
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error(f"Model file not found at{model_path}. please upload it")
    st.stop()

#When user clicks predict
if st.button("Predict reamaining battery life"):
    features =  np.array([[avg_daily_charge_cycles, avg_temp, fast_charge_ratio,
                           avg_discharge_depth, usage_hours_per_day, battery_capacity,
                           device_age_months, avg_charging_voltage, optimal_charging_time]])
    prediction_months = model.predict(features)[0]
    prediction_years = prediction_months/12
    st.success(f"Estimated Remaining Battery Life: {prediction_months:.2f} months and ({prediction_years:.2f} years")