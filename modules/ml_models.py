import numpy as np
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split


class AnomalyDetector:
    def __init__(self):
        self.random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
        self.isolation_forest = IsolationForest(random_state=42, contamination=0.1)
        self.dbscan = DBSCAN(eps=0.5, min_samples=5)

    def train_supervised(self, X, y):
        """Train supervised model for defect prediction."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.random_forest.fit(X_train, y_train)
        return self.random_forest.score(X_test, y_test)

    def detect_anomalies(self, X):
        """Detect anomalies using multiple methods."""
        # Isolation Forest
        if_predictions = self.isolation_forest.fit_predict(X)

        # DBSCAN
        dbscan_predictions = self.dbscan.fit_predict(X)

        return {
            'isolation_forest': if_predictions,
            'dbscan': dbscan_predictions
        }

    def predict_defect_probability(self, X):
        """Predict defect probability using Random Forest."""
        return self.random_forest.predict_proba(X)[:, 1]
