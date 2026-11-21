W, H = 48, 42
DX, DY = 5, 7          # sprite origin inside the bigger canvas

BLACK = "#141b1b"
YEL   = "#ffe18d"
BODY  = "#adbc3a"
DARK  = "#74a334"
SKIN  = "#c8966b"
WHITE = "#fce2ca"

# ---------- frame 1: original content on the bigger canvas ----------
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, DX, DY)

# ---------- the hit expression: eye rolled up, mouth wide open ----------
hurt = input_canvas.copy(name="hurt")
hurt.rect(17, 16, 3, 3, WHITE)        # clear the old pupil
hurt.rect(17, 15, 3, 2, BLACK)        # pupil rolled up against the top rim

hurt.rect(14, 21, 9, 6, BODY)         # wipe the closed mouth bracket
hurt.ellipse(18, 24, 4, 2, BLACK)     # open maw
hurt.line(15, 22, 21, 22, YEL)        # upper tooth row
hurt.line(17, 25, 19, 25, SKIN)       # tongue
hurt.set(14, 23, DARK)
hurt.set(22, 23, DARK)

# lower legs live on sprite rows 29-32
legL = hurt.select(6, 29, 7, 4)       # monster's right foot (image left)
legR = hurt.select(24, 29, 7, 4)      # planted foot (image right)
torso = hurt.copy(name="torso")
torso.clear(0, 29, 37, 4)

BANDS = [(0, 11), (12, 21), (22, 28)]


def pose(offsets, dy, lift, name):
    out = new_canvas(W, H, name=name)
    # body leans back: upper bands drift further right, the whole mass rises
    for (y0, y1), dx in zip(BANDS, offsets):
        part = torso.select(0, y0, 37, y1 - y0 + 1)
        part.copy_to(DX + dx, DY + y0 - dy, out, mode="over")

    hip = offsets[-1]
    # planted leg keeps its ground contact; the thigh stretches up to the hip
    for y in range(36 - dy, 36):
        frac = (35 - y) / (dy - 1) if dy > 1 else 0.0
        xo = int(round(hip * frac))
        out.set(29 + xo, y, BLACK)
        out.rect(30 + xo, y, 4, 1, DARK)
        out.set(34 + xo, y, BLACK)
    legR.copy_to(24 + DX, 29 + DY, out, mode="over")

    # the other leg swings up off the ground, thigh following the hip
    ly = 29 + DY - dy - lift
    lx = 6 + DX + hip - 1
    for i in range(lift + dy):
        out.set(lx + 1, ly + 4 + i, BLACK)
        out.rect(lx + 2, ly + 4 + i, 4, 1, DARK)
        out.set(lx + 6, ly + 4 + i, BLACK)
    legL.copy_to(lx, ly, out, mode="over")
    return out


f2 = pose([3, 2, 1], 2, 3, "f2")
f3 = pose([6, 4, 2], 4, 6, "f3")


def tint(c, rgb=(255, 50, 40), amount=0.6, dark=(62, 12, 12)):
    w, h = c.stats()["size"]
    mapping = {}
    for e in c.palette():
        r, g, b, a = e["rgba"]
        if a == 0:
            continue
        if r + g + b < 160:
            mapping[e["index"]] = (dark[0], dark[1], dark[2], a)
        else:
            mapping[e["index"]] = (
                int(r + (rgb[0] - r) * amount),
                int(g + (rgb[1] - g) * amount),
                int(b + (rgb[2] - b) * amount),
                a,
            )
    for y in range(h):
        for x in range(w):
            i = c.get(x, y)
            if i in mapping:
                c.set(x, y, mapping[i])
    return c


tint(f3)   # red impact filter over the whole monster

view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
