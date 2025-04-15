import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = bytes.fromhex("abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890")
iv = bytes.fromhex("1234567890abcdef1234567890abcdef")

# Fake alert data
data = {
    "device_id": "sim-001",
    "anomaly": "Modbus spike",
    "timestamp": "2025-04-15T18:00:00Z"
}

# Encrypt it
plaintext = json.dumps(data).encode()
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

with open("test.lasnap", "wb") as f:
    f.write(ciphertext)

print("✅ Encrypted test.lasnap created")
