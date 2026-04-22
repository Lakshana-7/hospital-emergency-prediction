import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('dataset.csv')
        return df
    except FileNotFoundError:
        return pd.DataFrame()

@st.cache_resource
def train_model(_df):
    if _df.empty:
        return None, None
        
    features = ['Previous_Day_Cases', 'Temperature', 'Holiday_Status', 'Flu_Cases', 
                'Day_of_Week', 'Humidity', 'Air_Quality_Index', 'Local_Event']
    
    # Check if new features exist
    missing_features = [f for f in features if f not in _df.columns]
    if missing_features:
        return None, None
        
    X = _df[features]
    y = _df['Emergency_Cases']
    
    model = LinearRegression()
    model.fit(X, y)
    return model, features

def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }
        
        .reportview-container {
            background: #f8f9fa;
        }
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .metric-card {
            background-color: white;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            text-align: center;
            border-top: 4px solid #ff4b4b;
        }
        .metric-value {
            font-size: 56px;
            font-weight: 800;
            color: #ff4b4b;
            line-height: 1.2;
        }
        .metric-label {
            color: #6c757d;
            font-size: 16px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        div[data-testid="stSidebarNav"] {
            padding-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
