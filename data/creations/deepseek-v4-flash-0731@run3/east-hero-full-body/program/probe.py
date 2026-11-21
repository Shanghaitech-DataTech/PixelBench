from pixelbench_api import load

r = load("exports/east-hero.pixelart.json", add=False, name="r")

pal = r.palette()
for p in pal:
    print(p["index"], p["name"], p["rgba"])

probes = [
    (122, 42, "hat cone top"),
    (122, 66, "cone mid"),
    (122, 80, "brim inner"),
    (150, 92, "brim right"),
    (124, 106, "face"),
    (124, 126, "chest"),
    (100, 130, "left shoulder"),
    (150, 230, "right robe hem"),
    (82, 170, "sword blade"),
    (82, 150, "hand/pommel"),
    (82, 200, "sword lower"),
    (66, 164, "sword guard"),
    (150, 158, "sash knot"),
    (120, 150, "sash"),
    (70, 170, "hair left"),
    (180, 165, "sash tail"),
    (122, 96, "under brim"),
    (196, 46, "moon"),
    (172, 34, "glow area"),
    (30, 100, "far ridge top"),
    (120, 200, "robe center"),
    (112, 228, "boot"),
    (128, 60, "sky mid"),
    (140, 120, "robe shoulder"),
]
print()
for (x, y, label) in probes:
    idx = r.get(x, y)
    print("%-16s (%d,%d) idx=%d name=%s" % (label, x, y, idx, r.color_name(idx)))
