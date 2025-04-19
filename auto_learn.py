import json
import os

def load_snapshot(snapshot_path):
    with open(snapshot_path, "r") as f:
        return json.load(f)

def auto_learn(snapshot_path):
    print(f"[*] Loading snapshot from {snapshot_path}")
    snapshot = load_snapshot(snapshot_path)

    keys = set()

    # If it's a dict, treat it as one record
    if isinstance(snapshot, dict):
        keys.update(snapshot.keys())

    # If it's a list, iterate through and gather keys
    elif isinstance(snapshot, list):
        for record in snapshot:
            if isinstance(record, dict):
                keys.update(record.keys())
            else:
                print(f"[!] Skipping non-dict record: {record}")

    else:
        print("[!] Unknown snapshot format")
        return

    print(f"[✓] Snapshot contains keys: {', '.join(keys)}")

    os.makedirs("profiles", exist_ok=True)
    profile_path = f"profiles/profile_auto_{os.path.basename(snapshot_path)}.json"
    with open(profile_path, "w") as f:
        json.dump({"learned_keys": list(keys)}, f, indent=2)

    print(f"[✓] Auto-learn profile saved to {profile_path}")
