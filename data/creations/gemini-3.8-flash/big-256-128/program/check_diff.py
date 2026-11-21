# Let's check what changed in the castle area
with open("main.py") as f:
    code = f.read()
# Let's check any lines affecting y in range 60 to 80
import re
for line in code.splitlines():
    if "70" in line or "72" in line or "65" in line or "75" in line:
        print(line)
