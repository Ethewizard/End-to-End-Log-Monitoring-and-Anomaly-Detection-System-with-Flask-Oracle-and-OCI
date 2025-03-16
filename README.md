Here’s the **combined and formatted README** with the updated project structure:

---

# 🚀 End-to-End Log Monitoring and Anomaly Detection System with Flask, Oracle, and OCI  

## 📝 **Project Overview**  
This project is a full-stack log monitoring and anomaly detection system using Flask, Oracle Autonomous Database, and OCI. It includes:  
✅ RESTful Flask API for log ingestion and retrieval  
✅ Oracle Autonomous Database for persistent storage  
✅ Machine learning-based anomaly detection using Isolation Forest  
✅ Streamlit dashboard for real-time visualization  
✅ Deployment with Docker and Kubernetes on OCI  

---

## 📂 **Project Structure**  
├── api.py                   # Handles log ingestion and processing
├── app.py                   # Flask application setup
├── Dockerfile               # Docker configuration
├── kubernetes-deployment.yaml # Kubernetes deployment setup
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


---

## 🎯 **Features**  
✅ Log ingestion and storage in Oracle Autonomous Database  
✅ Anomaly detection using Isolation Forest  
✅ RESTful API to fetch logs  
✅ Real-time dashboard using Streamlit  
✅ Containerized deployment with Docker  
✅ Scalable on Kubernetes and OCI  

---

## 🚀 **Step-by-Step Setup Guide**

### **1. Install Dependencies**  
Install required packages on Ubuntu:  
```bash
sudo apt update && sudo apt upgrade -y  
sudo apt install -y python3 python3-pip git docker.io docker-compose kubectl
```

---

### **2. Clone the Repository**  
```bash
git clone https://github.com/Ethewizard/End-to-End-Log-Monitoring-and-Anomaly-Detection-System-with-Flask-Oracle-and-OCI.git  
cd End-to-End-Log-Monitoring-and-Anomaly-Detection-System-with-Flask-Oracle-and-OCI
```

---

### **3. Set Up Virtual Environment**  
Create and activate a virtual environment:  
```bash
python3 -m venv venv  
source venv/bin/activate
```

---

### **4. Install Python Dependencies**  
```bash
pip install --upgrade pip  
pip install -r requirements.txt
```

---

### **5. Configure Oracle Database**  
1. Download Oracle Instant Client from [Oracle](https://www.oracle.com/database/technologies/instant-client.html).  
2. Unzip to `/opt/oracle/instantclient`.  
3. Set environment variables:  
```bash
export LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH  
export PATH=/opt/oracle/instantclient:$PATH  
export ORACLE_HOME=/opt/oracle/instantclient
```

---

### **6. Set Up Docker**  
Add Docker permissions:  
```bash
sudo usermod -aG docker $USER  
newgrp docker
```

Build and start Docker containers:  
```bash
docker-compose up --build -d
```

Verify running containers:  
```bash
docker ps
```

---

### **7. Deploy Kubernetes**  
Create a namespace:  
```bash
kubectl create namespace log-monitoring
```

Deploy Kubernetes objects:  
```bash
kubectl apply -f k8s-deployment.yaml -n log-monitoring
```

Check status:  
```bash
kubectl get pods -n log-monitoring
```

---

### **8. Start Flask API**  
```bash
python app.py
```

---

### **9. Start Streamlit Dashboard**  
```bash
streamlit run dashboard.py
```

---

### **10. Test Logs and Anomaly Detection**  
Send a test log:  
```bash
curl -X POST http://localhost:5000/logs -d '{"message": "Test log"}' -H "Content-Type: application/json"
```

---

### **11. Stop Services**  
Stop Flask:  
```bash
pkill -f app.py
```

Stop Docker:  
```bash
docker-compose down
```

Delete Kubernetes objects:  
```bash
kubectl delete -f k8s-deployment.yaml -n log-monitoring
```

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
✅ Add authentication for API security  
✅ Extend ML model with more complex features  
✅ Implement real-time alerting for anomalies  

---

## 🙌 **Contributing**  
Feel free to open an issue or submit a pull request!  

---

## 📄 **License**  
This project is licensed under the MIT License.  

---

This version is more polished and GitHub-ready! Let me know if you want to adjust anything. 😎
