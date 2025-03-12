import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
        self.train_model()

    def train_model(self):
        # Sample data for training
        X = np.random.normal(0, 1, (100, 1))
        X[-5:] = X[-5:] + 10  # Inject anomalies
        self.model.fit(X)
        print("✅ Model trained")

    def predict(self, value):
        prediction = self.model.predict([[value]])
        return prediction[0] == -1

# Initialize globally for reuse
anomaly_detector = AnomalyDetector()
