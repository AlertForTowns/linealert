
"""
📟 LineAlert AFib-Inspired Drift Detector
- Monitors timing intervals between packets
- Flags sustained drift based on deviation thresholds
- Inspired by how AFib monitors track heartbeat irregularities
"""

import time
import statistics
from datetime import datetime

# === CONFIGURABLE PARAMETERS ===
WINDOW_SIZE = 10              # How many intervals to average for baseline
DRIFT_THRESHOLD_PCT = 0.20    # 20% deviation from baseline triggers alert
SUSTAINED_COUNT = 3           # Must exceed threshold this many times in a row

# === SIMULATED TIMESTAMPS (replace with real capture later) ===
# Simulated packet arrival times in seconds (normally every 1s)
simulated_arrivals = [
    0, 1.01, 2.03, 3.00, 4.02, 5.00, 6.00, 7.00, 8.00, 9.01,  # Normal
    10.25, 11.5, 13.1, 14.6, 16.1, 17.6,                      # Drift
    18.5, 19.5, 20.5, 21.5, 22.5                              # Recovery
]

def detect_drift(arrivals):
