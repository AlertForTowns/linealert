# webhook_alert.py
import json
import requests
from datetime import datetime

def send_webhook_alert(alert_data, webhook_url):
    """
    Sends alert data to the specified webhook URL (e.g., Slack, Discord).
    """
    timestamp = datetime.utcnow().isoformat() + "Z"
    alert_data["timestamp"] = timestamp

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(alert_data))
        if response.status_code == 200 or response.status_code == 204:
            print(f"✅ Webhook alert sent at {timestamp}")
        else:
            print(f"⚠️ Webhook alert failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Exception sending webhook alert: {e}")

# Example usage:
if __name__ == "__main__":
    test_alert = {
        "device": "PLC-1",
        "code": 43,
        "severity": "medium",
        "description": "Test alert via webhook"
    }
    test_url = "https://your-webhook-url.com"  # Replace with real webhook
    send_webhook_alert(test_alert, test_url)
