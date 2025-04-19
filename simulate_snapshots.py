import os
from auto_learn import auto_learn

def simulate():
    snapshots = [
        "snapshot_1.lasnap",
        "snapshot_2.lasnap",
        "snapshot_3.lasnap",
        "snapshot_4.lasnap",
    ]
    for snap_name in snapshots:
        print(f"[+] Generating snapshot: {snap_name}")
        # Normally you would call snapshot generation logic here
        print(f"[+] Running auto-learn for {snap_name}")
        auto_learn(snap_name)  # Pass string, not list

if __name__ == "__main__":
    simulate()
