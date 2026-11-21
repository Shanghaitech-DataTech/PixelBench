import os
from pixelbench_api import *
print(os.getcwd())
for root, dirs, files in os.walk('.'):
    if root.count(os.sep) > 3:
        continue
    for f in files:
        print(os.path.join(root, f))
