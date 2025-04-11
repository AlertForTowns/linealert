import os
from cryptography.fernet import Fernet
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Retrieve the Azure connection string and Fernet key
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
fernet_key = os.getenv("FERNET_KEY")

# Initialize the Fernet cipher suite for encryption
cipher_suite = Fernet(fernet_key)

def encrypt_data(data):
    """Encrypt data using the Fernet key"""
    return cipher_suite.encrypt(data.encode())

def upload_file_to_azure(file_path, file_name):
    """Upload the encrypted snapshot to Azure Blob Storage"""
    try:
        # Create a BlobServiceClient using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_name = "your-container-name"  # Replace with your container name
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"[+] Uploaded {file_name} to Azure Blob Storage.")
    except Exception as e:
        print(f"[!] Upload failed: {e}")

def write_lasnap(profile_data, file_path):
    """Encrypt the profile and save as a .lasnap file"""
    encrypted_data = encrypt_data(str(profile_data))
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

# Example usage
profile_data = {"detected_protocols": ["TCP", "ICMP"], "endpoint_summary": {"127.0.0.1": {"packet_count": 12}}}
snapshot_file_path = "/home/azureuser/linealert/auto_profile/snapshots/snapshot_20250410T193803Z.lasnap"
write_lasnap(profile_data, snapshot_file_path)

# Upload the snapshot to Azure
upload_file_to_azure(snapshot_file_path, "test_upload.lasnap")
