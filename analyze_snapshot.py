import argparse
from decrypt_snapshot import mock_decrypt
from auto_profile import generate_profile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze .lasnap snapshot file")
    parser.add_argument("--input", required=True, help="Path to encrypted snapshot")
    args = parser.parse_args()

    decrypted_file = "decrypted_snapshot.json"
    profile_file = "device_profile.json"

    print("[*] Decrypting snapshot...")
    mock_decrypt(args.input, decrypted_file)

    print("[*] Generating device behavior profile...")
    generate_profile(decrypted_file, profile_file)

    print("[+] Analysis complete.")
