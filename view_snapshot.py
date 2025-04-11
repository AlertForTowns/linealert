# view_snapshot.py
import json
import argparse

def display_snapshot(snapshot_path):
    try:
        with open(snapshot_path, 'r') as f:
            data = json.load(f)

        print("\n====== LineAlert Snapshot Viewer ======\n")
        print(f"📅 Timestamp : {data.get('timestamp', 'N/A')}")
        print(f"🖥️ Device    : {data.get('device', 'N/A')}")
        print(f"🔌 Protocol  : {data.get('protocol', 'N/A')}")
        print(f"⚠️  Event     : {data.get('event', 'N/A')}")
        
        severity = data.get('severity', 'N/A').lower()
        if severity in ['high', 'critical']:
            print(f"🚨 Severity  : {severity.upper()} ⚠️")
        else:
            print(f"🟢 Severity  : {severity.capitalize()}")

        print("\n=======================================\n")

    except FileNotFoundError:
        print("[!] File not found.")
    except json.JSONDecodeError:
        print("[!] Invalid JSON file.")
    except Exception as e:
        print(f"[!] Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View a LineAlert snapshot file.")
    parser.add_argument("--input", required=True, help="Path to the .json snapshot file")
    args = parser.parse_args()

    display_snapshot(args.input)
