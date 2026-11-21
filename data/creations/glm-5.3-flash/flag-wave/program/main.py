src = input_canvas
W, H = 48, 56

# --- analyse the flag cloth (x >= 20): the tower occupies x 0..19 and never moves ---
d3 = {}          # vertical offset per column for the LOWEST fly-end position
for x in range(20, W):
    top = None; bot = None
    for y in range(H):
        if src.get(x, y):
            if top is None: top = y
            bot = y
    # mirror the column about the hoist centre line y = 23.5
    d3[x] = 47 - top - bot
d2 = {x: d3[x] // 2 for x in d3}   # exact midpoint of the swing

def build(dmap, name):
    c = new_canvas(W, H, name=name)
    for y in range(H):
        for x in range(W):
            v = src.get(x, y)
            if v:
                ny = y + dmap.get(x, 0)
                if 0 <= ny < H:
                    c.set(x, ny, v)
    return c

f1 = src.copy(name='output')      # frame 1: original picture, fly end highest
f2 = build(d2, 'frame2')          # frame 2: halfway down
f3 = build(d3, 'frame3')          # frame 3: fly end lowest (mirrored)

# --- verification ---
for x in range(W):
    for y in range(H):
        assert f1.get(x, y) == src.get(x, y), "frame 1 must equal the input"
for f in (f2, f3):
    n = sum(1 for x in range(W) for y in range(H) if f.get(x, y))
    assert n == 1520, f"pixel count changed: {n}"
    assert f.get(20, 12) and f.get(27, 35), "hoist must stay attached"

for f in (f1, f2, f3):
    print(f.stats_text())
print("fly-end tip rows  (x=44..47):",
      [next(y for y in range(H) if f.get(44, y)) for f in (f1, f2, f3)])
print("OK")

finish([f1, f2, f3])
