from flask import Flask, request, jsonify
from datetime import datetime
import cx_Oracle
import random
import os
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)
LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]

# Oracle DB Connection using environment variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_service = os.getenv("DB_SERVICE")

if None in (db_user, db_password, db_host, db_port, db_service):
    print("Error: One or more required environment variables are missing.")
    conn, cursor = None, None
else:
    try:
        dsn = f"{db_host}:{db_port}/{db_service}"
        conn = cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn)
        cursor = conn.cursor()
    except cx_Oracle.DatabaseError as e:
        print(f"Database connection error: {e}")
        conn, cursor = None, None

@app.route("/logs", methods=["POST"])
def ingest_log():
    if not conn:
        return jsonify({"error": "Database connection not available"}), 500
    
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_level = data.get("level", random.choice(LOG_LEVELS))
    message = data.get("message", "Generated log entry")
    
    try:
        cursor.execute("INSERT INTO logs (timestamp, level, message) VALUES (:1, :2, :3)", (timestamp, log_level, message))
        conn.commit()
        return jsonify({"status": "success"}), 201
    except cx_Oracle.DatabaseError as e:
        return jsonify({"error": str(e)}), 500

@app.route("/logs", methods=["GET"])
def retrieve_logs():
    if not conn:
        return jsonify({"error": "Database connection not available"}), 500
    
    try:
        cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC FETCH FIRST 50 ROWS ONLY")
        logs = [dict(timestamp=row[0], level=row[1], message=row[2]) for row in cursor.fetchall()]
        return jsonify(logs)
    except cx_Oracle.DatabaseError as e:
        return jsonify({"error": str(e)}), 500

@app.route("/detect_anomalies", methods=["GET"])
def detect_anomalies():
    if not conn:
        return jsonify({"error": "Database connection not available"}), 500
    
    try:
        cursor.execute("SELECT timestamp, level FROM logs")
        data = cursor.fetchall()
        if not data:
            return jsonify([])
        
        feature_data = np.array([[hash(row[1])] for row in data])
        model = IsolationForest(contamination=0.1)
        model.fit(feature_data)
        anomalies = model.predict(feature_data)
        
        anomaly_logs = [dict(timestamp=data[i][0], level=data[i][1], anomaly=bool(anomalies[i] == -1)) for i in range(len(data))]
        return jsonify(anomaly_logs)
    except cx_Oracle.DatabaseError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
