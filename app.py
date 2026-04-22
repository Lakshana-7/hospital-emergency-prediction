import streamlit as st
from utils import inject_custom_css

st.set_page_config(
    page_title="Hospital Emergency Prediction", 
    page_icon="🏥", 
    layout="wide",
    initial_sidebar_state="expanded"
)
inject_custom_css()

st.title("🏥 Hospital Emergency Prediction System")
st.markdown("### Welcome to the Hospital Analytics Platform")
st.markdown("""
This system uses **Machine Learning** to help hospital administration and emergency departments forecast patient admissions based on historical data, environmental conditions, and local events.

#### 🧭 Navigation
Please use the sidebar on the left to navigate through the platform:
- **🔮 Predictor:** Enter today's metrics to get a real-time prediction of expected emergency admissions.
- **📊 Dashboard:** View interactive charts analyzing historical trends and the impact of different factors (like AQI or temperature) on hospital visits.
- **📚 Dataset:** Browse, filter, and download the historical data that powers our AI model.

#### 🧠 How it Works
The underlying AI uses a **Linear Regression** model trained on a full year of historical hospital data. It analyzes complex relationships between:
*   Core healthcare metrics (Previous Day Cases, Flu Cases)
*   Environmental conditions (Temperature, Humidity, Air Quality Index)
*   Time and events (Day of the Week, Holidays, Local Mass Gatherings)
""")

st.info("👈 Select a tool from the sidebar to get started.")
