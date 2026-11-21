from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())

def probe(pts):
    bad = []
    for (x, y) in pts:
        idx = c.get(x, y)
        name = c.color_name(idx) if idx is not None else "transparent"
        print("(%3d,%3d) -> %s" % (x, y, name))
        if name in ("#3f7a33ff", "#35682bff", "#4a8a39ff", "#59994aff", "#2c4a24ff", "#2e5c26ff", "transparent"):
            bad.append((x, y))
    return bad

print("--- roof right edge vs gable rake (must be roof/wall, never grass) ---")
b1 = probe([(x, y) for y in (60, 64, 68, 72, 76) for x in (66, 69, 72, 75)])
print("--- roof lower edge vs wall top (must be roof/wall) ---")
b2 = probe([(x, y) for x in (28, 36, 44, 52, 60) for y in (80, 84, 88)])
print("--- ridge cap / chimney junction (must be cap, chimney or roof) ---")
b3 = probe([(x, y) for x in (58, 62, 66, 70) for y in (20, 24, 28)])
print("--- wall base vs ground (must be wall, shadow or grass) ---")
b4 = probe([(x, y) for x in (34, 48, 62) for y in (104, 106)])
print("BAD:", b1 + b2 + b3 + b4)
