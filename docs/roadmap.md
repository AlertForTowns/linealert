# LineAlert Roadmap

This roadmap outlines what's next for the LineAlert project.

Built to give small-town and underfunded OT environments access to real visibility — without agents, probes, or expensive licensing.

---

## ✅ Completed in v0.1 (MVP)

- Passive `.pcap` traffic snapshot tool
- `.lasnap` file format with AES encryption
- Auto-profiling OT device behavior (Modbus)
- Baseline behavior comparison + anomaly flagging
- CLI snapshot viewer
- Webhook-ready alerting system
- Initial documentation: `how_it_works.md`, README

---

## 🔜 Next Priorities

### 🖥️ Snapshot Viewer (Flask)
- Lightweight web UI for viewing `.lasnap` files
- Deployable to local dashboards or offline infrastructure

### 🧠 Auto-Learn Mode
- Allow behavior profiles to evolve with confirmed inputs
- CLI flags or interactive prompt to accept/reject new patterns

### 🧪 Protocol Expansion
- BACnet support
- DNP3 support
- IEC-104 support

### 🧰 CLI Tooling + Installability
- Package via `setuptools` or `poetry`
- Add command aliases (e.g. `linealert snap`, `linealert view`)

### 📁 Examples
- Public `.pcap` + `.lasnap` files to help users test
- Side-by-side snapshots of normal vs malicious behavior

---

## 💡 Ideas Under Discussion

- `lasnap-validator` CLI for integrity / format checking
- Multiple profile sets by environment or operator
- Configurable alert levels & thresholds
- `.lasnap` viewer export to HTML or CSV
- Passive wire capture support (opt-in, safe sandboxed mode)

---

Got an idea or something you wish this did?  
[Open an issue](https://github.com/anthonydgar30000/linealert/issues) or post in Discussions!
