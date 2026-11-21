c = input_canvas

def runs(y, x0, x1):
    out = []
    prev = None
    start = x0
    for x in range(x0, x1 + 1):
        idx = c.get(x, y)
        if idx != prev:
            if prev not in (None, 0):
                out.append((start, x - 1, prev))
            prev = idx
            start = x
    if prev not in (None, 0):
        out.append((start, x1, prev))
    return out

print("EYE/MOUTH rows 11-26, x 10-26 (colour id):")
for y in range(11, 27):
    print(" y=%2d" % y, runs(y, 10, 26))
print()
print("FEET rows 26-32, full width:")
for y in range(26, 33):
    print(" y=%2d" % y, runs(y, 0, 36))
print()
print("HEAD top rows 0-10, full width:")
for y in range(0, 11):
    print(" y=%2d" % y, runs(y, 0, 36))

# ---- rotation calibration test ----
t = c.copy(name="t")
print()
print("pixel(27,32) id =", t.get(27, 32))
t.set(27, 32, (255, 0, 255))
s = t.select(0, 0, 37, 33)
s.rotate(12, algorithm="rotsprite")
pv = s.preview()
w, h, data = pv.to_rgba()
print("preview size:", w, h)
found = []
for y in range(h):
    for x in range(w):
        i = (y * w + x) * 4
        if data[i + 3] > 0 and data[i] > 200 and data[i + 2] > 200 and data[i + 1] < 100:
            found.append((x, y))
print("marker(27,32) found at:", found)
