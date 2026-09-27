import numpy as np

class AnomalyDetector:
    def __init__(self, threshold=2.0):
        # Threshold multiplier based on standard deviations
        self.threshold = threshold

    def analyze_logs(self, request_counts):
        """
        Analyzes a list of request counts using Z-score calculation.
        """
        if not request_counts or len(request_counts) < 3:
            return {"status": "insufficient_data", "anomalies": []}

        data = np.array(request_counts)
        mean = np.mean(data)
        std_dev = np.std(data)

        if std_dev == 0:
            return {"status": "normal", "anomalies": []}

        # Calculate Z-scores
        z_scores = (data - mean) / std_dev
        anomaly_indices = np.where(np.abs(z_scores) > self.threshold)[0].tolist()

        return {
            "status": "threat_detected" if anomaly_indices else "normal",
            "mean_traffic": float(mean),
            "anomalies_found": len(anomaly_indices),
            "flagged_indices": anomaly_indices
        }
