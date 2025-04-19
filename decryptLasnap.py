import json
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2


KEY = b'linealert1234567890linealert1234'
print(f"[DEBUG] Key length: {len(KEY)}")     # Now it prints correctly



def decrypt_lasnap(file_path, output_path='/tmp/decrypted_snapshot.lasnap'):
    with open(file_path, 'r') as f:
        data = json.load(f)

    nonce = base64.b64decode(data['nonce'])
    tag = base64.b64decode(data['tag'])
    ciphertext = base64.b64decode(data['ciphertext'])

    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    with open(output_path, 'wb') as f:
        f.write(plaintext)

    print(f"[✅] Snapshot decrypted to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 decryptLasnap.py <input_encrypted.lasnap>")
        exit(1)
    decrypt_lasnap(sys.argv[1])
