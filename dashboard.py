import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/logs"

st.title("📊 Log Monitoring Dashboard")

response = requests.get(API_URL)
data = response.json().get('data', [])

st.write(f"Total Logs: {len(data)}")

for row in data:
    log_id, message, created_at = row
    color = "red" if "anomaly" in message else "green"
    st.markdown(f"<span style='color:{color}'>{message} ({created_at})</span>", unsafe_allow_html=True)
