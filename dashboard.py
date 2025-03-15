import streamlit as st
import cx_Oracle
import pandas as pd

# Oracle Autonomous Database connection
def get_db_connection():
    dsn = cx_Oracle.makedsn("hostname", "port", service_name="service_name")
    connection = cx_Oracle.connect(user="username", password="password", dsn=dsn)
    return connection

# Fetch logs from the database
def fetch_logs():
    conn = get_db_connection()
    query = "SELECT * FROM logs ORDER BY timestamp DESC"
    logs_df = pd.read_sql(query, conn)
    conn.close()
    return logs_df

# Display logs in Streamlit
st.title("Log Monitoring and Anomaly Detection")
st.subheader("Real-time Log Visualization")

# Display logs in a table
logs_df = fetch_logs()
st.dataframe(logs_df)
