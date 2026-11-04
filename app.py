import streamlit as st
import pandas as pd
import joblib
import json

st.title("Employee Attrition Prediction App")

# Load resources
model = joblib.load('model.pkl')
with open('feature_columns.json', 'r') as f:
    features = json.load(f)

st.write("### Model Features:")
st.write(features)
