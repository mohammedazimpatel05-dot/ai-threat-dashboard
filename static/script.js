async function fetchAnalysis() {
    try {
        const response = await fetch('/api/analyze');
        const data = await response.json();
        
        document.getElementById('status').innerText = data.analysis.status;
        document.getElementById('mean').innerText = data.analysis.mean_traffic || 0;
        document.getElementById('anomalies').innerText = data.analysis.anomalies_found || 0;
        document.getElementById('log-data').innerText = JSON.stringify(data.metrics, null, 2);
    } catch (err) {
        console.error("Failed to fetch dashboard data:", err);
    }
}

window.onload = fetchAnalysis;
