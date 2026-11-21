from pixelbench_api import load

c = load("exports/subway_platform.pixelart.json", add=False)
print(c.palette())
print()
probes = [
    ("header door", 30, 0), ("pillar", 34, 1), ("glass", 40, 15), ("train body", 44, 15),
    ("roof", 33, 15), ("window band", 37, 15), ("skirt", 52, 3), ("floor", 58, 5),
    ("P1 head", 40, 17), ("P1 body", 44, 16), ("P2 head", 35, 32), ("P3 head", 41, 51),
    ("P3 torso", 45, 49), ("bench seat", 54, 35), ("bag", 46, 46),
]
for label, y, x in probes:
    print(f"{label:12s} ({x},{y}) = {c.color_name(c.get(x, y))}")
