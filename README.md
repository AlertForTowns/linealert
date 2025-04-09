# LineAlert 🚨

LineAlert is an open-source project designed to passively monitor OT (Operational Technology) environments with minimal resource usage and maximum public impact. Built for small municipalities and industrial sites, LineAlert aims to provide real-time insights into system behavior and potential security issues — all without disrupting operations.

## ✅ Key Features

- 📡 **Passive Monitoring** — No network injection, no interference. Just observation.
- 🤖 **AI-Powered Log Analysis** — Real-time log insights using GPT for anomaly detection and human-readable summaries.
- 🕵️ **Live Alerts** — Detects and highlights suspicious activity such as invalid SSH login attempts or heartbeat anomalies.
- 💻 **Field-Ready** — Designed to run on minimal hardware like Raspberry Pi.
- 🧠 **Customizable Profiles** — Tailor alerts to the specific OT systems in your environment.

## ⚙️ Current Functionality

- Monitors `/var/log/syslog` in real-time
- Detects login failures, unusual patterns, and heartbeat reports
- Uses GPT (via OpenAI API) to interpret log meaning and surface potential threats
- Logs and displays alerts on screen in real-time

## 🧠 GPT Integration

LineAlert uses GPT (OpenAI) to:
- Parse and understand log data contextually
- Detect subtle behavioral changes that static tools might miss
- Provide human-readable summaries of log events

The API key is stored securely in a `.env` file, and the project is compatible with OpenAI's legacy `0.28.0` Python SDK.

## 🌐 Use Cases

- Municipal water treatment
- Solar fields
- Industrial automation sites
- Any system with OT equipment that deserves protection

## ⚙️ Quick Start

```bash
# Clone the repo
git clone https://github.com/your-org/linealert.git
cd linealert

# Install dependencies
sudo pip3 install openai python-dotenv watchdog

# Set up your .env file
nano ~/.alertline.env
# Add: OPENAI_API_KEY=sk-...

# Run the monitoring tool
sudo -E python3 log_gpt.py
```

## 📍 Roadmap

- Alert storage & forwarder (syslog/export options)
- Web interface/dashboard
- Profile-based alert tuning
- Offline GPT support (via local LLM)

---

> 💡 *Built by Anthony Edgar for the people — because even small towns deserve big protection.*

---

