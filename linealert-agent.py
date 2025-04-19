# linealert-agent.py (partial)
import json
import os
import shutil
from subprocess import run, CalledProcessError

SNAP_PATH = "snapshot.lasnap"
DECRYPTED_PATH = "/tmp/decrypted_snapshot.lasnap"

# Check if snapshot is already decrypted
with open(SNAP_PATH) as f:
    sample = json.load(f)
    if "nonce" not in sample:
        print("[*] Skipping decryption (already plaintext snapshot)")
        shutil.copy(SNAP_PATH, DECRYPTED_PATH)
    else:
        print("[*] Decrypting snapshot...")
        try:
            run(["python3", "decryptLasnap.py", SNAP_PATH], check=True)
        except CalledProcessError:
            print("[!!] Decryption failed")
            exit(1)

# Continue with the rest of the simulation logic...
