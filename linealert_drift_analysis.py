import sys
import json
from datetime import datetime

DRIFT_THRESHOLD = 2.0  # seconds (sustained variation)
WINDOW_SIZE = 5        # moving window size

def load_snapshot(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    timestamps = [pkt['timestamp'] for pkt in data.get('packets', [])]
    return [float(t) for t in timestamps if t]

def detect_drift(timestamps):
    if len(timestamps) < 2:
        return []

    intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    baseline = sum(intervals[:WINDOW_SIZE]) / WINDOW_SIZE
    drift_points = []

    for i in range(WINDOW_SIZE, len(intervals)):
        window_avg = sum(intervals[i-WINDOW_SIZE:i]) / WINDOW_SIZE
        drift = abs(window_avg - baseline)

        if drift > DRIFT_THRESHOLD:
            drift_points.append({
                "index": i,
                "timestamp": timestamps[i],
                "drift": drift,
                "type": "AFib-style timing anomaly"
            })

    return drift_points

def write_report(drift_data, out_path):
    with open(out_path, 'w') as f:
        for event in drift_data:
            f.write(f"{event['timestamp']:.3f}s — Drift={event['drift']:.3f}s at packet #{event['index']} ({event['type']})\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 linealert_drift_analysis.py <snapshot.lasnap>")
        sys.exit(1)

    snap_path = sys.argv[1]
    try:
        ts = load_snapshot(snap_path)
        drift_data = detect_drift(ts)
        out_file = snap_path.replace('.lasnap', '_drift_report.txt')
        write_report(drift_data, out_file)
        print(f"[✅] Drift report written: {out_file}")
    except Exception as e:
        print(f"[❌] Error: {e}")

