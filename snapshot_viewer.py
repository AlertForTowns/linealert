import json
import argparse

def load_snapshots(file):
    with open(file, 'r') as f:
        data = json.load(f)
        return data if isinstance(data, list) else [data]

def display(snapshots, severity_filter=None):
    for snap in snapshots:
        if severity_filter and snap.get("severity") != severity_filter:
            continue
        print(json.dumps(snap, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Snapshot Viewer CLI")
    parser.add_argument("--input", required=True, help="Path to decrypted JSON file")
    parser.add_argument("--severity", help="Optional severity filter: low/medium/high")
    args = parser.parse_args()

    snapshots = load_snapshots(args.input)
    display(snapshots, severity_filter=args.severity)
