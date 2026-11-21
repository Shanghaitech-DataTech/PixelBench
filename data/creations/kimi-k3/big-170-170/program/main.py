import math, random

out = input_canvas.copy(name="output")

# ---------- palette ----------
PANEL   = out.color('#1c184b')
PANEL_D = out.color('#16133d')
PANEL_L = out.color('#2a2260')
SHELF   = out.color('#3b3560')
SHELF_L = out.color('#6e68a0')
GLASS   = out.color('#efe0d2')
GLASS_D = out.color('#1e2c50')
PUD     = out.color('#233a4e')
BOT     = out.color('#c8402a')
BOT_D   = out.color('#7a2418')
BOT_L   = out.color('#e8e8f0')
CAN1    = out.color('#3a7ab8')
CAN1_D  = out.color('#24486e')
CAN2    = out.color('#48b0a0')
CAN2_D  = out.color('#2a6e64')
JUICE   = out.color('#c8b040')
JUICE_D = out.color('#6e5c20')
SKY     = out.color('#0b3245')
SKY_D   = out.color('#0a2e3f')
CLOUD   = out.color('#14485c')
GRASS   = out.color('#162524')
GROUND  = out.color('#3f3136')

# ---------- helpers ----------
_palc = {}
def rgba(x, y):
    idx = out.get(x, y)
    v = _palc.get(idx)
    if v is None:
        for e in out.palette():
            _palc[e['index']] = e['rgba']
        v = _palc.get(idx, (0, 0, 0, 0))
    return v

def q8(v):
    return max(0, min(255, (int(v) // 8) * 8 + 4))

def blend(rgb, tgt, t):
    return (q8(rgb[0] + (tgt[0] - rgb[0]) * t),
            q8(rgb[1] + (tgt[1] - rgb[1]) * t),
            q8(rgb[2] + (tgt[2] - rgb[2]) * t))

def bottle(x, y, h, body, dark):
    out.rect(x, y, 3, h, body)
    out.set(x, y, dark); out.set(x, y + h - 1, dark)
    out.rect(x + 1, y - 2, 1, 2, body)
    out.set(x + 1, y - 3, BOT_L)

def can(x, y, h, body, dark):
    out.rect(x, y, 4, h, body)
    out.set(x, y, dark); out.set(x + 3, y, dark)
    out.set(x, y + h - 1, dark); out.set(x + 3, y + h - 1, dark)
    out.set(x + 1, y + 1, BOT_L)

def carton(x, y, h, body, dark):
    out.rect(x, y, 4, h, body)
    out.set(x, y, dark); out.set(x + 3, y, dark)
    out.set(x, y + h - 1, dark); out.set(x + 3, y + h - 1, dark)
    out.rect(x + 1, y - 1, 2, 1, dark)

# ---------- 1. rebuild the vending machine over the fox ----------
out.rect(84, 54, 41, 69, GLASS)   # bright interior window
rows = [(66, [(bottle, 88, 8, BOT, BOT_D), (can, 93, 6, CAN1, CAN1_D),
              (bottle, 99, 8, BOT, BOT_D), (can, 104, 6, CAN2, CAN2_D),
              (bottle, 110, 8, BOT, BOT_D), (can, 115, 6, CAN1, CAN1_D),
              (carton, 120, 6, JUICE, JUICE_D)]),
        (84, [(can, 88, 6, CAN2, CAN2_D), (bottle, 94, 8, BOT, BOT_D),
              (can, 99, 6, CAN1, CAN1_D), (bottle, 105, 8, BOT, BOT_D),
              (can, 111, 6, CAN2, CAN2_D), (carton, 116, 6, JUICE, JUICE_D),
              (bottle, 121, 7, BOT, BOT_D)]),
        (102, [(bottle, 88, 8, BOT, BOT_D), (carton, 93, 6, JUICE, JUICE_D),
               (bottle, 99, 8, BOT, BOT_D), (can, 104, 6, CAN2, CAN2_D),
               (bottle, 110, 8, BOT, BOT_D), (can, 115, 6, CAN1, CAN1_D),
               (carton, 120, 6, JUICE, JUICE_D)]),
        (120, [(can, 88, 6, CAN1, CAN1_D), (bottle, 94, 8, BOT, BOT_D),
               (can, 99, 6, CAN2, CAN2_D), (bottle, 105, 8, BOT, BOT_D),
               (can, 111, 6, CAN1, CAN1_D), (bottle, 117, 7, BOT, BOT_D)])]
for shelf_y, items in rows:
    for it in items:
        it[0](it[1], shelf_y - it[2], it[2], it[3], it[4])
for shelf_y, items in rows:
    out.rect(84, shelf_y, 41, 2, SHELF)
    out.rect(84, shelf_y, 41, 1, SHELF_L)
out.rect(80, 54, 4, 72, PANEL)          # left inner frame
out.rect(84, 123, 41, 3, PANEL)         # window bottom frame
out.rect(80, 126, 45, 1, PANEL_L)
out.rect(80, 127, 45, 19, PANEL)        # machine front (was legs)
out.rect(81, 131, 43, 1, PANEL_L)
out.rect(84, 136, 32, 7, GLASS_D)       # pickup hatch
out.rect(84, 136, 32, 1, PANEL_D)
out.rect(84, 142, 32, 1, PANEL_D)
for x in range(96, 118):                # soften hatch behind front wheel arc
    ytop = 158 - int(math.sqrt(max(0, 484 - (x - 118) ** 2)))
    for y in range(max(136, ytop), 143):
        if rgba(x, y)[:3] == (30, 44, 80):
            out.set(x, y, PUD)
out.rect(125, 54, 9, 92, PANEL)         # right narrow panel
out.rect(125, 54, 9, 1, PANEL_L)
out.rect(128, 104, 4, 5, GLASS_D)       # dispensing button
out.set(129, 105, '#7fd8e8'); out.set(130, 106, '#4a90a8')
out.set(129, 103, SHELF_L)
out.rect(82, 146, 50, 3, PANEL_D)       # base shadow + feet
out.rect(84, 149, 6, 2, PANEL_D)
out.rect(122, 149, 6, 2, PANEL_D)

# ---------- 2. seam patches around the machine ----------
for x, y in [(76, 60), (77, 60), (76, 62), (77, 62), (78, 62), (76, 64),
             (79, 60), (78, 60), (79, 64), (78, 64), (77, 66), (76, 68),
             (77, 70), (76, 72), (77, 74), (78, 72), (79, 76), (78, 78),
             (77, 78), (76, 80), (78, 82), (77, 84), (78, 86), (79, 82)]:
    out.set(x, y, SKY if (x + y) % 3 else SKY_D)
out.set(76, 66, CLOUD); out.set(77, 68, CLOUD); out.set(76, 74, CLOUD)
for x in range(84, 136, 3):             # sky just above roof
    out.set(x, 52, SKY); out.set(x + 1, 53, SKY_D)
for x in range(84, 134, 5):
    out.set(x, 51, CLOUD)
out.rect(62, 100, 17, 12, SKY_D)        # handlebar/mirror stubs -> sky
out.rect(63, 101, 14, 3, CLOUD)
out.rect(66, 107, 11, 4, SKY)
for (x, y) in [(76, 144), (77, 144), (78, 144), (79, 144), (76, 145), (77, 145),
               (78, 145), (79, 145), (75, 143), (76, 143)]:
    out.set(x, y, GRASS if y < 144 else GROUND)

# ---------- 3. puddle where the fox sat ----------
out.ellipse(104, 151, 13, 3, PUD)
out.ellipse(104, 150, 10, 2, '#2c4a62')
out.set(97, 150, '#6f93ad'); out.set(100, 151, '#6f93ad')
out.set(110, 150, '#5d829c'); out.set(106, 152, '#8fb0c8')

# ---------- 4. lightning bolts ----------
try:
    def bolt(points, core='#fff8d8'):
        for i in range(len(points) - 1):
            x0, y0 = points[i]; x1, y1 = points[i + 1]
            out.line(x0, y0, x1, y1, '#e8d890')
            out.line(x0 + 1, y0, x1 + 1, y1, '#e8d890')
        for i in range(len(points) - 1):
            x0, y0 = points[i]; x1, y1 = points[i + 1]
            out.line(x0, y0, x1, y1, core)
    bolt([(58, 8), (49, 30), (55, 32), (44, 56), (50, 58), (40, 82)])
    bolt([(49, 30), (41, 42), (45, 44), (38, 56)], core='#ffe89a')
    bolt([(55, 32), (62, 46), (58, 48), (63, 60)], core='#ffe89a')
    bolt([(158, 4), (151, 24), (156, 26), (148, 46)])
    bolt([(156, 26), (162, 38), (159, 40)], core='#ffe89a')
except Exception:
    pass

# ---------- 5. storm darkening (explicit opaque blends) ----------
for y in range(170):
    for x in range(170):
        r, g, b, a = rgba(x, y)
        if a == 0 or r + g + b > 480:
            continue
        if 80 <= x <= 134 and 50 <= y <= 146:
            t, tgt = 0.18, (10, 10, 24)     # keep the machine glowing
        elif y < 128:
            t, tgt = 0.35, (3, 8, 16)       # sky
        elif y < 142:
            t, tgt = 0.30, (2, 8, 10)       # grass band
        else:
            t, tgt = 0.38, (8, 8, 20)       # ground
        out.set(x, y, blend((r, g, b), tgt, t))
out.rect(62, 100, 17, 12, SKY_D)            # repaint patch after darkening
out.rect(64, 102, 13, 2, '#0e3b50')

# ---------- 6. wet ground sheen + reflections ----------
try:
    rnd = random.Random(7)
    for y in range(143, 170, 2):
        x = rnd.randrange(0, 160)
        ln = rnd.randrange(4, 12)
        t = rnd.uniform(0.15, 0.4)
        for xx in range(x, min(170, x + ln)):
            r, g, b, a = rgba(xx, y)
            if a:
                out.set(xx, y, blend((r, g, b), (26, 60, 78), t))
    for y in (150, 152, 154):               # purple reflection under machine
        for xx in range(86, 130):
            if rnd.random() < 0.55:
                r, g, b, a = rgba(xx, y)
                if a:
                    out.set(xx, y, blend((r, g, b), (46, 40, 96), 0.35))
    for xx, yy in [(85, 163), (86, 163), (84, 164), (88, 163), (60, 166),
                   (62, 167), (63, 166), (105, 160), (107, 161), (40, 162), (42, 163)]:
        r, g, b, a = rgba(xx, yy)
        if a:
            out.set(xx, yy, blend((r, g, b), (220, 230, 240), 0.25))
except Exception:
    pass

# ---------- 7. rain: semi-transparent droplet streaks ----------
try:
    rr = random.Random(42)
    layers = [((170, 200, 225), 0.35, 150, 90, 1, 5),
              ((190, 215, 240), 0.50, 170, 60, 1, 7),
              ((215, 235, 250), 0.65, 200, 30, 2, 9)]
    for tint, k, alpha, n, w, ln in layers:
        for i in range(n):
            x = rr.randrange(0, 170)
            y = rr.randrange(-10, 168)
            for kk in range(ln):
                xx, yy = x - (kk // 2), y + kk
                if 0 <= xx < 170 and 0 <= yy < 170:
                    r, g, b, a = rgba(xx, yy)
                    if a:
                        out.set(xx, yy, blend((r, g, b), tint, k) + (alpha,))
                    if w == 2 and kk % 2 == 0 and xx + 1 < 170:
                        r, g, b, a = rgba(xx + 1, yy)
                        if a:
                            out.set(xx + 1, yy, blend((r, g, b), tint, k) + (alpha // 2,))
    for i in range(14):                     # big near droplets
        x = rr.randrange(0, 168); y = rr.randrange(0, 160)
        for dx in (0, 1):
            for dy in (0, 1):
                r, g, b, a = rgba(x + dx, y + dy)
                if a:
                    out.set(x + dx, y + dy, blend((r, g, b), (225, 242, 252), 0.7) + (210,))
except Exception:
    pass

# ---------- 8. clinging water droplets ----------
try:
    rr2 = random.Random(99)
    def drip(x, y, bright=(235, 246, 255)):
        r, g, b, a = rgba(x, y)
        if not a:
            return
        out.set(x, y, blend((r, g, b), bright, 0.62))
        if y + 1 < 170:
            r2, g2, b2, a2 = rgba(x, y + 1)
            if a2:
                out.set(x, y + 1, blend((r2, g2, b2), bright, 0.28))
    for i in range(34):                     # on the vending machine
        drip(rr2.randrange(80, 135), rr2.randrange(54, 146))
    for x in range(84, 134, 4):             # roof edge beads
        for yy in range(51, 58):
            r, g, b, a = rgba(x, yy)
            if a and r < 70 and b > 50:
                drip(x, yy, (210, 225, 255))
                break
    for i in range(30):                     # on the motorcycle
        drip(rr2.randrange(28, 126), rr2.randrange(106, 150))
    for i in range(12):                     # on the pole
        drip(rr2.randrange(35, 43), rr2.randrange(10, 130), (200, 215, 235))
    for i in range(26):                     # splash ticks on the ground
        x = rr2.randrange(0, 170); y = rr2.randrange(143, 168)
        r, g, b, a = rgba(x, y)
        if a:
            out.set(x, y, blend((r, g, b), (200, 220, 240), 0.5) + (170,))
except Exception:
    pass

view(out, scale=4)
try:
    save("output", out)
except Exception:
    pass
finish(out)
