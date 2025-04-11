import json
from datetime import datetime
from cryptography.fernet import Fernet
import os

# Load the AES encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# Sample snapshot data – replace this dict with your real data input
snapshot_data = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "device": "Simulated PLC-1",
    "protocol": "Modbus",
    "event": "Unauthorized coil write",
    "severity": "high"
}

# Convert to JSON and encrypt
snapshot_json = json.dumps(snapshot_data).encode()
encrypted_data = fernet.encrypt(snapshot_json)

# Create filename with UTC timestamp
timestamp_str = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
filename = f"snapshots/snapshot_{timestamp_str}.lasnap"

# Ensure snapshots/ exists
os.makedirs("snapshots", exist_ok=True)

# Save encrypted data
with open(filename, "wb") as f:
    f.write(encrypted_data)

print(f"[+] Snapshot saved and encrypted as: {filename}")
