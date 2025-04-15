# =============================
# linealert-agent.py (Client)
# =============================

import requests
import socket
import uuid
import json
import os

CONFIG_SERVER_URL = "http://localhost:8000/api/init"  # Change to prod later
TENANT_KEY = "city_of_cobourg"  # Hardcoded for now
FIRMWARE_VERSION = "1.0.0"

RUNTIME_CONFIG_FILE = "runtime_config.json"

def get_device_id():
    hostname = socket.gethostname()
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
                    for ele in range(0,8*6,8)][::-1])
    return f"{hostname}_{mac[-5:].replace(':', '')}"

def register_with_server():
    device_id = get_device_id()
    payload = {
        "device_id": device_id,
        "tenant_key": TENANT_KEY,
        "version": FIRMWARE_VERSION
    }

    try:
        print(f"[>] Connecting to config server as {device_id}...")
        res = requests.post(CONFIG_SERVER_URL, json=payload, timeout=10)
        res.raise_for_status()

        config = res.json()
        with open(RUNTIME_CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"[+] Config received for tenant '{TENANT_KEY}':")
        print(json.dumps(config, indent=2))

        if config.get("firmware_update", {}).get("required"):
            print("[!] Firmware update required! Version:", config["firmware_update"]["latest_version"])
            print("    Download URL:", config["firmware_update"]["url"])
        else:
            print("[✓] Firmware is up to date.")

    except Exception as e:
        print("[X] Failed to contact config server:", str(e))

if __name__ == "__main__":
    register_with_server()
