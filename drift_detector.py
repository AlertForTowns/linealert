import json
from datetime import datetime

# ------------------------
# Loaders
# ------------------------

def load_json(path):
    with open(path) as f:
        return json.load(f)

# ------------------------
# Drift Core
# ------------------------

def calculate_drift(baseline, snapshot):
    drift_report = []
    total_drift = 0
    drift_count = 0

    for base_device in baseline["devices"]:
        ip = base_device["ip"]
        match = next((dev for dev in snapshot["devices"] if dev["ip"] == ip), None)
        if not match:
            continue

        for base_fn in base_device["functions"]:
            fn_code = base_fn["function_code"]
            base_count = base_fn["count"]

            snap_fn = next((fn for fn in match["functions"] if fn["function_code"] == fn_code), None)
            if not snap_fn:
                continue

            current_count = snap_fn["count"]
            if base_count == 0:
                continue  # Avoid division by zero

            drift = abs(current_count - base_count) / base_count * 100

            drift_type = classify_drift_type(base_count, current_count)

            drift_report.append({
                "ip": ip,
                "function_code": fn_code,
                "baseline": base_count,
                "current": current_count,
                "drift_percent": round(drift, 2),
                "type": drift_type
            })

            total_drift += drift
            drift_count += 1

    avg_drift = total_drift / drift_count if drift_count else 0
    return drift_report, round(avg_drift, 2)

# ------------------------
# Drift Classifier
# ------------------------

def classify_drift_type(baseline, current):
    if current > baseline:
        return "upward"
    elif current < baseline:
        return "downward"
    else:
        return "no change"

# ------------------------
# Logger
# ------------------------

def log_alerts(drift_report, avg_drift, log_file="drift_alerts.txt"):
    with open(log_file, "w") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not drift_report:
            f.write(f"[{timestamp}] No significant drift detected.\n")
            return

        f.write(f"[{timestamp}] DRIFT DETECTED\n")
        for entry in drift_report:
            f.write(
                f"  Device: {entry['ip']}, Function: {entry['function_code']}, "
                f"Drift: {entry['drift_percent']}% (Baseline: {entry['baseline']}, "
                f"Current: {entry['current']}, Type: {entry['type']})\n"
            )
        f.write(f"  Total Drift Score: {avg_drift}%\n")

# ------------------------
# Runner
# ------------------------

def main(baseline_path, snapshot_path):
    baseline = load_json(baseline_path)
    snapshot = load_json(snapshot_path)
    report, avg_drift = calculate_drift(baseline, snapshot)
    log_alerts(report, avg_drift)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 drift_detector.py baseline.json snapshot.json")
    else:
        main(sys.argv[1], sys.argv[2])
