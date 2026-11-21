W, H = 44, 41
OX, OY = 3, 4
GROUND = OY + 32          # canvas row the foot claws stand on in frame 1
ANGLE = 13                # clockwise lean-back, degrees

# ---------------- frame 1 : the original picture ----------------
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, OX, OY)

# ---------------- source edits : eye and mouth ----------------
src = input_canvas.copy(name="src")
DARK  = src.color('c0')
WHITE = src.color('c5')
LIP   = src.color('c4')

# the single eye: the pupil rolls upward, pressed against the top lid
for y in range(15, 20):
    for x in range(16, 20):
        if src.get(x, y) == DARK:
            src.set(x, y, WHITE)
for y in (15, 16):
    for x in (17, 18, 19):
        src.set(x, y, DARK)

# the mouth: tears open into a dark, lens-shaped opening with a lower lip
for x in range(16, 21):
    src.set(x, 22, DARK)
for x in range(14, 23):
    src.set(x, 23, DARK)
for x in range(15, 22):
    src.set(x, 24, DARK)
for x in range(16, 21):
    src.set(x, 25, LIP)

# ---------------- frame 2 : the recoil pose ----------------
recipe = src.select(0, 0, 37, 33).rotate(ANGLE, algorithm="rotsprite")
pv = recipe.preview()
pw, ph, pd = pv.to_rgba()
vis = [(x, y) for y in range(ph) for x in range(pw) if pd[(y * pw + x) * 4 + 3] > 0]
bx0 = min(p[0] for p in vis); bx1 = max(p[0] for p in vis)
by0 = min(p[1] for p in vis); by1 = max(p[1] for p in vis)
yR = max(y for (x, y) in vis if 22 <= x <= 32)      # lowest pixel of the planted (right) foot
dx = round(OX + 18.5 - pw / 2)                       # keep the body's centre column
dy = GROUND - yR                                     # keep the planted foot on the ground
if by1 + dy > H - 1: dy = H - 1 - by1
if by0 + dy < 0:     dy = -by0
if bx0 + dx < 0:     dx = -bx0
if bx1 + dx > W - 1: dx = W - 1 - bx1
print("preview", pw, "x", ph, "| bbox", (bx0, by0, bx1, by1),
      "| planted foot bottom", yR, "| blit", (dx, dy))

f2 = new_canvas(W, H, name="f2")
f2.blit(pv, dx, dy)

# ---------------- frame 3 : the blow lands - red filter ----------------
f3 = new_canvas(W, H, name="f3")
w2, h2, rgba = f2.to_rgba()
KR, SG, SB = 0.50, 0.30, 0.30       # push red up, crush green/blue: a red flash
cache = {}
for y in range(h2):
    for x in range(w2):
        i = (y * w2 + x) * 4
        if rgba[i + 3] == 0:
            continue
        key = (rgba[i], rgba[i + 1], rgba[i + 2])
        v = cache.get(key)
        if v is None:
            v = (round(key[0] + KR * (255 - key[0])),
                 round(key[1] * SG),
                 round(key[2] * SB), 255)
            cache[key] = v
        f3.set(x, y, v)
print("frame 3 palette:", [p['rgba'] for p in f3.palette() if p['index'] > 0])

# ---------------- report ----------------
for c in (f1, f2, f3):
    print(c.stats_text())

def dump(c, x0, y0, x1, y1, label):
    print("---", label, "---")
    print("    " + "".join(str(i % 10) for i in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            idx = c.get(x, y)
            row.append("." if idx in (0, None) else chr(ord('a') + idx - 1))
        print(f"{y:3d} " + "".join(row))

dump(f2, 0, 0, 43, 40, "frame 2")
dump(f3, 0, 0, 43, 40, "frame 3")

finish([f1, f2, f3])
