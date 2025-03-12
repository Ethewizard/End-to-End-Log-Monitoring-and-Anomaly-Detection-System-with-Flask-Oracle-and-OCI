from flask import Flask, request, jsonify
from db_setup import insert_log, query_logs
from anomaly_detection import anomaly_detector

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "success", "message": "API is running"}), 200

@app.route('/log', methods=['POST'])
def add_log():
    try:
        data = request.get_json()
        log_message = data.get('log_message')

        if not log_message:
            return jsonify({"status": "error", "message": "Missing log_message"}), 400
        
        # Anomaly detection
        is_anomaly = anomaly_detector.predict(len(log_message))
        status = "anomaly" if is_anomaly else "normal"

        insert_log(f"{status} - {log_message}")
        return jsonify({"status": "success", "message": f"Log added (status: {status})"}), 201
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        logs = query_logs()
        return jsonify({"status": "success", "data": logs}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
