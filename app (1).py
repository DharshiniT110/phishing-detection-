import streamlit as st
import pandas as pd
import pickle

# Page config
st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Phishing Website Detection System")
st.write(
    "This application uses a **Tuned XGBoost model** to detect whether a website is "
    "**Phishing** or **Legitimate** based on URL features."
)

# Load trained model
@st.cache_resource
def load_model():
    with open("model/phishing_xgboost_tuned.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# Feature names (must match training order)
feature_names = [
    'having_IP_Address', 'URL_Length', 'Shortining_Service',
    'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
    'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
    'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
    'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
    'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
    'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
    'Google_Index', 'Links_pointing_to_page', 'Statistical_report'
]

st.subheader("📥 Enter Website Feature Values")

user_input = {}

for feature in feature_names:
    user_input[feature] = st.number_input(
        label=feature,
        value=0,

