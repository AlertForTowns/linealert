# LineAlert: Technical Appendix – Design Decisions and Rationale

This appendix explains the core architectural decisions behind LineAlert, a passive OT network monitoring and profiling system. Each decision is grounded in real-world constraints, cybersecurity best practices, and the goal of serving under-resourced or fragile operational environments.

---

## 🔐 1. AES Encryption for Snapshots (At-Rest Protection)

**Decision:** LineAlert uses AES (Advanced Encryption Standard) to encrypt `.lasnap` snapshot files while they are at rest.

**Why:**
- Protects sensitive OT traffic data if a device is physically stolen or accessed
- AES is globally trusted, fast, and supported in nearly all modern cryptographic libraries
- Ensures confidentiality of traffic and metadata without slowing down field systems
- Enables secure cloud or USB storage

**Tech Details:**
- AES-256 in CBC or GCM mode
- Key stored locally via environment variable (future: TPM/HSM integration)

---

## 📸 2. `.lasnap` Snapshot Format (Passive, Structured Traffic Capture)

**Decision:** Captured traffic is stored in a custom `.lasnap` format rather than raw `.pcap` files.

**Why:**
- `.pcap` is powerful but lacks built-in encryption, metadata tagging, or portability
- `.lasnap` files include timestamp, session metadata, device identifiers, and encryption
- Easier to manage, rotate, and upload to secure blob storage
- Designed for behavioral analysis and forensic inspection

**Tech Details:**
- JSON-wrapped + binary payload (modular design for compression/encryption)
- Supports tagging with plant/device ID, timestamp, and profiling hashes

---

## 🕵️ 3. Passive Monitoring (Non-Intrusive, Safe for OT)

**Decision:** LineAlert captures traffic passively instead of performing active scans, polling, or intrusive traffic injection.

**Why:**
- Active scanning can trip safety systems, disrupt fragile control networks, or cause downtime
- Passive listening allows full visibility without operational risk
- Ensures the tool is usable in live environments without IT/OT conflict

**Tech Details:**
- Packet capture via libpcap or raw sockets (Linux-based)
- Runs in mirror port / tap / SPAN mode only

---

## 🧠 4. Auto-Profiling of Behavior (Baseline Learning)

**Decision:** LineAlert builds a behavioral profile of normal device communication patterns over time.

**Why:**
- Most OT devices are deterministic; their communication is repetitive and predictable
- Profiling enables detection of anomalies even without signatures or threat intel
- Useful for visibility in “dark” networks with no logging or existing monitoring

**Tech Details:**
- Protocol parser for Modbus (first supported protocol)
- Tracks timing, frequency, and function code patterns per device
- Profiles saved per device/IP, optionally encrypted

---

## ⚠️ 5. Anomaly Detection via Snapshot Diffs

**Decision:** Snapshots are compared over time to detect behavioral drift or unexpected communication changes.

**Why:**
- Works without constant cloud connection or SIEM integration
- Flags new devices, function code usage spikes, or timing anomalies
- Provides operators with actionable deltas without needing deep expertise

**Tech Details:**
- Diffs performed on parsed profile summaries
- Timestamps and unique IDs link anomalies to specific `.lasnap` snapshots

---

## 🌐 6. Optional Cloud Upload (Blob Storage for Snapshots)

**Decision:** Snapshots can be optionally uploaded to a secure cloud bucket (e.g. Azure Blob, AWS S3)

**Why:**
- Enables central review of traffic without logging into edge device
- Supports long-term archiving or offsite forensics
- Works well with air-gapped models that sync periodically

**Tech Details:**
- Encrypted before upload
- Timestamped object names for integrity and rotation

---

## 🔁 7. Snapshot Rotation and Retention Policy

**Decision:** Snapshot files are automatically rotated and pruned to maintain a minimal storage footprint.

**Why:**
- OT devices often have limited disk space
- Prevents storage exhaustion
- Retains only the most recent or relevant forensic material

**Tech Details:**
- Configurable max age, max size, and max count
- First-In, First-Out (FIFO) deletion logic
- Can retain specific snapshots flagged by anomalies

---

## ⚙️ 8. Alerting Logic and Webhook Integration

**Decision:** Behavioral anomalies can trigger alerts, optionally sent via webhook or logged locally.

**Why:**
- Operators need to be notified of critical changes (new device, function spike, unusual timing)
- Webhooks support integration with SIEMs, dashboards, or messaging tools
- Keeps LineAlert lightweight and loosely coupled

**Tech Details:**
- JSON alert payloads with snapshot ref, device ID, and anomaly type
- Configurable severity levels and throttle windows

---

## 🧪 9. Snapshot Viewer (CLI and Dashboard – In Progress)

**Decision:** Build a viewer for inspecting `.lasnap` files without decrypting them manually.

**Why:**
- Enables rapid inspection by field operators or analysts
- Improves transparency and usability
- Will serve as the frontend for both CLI and web dashboard interfaces

**Tech Details:**
- AES decryption pipeline
- Parses snapshot metadata + preview of captured sessions
- Long-term plan: filter by time, device, protocol

---

## 🔄 10. Auto-Learn Mode (Profile Updating & Drift Tolerance)

**Decision:** A future feature will allow profiles to adapt to new normal behavior over time.

**Why:**
- Networks evolve (e.g., scheduled maintenance or new devices)
- Prevents alert fatigue from expected behavioral changes
- Keeps profiles current while preserving audit traceability

**Tech Details:**
- Profile diff scoring over multiple intervals
- Change confirmation logic before auto-update
- Versioned profile history for rollback
