
import streamlit as st
import pickle
import pandas as pd

st.title("Starbucks AI Project")
st.write("Ye hamara Starbucks Prediction Software hai")

# Model load karna
try:
    with open("starbucks_decision_tree_model.pkl", "rb") as f:
        model = pickle.load(f)
    st.success("Model Load Ho Gaya!")
except Exception as e:
    st.error(f"Model nahi mila: {e}")

st.write("Sir, ye model Decision Tree se train hua hai.")
