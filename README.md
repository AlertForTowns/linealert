# ⚡ LineAlert

**Passive OT Network Monitoring for the Real World.**  
No logging? No visibility? No budget?  
LineAlert listens silently, learns what's normal, and alerts when it’s not.

Built for fragile, under-monitored industrial systems that actually run society.

---

## 🧠 What It Does

LineAlert is a lightweight, modular tool that:

- 📸 Captures passive snapshots of OT traffic (`.lasnap` format)
- 🔐 Encrypts snapshots using AES (at-rest protection)
- 🧠 Learns normal device behavior over time (auto-profiling)
- ⚠️ Detects anomalies via snapshot diffing
- 🌐 Optionally uploads snapshots to secure cloud storage
- 🧾 Maintains a live asset inventory — with no active scans
- 🚨 Sends alerts when patterns break, even without threat intel

---

## 🔧 Key Modules

| File                  | Role                                  |
|-----------------------|---------------------------------------|
| `main.py`             | Orchestrates packet capture and flow  |
| `asset_discovery.py`  | Tracks and updates live OT asset inventory |
| `auto_profile.py`     | Builds behavioral baselines from `.lasnap` |
| `send_alert.py`       | Triggers alerts via webhook or logs   |
| `snapshot_viewer.py`  | CLI tool to decrypt and explore snapshots |
| `snapshot_encryptor.py` | AES-based `.lasnap` protection     |

Each module has a single concern.  
Together, they operate like a **relational system** — assets, snapshots, profiles, and alerts flow like data between tables.

---

## 🧠 Design Philosophy

LineAlert is built using principles from both **software engineering** and **OT network architecture**:

- **Separation of Concerns** → Each module has a distinct role, like services in a layered control system  
- **Separation of Roles** → Mirrors real OT environments: sensor, logger, analyst, alert  
- **Relational Thinking** → Inspired by the structure of relational databases, enabling composability and clarity

📄 Full breakdown in the [Technical Appendix](./TECHNICAL_APPENDIX.md)

---

## 🔄 How It Works (High-Level Flow)

```text
[ Passive Packet Capture ]
            ↓
[ AES-encrypted .lasnap Snapshot ]
            ↓
[ Auto-Profile Behavior ]
            ↓
[ Diff Snapshot vs. Baseline ]
            ↓
[ Alert if Anomaly ]
            ↓
[ Optional Upload to Cloud Blob ]
🚀 Getting Started
Requirements:

Python 3.8+

scapy, cryptography, psutil, argparse, etc.

Quick Start:

bash
Copy
Edit
git clone https://github.com/yourhandle/linealert.git
cd linealert
pip install -r requirements.txt
sudo python3 main.py --iface eth0
Optional:
Configure environment variables for AES key and cloud blob upload path.

🔭 Roadmap
 Auto-learn mode (adaptive profiling)

 Snapshot diff scoring + severity ranking

 Web-based viewer/dashboard (React or Flask)

 DNP3, BACnet protocol support

 Role inference (HMI / PLC / sensor tagging)

 CVE fingerprinting of legacy device behavior

🤝 Feedback & Contributions
LineAlert is FOSS and in active development.
Pull requests, issue reports, and real-world OT test data are welcome.

You can also contact me if you're an OT professional and want to stress test the pipeline or suggest features.

📜 License
Apache 2.0 — because tools like this should be free to build, use, and remix.

⚠️ Disclaimer
LineAlert is in early stages.
Use at your own discretion in live OT environments — especially fragile or safety-critical networks.
Always coordinate with plant engineers and network owners before deploying in production.



Test auto-docs workflow
