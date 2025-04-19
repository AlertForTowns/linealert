#!/bin/bash

# Navigate to correct working directory
cd /home/azureuser/linealert || exit 1

# Run the correct Python script (adjust name if needed)
python3 auto_profile.py >> logs/auto_profile.log 2>&1
