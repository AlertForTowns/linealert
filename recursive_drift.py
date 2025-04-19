import json, os, datetime

def load_json(path):
    with open(path) as f:
        return json.load(f)

def calculate_drift(baseline, snapshot):
    scores = []
    for base_device in baseline["devices"]:
        ip = base_device["ip"]
        base_funcs = {f["function_code"]: f["count"] for f in base_device["functions"]}
        snap_device = next((d for d in snapshot["devices"] if d["ip"] == ip), None)
        if not snap_device:
            continue
        for f in snap_device["functions"]:
            code = f["function_code"]
            current = f["count"]
            if code in base_funcs and base_funcs[code] != 0:
                drift = abs(current - base_funcs[code]) / base_funcs[code]
                scores.append(drift)
    return sum(scores) / len(scores) if scores else 0

def recursively_evolve(baseline, snapshots, log_file="drift_trends.txt"):
    with open(log_file, "w") as log:
        for snap in snapshots:
            timestamp = datetime.datetime.now().isoformat()
            drift = calculate_drift(baseline, snap)
            log.write(f"[{timestamp}] Drift Score: {round(drift*100, 2)}%\n")
            if drift > 0.1:
                for dev in baseline["devices"]:
                    snap_dev = next((d for d in snap["devices"] if d["ip"] == dev["ip"]), None)
                    if not snap_dev:
                        continue
                    for base_func in dev["functions"]:
                        match = next((f for f in snap_dev["functions"] if f["function_code"] == base_func["function_code"]), None)
                        if match:
                            base_func["count"] = int((base_func["count"] + match["count"]) / 2)
    return baseline

def main():
    baseline = load_json("baseline.json")
    snapshot_files = sorted(f for f in os.listdir("snapshots") if f.endswith(".json"))
    snapshots = [load_json(os.path.join("snapshots", f)) for f in snapshot_files]

    evolved = recursively_evolve(baseline, snapshots)
    with open("evolved_baseline.json", "w") as f:
        json.dump(evolved, f, indent=2)
    print("[✓] Drift analysis complete. Trend logged to drift_trends.txt.")

if __name__ == "__main__":
    main()

