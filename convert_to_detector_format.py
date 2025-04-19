import json

def convert(input_file, output_file):
    with open(input_file) as f:
        raw = json.load(f)

    formatted = {"devices": []}

    for ip, data in raw.items():
        functions = []
        for fn_code, count in data["function_calls"].items():
            functions.append({
                "function_code": fn_code,
                "count": count
            })
        formatted["devices"].append({
            "ip": ip,
            "functions": functions
        })

    with open(output_file, "w") as f:
        json.dump(formatted, f, indent=2)

    print(f"[✓] Converted {input_file} → {output_file}")

if __name__ == "__main__":
    convert("baseline_raw.json", "baseline.json")
    convert("snapshot_raw.json", "snapshot.json")
