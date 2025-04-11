import argparse
import json
import requests


def send_alert(snapshot_path, webhook_url):
    with open(snapshot_path, 'r') as f:
        data = json.load(f)

    severity = data.get("severity", "").lower()
    event = data.get("event", "")
    device = data.get("device", "")
    timestamp = data.get("timestamp", "")
    
    if severity == "high":
        message = {
            "text": f"🚨 High Severity Alert from LineAlert!\n"
                    f"📅 Timestamp: {timestamp}\n"
                    f"🖥️ Device: {device}\n"
                    f"⚠️ Event: {event}\n"
                    f"🚨 Severity: HIGH"
        }

        try:
            response = requests.post(webhook_url, json=message)
            if response.status_code == 200:
                print("[+] Alert sent successfully.")
            else:
                print(f"[!] Failed to send alert: {response.status_code} {response.text}")
        except Exception as e:
            print(f"[!] Error sending alert: {e}")
    else:
        print("[i] No alert sent — severity is not high.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send LineAlert to webhook")
    parser.add_argument("--input", required=True, help="Path to decrypted snapshot JSON")
    parser.add_argument("--webhook", required=True, help="Webhook URL to send alert")
    args = parser.parse_args()

    send_alert(args.input, args.webhook)
