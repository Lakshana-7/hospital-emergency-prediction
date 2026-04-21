# hospital-emergency-prediction
A machine learning project using Linear Regression and Streamlit to predict hospital emergency admissions based on healthcare data.

# 🏥 Hospital Emergency Prediction System

## 📌 Overview
The **Hospital Emergency Prediction System** is a machine learning-powered web application developed to predict the number of emergency patient admissions in hospitals.

This project uses **Linear Regression** to forecast emergency cases based on healthcare-related parameters such as previous day admissions, temperature, holiday status, and flu cases.

It is designed to assist hospitals in **resource planning, emergency preparedness, and efficient patient care management**.

---

## 🎯 Objective
To build a predictive analytics system that estimates hospital emergency admissions using machine learning techniques.

---

## 🛠️ Technologies Used
- 🐍 Python
- 📊 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 📈 Matplotlib
- 🌐 Streamlit

---

## 🧠 Machine Learning Algorithm
### 📍 Linear Regression

The model follows the equation:

y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \beta_4x_4

Where:
- **y** → Predicted emergency cases
- **x₁** → Previous day cases
- **x₂** → Temperature
- **x₃** → Holiday status
- **x₄** → Flu cases

---

## ✨ Features
- 📈 Predicts hospital emergency admissions
- 💻 Interactive GUI built with Streamlit
- ⚡ Real-time user input and instant prediction
- 📋 Dataset preview table
- 📊 Trend visualization using graphs
- 🧾 Clean and user-friendly dashboard

---

## 📂 Project Structure

```text
hospital-emergency-prediction-system/
│
├── app.py
├── dataset.csv
├── requirements.txt
└── README.md
```

---

## 📝 Input Parameters
The model takes the following inputs:

- 🏥 Previous Day Cases
- 🌡️ Temperature
- 🎉 Holiday Status
- 🤒 Flu Cases

---

## 🎯 Output
- 📌 Predicted number of hospital emergency admissions

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit Application
```bash
streamlit run app.py
```

---

## 💡 Applications
This system can help hospitals in:

- 👩‍⚕️ Doctor and nurse scheduling
- 🛏️ Emergency bed allocation
- 💊 Medicine stock preparation
- 🚑 Emergency response planning
- 📅 Daily hospital resource management

---

## 🚀 Future Enhancements
- 🌍 Use real-world hospital datasets
- 🤖 Implement advanced ML models (Random Forest / XGBoost)
- ☁️ Deploy as a live web application
- 📊 Add advanced dashboards and analytics
- 🔗 Integrate with hospital databases

---

## 👩‍💻 Developed By
**Lakshana**  
🎓 B.Tech – Artificial Intelligence and Data Science  
📚 Mini Project – Machine Learning
