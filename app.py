import streamlit as st
import requests
import pandas as pd
import time

st.title("Live Log Monitoring Dashboard")

API_URL = "http://localhost:5000/logs"

@st.cache_data(ttl=2)  # Cache data for 2 seconds to reduce API load
def fetch_logs():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching logs: {e}")
    return []

log_placeholder = st.empty()

while True:
    logs = fetch_logs()
    
    if logs:
        df = pd.DataFrame(logs)
        log_placeholder.dataframe(df)
    else:
        log_placeholder.write("No logs available.")
    
    time.sleep(2)
    st.rerun()  # Refresh UI properly
