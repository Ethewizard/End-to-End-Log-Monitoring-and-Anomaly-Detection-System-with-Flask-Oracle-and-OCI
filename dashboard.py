import requests
import streamlit as st

API_URL = "http://127.0.0.1:5000/logs"  # Make sure this is correct

# Fetch the logs from the Flask API
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json().get('data')  # Assuming the API response contains 'data'
    else:
        data = ''
except requests.exceptions.RequestException as e:
    data = ''
    st.error(f"Error fetching logs: {str(e)}")

# Check if data is None or empty before calling len()
if data is not None and len(data) > 0:
    st.write(f"Total Logs: {len(data)}")
else:
    st.write("No logs available or unable to fetch logs.")
