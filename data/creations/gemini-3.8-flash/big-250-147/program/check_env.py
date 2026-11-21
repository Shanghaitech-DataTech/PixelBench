import os
import glob

# Check current directory and environment
print("CWD:", os.getcwd())
# Check environment variables
for k, v in os.environ.items():
    if "TASK" in k or "BENCH" in k or "PIXEL" in k:
        print(f"{k}: {v}")

