import pixelbench
import inspect

print("pixelbench file:", pixelbench.__file__)
print("pixelbench dir:", dir(pixelbench))

# search in pixelbench package
import os
pb_dir = os.path.dirname(pixelbench.__file__)
print("pb_dir:", pb_dir)

for root, dirs, files in os.walk(pb_dir):
    for f in files:
        if 'snow' in f.lower() or 'pine' in f.lower() or 'task' in f.lower():
            print("Found in pb:", os.path.join(root, f))
