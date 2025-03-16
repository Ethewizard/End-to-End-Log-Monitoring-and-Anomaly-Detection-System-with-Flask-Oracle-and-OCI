import streamlit as st
import requests
import pandas as pd
import numpy as np
import time
from datetime import datetime

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

def generate_random_logs(n=5):
    """Generate random logs if no logs are available."""
    data = {
        "timestamp": [datetime.now().strftime('%Y-%m-%d %H:%M:%S') for _ in range(n)],
        "level": np.random.choice(["INFO", "WARNING", "ERROR", "DEBUG"], size=n),
        "message": np.random.choice(
            [
                "User login successful",
                "Failed to connect to database",
                "Request timeout",
                "Data ingestion completed",
                "Unauthorized access attempt"
            ], 
            size=n
        ),
        "source": np.random.choice(["API", "DB", "AUTH", "NETWORK"], size=n)
    }
    return pd.DataFrame(data)

log_placeholder = st.empty()

while True:
    logs = fetch_logs()
    
    if logs:
        df = pd.DataFrame(logs)
    else:
        st.warning("No logs available — Generating random logs...")
        df = generate_random_logs()

    log_placeholder.dataframe(df, height=300)
    
    time.sleep(2)
    st.rerun()  # Refresh UI properly
