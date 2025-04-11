import json
import argparse

def compare_profile(snapshot_file, baseline_file):
    with open(snapshot_file, 'r') as f:
        snapshot = json.load(f)

    with open(baseline_file, 'r') as f:
        baseline = json.load(f)

    device_match = snapshot.get("device") == baseline.get("device")
    protocol_match = snapshot.get("protocol") == baseline.get("protocol")
    event = snapshot.get("event")

    event_allowed = event in baseline.get("allowed_events", [])

    print("[*] Comparing snapshot to baseline...")
    if device_match and protocol_match and event_allowed:
        print("[+] Snapshot behavior matches baseline.")
    else:
        print("[!] Anomaly detected:")
        if not device_match:
            print(f"    - Device mismatch: {snapshot.get('device')} vs {baseline.get('device')}")
        if not protocol_match:
            print(f"    - Protocol mismatch: {snapshot.get('protocol')} vs {baseline.get('protocol')}")
        if not event_allowed:
            print(f"    - Event '{event}' is NOT in allowed list: {baseline.get('allowed_events')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare snapshot to behavioral baseline.")
    parser.add_argument('--snapshot', required=True, help="Path to decrypted snapshot JSON")
    parser.add_argument('--baseline', required=True, help="Path to baseline profile JSON")
    args = parser.parse_args()

    compare_profile(args.snapshot, args.baseline)
