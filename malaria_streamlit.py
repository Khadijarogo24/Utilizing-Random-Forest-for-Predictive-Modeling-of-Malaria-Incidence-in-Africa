import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

# Sample training data (for demo purpose)
data = pd.DataFrame({
    'Incidence of malaria (per 1,000 population at risk)': [100, 150, 80, 200],
    'Malaria cases reported': [3000, 5000, 2000, 7000],
    'Use of insecticide-treated bed nets (% of under-5 population)': [70, 50, 80, 40],
    'Children with fever receiving antimalarial drugs (% of children under age 5 with fever)': [60, 45, 70, 30],
    'Intermittent preventive treatment (IPT) of malaria in pregnancy (% of pregnant women)': [55, 30, 65, 25],
    'People using safely managed drinking water services (% of population)': [75, 60, 85, 55],
    'People using at least basic sanitation services (% of population)': [70, 50, 90, 40],
    'Malaria Risk': [1, 1, 0, 1]
})

X = data.drop('Malaria Risk', axis=1)
y = data['Malaria Risk']

model = RandomForestClassifier()
model.fit(X, y)

# Streamlit App Configuration
st.set_page_config(page_title="🌍 Malaria Risk Predictor", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #00796b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 6px;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🦟 Malaria Risk Prediction")
st.image("https://cdn.pixabay.com/photo/2016/08/05/10/43/mosquito-1574100_960_720.jpg", use_column_width=True)
st.markdown("""
Enter the relevant data below to predict the likelihood of malaria incidence in your area.
""")

# African countries list
african_countries = [
    "Nigeria", "Ghana", "Kenya", "Uganda", "Tanzania", "Ethiopia", "South Africa", "Cameroon", "Zimbabwe",
    "Zambia", "Sudan", "Senegal", "Mozambique", "Malawi", "Mali", "Niger", "Rwanda", "Burkina Faso",
    "Côte d'Ivoire", "Chad", "Angola", "Benin", "Botswana", "Burundi", "Central African Republic",
    "Congo", "DR Congo", "Djibouti", "Eritrea", "Gabon", "Gambia", "Guinea", "Guinea-Bissau",
    "Lesotho", "Liberia", "Madagascar", "Mauritania", "Namibia", "Sierra Leone", "Somalia", "South Sudan",
    "Swaziland", "Togo"
]

# Country selection
country = st.selectbox("Select African Country", african_countries)

# Input features
incidence = st.number_input("Incidence of malaria (per 1,000 population at risk)", min_value=0.0)
cases = st.number_input("Malaria cases reported", min_value=0)
bed_nets = st.number_input("Use of insecticide-treated bed nets (% of under-5 population)", min_value=0.0, max_value=100.0)
antimalarial = st.number_input("Children with fever receiving antimalarial drugs (% of children under age 5 with fever)", min_value=0.0, max_value=100.0)
iptd = st.number_input("Intermittent preventive treatment (IPT) of malaria in pregnancy (% of pregnant women)", min_value=0.0, max_value=100.0)
water = st.number_input("People using safely managed drinking water services (% of population)", min_value=0.0, max_value=100.0)
sanitation = st.number_input("People using at least basic sanitation services (% of population)", min_value=0.0, max_value=100.0)

# Prediction
data_store = []
if st.button("Predict Malaria Risk"):
    input_data = np.array([[
        incidence, cases, bed_nets, antimalarial, iptd, water, sanitation
    ]])
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")
    st.markdown(f"### Country Selected: **{country}**")

    result_text = "High Risk" if prediction == 1 else "Low Risk"

    if prediction == 1:
        st.error("⚠️ High Risk: Malaria is likely to be prevalent based on the data provided.")
        st.markdown("""
        ### 🚨 Recommendations:
        - Increase preventive measures like bed nets and IPT coverage.
        - Improve water and sanitation facilities.
        - Conduct further medical testing and interventions.
        """)
    else:
        st.success("✅ Low Risk: Malaria incidence appears to be low based on the data.")
        st.markdown("""
        ### 🛡️ Advice:
        - Continue maintaining good health infrastructure.
        - Ensure continuous access to preventive malaria care.
        """)

    st.markdown("""
    ---
    ### 🔍 Model Features and Interpretation:
    | Feature | High Risk Indicator | Low Risk Indicator |
    |--------|----------------------|--------------------|
    | **Incidence of malaria (per 1,000)** | High value → high chance | Low value → low chance |
    | **Malaria cases reported** | Higher number → higher chance | Fewer cases → lower chance |
    | **Use of bed nets (%)** | Low usage → higher chance | High usage → lower chance |
    | **Antimalarial drugs to children (%)** | Low % → higher chance | High % → lower chance |
    | **IPT in pregnancy (%)** | Low % → higher risk | High % → lower risk |
    | **Drinking water access (%)** | Low access → higher risk | High access → lower risk |
    | **Sanitation services (%)** | Poor sanitation → higher risk | Better sanitation → lower risk |
    """)

# Clear form button
if st.button("Clear Form"):
    st.experimental_rerun()
