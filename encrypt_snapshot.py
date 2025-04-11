# encrypt_snapshot.py
import argparse
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

def pad(data):
    padding_len = 16 - len(data) % 16
    return data + chr(padding_len) * padding_len

def encrypt_file(input_path, output_path, key):
    with open(input_path, 'r') as f:
        plaintext = f.read()
    
    padded = pad(plaintext)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded.encode())

    with open(output_path, 'wb') as f:
        f.write(iv + ciphertext)

def main():
    parser = argparse.ArgumentParser(description="Encrypt a snapshot into .lasnap format")
    parser.add_argument("--input", required=True, help="Input JSON file")
    parser.add_argument("--output", required=True, help="Output .lasnap file")
    parser.add_argument("--key", required=True, help="Encryption key (32-byte base64 string)")

    args = parser.parse_args()
    key = base64.b64decode(args.key)

    if len(key) != 32:
        print("[!] Error: Key must decode to 32 bytes for AES-256.")
        return

    encrypt_file(args.input, args.output, key)
    print(f"[+] Snapshot encrypted to: {args.output}")

if __name__ == "__main__":
    main()
