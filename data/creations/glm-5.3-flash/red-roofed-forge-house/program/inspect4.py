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
        if name in ("#3f7a33ff", "#35682bff", "#4a8a39ff", "#59994aff", "#2c4a24ff", "transparent"):
            bad.append((x, y))
    return bad

print("--- gap between roof right edge and gable rake ---")
b1 = probe([(x, y) for y in (62, 66, 70, 74) for x in (67, 70, 73, 76, 79)])
print("--- eaves / wall top left slope ---")
b2 = probe([(x, y) for x in (34, 44, 54) for y in (58, 62, 66, 70)])
print("--- roof lower edge vs wall top (should be roof or wall, never grass) ---")
b3 = probe([(x, y) for x in (30, 40, 50, 60, 70, 80) for y in (78, 82, 86)])
print("BAD PIXELS:", b1 + b2 + b3)
