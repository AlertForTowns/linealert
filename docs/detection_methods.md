# Detection Methods

LineAlert currently supports two layers of threat detection:

### 1. Adaptive Baseline Profiling
- Tracks normal Modbus function codes per device over time.
- Detects anomalies or deviations from expected behavior.

### 2. Signature-Based Detection (New!)
- Uses a signature file (`modbus_signatures.yaml`) to detect known-bad Modbus function codes.
- Useful for identifying reconnaissance, sabotage, or manipulation techniques often seen in attacks on OT systems.

## How to Contribute
To add or modify signatures, edit `modbus_signatures.yaml`.

Each entry requires:
- `function_code`: integer (decimal)
- `description`: what this code is typically used for
- `severity`: low / medium / high

More features coming soon.
