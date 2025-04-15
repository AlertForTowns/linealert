import argparse
import json
import os

parser = argparse.ArgumentParser(description="LineAlert Snapshot Viewer")
parser.add_argument('--input', required=True, help='Path to .lasnap snapshot file')
args = parser.parse_args()

if not os.path.exists(args.input):
    print("[!] File not found.")
    exit(1)

with open(args.input, 'r') as f:
    data = json.load(f)

print("\n====== LineAlert Snapshot Viewer ======\n")

print("📅 Timestamp :", data.get("timestamp", "N/A"))
print("🖥️ Device    :", data.get("device", "N/A"))
print("🔌 Protocol  :", data.get("protocol", "N/A"))
print("⚠️  Status    :", data.get("status", "N/A"))
print("📦 Packets   :", data.get("packets", "N/A"))
print("🟢 Severity  :", data.get("severity", "N/A"))

print("\n=======================================\n")
