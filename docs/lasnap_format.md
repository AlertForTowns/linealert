# 📄 LineAlert Snapshot (.lasnap) File Format

This document defines the standard JSON structure for `.lasnap` snapshot files used throughout the LineAlert ecosystem.

Maintaining consistency in this format ensures compatibility across modules like:
- `snapshot_generator.py`
- `auto_profile.py`
- `view_snapshot.py`
- `decrypt_snapshot.py`
- `send_alert.py`

---

## 🔧 File Type & Structure

- **File extension**: `.lasnap`
- **Format**: JSON (optionally encrypted with `.lasnap.json` or binary wrapper)
- **Required**: UTF-8 encoding, flat key-value structure

---

## 📚 Required Fields

| Field       | Type     | Description                                      |
|-------------|----------|--------------------------------------------------|
| `timestamp` | string   | ISO 8601 timestamp of snapshot creation          |
| `device`    | string   | Logical name or ID of the monitored device       |
| `status`    | string   | Summary state of device (`normal`, `alert`, etc)|
| `packets`   | integer  | Total number of packets captured in the snapshot |

---

## 🧠 Optional Fields

| Field       | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| `protocol`  | string   | Identified protocol (e.g., Modbus, BACnet)        |
| `event`     | string   | Description of specific anomaly or alert          |
| `severity`  | string   | Risk level (`low`, `medium`, `high`, `critical`)  |
| `notes`     | string   | Analyst notes or classification tags              |

---

## ✅ Example Snapshot

```json
{
  "timestamp": "2025-04-14T18:42:00Z",
  "device": "PLC-1",
  "status": "normal",
  "packets": 340,
  "protocol": "Modbus",
  "event": "none",
  "severity": "low"
}
🚦 Future Compatibility
This schema may evolve to support:

Asset metadata (e.g., firmware version, vendor ID)

Layer 2/3 traffic summaries

Multi-device rollups (per snapshot)

✅ Action for Contributors
Ensure all .lasnap files written by any LineAlert component adhere to this schema.

Use this as a baseline for creating mock data, testing pipelines, and validating snapshots.

This document is versioned and subject to refinement as the LineAlert platform matures.

yaml
Copy
Edit

---

Let me know if you want to link this in your README, validate `.lasnap` files on ingest, or just keep buildi
