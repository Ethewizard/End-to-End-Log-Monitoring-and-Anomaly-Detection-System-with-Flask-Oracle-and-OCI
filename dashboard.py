import requests
import streamlit as st

API_URL = "http://127.0.0.1:5000/logs"  # Make sure this URL points to your Flask API

# Fetch the logs from the Flask API
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json().get('data')  # Assuming the API response contains 'data'
    else:
        data = []
except requests.exceptions.RequestException as e:
    data = []
    st.error(f"Error fetching logs: {str(e)}")

# Display logs or handle empty log data
if data:
    st.write(f"Total Logs: {len(data)}")
    for log in data:
        st.write(f"Log ID: {log['log_id']} - Message: {log['log_message']} - Timestamp: {log['timestamp']}")
else:
    st.write("No logs available or unable to fetch logs.")

# Example anomaly detection (could be more complex based on your needs)
def detect_anomalies(logs):
    # Simple anomaly detection by checking for error messages
    anomalies = [log for log in logs if "error" in log['log_message'].lower()]
    return anomalies

# Run anomaly detection
anomalies = detect_anomalies(data)

if anomalies:
    st.subheader("Anomalies Detected")
    for anomaly in anomalies:
        st.write(f"Anomaly - Log ID: {anomaly['log_id']} - Message: {anomaly['log_message']} - Timestamp: {anomaly['timestamp']}")
else:
    st.write("No anomalies detected.")
