# LineAlert System Design

## Overview

LineAlert is a cutting-edge open-source cybersecurity platform designed to passively monitor Operational Technology (OT) systems. This document outlines the architecture and key components of the system, now with integrated AI-powered real-time log analysis using GPT.

---

## Key Components

- **Passive Data Collection**  
  Monitors logs from OT network interfaces (e.g., from firewalls, switches, or Linux syslog) without injecting traffic.

- **AI-Powered Log Analysis**  
  Uses OpenAI’s GPT to analyze logs in real-time, identify suspicious behavior, and generate human-readable insights.

- **Live Alerts**  
  Detects failed logins, irregular heartbeat events, and other anomalies. Sends immediate alerts via console output (future support for email, Slack, etc. planned).

- **Field-Ready Hardware**  
  Designed to run efficiently on resource-constrained hardware like Raspberry Pi or fanless industrial PCs.

- **Custom Profiles**  
  Tailors detection rules for different kinds of OT equipment (PLCs, RTUs, sensors).

---

## GPT Integration Details

- **Environment-based Key Loading**  
  The OpenAI API key is stored in `~/.alertline.env` for secure access and is loaded at runtime.

- **Models Used**  
  Currently supports `gpt-3.5-turbo` with optional support for more advanced models.

- **Real-Time Triggering**  
  Uses the Python `watchdog` module to monitor log files and send new lines to GPT as they appear.

- **Prompt Engineering**  
  Prompts are optimized to summarize log context, flag anomalies, and explain their implications in plain English.

---

## Future Enhancements

- Add support for cloud push alerts (via webhook/email/SIEM integration)
- Train local models for offline anomaly detection
- Add device fingerprinting for OT traffic baseline monitoring
