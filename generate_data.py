import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 365 days of data
days = 365

# Features
# Previous Day Cases: typically between 20 to 100
prev_cases = np.random.randint(20, 100, days)

# Temperature: typical values between 0 to 40 Celsius
temperature = np.random.uniform(0, 40, days)

# Holiday Status: 1 if holiday, 0 otherwise (approx 10% holidays)
holiday_status = np.random.choice([0, 1], days, p=[0.9, 0.1])

# Flu Cases: typically between 0 to 50
flu_cases = np.random.randint(0, 50, days)

# NEW FEATURES:
# Day of the Week: 0 (Monday) to 6 (Sunday)
day_of_week = np.arange(days) % 7

# Humidity: percentage 20% to 100%
humidity = np.random.uniform(20, 100, days)

# Air Quality Index: 0 to 300
aqi = np.random.randint(0, 300, days)

# Local Event: 1 if there's a large event, 0 otherwise (approx 5% events)
local_event = np.random.choice([0, 1], days, p=[0.95, 0.05])


# Target: Current Day Emergency Cases
# Linear relation with noise: 
# y = 10 + 0.5*prev - 0.2*temp + 15*holiday + 0.8*flu + noise
# New components:
# Monday (0) might have more cases (+5), Weekend (5,6) might have slightly more (+3)
day_impact = np.where(day_of_week == 0, 5, np.where(day_of_week >= 5, 3, 0))

# Humidity impact (high humidity -> slightly more cases)
humidity_impact = 0.05 * humidity

# AQI impact (high AQI -> respiratory issues -> more cases)
aqi_impact = 0.03 * aqi

# Local event impact (+10 cases)
event_impact = 10 * local_event

noise = np.random.normal(0, 5, days)
emergency_cases = (10 + 
                   0.5 * prev_cases - 
                   0.2 * temperature + 
                   15 * holiday_status + 
                   0.8 * flu_cases + 
                   day_impact + 
                   humidity_impact + 
                   aqi_impact + 
                   event_impact +
                   noise).astype(int)

# Ensure no negative cases
emergency_cases = np.maximum(emergency_cases, 0)

# Create DataFrame
df = pd.DataFrame({
    'Previous_Day_Cases': prev_cases,
    'Temperature': np.round(temperature, 1),
    'Holiday_Status': holiday_status,
    'Flu_Cases': flu_cases,
    'Day_of_Week': day_of_week,
    'Humidity': np.round(humidity, 1),
    'Air_Quality_Index': aqi,
    'Local_Event': local_event,
    'Emergency_Cases': emergency_cases
})

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("Successfully generated dataset.csv with 365 records including new features.")
