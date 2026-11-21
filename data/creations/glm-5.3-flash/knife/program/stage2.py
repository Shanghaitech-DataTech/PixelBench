import numpy as np

# ---------- 1) marker test: what does rotate(theta) mean here? ----------
t = new_canvas(21, 21)
t.set(2, 2, '#ff0000')
t.set(18, 18, '#0000ff')
r = t.select(0, 0, 21, 21).rotate(30, algorithm="nearest")
p = r.preview()
W, H = p.stats()["size"]
print("marker preview size", W, H)
arr = np.frombuffer(p.to_rgba()[2], dtype=np.uint8).reshape(H, W, 4)
ys, xs = np.nonzero((arr[:, :, 0] == 255) & (arr[:, :, 1] == 0) & (arr[:, :, 3] > 0))
red = (xs.mean(), ys.mean()) if len(xs) else None
ys, xs = np.nonzero((arr[:, :, 2] == 255) & (arr[:, :, 0] == 0) & (arr[:, :, 3] > 0))
blue = (xs.mean(), ys.mean()) if len(xs) else None
print("red", red, "blue", blue)
if red and blue:
    dx, dy = red[0] - blue[0], red[1] - blue[1]
    print("red-blue vector", dx, dy, "-> |dx|<|dy| means VISUAL-CW, |dx|>|dy| means VISUAL-CCW")

# ---------- 2) full-res dump of the rotated knife ----------
out = input_canvas.copy(name="output")
out.mirror(axis="h")
s = out.select(0, 0, 93, 128)
rot = s.rotate(53, algorithm="rotsprite").preview()
print("rot size", rot.stats()["size"], rot.stats_text())

pal = rot.palette()
letters = "abcdefghijklmnopqrstuvwxyz0123456789"
rev = {}
for k, q in enumerate(pal):
    if q["index"] > 0:
        rev[q["index"]] = letters[k % len(letters)]
print("palette:", [(q["index"], q["rgba"]) for q in pal])

def dump(canvas, x0, x1, y0, y1, step=1):
    for y in range(y0, y1):
        row = ""
        for x in range(x0, x1, step):
            i = canvas.get(x, y)
            row += "." if i == 0 else rev.get(i, "?")
        print("x%03d y=%3d %s" % (x0, y, row))

print("=== LEFT (handle) end ===")
dump(rot, 0, 52, 58, 96)
print("=== RIGHT (tip) end ===")
dump(rot, 108, 159, 55, 96)
