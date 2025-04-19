import json
import os
from drift_detector import calculate_drift, log_alerts

# ----------------------------
# Test Case Definition
# ----------------------------

TEST_CASES = [
    {
        "name": "Mild upward drift",
        "description": "Increase function counts by 30%",
        "multiplier": 1.3,
        "expected_drift": True
    },
    {
        "name": "Downward drift",
        "description": "Decrease function counts by 40%",
        "multiplier": 0.6,
        "expected_drift": True
    },
    {
        "name": "No drift (control)",
        "description": "Same function counts",
        "multiplier": 1.0,
        "expected_drift": False
    }
]

# ----------------------------
# Snapshot Generator
# ----------------------------

def inject_drift(baseline_data, multiplier):
    new_data = {"devices": []}
    for device in baseline_data["devices"]:
        new_device = {"ip": device["ip"], "functions": []}
        for fn in device["functions"]:
            new_fn = {
                "function_code": fn["function_code"],
                "count": int(fn["count"] * multiplier)
            }
            new_device["functions"].append(new_fn)
        new_data["devices"].append(new_device)
    return new_data

# ----------------------------
# Test Runner
# ----------------------------

def run_tests(baseline_path):
    baseline = json.load(open(baseline_path))

    for test in TEST_CASES:
        print(f"\n🧪 Running Test: {test['name']}")
        print(f"→ {test['description']}")

        # Generate snapshot
        snapshot = inject_drift(baseline, test["multiplier"])
        temp_snapshot_path = "temp_snapshot.json"
        json.dump(snapshot, open(temp_snapshot_path, "w"), indent=2)

        # Run drift detection
        drift_report, avg_drift = calculate_drift(baseline, snapshot)

        # Evaluate pass/fail
        if test["expected_drift"] and avg_drift > 0:
            result = "✅ PASS"
        elif not test["expected_drift"] and avg_drift == 0:
            result = "✅ PASS"
        else:
            result = "❌ FAIL"

        print(f"→ Avg Drift: {avg_drift}% — {result}")
        log_alerts(drift_report, avg_drift, log_file=f"test_log_{test['name'].replace(' ', '_')}.txt")

    # Cleanup
    if os.path.exists(temp_snapshot_path):
        os.remove(temp_snapshot_path)

# ----------------------------
# Run It
# ----------------------------

if __name__ == "__main__":
    run_tests("baseline.json")
