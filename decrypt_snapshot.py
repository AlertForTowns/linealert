import argparse
import json

def mock_decrypt(input_file, output_file):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    # Fake decrypted content for testing
    decrypted = {
        "timestamp": "2025-04-11T12:31:50Z",
        "device": "Simulated PLC-1",
        "protocol": "Modbus",
        "event": "Unauthorized coil write",
        "severity": "high"
    }

    with open(output_file, 'w') as f:
        json.dump(decrypted, f, indent=2)

    print(f"Decrypted to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    mock_decrypt(args.input, args.output)
