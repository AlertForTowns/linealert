# auto_profile.py

def run_profile(snapshot_data):
    alerts = []

    traffic = snapshot_data.get("traffic", [])

    for entry in traffic:
        protocol = entry.get("protocol", "").lower()

        if protocol == "modbus":
            func_code = entry.get("function_code")
            if func_code in [8, 43]:  # Diagnostics or Encapsulated Interface
                alerts.append(f"🚨 Suspicious Modbus function code {func_code} detected.")
            if entry.get("error"):
                alerts.append(f"❗ Modbus error detected: {entry['error']}")

        elif protocol == "s7":
            if entry.get("operation") == "stop_cpu":
                alerts.append("🛑 Siemens S7 CPU stop command detected!")

        elif protocol == "dnp3":
            if entry.get("command") == "operate" and entry.get("auth") == "unauthenticated":
                alerts.append("⚠️ Unauthenticated DNP3 operate command detected.")

    if not alerts:
        alerts.append("✅ No anomalies detected in snapshot.")

    return alerts
