# LineAlert

**LineAlert** is a lightweight, field-ready cybersecurity monitoring and profiling system purpose-built to protect public-serving infrastructure such as municipal water treatment plants, solar fields, and smart city installations.

## 🚀 Purpose
LineAlert was designed to help small municipalities and public institutions monitor their operational technology (OT) environments **passively and proactively**, without needing deep cybersecurity expertise or expensive infrastructure.

## 🧠 Key Features

### ✅ Auto-Profile Builder
- Parses `.pcap` packet capture files
- Detects common protocols (TCP, UDP, ICMP, Modbus, etc.)
- Extracts source/destination IPs, ports, byte counts, packet stats
- Generates a machine-readable behavioral profile (`new_profile.json`)

### 📸 Snapshot Limiter & Local Cleanup
- Automatically takes packet snapshots on suspicious activity
- Limits number of snapshots per hour to avoid disk abuse
- Automatically deletes snapshots after a retention window (default: 24h)
- Supports premium features: `.lasnap` encrypted backups + cloud upload

### 🔐 Proprietary Snapshot Format (Pro Tier)
- Future `.lasnap` files will be encrypted and optionally cloud-synced
- Allows for safe transfer and remote diagnostics
- Represents an IP asset for licensing, upselling, and trust-building

## 📦 Folder Structure
```
linealert/
├── auto_profile/
│   ├── builder.py               # Auto profile logic
│   └── snapshot_limiter.py     # Snapshot management
├── snapshots/                  # Where snapshots are saved
├── sample.pcap                 # Test packet capture
├── profile_gpt.py              # CLI wrapper for profiling
├── new_profile.json            # Output profile
├── README.md                   # You're here
└── ...
```

## 🛠️ How to Use
```bash
python3 profile_gpt.py --pcap sample.pcap --output new_profile.json
```

## 💡 Vision
We believe even the smallest towns deserve enterprise-grade protection. LineAlert is part of a larger mission to keep critical infrastructure safe, transparent, and **accountable to the public**.

## ✍️ Author
Built by someone in the trenches, not a suit in a boardroom.
This project exists to save lives.

## ⚖️ License
Apache 2.0

## 🛣️ Roadmap
- [x] PCAP parser & profiler
- [x] Snapshot limiter + cleanup
- [ ] `.lasnap` encrypted snapshots
- [ ] Cloud backup integration
- [ ] Behavioral anomaly detection engine
- [ ] Drag-and-drop web interface

---
> Everybody’s got a story that could break your heart.  
> That’s why we protect the line.
