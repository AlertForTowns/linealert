import argparse
from auto_profile import builder

def main():
    parser = argparse.ArgumentParser(description="Generate protocol behavior profile from PCAP")
    parser.add_argument("--pcap", required=True, help="Path to PCAP file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    print(f"[+] Processing PCAP: {args.pcap}")
    profile = builder.build_profile(args.pcap)

    with open(args.output, "w") as f:
        import json
        json.dump(profile, f, indent=4)
    print(f"[+] Profile written to: {args.output}")

if __name__ == "__main__":
    main()
