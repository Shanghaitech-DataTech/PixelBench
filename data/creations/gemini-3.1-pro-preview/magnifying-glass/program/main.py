from pixelbench_api import *

c = new_canvas(16, 16)

# 1. Handle (drawn first, behind everything)
for x in range(2, 8):
    c.set(x, 13 - x, "#9c6b3a") # hi
    c.set(x, 14 - x, "#704822") # base
    c.set(x, 15 - x, "#704822") # base
    c.set(x, 16 - x, "#4a2e15") # dark

# Handle Tip
c.set(1, 12, "#704822") # base
c.set(1, 13, "#4a2e15") # dark

# 2. Lens
cmap = {
    '7': "#4a4a4a", # outer rim
    '8': "#8a8a8a", # inner rim
    '9': "#88ccff", # glass base
    'A': "#ffffff", # glass hi
    'B': "#5599cc", # glass shadow
    'C': "#bce3ff", # glass glare
    'D': "#c0c0c0", # inner rim hi
    'E': "#6a6a6a", # outer rim hi
    '.': None
}

lens = [
    "..EE777..",
    ".EDDD887.",
    "EDDAC9887",
    "EDAC99B87",
    "78C999B87",
    "78999BB87",
    "7889BB887",
    ".7888887.",
    "..77777.."
]

for dy, row in enumerate(lens):
    for dx, char in enumerate(row):
        color = cmap.get(char)
        if color:
            c.set(7 + dx, 0 + dy, color)

# 3. Connector (drawn last, over lens and handle)
for x in range(6, 9):
    c.set(x, 13 - x, "#ffd700") # hi
    c.set(x, 14 - x, "#b8860b") # base
    c.set(x, 15 - x, "#b8860b") # base
    c.set(x, 16 - x, "#8b6508") # dark

finish(c)
