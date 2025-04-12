import os
import json
import datetime
import subprocess
from scapy.all import sniff, IP, TCP

# === Configuration ===
INTERFACE = "eth0"  # Change if needed
SNAPSHOT_DIR = "snapshots"
DEFAULT_PASSWORD = "linealertdefault"

# === Ensure output directory exists ===
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

# === Generate timestamped filenames ===
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
output_file = os.path.join(SNAPSHOT_DIR, f"snapshot_{timestamp}.lasnap")
encrypted_output_file = os.path.join(SNAPSHOT_DIR, f"encrypted_{timestamp}.lasnap")

# === Packet filter for Modbus TCP ===
def filter_packet(packet):
    return IP in packet and TCP in packet and packet[TCP].dport == 502

# === Packet handler ===
def handle_packet(packet):
    summary = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "src": packet[IP].src,
        "dst": packet[IP].dst,
        "proto": "TCP",
        "sport": packet[TCP].sport,
        "dport": packet[TCP].dport,
        "len": len(packet),
        "payload": str(bytes(packet[TCP].payload).hex())
    }
    packet_list.append(summary)

# === Capture packets ===
print("[*] Capturing Modbus TCP traffic on port 502...")
packet_list = []
sniff(filter=filter_packet, prn=handle_packet, timeout=10, iface=INTERFACE)

# === Save unencrypted snapshot ===
with open(output_file, "w") as f:
    json.dump(packet_list, f, indent=2)
print(f"[+] Snapshot saved to {output_file}")

# === Encrypt snapshot ===
print("[*] Encrypting snapshot...")
try:
    subprocess.run([
        "python3",
        "snapshot_encryptor.py",
        output_file,
        encrypted_output_file,
        DEFAULT_PASSWORD
    ], check=True)
    print(f"[+] Encrypted snapshot saved to {encrypted_output_file}")
except subprocess.CalledProcessError:
    print("[-] Encryption failed.")


import subprocess

# After snapshot and encryption, run profiling
print("[+] Running auto_profile.py...")
subprocess.run(["python3", "auto_profile.py"])

# Then send alert based on the generated profile
print("[+] Sending alerts...")
subprocess.run(["python3", "send_alert.py"])
