import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import load_data, train_model, inject_custom_css

st.set_page_config(page_title="Predictor | Hospital Emergency", page_icon="🔮", layout="wide")
inject_custom_css()

st.title("🔮 Emergency Admission Predictor")
st.markdown("Enter today's parameters below to forecast the expected number of emergency patient admissions.")

df = load_data()
model, features = train_model(df)

if df.empty or model is None:
    st.error("Dataset not found or missing features! Please run the data generator.")
    st.stop()

# --- INPUT FORM ---
with st.container():
    st.markdown("### 📝 Input Parameters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏥 Healthcare")
        prev_cases = st.number_input("Previous Day Cases", min_value=0, max_value=200, value=int(df['Previous_Day_Cases'].mean()), step=1)
        flu_cases = st.number_input("Flu Cases", min_value=0, max_value=200, value=int(df['Flu_Cases'].mean()), step=1)
        
    with col2:
        st.subheader("🌦️ Environment")
        temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=float(df['Temperature'].mean()), step=0.1)
        humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=int(df['Humidity'].mean()), step=1)
        aqi = st.slider("Air Quality Index (AQI)", min_value=0, max_value=500, value=int(df['Air_Quality_Index'].mean()), step=5)
        
    with col3:
        st.subheader("📅 Time & Events")
        day_mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
        day_of_week = st.selectbox("Day of the Week", options=list(day_mapping.keys()), format_func=lambda x: day_mapping[x])
        holiday = st.selectbox("Holiday Status", options=[0, 1], format_func=lambda x: "Yes (Holiday)" if x == 1 else "No (Regular Day)")
        local_event = st.selectbox("Local Event / Mass Gathering", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

st.markdown("---")

# --- PREDICTION ---
input_data = pd.DataFrame({
    'Previous_Day_Cases': [prev_cases],
    'Temperature': [temperature],
    'Holiday_Status': [holiday],
    'Flu_Cases': [flu_cases],
    'Day_of_Week': [day_of_week],
    'Humidity': [humidity],
    'Air_Quality_Index': [aqi],
    'Local_Event': [local_event]
})

prediction = model.predict(input_data)[0]
prediction = max(int(np.round(prediction)), 0)

st.subheader("🎯 Prediction Result")
col_res1, col_res2 = st.columns([1, 2])

with col_res1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Expected Admissions</div>
        <div class="metric-value">{prediction}</div>
        <div style="color: gray; font-size: 14px; margin-top: 5px;">Patients</div>
    </div>
    """, unsafe_allow_html=True)
    
with col_res2:
    st.markdown("#### 🧠 Model Feature Impacts")
    display_names = {
        'Previous_Day_Cases': 'Prev. Day Cases',
        'Temperature': 'Temperature',
        'Holiday_Status': 'Holiday',
        'Flu_Cases': 'Flu Cases',
        'Day_of_Week': 'Day of Week',
        'Humidity': 'Humidity',
        'Air_Quality_Index': 'AQI',
        'Local_Event': 'Local Event'
    }
    formatted_features = [display_names[f] for f in features]
    coef_df = pd.DataFrame({'Feature': formatted_features, 'Impact (Coefficient)': model.coef_})
    
    fig, ax = plt.subplots(figsize=(8, 3.5))
    colors = ['#3498db' if c > 0 else '#e74c3c' for c in model.coef_]
    ax.barh(coef_df['Feature'], coef_df['Impact (Coefficient)'], color=colors)
    ax.set_xlabel('Weight/Impact on Prediction')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot(fig)
