import argparse
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_snapshot(input_file, output_file, key_b64):
    key = base64.b64decode(key_b64)
    if len(key) != 32:
        raise ValueError("Key must decode to 32 bytes for AES-256.")

    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"[+] Decrypted to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt an AES-encrypted LineAlert snapshot.")
    parser.add_argument("--input", required=True, help="Path to encrypted .lasnap file")
    parser.add_argument("--output", required=True, help="Path to save decrypted JSON")
    parser.add_argument("--key", required=True, help="Base64-encoded 32-byte AES key")
    args = parser.parse_args()

    decrypt_snapshot(args.input, args.output, args.key)
