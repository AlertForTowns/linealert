from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()
FERNET_KEY = os.getenv("FERNET_KEY").encode()

def encrypt_data(data: bytes) -> bytes:
    """Encrypt data using AES (Fernet symmetric encryption)."""
    return Fernet(FERNET_KEY).encrypt(data)

def decrypt_data(data: bytes) -> bytes:
    """Decrypt data using AES (Fernet symmetric encryption)."""
    return Fernet(FERNET_KEY).decrypt(data)
