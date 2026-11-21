import os
for root, dirs, files in os.walk('.'):
    if files:
        print(root, files[:20])
print("CWD", os.getcwd())
