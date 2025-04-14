# LineAlert Deployment Guide

This guide outlines a lightweight deployment method for installing LineAlert in small industrial environments, such as water treatment plants, solar fields, or municipal pump stations.

---

## 🧰 Hardware Requirements

- Raspberry Pi 4 (4GB+ recommended)
- MicroSD card (32GB+)
- USB-to-Ethernet adapter (if second NIC is required)
- Passive network tap or SPAN/mirror port from managed switch
- Optional: power backup (UPS) if reliability is critical

---

## 🖥️ Software Requirements

- Ubuntu Server 22.04 LTS (or similar minimal Linux distro)
- Python 3.10+
- `tcpdump`, `tshark`, or equivalent capture tool
- LineAlert source code (clone from GitHub)

---

## ⚙️ Installation (Manual Prototype Flow)

1. **Install OS** and perform basic setup (hostname, SSH, updates).
2. **Clone the repo**:
   ```bash
   git clone https://github.com/your-org/linealert.git
   cd linealert
Install dependencies:

bash
Copy
Edit
sudo apt update
sudo apt install tcpdump python3-pip
pip3 install -r requirements.txt
Connect monitoring interface to SPAN/mirror port or passive tap.

Run snapshot capture and profiling:

bash
Copy
Edit
python3 snapshot_capture.py
python3 auto_profile.py
Review output in /snapshots and /profiles folders.

Note: future versions will include automated install scripts and snapshot viewers.

📡 Network Placement
Place the LineAlert device at a strategic observation point — ideally:

Behind the main firewall, but before core controllers

Connected to the switch that handles PLC or SCADA communications

🔐 Security Notes
LineAlert is read-only and passive; it does not inject or alter traffic.

Harden the OS (SSH keys, firewall rules, regular patching)

Encrypt .lasnap files before offloading (coming soon)

📦 Coming Soon
Setup script (setup.sh) for faster deployments

CLI-based snapshot viewer

REST-based alert push via webhook

yaml
Copy
Edit

---

Want to review this before we move to `air_gap_myth.md`? Or charge ahead and knock that one out too?
