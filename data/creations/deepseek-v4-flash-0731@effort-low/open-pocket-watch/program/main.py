import math
from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, background=(16, 13, 11))

BG = (16, 13, 11)
# gold gradient (dark -> bright), light comes from the top-left
G0 = (250, 216, 128)
G1 = (222, 175, 85)
G2 = (188, 144, 58)
G3 = (142, 102, 38)
G4 = (98, 68, 28)
G5 = (56, 38, 18)
GOLD = [G0, G1, G2, G3, G4, G5]
IV = [(244, 234, 210), (216, 205, 178), (172, 160, 132)]
DARK = (38, 32, 26)
PLATE = (30, 22, 16)   # dark recess showing the movement
HIL = (255, 232, 168)
STEEL = (172, 172, 178)


def norm(v):
    l = math.hypot(v[0], v[1]) or 1.0
    return (v[0] / l, v[1] / l)


def shaded_circle(cx, cy, r, ramp, light=(-0.85, -0.85)):
    r = int(r)
    lx, ly = norm(light)
    for dy in range(-r, r + 1):
        py = cy + dy
        if not (0 <= py < 64):
            continue
        for dx in range(-r, r + 1):
            px = cx + dx
            if 0 <= px < 64:
                d = math.hypot(dx, dy)
                if d <= r:
                    b = (dx * lx + dy * ly) / d if d > 0 else 0.0
                    b = b * 0.5 + 0.5
                    idx = int(round(b * (len(ramp) - 1)))
                    idx = max(0, min(len(ramp) - 1, idx))
                    c.set(px, py, ramp[idx])


def line(x0, y0, x1, y1, col, thick=1):
    d = math.hypot(x1 - x0, y1 - y0) or 1
    px, py = (y1 - y0) / d, (x0 - x1) / d
    steps = int(d) + 1
    for i in range(steps + 1):
        t = i / steps
        bx, by = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        for ox in range(-thick, thick + 1):
            for oy in range(-thick, thick + 1):
                x, y = int(round(bx + px * ox)), int(round(by + py * oy))
                if 0 <= x < 64 and 0 <= y < 64:
                    c.set(x, y, col)


def gear(cx, cy, r, teeth, toothf=0.42):
    step = 2.0 * math.pi / teeth
    for i in range(teeth):
        a = i * step
        for rr in range(int(r * 0.62), int(r * 1.16) + 1):
            x = int(round(cx + math.cos(a) * rr))
            y = int(round(cy + math.sin(a) * rr))
            if 0 <= x < 64 and 0 <= y < 64:
                c.set(x, y, G1)
    # body with shading
    for dy in range(-r, r + 1):
        py = cy + dy
        if not (0 <= py < 64):
            continue
        for dx in range(-r, r + 1):
            px = cx + dx
            if 0 <= px < 64:
                d = math.hypot(dx, dy)
                if d <= r * 0.94:
                    b = (-dx - dy) / (d * math.sqrt(2)) if d > 0 else 0.0
                    b = max(0.0, min(1.0, b * 0.5 + 0.5))
                    idx = int(round(b * 5))
                    idx = max(0, min(5, idx))
                    c.set(px, py, GOLD[idx])
    # centre screw
    sr = max(1, int(r * 0.24))
    for dy in range(-sr, sr + 1):
        for dx in range(-sr, sr + 1):
            if dx * dx + dy * dy <= sr * sr:
                x, y = cx + dx, cy + dy
                if 0 <= x < 64 and 0 <= y < 64:
                    c.set(x, y, G4)
    c.set(cx, cy, G0)


# ---------- back lid (open movement) top-right ----------
BACK = (46, 30)
shaded_circle(BACK[0], BACK[1], 13, GOLD)
shaded_circle(BACK[0], BACK[1], 10, [G5, G4, G3, G2, G3, G4])
# deep recess plate
for dy in range(-10, 11):
    for dx in range(-10, 11):
        if dx * dx + dy * dy <= 10 * 10:
            x, y = BACK[0] + dx, BACK[1] + dy
            if 0 <= x < 64 and 0 <= y < 64:
                c.set(x, y, PLATE)

# gears meshing inside the lid
gear(45, 30, 6, 8)
gear(38, 36, 4, 7)
gear(52, 36, 4, 7)
gear(45, 39, 3, 6)
gear(38, 25, 3, 6)
gear(52, 27, 3, 6)
gear(45, 36, 3, 8)

# bright rim highlights on the lid (left-top) + screws
for k in range(-140, -39):
    a = math.radians(k)
    x = int(round(BACK[0] + math.cos(a) * 13))
    y = int(round(BACK[1] + math.sin(a) * 13))
    for ox in range(-1, 2):
        for oy in range(-1, 2):
            xx, yy = x + ox, y + oy
            if 0 <= xx < 64 and 0 <= yy < 64:
                if abs(math.hypot(xx - BACK[0], yy - BACK[1]) - 13) < 1.2:
                    c.set(xx, yy, HIL)
screws = [(38, 19), (54, 23), (53, 38)]
for (sx, sy) in screws:
    c.set(sx, sy, G5)
    c.set(sx - 1, sy - 1, HIL)

# ---------- front dial (left) ----------
FR = (20, 34)
shaded_circle(FR[0], FR[1], 15, GOLD)
shaded_circle(FR[0], FR[1], 11.5, IV)
# bright bezel sweep + depth shadow
for k in range(-150, -30):
    a = math.radians(k)
    for rr in range(int(10.6), 16):
        x = int(round(FR[0] + math.cos(a) * rr))
        y = int(round(FR[1] + math.sin(a) * rr))
        if 0 <= x < 64 and 0 <= y < 64:
            d = math.hypot(x - FR[0], y - FR[1])
            if d > 11.2:
                c.set(x, y, HIL)

# tick marks
for kk in range(60):
    a = math.radians(kk * 6 - 90)
    if kk % 5 == 0:
        r0, r1 = 7.5, 10.4
        col = DARK
    else:
        r0, r1 = 9.2, 10.4
        col = (96, 84, 62)
    for rr in range(int(r0), int(r1) + 1):
        x = int(round(FR[0] + math.cos(a) * rr))
        y = int(round(FR[1] + math.sin(a) * rr))
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, col)

# hands (10:08) — classic openwork hands
for rr in range(1, 11):
    x = int(round(FR[0] + math.cos(math.radians(240)) * rr))
    y = int(round(FR[1] + math.sin(math.radians(240)) * rr))
    if 0 <= x < 64 and 0 <= y < 64:
        col = (46, 38, 28) if rr < 11 else DARK
        c.set(x, y, col)
for rr in range(1, 13):
    x = int(round(FR[0] + math.cos(math.radians(270)) * rr))
    y = int(round(FR[1] + math.sin(math.radians(270)) * rr))
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, (46, 38, 28) if rr < 13 else DARK)
c.set(FR[0], FR[1], DARK)
c.set(FR[0] - 1, FR[1] - 1, (60, 52, 40))

# crown + ring + chain
for y in range(16, 20):
    for x in range(15, 23):
        c.set(x, y, G3)
    for x in range(14, 24):
        c.set(x, 15, G2)
    for x in range(14, 24):
        c.set(x, 14, G1)
shaded_circle(20, 11, 4, [G0, G2, G4, G2, G0])
# chain links from crown curving up to the top-left edge
def chain_link(lx, ly, ang, col1=G2, col2=G4):
    a = math.radians(ang)
    for rr in range(1, 4):
        for oa in range(0, 360, 15):
            s = math.radians(oa)
            x = int(round(lx + math.cos(s) * rr * 0.9))
            y = int(round(ly + math.sin(s) * rr * 0.9))
            if 0 <= x < 64 and 0 <= y < 64:
                c.set(x, y, col1 if oa % 30 == 0 else col2)
# chain path up toward top edge
seg = [(20, 8), (19, 5), (17, 2), (13, 0)]
for i, (lx, ly) in enumerate(seg):
    ang = -90 + i * 8
    chain_link(lx, ly, -90, G1 if i == 0 else G2, G4)
# short chain segments at the very top connecting off-canvas
c.set(10, 0, G3); c.set(11, 1, G3); c.set(12, 1, G4); c.set(13, 1, G4)

# center stud on dial
shaded_circle(FR[0], FR[1], 2, [HIL, G1, G3, G5, G3])

finish(c)
print(c.stats_text())
