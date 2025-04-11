# auto_profile.py
import json
import os
from datetime import datetime

def load_profile(profile_path):
    if os.path.exists(profile_path):
        with open(profile_path, 'r') as f:
            return json.load(f)
    return {
        "device": None,
        "protocols_seen": [],
        "event_types": [],
        "severity_levels": [],
        "first_seen": None,
        "last_seen": None
    }

def update_profile(profile, snapshot):
    changed = False

    if profile["device"] is None:
        profile["device"] = snapshot["device"]
        changed = True

    if snapshot["protocol"] not in profile["protocols_seen"]:
        profile["protocols_seen"].append(snapshot["protocol"])
        changed = True

    if snapshot["event"] not in profile["event_types"]:
        profile["event_types"].append(snapshot["event"])
        changed = True

    if snapshot["severity"] not in profile["severity_levels"]:
        profile["severity_levels"].append(snapshot["severity"])
        changed = True

    timestamp = snapshot["timestamp"]
    if profile["first_seen"] is None or timestamp < profile["first_seen"]:
        profile["first_seen"] = timestamp
        changed = True

    if profile["last_seen"] is None or timestamp > profile["last_seen"]:
        profile["last_seen"] = timestamp
        changed = True

    return profile, changed

def main(snapshot_path):
    with open(snapshot_path, 'r') as f:
        snapshot = json.load(f)

    device_name = snapshot["device"].replace(" ", "_")
    profile_path = f"profiles/profile_{device_name}.json"
    os.makedirs("profiles", exist_ok=True)

    profile = load_profile(profile_path)
    updated_profile, changed = update_profile(profile, snapshot)

    if changed:
        with open(profile_path, 'w') as f:
            json.dump(updated_profile, f, indent=2)
        print(f"[+] Profile updated for device: {snapshot['device']}")
    else:
        print(f"[-] No changes made to profile for device: {snapshot['device']}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to decrypted snapshot JSON file")
    args = parser.parse_args()
    main(args.input)
