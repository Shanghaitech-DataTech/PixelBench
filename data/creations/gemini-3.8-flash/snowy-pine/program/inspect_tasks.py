import os

pb_dir = '/host'
for root, dirs, files in os.walk(pb_dir):
    for f in files:
        if 'snowy' in f.lower() or 'pine' in f.lower():
            print("Found:", os.path.join(root, f))
