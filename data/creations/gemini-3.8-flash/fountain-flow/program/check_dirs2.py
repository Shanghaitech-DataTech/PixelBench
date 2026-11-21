import os
for root, dirs, files in os.walk('..'):
    if 'runs' in root and root != '..':
        continue
    print(root, dirs, files)
