import streamlit as st
import pandas as pd
from utils import load_data, inject_custom_css

st.set_page_config(page_title="Dataset | Hospital Emergency", page_icon="📚", layout="wide")
inject_custom_css()

st.title("📚 Dataset Explorer")
st.markdown("Browse, filter, and download the raw historical data used by the prediction model.")

df = load_data()

if df.empty:
    st.error("Dataset not found!")
    st.stop()

st.markdown("### 🔍 Raw Data Viewer")

# Simple filtering
st.sidebar.header("Filter Data")
min_cases = st.sidebar.number_input("Min Emergency Cases", min_value=0, max_value=int(df['Emergency_Cases'].max()), value=0)
show_only_holidays = st.sidebar.checkbox("Show only holidays")

filtered_df = df[df['Emergency_Cases'] >= min_cases]
if show_only_holidays:
    filtered_df = filtered_df[filtered_df['Holiday_Status'] == 1]

st.dataframe(filtered_df, use_container_width=True, height=400)

st.markdown("### 📥 Export Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Current Dataset as CSV",
    data=csv,
    file_name='hospital_emergency_dataset.csv',
    mime='text/csv',
)

st.markdown("---")
st.markdown("### 📖 Data Dictionary")
st.markdown("""
* **Previous_Day_Cases**: Number of emergency admissions on the previous day.
* **Temperature**: Average daily temperature in Celsius.
* **Holiday_Status**: `1` if it is a public holiday, `0` otherwise.
* **Flu_Cases**: Estimated number of local active flu cases.
* **Day_of_Week**: `0` for Monday through `6` for Sunday.
* **Humidity**: Average daily humidity percentage.
* **Air_Quality_Index**: Local AQI. Higher values indicate worse air quality.
* **Local_Event**: `1` if a mass gathering or significant local event occurred, `0` otherwise.
* **Emergency_Cases**: (Target Variable) Actual number of emergency hospital admissions.
""")
