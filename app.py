import streamlit as st
import requests
import pandas as pd
import time

st.title("Live Log Monitoring Dashboard")

API_URL = "http://localhost:5000/logs"

def fetch_logs():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

log_placeholder = st.empty()
while True:
    logs = fetch_logs()
    df = pd.DataFrame(logs)
    log_placeholder.dataframe(df)
    time.sleep(2)
