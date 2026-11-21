from pixelbench_api import *  # noqa

c = load("exports/player.pixelart.json", add=False)
CH = {}
m = {"outline": "O", "body": "B", "body_hi": "H", "body_sh": "s",
     "frame": "F", "glass": "g", "tape": "t", "tape_hi": "T",
     "cream": "C", "hub": "u", "panel": "P", "panel_hi": "p",
     "keysym": "k", "accent": "A", "metal": "M", "metal_hi": "m",
     "metal_dk": "d", "cable": "~"}
for entry in c.palette():
    if entry["rgba"][3] == 0:
        CH[entry["index"]] = "."
for entry in c.palette():
    idx = entry["index"]
    if idx in CH:
        continue
    CH[idx] = m.get(entry["name"] or "", "?")
print("   " + "".join(str(x % 10) for x in range(32)))
for y in range(32):
    print(f"{y:2d} " + "".join(CH.get(c.get(x, y), "?") for x in range(32)))
print(c.stats_text())
