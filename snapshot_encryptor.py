import os
import sys
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode

def derive_key(password: str, salt: bytes, length: int = 32) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(input_path, output_path, key):
    # Read the plaintext data
    with open(input_path, 'rb') as f:
        plaintext = f.read()

    # Pad the plaintext
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Generate nonce (IV)
    nonce = os.urandom(12)  # 12 bytes for AES-GCM

    # Create AES-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Store ciphertext + nonce + tag in a single file
    encrypted_data = {
        'nonce': urlsafe_b64encode(nonce).decode('utf-8'),
        'tag': urlsafe_b64encode(encryptor.tag).decode('utf-8'),
        'ciphertext': urlsafe_b64encode(ciphertext).decode('utf-8')
    }

    with open(output_path, 'w') as f:
        json.dump(encrypted_data, f, indent=2)

    print(f"[+] Encrypted snapshot saved to: {output_path}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 snapshot_encryptor.py <input_file> <output_file> <password>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    password = sys.argv[3]

    salt = b'static_salt_1234'  # In production, generate and store salt securely per file
    key = derive_key(password, salt)

    encrypt_file(input_path, output_path, key)

if __name__ == '__main__':
    main()
