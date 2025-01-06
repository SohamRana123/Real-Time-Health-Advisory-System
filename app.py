
# Frontend (Streamlit Dashboard)
import streamlit as st
import pandas as pd

# Simulated data for the frontend (placeholder for live updates)
def load_data():
    return pd.DataFrame([
        {"timestamp": "2025-01-01 12:00", "heart_rate": 80, "steps": 5000, "calories": 200},
        {"timestamp": "2025-01-01 12:01", "heart_rate": 85, "steps": 5200, "calories": 210},
        {"timestamp": "2025-01-01 12:02", "heart_rate": 90, "steps": 5300, "calories": 220},
    ])

# Streamlit Dashboard
st.title("Real-Time Health Advisory System")
data = load_data()
st.write("### Live Health Data")
st.dataframe(data)

st.write("### Personalized Recommendations")
st.write("Stay hydrated after exercise to maintain energy.")
st.write("Walking 10,000 steps daily improves cardiovascular health.")
