## LineAlert

LineAlert is a lightweight, field-ready cybersecurity monitoring and profiling system purpose-built to protect public-serving infrastructure such as municipal water treatment plants, solar fields, and smart city installations.

🚨 **This is not a toy project.** LineAlert is built to solve a real-world gap in passive, non-invasive OT cybersecurity monitoring — something that has not been properly addressed by traditional IT security tools.

### 🎯 Purpose
LineAlert was designed to help small municipalities and public institutions monitor their operational technology (OT) environments passively and proactively, without needing deep cybersecurity expertise or expensive infrastructure.

### 🔑 Key Features

#### ✅ Auto-Profile Builder
- Parses `.pcap` packet capture files
- Detects common protocols (TCP, UDP, ICMP, Modbus, etc.)
- Extracts source/destination IPs, ports, byte counts, packet stats
- Generates a machine-readable behavioral profile (`new_profile.json`)

#### 🧠 Snapshot Limiter & Local Cleanup
- Automatically takes packet snapshots on suspicious activity
- Limits number of snapshots per hour to avoid disk abuse
- Automatically deletes snapshots after a retention window (default: 24h)
- Supports premium features: `.lasnap` encrypted backups + cloud upload

#### 🔐 Proprietary Snapshot Format (Pro Tier)
- Future `.lasnap` files will be encrypted and optionally cloud-synced
- Allows for safe transfer and remote diagnostic inspections
- Represents an IP asset for licensing, upselling, and trust-building

### 📁 Folder Structure
```
linealert/
├── auto_profile/            # Auto profile logic
│   └── snapshot_limiter.py  # Snapshot management
├── baseline_profile.json    # Sample baseline
├── decrypted_snapshot.json  # Decrypted snapshot
├── device_profile.json      # AI output for profiling
├── profile_gen.py           # CLI wrapper profile
├── new_profile.json         # Output profile
├── requirements.txt         # Python dependencies
├── linealert.py             # Wire up modules here
```
