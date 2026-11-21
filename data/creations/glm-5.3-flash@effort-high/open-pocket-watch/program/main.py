import math

c = new_canvas(64, 64, background='#0a0705', name='open-pocket-watch')

# ---------------- palette ----------------
BG      = c.color('#0a0705', 'bg')
GLOW1   = c.color('#191007', 'glow1')
GLOW2   = c.color('#2a1c0c', 'glow2')
OUT     = c.color('#120b04', 'outline')
DEEP    = c.color('#4a3208', 'gold_deep')
DGOLD   = c.color('#6e4c10', 'gold_dark')
MGOLD   = c.color('#a3761c', 'gold_mid')
LGOLD   = c.color('#d4a437', 'gold_light')
HILITE  = c.color('#f7dc82', 'gold_hilite')
SPARK   = c.color('#fff6d8', 'spark')
STEELD  = c.color('#565b64', 'steel_dark')
STEELM  = c.color('#99a0aa', 'steel_mid')
STEELL  = c.color('#d9dee5', 'steel_light')
PLATED  = c.color('#2b1e0c', 'plate_dark')
PLATEM  = c.color('#5a431c', 'plate_mid')
RUBY    = c.color('#b81f3a', 'ruby')
RUBYL   = c.color('#ef6a84', 'ruby_light')
CREAM   = c.color('#efe3c4', 'dial')
CREAMD  = c.color('#c9b68c', 'dial_shade')
CREAMH  = c.color('#f8f0da', 'dial_hilite')
HANDD   = c.color('#1a2338', 'hand_dark')
HANDL   = c.color('#41598c', 'hand_light')

CX, CY = 27, 33          # watch centre
LX, LY = 47, 38          # open lid centre


def P(cx, cy, r, adeg):
    a = math.radians(adeg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc(cx, cy, r, a0, a1, col, step=2):
    a = a0
    while a <= a1:
        x, y = P(cx, cy, r, a)
        c.set(int(round(x)), int(round(y)), col)
        a += step


def thick_ray(cx, cy, r0, r1, a, col):
    """Radial tick, 2px wide."""
    x0, y0 = P(cx, cy, r0, a)
    x1, y1 = P(cx, cy, r1, a)
    x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
    c.line(x0, y0, x1, y1, col)
    if abs(math.cos(math.radians(a))) >= abs(math.sin(math.radians(a))):
        c.line(x0 + 1, y0, x1 + 1, y1, col)
    else:
        c.line(x0, y0 + 1, x1, y1 + 1, col)


def gear(cx, cy, rb, rt, n, body, shade, hub, jewel=False):
    for i in range(n):
        x, y = P(cx, cy, rt, 360.0 * i / n)
        c.set(int(round(x)), int(round(y)), body)
    c.circle(cx, cy, rb, body)
    if rb >= 3:
        c.circle(cx, cy, rb - 1, shade, fill=False)
    c.circle(cx, cy, 1, hub)
    if jewel:
        c.set(cx, cy, RUBY)
        c.set(cx - 1, cy - 1, RUBYL)


def sparkle(x, y):
    c.set(x, y, SPARK)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        c.set(x + dx, y + dy, LGOLD)


# ================= background glow =================
c.fill_at(0, 0, BG)
c.ellipse(26, 32, 24, 26, GLOW1)
c.ellipse(26, 32, 14, 16, GLOW2)

# ================= open lid (behind, right) =================
c.circle(LX, LY, 16, OUT)
c.circle(LX, LY, 15, MGOLD)
c.circle(LX, LY, 12, PLATED)                # deep recessed interior
c.circle(LX, LY, 11, DGOLD, fill=False)     # step into the recess
c.circle(LX, LY, 8, MGOLD, fill=False)      # polished inner ring
c.circle(LX, LY, 5, MGOLD)                  # centre medallion
c.circle(LX, LY, 3, DGOLD)
c.set(LX - 1, LY - 1, LGOLD)                # medallion glint
arc(LX, LY, 15, 182, 268, LGOLD)            # rim catching the light
arc(LX, LY, 14, 190, 258, HILITE)
arc(LX, LY, 15, 6, 84, DEEP)                # rim shadow
arc(LX, LY, 8, 200, 240, LGOLD, 3)          # brushed glints on the ring
arc(LX, LY, 11, 30, 62, DEEP, 3)
c.set(44, 28, SPARK)
c.set(43, 29, LGOLD)
c.set(51, 46, LGOLD)
c.set(50, 45, MGOLD)

# ================= hinges =================
c.rect(43, 22, 6, 3, DGOLD)
c.rect(43, 24, 6, 1, DEEP)
c.set(44, 23, LGOLD)
c.rect(41, 47, 6, 3, DGOLD)
c.rect(41, 49, 6, 1, DEEP)
c.set(42, 48, LGOLD)

# ================= crown + bow =================
c.circle(27, 5, 3, DGOLD, fill=False)
c.set(25, 3, LGOLD)
c.set(24, 4, LGOLD)
c.rect(24, 8, 7, 4, MGOLD)
c.rect(24, 8, 7, 1, LGOLD)
c.rect(24, 11, 7, 1, DEEP)
for x in (25, 27, 29):
    c.set(x, 9, DGOLD)
    c.set(x, 10, DGOLD)
c.set(26, 9, HILITE)

# ================= chain (drapes down the left edge) =================
chain = [(24, 4), (20, 4), (16, 5), (12, 7), (9, 10), (7, 14), (5, 18),
         (4, 23), (4, 28), (5, 33), (6, 38), (7, 43), (8, 48), (10, 53),
         (12, 57), (14, 60)]
for (x0, y0), (x1, y1) in zip(chain, chain[1:]):
    c.line(x0, y0, x1, y1, DGOLD)
    c.line(x0, y0 + 1, x1, y1 + 1, DGOLD)
for i, (x, y) in enumerate(chain):
    c.set(x, y, LGOLD if i % 2 == 0 else DEEP)
    c.set(x, y + 1, DGOLD)
c.circle(15, 61, 2, MGOLD)                  # clasp
c.set(14, 60, LGOLD)
c.set(16, 62, DEEP)

# ================= case + dial =================
c.circle(CX, CY, 21, OUT)
c.circle(CX, CY, 20, MGOLD)
c.circle(CX, CY, 17, CREAM)
arc(CX, CY, 19, 185, 265, LGOLD)            # band highlight upper-left
arc(CX, CY, 20, 192, 258, HILITE)
arc(CX, CY, 19, 5, 85, DEEP)                # band shadow lower-right
arc(CX, CY, 20, 12, 78, DGOLD)
arc(CX, CY, 19, 120, 150, LGOLD, 3)         # faint rim light lower-left
arc(CX, CY, 17, 25, 125, CREAMD)            # dial rim shading
arc(CX, CY, 17, 195, 265, CREAMH)

# chapter ring: ticks
for h in range(12):
    a = h * 30 - 90
    if h % 3 == 0:
        thick_ray(CX, CY, 12.5, 16, a, HANDD)
    else:
        x0, y0 = P(CX, CY, 14.5, a)
        x1, y1 = P(CX, CY, 16, a)
        c.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), HANDD)
for m in range(60):
    if m % 5 == 0:
        continue
    x, y = P(CX, CY, 15, m * 6 - 90)
    c.set(int(round(x)), int(round(y)), CREAMD)
c.circle(CX, CY, 12, CREAMD, fill=False)    # inner chapter edge

# ================= skeleton aperture with the gear train =================
AX, AY = 26, 43
c.circle(AX, AY, 8, PLATED)
c.circle(AX, AY, 8, DGOLD, fill=False)      # gold bezel of the window
arc(AX, AY, 8, 190, 260, LGOLD, 2)
c.circle(AX, AY, 7, PLATEM, fill=False)     # plate bevel

# wheels (meshing train)
gear(23, 40, 3, 4, 14, MGOLD, DGOLD, DGOLD)                  # barrel
c.circle(23, 40, 1, DGOLD)                                   # ratchet
c.set(23, 40, MGOLD)
c.set(22, 39, SPARK)
gear(30, 41, 2, 3, 12, STEELM, STEELD, STEELD, jewel=True)   # centre wheel
gear(27, 47, 2, 3, 10, STEELL, STEELM, STEELD)               # third wheel
gear(22, 47, 1, 2, 8, STEELM, STEELD, STEELD)                # escape wheel
# balance wheel
c.circle(31, 47, 2, DGOLD, fill=False)
c.line(29, 47, 33, 47, DGOLD)
c.line(31, 45, 31, 49, DGOLD)
c.set(31, 47, RUBY)
c.set(30, 46, RUBYL)

# bridge across the train, with jewels
c.line(32, 38, 24, 48, PLATEM)
c.line(32, 39, 25, 49, PLATEM)
c.line(32, 38, 24, 48, LGOLD)
c.set(30, 41, RUBY)
c.set(29, 40, RUBYL)
c.set(27, 45, RUBY)
c.set(32, 39, STEELL)                        # bridge screw
c.set(24, 48, STEELL)

# ================= glass reflection on the dial =================
c.set(20, 24, CREAMH)
c.set(21, 24, CREAMH)
c.set(22, 25, CREAMH)
c.set(33, 23, CREAMH)
c.set(34, 24, CREAMH)

# ================= hands (blued steel, 10:10) =================
x0, y0 = P(CX, CY, 8, -150)
c.line(CX, CY, int(round(x0)), int(round(y0)), HANDD)
c.line(CX, CY - 1, int(round(x0)), int(round(y0)) - 1, HANDL)
x1, y1 = P(CX, CY, 13, -30)
c.line(CX, CY, int(round(x1)), int(round(y1)), HANDD)
c.line(CX, CY - 1, int(round(x1)), int(round(y1)) - 1, HANDL)
c.circle(CX, CY, 2, MGOLD)                   # centre cap
c.set(CX, CY, DGOLD)
c.set(CX - 1, CY - 1, HILITE)

# ================= specular sparkles =================
sparkle(12, 25)
sparkle(47, 26)
sparkle(52, 44)
c.set(20, 14, HILITE)
c.set(40, 48, LGOLD)
c.set(9, 20, SPARK)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
save('watch', c)
finish(c)
