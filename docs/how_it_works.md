# How LineAlert Works

LineAlert was built out of frustration.

Most OT security tools are expensive, complex, and built for massive enterprises. But a lot of critical infrastructure — like small-town water systems, solar farms, and legacy industrial networks — are flying blind because they can’t afford those tools, and often can’t even touch the endpoints.

LineAlert is different.

It’s a free and open-source tool designed to **passively monitor OT traffic**, detect anomalies, and build behavior profiles — all without installing anything on live equipment.

---

## 🚦 The Core Idea

At its heart, LineAlert answers a simple question:

> *“What’s happening on this OT network — and is it normal?”*

It does this by:
- Analyzing packet captures (`.pcap` files)
- Generating behavior profiles of devices and protocols
- Alerting when something looks off

No probes. No agents. No cloud. Just passive inspection and local analysis.

---

## 🔁 How It Works — Step by Step

1. **Capture OT Traffic**  
   - Use a switch mirror port, tap, or span port to capture network traffic with `tcpdump` or similar.
   - Save it as a `.pcap` file.

2. **Create a Snapshot**  
   - LineAlert ingests the `.pcap` and creates a `.lasnap` file — a compressed, encrypted snapshot of relevant data and metadata.
   - Snapshots are stored locally and pruned automatically over time.

3. **Decrypt and Analyze**  
   - A CLI tool decrypts the `.lasnap` and extracts key metadata: protocols observed, Modbus function codes, address ranges, etc.
   - An internal profiler compares this against expected behavior patterns.

4. **Generate a Behavior Profile**  
   - LineAlert auto-builds a profile for each device — a structured summary of how that device behaves.
   - This becomes your “baseline” for future comparisons.

5. **Flag Anomalies**  
   - If LineAlert sees something outside the norm — strange addresses, unexpected commands, timing changes — it flags it for review.

6. **View the Snapshot**  
   - The CLI viewer lets you inspect snapshots directly: timestamps, devices, protocol behavior, and anomalies.
   - A web-based viewer (Flask) is in development.

---

## 🔐 Security & Philosophy

LineAlert is designed for environments where:
- Security is critical
- Budgets are limited
- Endpoints must remain untouched

That means:
- No endpoint installs or agents  
- No outbound traffic by default  
- AES-256 snapshot encryption  
- Local-only by design  
- Webhooks and alerting coming soon

---

## 🧠 Why This Exists

LineAlert is for the small-town OT tech, the burned-out sysadmin, the civic-minded hacker — anyone trying to protect infrastructure that big tech ignores.

It's not trying to replace Dragos or Nozomi. It's trying to give **everyone else a fighting chance**.

---

## 🤝 Want to Help?

If you’ve worked in OT, ICS, networking, or security — or if you're just curious — we’d love your help.

You can:
- Test it and open an issue
- Fork the code and contribute
- Help shape the roadmap
- Suggest features that would make it useful in the real world

> This project is still early — but the mission is real.

—
*LineAlert: Built to protect the places most people forget.*
