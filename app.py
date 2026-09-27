from flask import Flask, render_template, jsonify, request
from service.ai_detector import AnomalyDetector

app = Flask(__name__)
detector = AnomalyDetector(threshold=1.8)

# Simulated traffic log store
traffic_logs = [12, 15, 14, 13, 15, 110, 14, 12, 130, 15, 11]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['GET'])
def analyze():
    result = detector.analyze_logs(traffic_logs)
    return jsonify({
        "metrics": traffic_logs,
        "analysis": result
    })

@app.route('/api/log', methods=['POST'])
def add_log():
    data = request.get_json()
    count = data.get('count', 0)
    traffic_logs.append(count)
    return jsonify({"message": "Log recorded", "current_total": len(traffic_logs)})

if __name__ == '__main__':
    # Flask running on port 5000 accessible locally
    app.run(host='0.0.0.0', port=5000, debug=True)
