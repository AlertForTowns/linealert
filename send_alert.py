import json
from datetime import datetime
import os

def send_alert(alert_data):
    alert_data["timestamp"] = datetime.utcnow().isoformat() + "Z"
    alert_path = "alerts/alert_log.jsonl"
    
    # Make sure alerts directory exists
    os.makedirs("alerts", exist_ok=True)

    with open(alert_path, "a") as f:
        f.write(json.dumps(alert_data) + "\n")
