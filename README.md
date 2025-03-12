# 🚀 **End-to-End Log Monitoring and Anomaly Detection System with Flask, Oracle, and OCI**  
 

## 📝 **Project Overview**  
This project is a full-stack log monitoring and anomaly detection system using Flask, Oracle Autonomous Database, and OCI. It includes:  
✅ RESTful Flask API for log ingestion and retrieval  
✅ Oracle Autonomous Database for persistent storage  
✅ Machine learning-based anomaly detection using Isolation Forest  
✅ Streamlit dashboard for real-time visualization  
✅ Deployment with Docker and Kubernetes on OCI  

---

## 📂 **Project Structure**  
```
├── app.py               # Flask API for log ingestion and retrieval
├── db_setup.py          # Database connection and setup
├── anomaly_detection.py # Isolation Forest-based anomaly detection
├── dashboard.py         # Streamlit dashboard
├── Dockerfile           # Docker setup for deployment
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🎯 **Features**  
✅ Log ingestion and storage in Oracle Autonomous Database  
✅ Anomaly detection using Isolation Forest  
✅ RESTful API to fetch logs  
✅ Real-time dashboard using Streamlit  
✅ Containerized deployment with Docker  
✅ Scalable on Kubernetes and OCI  

---

## 🚀 **Getting Started**  
### 1. **Clone the Repository**  
```bash
git clone https://github.com/Ethewizard/End-to-End-Log-Monitoring-and-Anomaly-Detection-System-with-Flask-Oracle-and-OCI.git
cd your-repo
```

### 2. **Set Up the Environment**  
Create a virtual environment and install dependencies:  
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **Set Up Oracle Autonomous Database**  
- Download and configure Oracle Instant Client  
- Set up environment variables for `cx_Oracle`  

### 4. **Run Flask API**  
```bash
python app.py
```

### 5. **Test API**  
✅ Ping the API:  
```bash
curl http://127.0.0.1:5000/ping
```

✅ Insert Log:  
```bash
curl -X POST http://127.0.0.1:5000/log -H "Content-Type: application/json" -d '{"log_message": "Test log"}'
```

✅ Retrieve Logs:  
```bash
curl http://127.0.0.1:5000/logs
```

### 6. **Run Streamlit Dashboard**  
```bash
streamlit run dashboard.py
```

---

## 🧠 **Machine Learning - Isolation Forest**  
- Trained on sample data with synthetic anomalies  
- Real-time anomaly detection during log ingestion  
- Flags anomalies based on log length  

---

## 🐳 **Docker Build and Run**  
Build and run Docker container:  
```bash
docker build -t flask-api .
docker run -p 5000:5000 flask-api
```

---

## ☁️ **Deploy on OCI with Kubernetes**  
1. Tag and push to OCI Registry:  
```bash
docker tag flask-api your-oci-repo/flask-api:latest
docker push your-oci-repo/flask-api:latest
```

2. Deploy to Kubernetes:  
```bash
kubectl create deployment flask-api --image=your-oci-repo/flask-api:latest
kubectl expose deployment flask-api --type=LoadBalancer --port=5000
```

---

## 📸 **Demo**  
![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Demo+Screenshot)  

---

## 🏆 **Technologies Used**  
- **Python** – Core programming language  
- **Flask** – API development  
- **Oracle Autonomous Database** – Data storage  
- **Scikit-learn** – Machine learning  
- **Streamlit** – Dashboard  
- **Docker** – Containerization  
- **Kubernetes** – Orchestration  
- **OCI** – Cloud deployment  

---

## 🚨 **Potential Improvements**  
- Add authentication for API security  
- Extend ML model with more complex features  
- Implement real-time alerting for anomalies  

---

## 🙌 **Contributing**  
Feel free to open an issue or submit a pull request!  

---

## 📄 **License**  
This project is licensed under the [MIT License](LICENSE).  
