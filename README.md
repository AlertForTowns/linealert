# LineAlert

LineAlert is an open-source tool designed to passively monitor industrial control system (ICS) and operational technology (OT) networks — such as those used in small municipalities, water treatment facilities, and other critical infrastructure environments.

It aims to help detect unauthorized behavior or anomalies by building and comparing traffic behavior profiles over time.

---

## Key Features

- **Passive Network Sniffing**  
  Captures Modbus TCP (port 502) and other relevant ICS/OT traffic without injecting packets or disrupting the network.

- **Snapshot Generation**  
  Creates `.lasnap` files that represent network activity during a configurable time window. Snapshots are encrypted at rest using AES.

- **Auto-Profiling**  
  Extracts behavioral patterns from traffic (e.g., read/write function codes, device IDs) and builds baseline profiles for each device.

- **Anomaly Detection**  
  Compares new traffic against the baseline to flag deviations and optionally trigger alerts (via webhook or console log).

- **Snapshot Viewer CLI**  
  Decrypt and inspect `.lasnap` files manually or as part of automated pipelines.

---

## Components

- `snapshot_generator.py` – Captures live traffic and generates snapshots.
- `snapshot_encryptor.py` – Encrypts snapshots using AES.
- `decrypt_snapshot.py` – Decrypts `.lasnap` files for inspection or analysis.
- `auto_profile.py` – Builds a profile from historical or live data.
- `compare_to_baseline.py` – Compares current behavior to baseline.
- `send_alert.py` – Sends alert data (e.g., webhook, log, or email).
- `view_snapshot.py` – CLI viewer for decrypted snapshots.

---

## Example Use Case

1. Set up a Raspberry Pi with a SPAN port or tap on a Modbus TCP network.
2. Schedule periodic snapshots using `systemd` or cron.
3. Encrypt and upload snapshots to a secure location.
4. Auto-profile device behavior.
5. Trigger alerts when traffic deviates from the expected profile.

---

## Goals

- Encourage better visibility into ICS/OT environments that often lack basic monitoring.
- Provide a starting point for sysadmins and OT engineers looking to build their own monitoring and alerting workflows.

---

## Contributing

This is an early-stage project. Feedback from OT security professionals, sysadmins, and ICS integrators is especially welcome.

If you’ve worked in these environments, we’d love help with:
- Improving protocol coverage
- Fine-tuning profiling logic
- Real-world feedback on deployment

---

## Known Gaps / To-Do

- Protocol support is limited (Modbus TCP prioritized for now).
- No GUI (CLI-based only).
- Currently built for Python 3.10+ on Ubuntu.
- Limited error handling / logging.

---

## Real-World Context

This tool was inspired by high-profile incidents such as the 2021 Oldsmar, Florida water treatment facility breach, where attackers remotely accessed SCADA systems. Many small utilities still lack visibility into network traffic and behavior anomalies — LineAlert attempts to fill that gap with a lightweight, field-ready solution.

---

## License

Apache 2.0 – Use freely, contribute if you like.

