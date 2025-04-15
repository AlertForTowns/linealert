import argparse
import json
from signature_matcher import load_signatures, check_signatures

def load_snapshot(snapshot_path):
    with open(snapshot_path, "r") as f:
        return json.load(f)

def load_baseline(baseline_path):
    try:
        with open(baseline_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_baseline(baseline_path, baseline_data):
    with open(baseline_path, "w") as f:
        json.dump(baseline_data, f, indent=2)

def compare_to_baseline(snapshot, baseline):
    device = snapshot["device"]
    snapshot_codes = set(snapshot.get("function_codes", []))
    baseline_codes = set(baseline.get(device, []))

    new_codes = snapshot_codes - baseline_codes
    return list(new_codes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True, help="Path to snapshot file")
    parser.add_argument("--baseline", default="baseline.json", help="Path to baseline file")
    args = parser.parse_args()

    snapshot = load_snapshot(args.snapshot)
    baseline = load_baseline(args.baseline)
    signatures = load_signatures()

    new_behavior = compare_to_baseline(snapshot, baseline)

    # Signature-based detection
    sig_match = check_signatures(snapshot, signatures)

    if sig_match:
        print(f"🚨 Signature Match: Function Code {sig_match['matched_code']} ({sig_match['severity'].upper()})")
        print(f"📝 Description: {sig_match['description']}")
    elif new_behavior:
        print(f"📈 New behavior detected for {snapshot['device']}: {new_behavior}")
        baseline[snapshot["device"]] = list(set(baseline.get(snapshot["device"], [])) | set(new_behavior))
        save_baseline(args.baseline, baseline)
    else:
        print("✅ No new behavior detected. Baseline remains unchanged.")
