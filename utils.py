import json
from cryptography.fernet import Fernet

# Replace with your actual key management system
AES_KEY = b'your-32-byte-base64-key-goes-here===='

def decrypt_snapshot(file_bytes):
    fernet = Fernet(AES_KEY)
    decrypted = fernet.decrypt(file_bytes)
    return decrypted.decode("utf-8")

def parse_snapshot(snapshot_str):
    return json.loads(snapshot_str)

def detect_alerts(snapshot):
    alerts = []
    devices = snapshot.get("devices", [])

    for device in devices:
        if device.get("unexpected_behavior"):
            alerts.append(
                f"{device['id']} ({device['ip']}) showed unexpected behavior: {device['unexpected_behavior']}"
            )

        if device.get("new_command_detected"):
            alerts.append(
                f"{device['id']} executed a new/unseen command: {device['new_command_detected']}"
            )

    return alerts

