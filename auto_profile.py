import json

def generate_profile(input_file, output_file):
    with open(input_file, 'r') as f:
        snapshot = json.load(f)

    profile = {
        "device": snapshot.get("device"),
        "protocol": snapshot.get("protocol"),
        "expected_behavior": ["read coils", "read registers"],
        "flagged_behavior": [snapshot["event"]],
        "severity": snapshot["severity"]
    }

    with open(output_file, 'w') as f:
        json.dump(profile, f, indent=2)

    print(f"Profile written to: {output_file}")
