import json
import time
from datetime import datetime
from auto_learn import auto_learn  # Assuming this function is modularized
from send_alert import send_alert

def generate_snapshot(device_id, function_codes, snapshot_name):
    snapshot_data = {
        "device": device_id,
        "status": "active",
        "packets": 100 + len(function_codes) * 10,
        "function_codes": function_codes
    }
    with open(snapshot_name, "w") as f:
        json.dump(snapshot_data, f)

def simulate():
    device = "PLC-1"
    runs = [
        [3, 4],       # Normal
        [5, 6],       # New function codes
        [3, 4, 99],   # Anomalous
        [3, 4, 7, 8]  # Mixed
    ]

    for i, fc_list in enumerate(runs):
        snap_name = f"snapshot_{i+1}.lasnap"
        print(f"[+] Generating snapshot: {snap_name}")
        generate_snapshot(device, fc_list, snap_name)

        print(f"[+] Running auto-learn for {snap_name}")
        auto_learn(f"--snapshot {snap_name}".split())

        if 99 in fc_list:
            send_alert(
                device=device,
                alert_type="Anomaly",
                message="Function code 99 is highly unusual",
                severity="critical",
                snapshot_name=snap_name
            )

        time.sleep(2)

if __name__ == "__main__":
    simulate()
