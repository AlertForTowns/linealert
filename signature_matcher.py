import yaml

def load_signatures(filepath="modbus_signatures.yaml"):
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
        return data.get("signatures", [])

def check_signatures(snapshot, signatures):
    snapshot_codes = snapshot.get("function_codes", [])

    for sig in signatures:
        fc = sig.get("function_code")
        subfc = sig.get("subfunction", None)

        if fc in snapshot_codes:
            # Optional future logic: match subfunction if implemented in snapshot
            return {
                "matched_code": fc,
                "severity": sig.get("severity", "unknown"),
                "description": sig.get("description", "")
            }

    return None
