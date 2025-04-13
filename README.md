# LineAlert

[![Auto-Generated Docs](https://img.shields.io/badge/docs-generated-blue.svg)](./documentation_output.md)

## Overview

LineAlert is a comprehensive cybersecurity monitoring tool designed to protect public-serving infrastructure, such as municipal water systems and solar fields, through passive, field-ready monitoring. This tool focuses on providing small municipalities with affordable, reliable, and cutting-edge cybersecurity solutions.

---

## For OT Professionals

LineAlert is specifically designed to protect operational technology (OT) environments without interrupting daily operations. It’s tailored for environments where traditional IT security tools may not be a good fit.

### What It Does for OT Environments

- **Passive Monitoring**: Captures snapshots of OT traffic without actively probing or scanning devices, ensuring no disruption to operations.
- **Anomaly Detection**: Automatically learns normal device behavior over time and alerts when deviations occur, helping you spot potential issues without needing external threat intelligence.
- **Zero Active Scans**: LineAlert avoids network scans, reducing the risk of overloading devices and systems.
- **Asset Discovery**: Tracks OT assets with no need for active scanning, offering an up-to-date inventory of devices.
- **Cloud Integration**: Uploads encrypted snapshots to cloud storage for backup, with optional access for analysis and long-term archiving.

### Key Modules for OT Use

| File                  | Role                                                   |
| --------------------- | ------------------------------------------------------ |
| `main.py`             | Orchestrates packet capture and flow                   |
| `asset_discovery.py`  | Tracks and updates live OT asset inventory             |
| `auto_profile.py`     | Builds behavioral baselines from .lasnap               |
| `send_alert.py`       | Triggers alerts via webhook or logs                    |
| `snapshot_viewer.py`  | CLI tool to decrypt and explore snapshots              |
| `snapshot_encryptor.py`| AES-based .lasnap protection                          |

LineAlert’s modular approach mirrors how OT systems work: each module plays a role in ensuring continuous, uninterrupted monitoring.

---

## For IT Professionals

LineAlert is a cybersecurity tool designed for small municipalities that need a lightweight, easy-to-deploy solution to monitor their OT systems without overcomplicating their IT infrastructure. While LineAlert is targeted for OT environments, it can be seamlessly integrated with existing IT systems for comprehensive security monitoring.

### What It Does for IT Environments

- **Low Overhead**: The tool is designed to be lightweight, requiring minimal configuration and maintenance, making it a good fit for IT professionals managing various infrastructure.
- **AES Encryption**: Snapshots are encrypted to ensure sensitive OT data remains protected at rest, helping with compliance and data protection needs.
- **Webhooks for Alerts**: IT professionals can integrate LineAlert into existing monitoring systems, with webhook-based alerting that can tie into SIEMs (Security Information and Event Management) or other IT management tools.
- **Cloud Backup**: The tool offers secure, optional cloud storage for OT snapshots, providing a reliable backup system without complex IT overhead.
- **Scalable**: LineAlert is designed to scale from small to mid-sized municipal deployments, offering flexibility as your IT infrastructure grows.

### Key Modules for IT Integration

| File                  | Role                                                   |
| --------------------- | ------------------------------------------------------ |
| `main.py`             | Orchestrates packet capture and flow                   |
| `asset_discovery.py`  | Tracks and updates live OT asset inventory             |
| `auto_profile.py`     | Builds behavioral baselines from .lasnap               |
| `send_alert.py`       | Triggers alerts via webhook or logs                    |
| `snapshot_viewer.py`  | CLI tool to decrypt and explore snapshots              |
| `snapshot_encryptor.py`| AES-based .lasnap protection                          |

LineAlert is modular and flexible, allowing IT teams to integrate it with their existing IT tools for added visibility and security.

---

## Design Philosophy

LineAlert is built using principles from both software engineering and OT network architecture:

- **Separation of Concerns** → Each module has a distinct role, like services in a layered control system.
- **Separation of Roles** → Mirrors real OT environments: sensor, logger, analyst, alert.
- **Relational Thinking** → Inspired by the structure of relational databases, enabling composability and clarity.

---

## Full Breakdown

For a deeper dive into the design and functionality of LineAlert, please refer to the Technical appendix.


## 💬 Community Feedback

LineAlert is shaped by real-world feedback from sysadmins, OT techs, and cybersecurity professionals.

📖 [Read the feedback →](./COMMUNITY_FEEDBACK.md)



## Disclaimer

**LineAlert is a project currently in development.** While we are working hard to make it a fully functional and reliable cybersecurity tool, it is still a work in progress. Features, functionality, and documentation may change as we continue to refine and improve the tool. 

Please use LineAlert with caution in production environments, and always verify that it meets your specific operational and security needs before deployment.
