out = input_canvas.copy(name="output")
out.mirror(axis="h")
s = out.select(0, 0, 93, 128)
r = s.rotate(53, algorithm="rotsprite")
print("expanded size:", r.size)
prev = r.preview()
print(prev.stats_text())

# bounding box of visible pixels
st = prev.stats()
bx0, by0, bx1, by1 = st["bbox"]
print("bbox", st["bbox"])

# dump a coarse view of the rotated sprite
rev = {p["index"]: "abcdefghi"[p["index"] - 1] for p in prev.palette() if p["index"] > 0}
x0, y0, x1, y1 = bx0, by0, bx1, by1
for y in range(y0, y1 + 1, 2):
    row = ""
    for x in range(x0, x1 + 1, 2):
        i = prev.get(x, y)
        row += "." if i == 0 else rev.get(i, "?")
    print("y=%3d %s" % (y, row))
