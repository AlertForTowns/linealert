# LineAlert

**Passive OT traffic profiling and anomaly detection** — built for small-town infrastructure.

No agents. No probes. No cloud. Just `.pcap` snapshots → profiles → alerts.

---

🛠️ **MVP Now Live**

The core LineAlert snapshot pipeline is complete:
- Generate `.lasnap` snapshots from `.pcap` traffic
- Auto-profile OT devices and behavior (Modbus supported)
- Decrypt and view snapshot contents via CLI
- Flag anomalies compared to a baseline profile

➡️ [See how it works](docs/how_it_works.md)

This release is focused on small-town infrastructure and offline visibility.  
Feedback and contributions welcome.

---

## 🚦 Why LineAlert?

Industrial networks were never designed with security in mind.  
But most tools that help monitor OT environments are:
- Too expensive
- Too invasive
- Too tied to the cloud or vendor lock-in

LineAlert is a free and open-source tool built for environments with:
- **No endpoint access**
- **No monitoring**
- **No budget for enterprise OT gear**

---

## 🔄 What It Does

1. Takes in `.pcap` traffic captures
2. Creates encrypted `.lasnap` snapshots
3. Profiles OT device behavior
4. Flags unexpected or unusual traffic
5. Lets you review snapshot metadata via CLI or (soon) web UI

---

## 🔐 Security Principles

- No agents, no probes, no endpoint access
- AES encryption for snapshots
- Local-only by default (no outbound traffic)
- Webhook alerts planned for secure integrations

---

## 📁 Project Structure

```bash
.
├── snapshot_generator.py         # Converts PCAP to .lasnap snapshots
├── decrypt_snapshot.py           # Decrypts .lasnap files
├── view_snapshot.py              # CLI viewer for snapshot contents
├── auto_profile.py               # Builds behavior profiles (e.g. Modbus)
├── compare_to_baseline.py        # Flags anomalies against expected behavior
├── send_alert.py                 # MVP webhook-ready alert sender
├── snapshot_viewer_web.py        # Flask UI (in development)
├── docs/
│   ├── how_it_works.md           # Pipeline & overview
│   └── roadmap.md                # Project direction and goals
└── snapshots/                    # Saved or test .lasnap files
