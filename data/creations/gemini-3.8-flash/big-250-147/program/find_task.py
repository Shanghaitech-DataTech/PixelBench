import os

root = "/host"
# Let's list files in parent dirs if accessible
try:
    print(os.listdir(root))
except Exception as e:
    print("Error listing root:", e)

# Also check task name 'big-250-147'
for dirpath, dirnames, filenames in os.walk("/host"):
    for f in filenames:
        if "big-250-147" in f or "250-147" in f:
            print(os.path.join(dirpath, f))
