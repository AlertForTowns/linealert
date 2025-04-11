import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Load environment variables from .env

# Retrieve the Fernet key
fernet_key = os.getenv("FERNET_KEY")
cipher_suite = Fernet(fernet_key)

def write_lasnap(profile_data, file_path):
    """Encrypt the profile data and save it as a .lasnap file."""
    encrypted_data = cipher_suite.encrypt(str(profile_data).encode())
    
    # Write the encrypted data to a file
    with open(file_path, "wb") as f:
        f.write(encrypted_data)
    print(f"[+] Snapshot saved to: {file_path}")

# Example usage
profile_data = {"detected_protocols": ["TCP", "ICMP"], "endpoint_summary": {"127.0.0.1": {"packet_count": 12}}}
snapshot_file_path = "/home/azureuser/linealert/auto_profile/snapshots/snapshot_20250410T193803Z.lasnap"
write_lasnap(profile_data, snapshot_file_path)
