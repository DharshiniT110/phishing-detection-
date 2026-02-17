import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Phishing Website Detection System")
st.write(
    "This application uses a **Tuned XGBoost Model** to detect whether a website is "
    "**Phishing** or **Legitimate** based on 30 URL-based features."
)

# ---------------

