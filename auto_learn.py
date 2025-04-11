import argparse
import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def auto_learn(snapshot_file, baseline_file):
    snapshot = load_json(snapshot_file)
    baseline = load_json(baseline_file)

    event = snapshot.get("event")
    allowed_events = baseline.get("allowed_events", [])

    print("\n===== Auto-Learn Review =====")
    print(f"Event: {event}")
    print(f"Currently Allowed Events: {allowed_events}")
    print("==============================")

    if event in allowed_events:
        print("[✓] Event already in baseline. No action needed.")
    else:
        decision = input(f"\nAdd '{event}' to baseline? (y/N): ").strip().lower()
        if decision == 'y':
            allowed_events.append(event)
            baseline["allowed_events"] = allowed_events
            save_json(baseline, baseline_file)
            print("[+] Event added to baseline.")
        else:
            print("[!] No changes made to baseline.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-learn from a snapshot.")
    parser.add_argument("--snapshot", required=True, help="Path to decrypted snapshot JSON.")
    parser.add_argument("--baseline", required=True, help="Path to baseline profile JSON.")
    args = parser.parse_args()

    auto_learn(args.snapshot, args.baseline)
