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

Here’s a step-by-step guide to launching your log monitoring and anomaly detection system on a Linux machine.

---

### **Step 1: Install Required Dependencies**  
Ensure your Linux machine has Python, Docker, and Kubernetes installed.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip docker.io kubectl
```

Verify installations:

```bash
python3 --version
pip3 --version
docker --version
kubectl version --client
```

---

### **Step 2: Clone the Repository**  
Clone your project from GitHub.

```bash
git clone https://github.com/<your-username>/End-to-End-Log-Monitoring-and-Anomaly-Detection-System-with-Flask-Oracle-and-OCI.git
cd End-to-End-Log-Monitoring-and-Anomaly-Detection-System-with-Flask-Oracle-and-OCI

```

---

### **Step 3: Set Up Virtual Environment (Optional but Recommended)**  
Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### **Step 4: Configure Oracle Autonomous Database Connection**  
Modify `api.py` to include your Oracle DB connection details.

```python
conn = cx_Oracle.connect("user/password@dbhost:port/service")
```

Ensure the `cx_Oracle` package is installed.

```bash
pip install cx_Oracle
```

---

### **Step 5: Run Flask API Locally**  
Start the API server.

```bash
python api.py
```

Test if the API is running:

```bash
curl http://localhost:5000/logs
```

---

### **Step 6: Run Streamlit Dashboard**  
Open a new terminal and start the dashboard.

```bash
streamlit run app.py
```

Access the dashboard at:  
👉 `http://localhost:8501`

---

### **Step 7: Start Log Feeder**  
Open another terminal and run the log generator script.

```bash
python log_feeder.py
```

---

### **Step 8: Build and Run with Docker**  
Ensure Docker is running.

```bash
sudo systemctl start docker
```

Build the Docker images:

```bash
docker build -t log-monitoring-api -f Dockerfile .
docker run -p 5000:5000 log-monitoring-api
```

For the UI:

```bash
docker build -t log-monitoring-ui -f Dockerfile .
docker run -p 8501:8501 log-monitoring-ui
```

---

### **Step 9: Deploy on Kubernetes (OCI or Local Minikube)**  
If using Minikube, start it:

```bash
minikube start
```

Apply Kubernetes configurations:

```bash
kubectl apply -f kubernetes-deployment.yaml
```

Check running pods:

```bash
kubectl get pods
```

Expose the service:

```bash
kubectl expose deployment log-monitoring --type=LoadBalancer --port=80
```

Get the service URL:

```bash
minikube service log-monitoring-service --url
```

Access your app at the provided URL.

---

### **Step 10: Monitor Logs and Anomalies**  
Check logs:

```bash
kubectl logs -l app=log-monitoring
```

Test anomaly detection API:

```bash
curl http://localhost:5000/detect_anomalies
```

---

🚀 **Your system is now live!** Let me know if you need additional configurations.

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
