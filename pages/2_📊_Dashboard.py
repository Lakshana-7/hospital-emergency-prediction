import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, inject_custom_css

st.set_page_config(page_title="Dashboard | Hospital Emergency", page_icon="📊", layout="wide")
inject_custom_css()

st.title("📊 Analytics Dashboard")
st.markdown("Explore historical trends and relationships in the hospital admission data.")

df = load_data()

if df.empty:
    st.error("Dataset not found!")
    st.stop()

# Create dummy dates for plotting purposes (assuming past 365 days ending today)
dates = pd.date_range(end=pd.Timestamp.today(), periods=len(df))
df_display = df.copy()
df_display['Date'] = dates

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Admissions (Year)", f"{df['Emergency_Cases'].sum():,}")
col2.metric("Daily Average", f"{int(df['Emergency_Cases'].mean())}")
col3.metric("Max Daily Admissions", f"{df['Emergency_Cases'].max()}")
col4.metric("Average AQI", f"{int(df['Air_Quality_Index'].mean())}")

st.markdown("---")

# --- CHARTS ---
st.subheader("📈 Admission Trends Over Time")
fig_time = px.line(df_display, x='Date', y='Emergency_Cases', 
                   title='Daily Emergency Admissions (Past Year)',
                   labels={'Emergency_Cases': 'Emergency Cases'},
                   color_discrete_sequence=['#ff4b4b'])
fig_time.update_layout(xaxis_title="Date", yaxis_title="Number of Patients", hovermode="x unified")
st.plotly_chart(fig_time, use_container_width=True)

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("🌫️ AQI vs Admissions")
    fig_aqi = px.scatter(df, x='Air_Quality_Index', y='Emergency_Cases', 
                         trendline="ols",
                         title="Impact of Air Quality on Emergencies",
                         color='Emergency_Cases',
                         color_continuous_scale='Reds')
    st.plotly_chart(fig_aqi, use_container_width=True)

with col_chart2:
    st.subheader("🤒 Flu Cases vs Admissions")
    fig_flu = px.scatter(df, x='Flu_Cases', y='Emergency_Cases', 
                         trendline="ols",
                         title="Correlation: Flu Season and Hospital Visits",
                         color='Emergency_Cases',
                         color_continuous_scale='Blues')
    st.plotly_chart(fig_flu, use_container_width=True)
    
st.subheader("📅 Admissions by Day of the Week")
day_map = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
df_display['Day_Name'] = df_display['Day_of_Week'].map(day_map)
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Calculate average per day
avg_by_day = df_display.groupby('Day_Name')['Emergency_Cases'].mean().reindex(day_order).reset_index()

fig_day = px.bar(avg_by_day, x='Day_Name', y='Emergency_Cases', 
                 title="Average Admissions by Day of Week",
                 color='Emergency_Cases',
                 color_continuous_scale='Purples')
st.plotly_chart(fig_day, use_container_width=True)
