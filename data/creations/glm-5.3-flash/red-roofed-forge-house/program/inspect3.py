from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())

def probe(pts):
    for (x, y) in pts:
        idx = c.get(x, y)
        print("(%3d,%3d) -> %s" % (x, y, c.color_name(idx) if idx is not None else "transparent"))

print("--- gap between roof right edge and gable rake (should be wall/roof, not grass) ---")
probe([(x, y) for y in (62, 66, 70, 74) for x in (67, 70, 73, 76, 79)])
print("--- roof eaves / wall top on the left slope ---")
probe([(x, y) for x in (34, 44, 54) for y in (60, 64, 68, 72)])
