import math

DEBUG = False
W = H = 256
CX, CY = 128, 102

# ------------------------------------------------------------------ palette
OUT = "#0b0a12"   # near-black outline
BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = (
    "#332608", "#4e3a16", "#6f5520", "#8f6e2c", "#b8944a", "#d6b262", "#efd693", "#fff0c4")
GL0, GL1, GL2, GL3, GL4 = "#3a2a0e", "#7a5a1c", "#ffcf7a", "#ffe6ad", "#fff8dc"
CY0, CY1, CY2, CY3, CY4, CY5 = "#123a4a", "#18566c", "#2e93aa", "#4cb8cc", "#7fe8f0", "#c8faff"
ST0, ST1, ST2, ST3, ST4, ST5 = "#141420", "#22222c", "#2e2e3a", "#3c3c4a", "#4d4d5e", "#63637a"
BG0, BG1, BG2, BG3, BG4, BG5 = "#08080f", "#0a0c17", "#0d1021", "#111827", "#161f33", "#1d2842"
FL0, FL1, FL2 = "#0e0e17", "#171725", "#1f1f30"
PL0, PL1, PL2, PL3 = "#06060c", "#0b0b14", "#161621", "#1f1f30"
CR0, CR1, CR2, CR3, CR4 = "#0a1820", "#25617a", "#4f9ebc", "#8ecfe6", "#d8f4ff"

c = new_canvas(W, H, background=BG0, name="arcane")

# ------------------------------------------------------------------ helpers

def arc_pts(cx, cy, r, a0, a1, dens=2.0):
    span = a1 - a0
    n = max(6, int(abs(math.radians(span)) * max(r, 1) * dens) + 1)
    return [(cx + r * math.cos(math.radians(a0 + span * i / n)),
             cy + r * math.sin(math.radians(a0 + span * i / n))) for i in range(n + 1)]


def draw_pts(pts, col):
    for x, y in pts:
        c.set(int(round(x)), int(round(y)), col)


def thick_line(x0, y0, x1, y1, w, col):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    for o in range(w):
        off = o - (w - 1) / 2.0
        c.line(int(round(x0 + nx * off)), int(round(y0 + ny * off)),
               int(round(x1 + nx * off)), int(round(y1 + ny * off)), col)


def ring_band(ri, ro, base, light, shade, cx=CX, cy=CY, la=156, lb=292, sa=-24, sb=112):
    for r in range(ri, ro + 1):
        c.circle(cx, cy, r, base, fill=False)
    for r in range(ri, ro + 1):
        draw_pts(arc_pts(cx, cy, r, la, lb), light)
        draw_pts(arc_pts(cx, cy, r, sa, sb), shade)


def ring_ticks(cx, cy, r, step, col, length=1, start=0):
    for a in range(start, 360, step):
        for k in range(length):
            c.set(int(round(cx + (r + k) * math.cos(math.radians(a)))),
                  int(round(cy + (r + k) * math.sin(math.radians(a)))), col)


RUNES = [
    ["#.#", ".#.", "#.#"], [".#.", "###", ".#."], ["#..", "###", "#.."],
    ["..#", "###", "..#"], ["###", ".#.", ".#."], ["#.#", "###", "#.#"],
    [".#.", "#.#", ".#."], ["#..", "#.#", ".#."], ["##.", "..#", "##."],
    ["..#", "#.#", "#.."], ["#.#", ".##", "..#"], [".##", "#.#", "##."],
]


def glyph(x, y, pat, col):
    for j, row in enumerate(pat):
        for i, ch in enumerate(row):
            if ch != ".":
                c.set(x + i, y + j, col)


def rune_ring(cx, cy, r, step, bright, dim, offset=0, swap=2):
    k = 0
    for a in range(offset, 360 + offset, step):
        pat = RUNES[k % len(RUNES)]
        col = bright if k % swap == 0 else dim
        glyph(int(round(cx + r * math.cos(math.radians(a)))) - 1,
              int(round(cy + r * math.sin(math.radians(a)))) - 1, pat, col)
        k += 1


def ellipse_ring(rx, ry, rot, thick, base, light, shade, outline=OUT, cx=CX, cy=CY):
    rr = math.radians(rot)

    def pts(d):
        n = max(130, int(2 * math.pi * max(rx, ry) * 2.0))
        out = []
        for i in range(n + 1):
            a = 2 * math.pi * i / n
            x = (rx + d) * math.cos(a)
            y = (ry + d) * math.sin(a)
            out.append((cx + x * math.cos(rr) - y * math.sin(rr),
                        cy + x * math.sin(rr) + y * math.cos(rr)))
        return out

    draw_pts(pts(-1), outline)
    draw_pts(pts(thick), outline)
    for d in range(thick):
        for (x, y) in pts(d):
            col = base
            if y < cy - 0.42 * ry:
                col = light
            elif y > cy + 0.30 * ry:
                col = shade
            c.set(int(round(x)), int(round(y)), col)


def gear(cx, cy, r, teeth, base=BR3, light=BR5, shade=BR1, dark=OUT):
    c.circle(cx, cy, r + 2, dark)
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        tx = int(round(cx + (r + 1) * math.cos(a)))
        ty = int(round(cy + (r + 1) * math.sin(a)))
        c.rect(tx - 1, ty - 1, 2, 2, base)
    c.circle(cx, cy, r, base)
    for r2 in (r, r - 1):
        draw_pts(arc_pts(cx, cy, r2, 150, 300), light)
        draw_pts(arc_pts(cx, cy, r2, -30, 120), shade)
    c.circle(cx, cy, max(1, r // 3), OUT)
    for i in range(0, 360, 72):
        c.set(int(round(cx + (r - 2) * math.cos(math.radians(i)))),
              int(round(cy + (r - 2) * math.sin(math.radians(i)))), BR6)


def crystal(cx, cy, s):
    c.circle(cx, cy, s + 4, CY0)
    c.circle(cx, cy, s + 2, CY1)
    top = cy - int(s * 1.5)
    bot = cy + int(s * 1.5)
    c.poly([(cx, top - 1), (cx + s + 1, cy), (cx, bot + 1), (cx - s - 1, cy)], CR0)
    c.poly([(cx, top), (cx + s, cy), (cx, bot), (cx - s, cy)], CR2)
    c.poly([(cx, top), (cx - s, cy), (cx, cy)], CR4)
    c.poly([(cx, top), (cx + s, cy), (cx, cy)], CR3)
    c.poly([(cx, bot), (cx + s, cy), (cx, cy)], CR1)
    c.poly([(cx, bot), (cx - s, cy), (cx, cy)], CY2)
    c.set(cx - 1, cy - 3, "#ffffff" if False else CR4)
    c.set(cx - 2, cy - 2, CR4)


def dial(cx, cy, r, ang, face=GL0):
    c.circle(cx, cy, r + 3, OUT)
    c.circle(cx, cy, r + 2, BR2)
    draw_pts(arc_pts(cx, cy, r + 2, 152, 298), BR5)
    draw_pts(arc_pts(cx, cy, r + 2, -28, 118), BR0)
    c.circle(cx, cy, r, face)
    c.circle(cx, cy, r, BR1, fill=False)
    for a in range(0, 360, 30):
        n = 2 if a % 90 == 0 else 1
        col = BR5 if n == 2 else BR3
        for k in range(n):
            c.set(int(round(cx + (r - 1 - k) * math.cos(math.radians(a)))),
                  int(round(cy + (r - 1 - k) * math.sin(math.radians(a)))), col)
    thick_line(cx, cy, cx + (r - 2) * math.cos(math.radians(ang)),
               cy + (r - 2) * math.sin(math.radians(ang)), 1, GL3)
    c.circle(cx, cy, 2, BR5)
    c.set(cx, cy, GL4)


# ================================================================ BACKGROUND

for r, col in [(122, BG1), (112, BG2), (100, BG3), (86, BG4), (70, BG5)]:
    c.circle(CX, CY - 6, r, col)

# floor
c.rect(0, 196, 256, 60, FL0)
c.rect(0, 196, 256, 4, FL1)
c.rect(0, 200, 256, 1, FL2)
for tx in (-90, -20, 50, 128, 206, 276, 346):
    c.line(128, 198, tx, 256, FL1)
for y in (218, 240, 254):
    c.line(0, y, 255, y, FL1)
c.ellipse(128, 252, 82, 7, BG0)
c.ellipse(128, 252, 70, 5, PL0)

# pillars
for x0 in (4, 224):
    c.rect(x0, 0, 28, 198, PL1)
    inner = x0 + 26 if x0 == 4 else x0
    c.rect(inner, 0, 2, 198, PL3)
    for gx in (x0 + 7, x0 + 13, x0 + 19):
        c.line(gx, 14, gx, 186, PL0)
    c.rect(x0 - 2, 4, 32, 12, PL2)
    c.rect(x0 - 2, 4, 32, 2, PL3)
    c.rect(x0 - 2, 15, 32, 1, PL0)
    c.rect(x0 - 2, 184, 32, 14, PL2)
    c.rect(x0 - 2, 184, 32, 2, PL3)
    c.rect(x0 - 2, 197, 32, 1, PL0)

c.rect(0, 0, 256, 6, PL1)
c.rect(0, 5, 256, 1, PL3)
c.rect(0, 6, 256, 1, PL0)

# warm light from the instrument spilling onto the pillars
for (y0, y1, col) in [(16, 48, BR0), (48, 74, BR1), (74, 98, BR2),
                      (98, 122, BR2), (122, 148, BR1), (148, 180, BR0)]:
    c.line(31, y0, 31, y1, col)
    c.line(224, y0, 224, y1, col)
for (y0, y1, col) in [(58, 80, BR0), (80, 96, BR1), (96, 120, BR1), (120, 144, BR0)]:
    c.line(29, y0, 29, y1, col)
    c.line(226, y0, 226, y1, col)
c.line(31, 96, 31, 112, BR3)
c.line(224, 96, 224, 112, BR3)

# ================================================================ PEDESTAL

c.rect(68, 242, 120, 10, ST2)
c.rect(68, 242, 120, 2, ST3)
c.rect(68, 251, 120, 1, ST0)
c.rect(68, 244, 6, 8, ST3)
c.rect(180, 242, 8, 10, ST1)
c.rect(80, 232, 96, 11, ST2)
c.rect(80, 232, 96, 2, ST4)
c.rect(80, 231, 96, 1, ST0)
c.rect(80, 232, 5, 11, ST3)
c.rect(166, 232, 10, 11, ST1)
c.line(80, 240, 176, 240, ST1)
for bx in (88, 110, 148, 168):
    c.line(bx, 234, bx, 241, ST1)

c.rect(96, 214, 64, 18, ST3)
c.rect(96, 214, 6, 18, ST4)
c.rect(96, 215, 1, 17, ST5)
c.rect(152, 214, 8, 18, ST1)
c.line(96, 231, 160, 231, ST1)
for fx in (108, 118, 138, 148):
    c.line(fx, 215, fx, 230, ST1)

c.rect(86, 206, 84, 9, ST3)
c.rect(86, 206, 84, 3, ST4)
c.rect(86, 206, 84, 1, ST5)
c.rect(86, 206, 4, 9, ST5)
c.rect(164, 206, 6, 9, ST1)
c.line(86, 209, 170, 209, ST2)
c.line(80, 239, 176, 239, ST1)
c.line(68, 249, 188, 249, ST1)
c.rect(104, 232, 48, 1, BR1)
c.rect(118, 242, 24, 1, BR1)
c.rect(96, 214, 64, 1, BR1)
# light from the instrument falling on the slab
c.rect(104, 206, 52, 1, BR3)
c.rect(112, 207, 36, 1, BR2)
c.ellipse(128, 207, 30, 4, GL1)
c.ellipse(128, 207, 20, 3, GL2)

# carved emblem on the column
c.circle(128, 223, 8, ST2)
c.circle(128, 223, 8, ST4, fill=False)
draw_pts(arc_pts(128, 223, 8, 150, 300), ST5)
c.circle(128, 223, 4, ST0)
for i, pat in enumerate([["#.#", ".#.", "#.#"], [".#.", "###", ".#."]]):
    glyph(127, 222, pat, CY3)
c.line(104, 216, 109, 227, ST1)
c.line(109, 227, 106, 234, ST1)
c.line(150, 217, 147, 228, ST1)
c.line(147, 228, 150, 234, ST0)

# ================================================================ INSTRUMENT

# aura behind the core
for r, col in [(58, GL0), (46, "#4a3610"), (36, BR0), (27, BR1)]:
    c.circle(CX, CY, r, col)

# struts
for ang in (45, 135, 225, 315):
    ex = CX + 88 * math.cos(math.radians(ang))
    ey = CY + 88 * math.sin(math.radians(ang))
    thick_line(CX, CY, ex, ey, 4, OUT)
    thick_line(CX, CY, ex, ey, 3, BR2)
    thick_line(CX - 1, CY - 1, ex - 1, ey - 1, 1, BR4)
for ang in (0, 90, 180, 270):
    ex = CX + 88 * math.cos(math.radians(ang))
    ey = CY + 88 * math.sin(math.radians(ang))
    thick_line(CX, CY, ex, ey, 3, OUT)
    thick_line(CX, CY, ex, ey, 1, BR3)

# ---- outer rim
c.circle(CX, CY, 95, OUT, fill=False)
ring_band(88, 94, BR3, BR5, BR1)
c.circle(CX, CY, 96, OUT, fill=False)
draw_pts(arc_pts(CX, CY, 93, 195, 255), BR6)
draw_pts(arc_pts(CX, CY, 89, 15, 60), BR6)
c.circle(CX, CY, 87, OUT, fill=False)
c.circle(CX, CY, 86, BR0, fill=False)
ring_ticks(CX, CY, 89, 4, BR1, 1)
ring_ticks(CX, CY, 93, 20, BR6, 1)
ring_ticks(CX, CY, 91, 60, BR4, 2)
for a in range(0, 360, 30):
    x = CX + 91 * math.cos(math.radians(a))
    y = CY + 91 * math.sin(math.radians(a))
    c.set(int(round(x)), int(round(y)), BR6)

# cardinal medallions
for a in range(0, 360, 90):
    mx = int(round(CX + 91 * math.cos(math.radians(a))))
    my = int(round(CY + 91 * math.sin(math.radians(a))))
    c.poly([(mx, my - 4), (mx + 4, my), (mx, my + 4), (mx - 4, my)], OUT)
    c.poly([(mx, my - 3), (mx + 3, my), (mx, my + 3), (mx - 3, my)], BR5)
    c.set(mx, my, CY4)
    c.set(mx - 1, my, CY2)
    c.set(mx + 1, my, CY3)

# diagonal spikes
for a in range(45, 360, 90):
    tip = (CX + 108 * math.cos(math.radians(a)), CY + 108 * math.sin(math.radians(a)))
    b1 = (CX + 92 * math.cos(math.radians(a - 5)), CY + 92 * math.sin(math.radians(a - 5)))
    b2 = (CX + 92 * math.cos(math.radians(a + 5)), CY + 92 * math.sin(math.radians(a + 5)))
    c.poly([tip, b1, b2], OUT)
    c.poly([(tip[0] - 1, tip[1] - 1), (b1[0], b1[1]), (b2[0], b2[1])], BR3)
    c.line(int(b1[0]), int(b1[1]), int(tip[0]) - 1, int(tip[1]) - 1, BR5)

# ---- ring A
c.circle(CX, CY, 83, OUT, fill=False)
ring_band(76, 82, BR3, BR5, BR1)
c.circle(CX, CY, 84, OUT, fill=False)
c.circle(CX, CY, 75, OUT, fill=False)
draw_pts(arc_pts(CX, CY, 81, 200, 250), BR6)
ring_ticks(CX, CY, 77, 5, BR1, 1)
ring_ticks(CX, CY, 80, 10, BR6, 1)
rune_ring(CX, CY, 79, 24, BR1, BR2, offset=6, swap=2)

# alchemical marks engraved on the rim
for idx, ang in enumerate(range(45, 405, 90)):
    px = int(round(CX + 91 * math.cos(math.radians(ang))))
    py = int(round(CY + 91 * math.sin(math.radians(ang))))
    if idx % 3 == 0:
        c.poly([(px, py - 2), (px + 2, py + 2), (px - 2, py + 2)], BR1)
    elif idx % 3 == 1:
        c.rect(px - 1, py - 1, 3, 3, BR1)
    else:
        c.circle(px, py, 2, BR1)

# orbital trails threading the gaps between the rings
for a in range(0, 360, 7):
    c.set(int(round(CX + 85 * math.cos(math.radians(a)))),
          int(round(CY + 85 * math.sin(math.radians(a)))), CY2)
for a in range(5, 360, 9):
    c.set(int(round(CX + 63 * math.cos(math.radians(a)))),
          int(round(CY + 63 * math.sin(math.radians(a)))), CY1)
for a in range(3, 360, 8):
    c.set(int(round(CX + 52 * math.cos(math.radians(a)))),
          int(round(CY + 52 * math.sin(math.radians(a)))), GL2)
for a in range(6, 360, 10):
    c.set(int(round(CX + 41 * math.cos(math.radians(a)))),
          int(round(CY + 41 * math.sin(math.radians(a)))), CY3)
# a bright mote riding the outer trail
for a in (128, 133, 138):
    c.set(int(round(CX + 85 * math.cos(math.radians(a)))),
          int(round(CY + 85 * math.sin(math.radians(a)))), CY5)

# ---- rune ring
c.circle(CX, CY, 73, OUT, fill=False)
ring_band(65, 71, BR2, BR4, BR0)
c.circle(CX, CY, 72, OUT, fill=False)
c.circle(CX, CY, 64, BR0, fill=False)
rune_ring(CX, CY, 68, 15, CY5, CY3)
ring_ticks(CX, CY, 66, 15, BR1, 1, start=4)

# ---- thin ring
c.circle(CX, CY, 61, OUT, fill=False)
ring_band(55, 59, BR3, BR5, BR1)
c.circle(CX, CY, 60, OUT, fill=False)
c.circle(CX, CY, 54, BR0, fill=False)
ring_ticks(CX, CY, 57, 9, BR1, 1)

# ---- inner glowing rune ring
c.circle(CX, CY, 50, OUT, fill=False)
ring_band(43, 49, BR2, BR4, BR0)
c.circle(CX, CY, 51, OUT, fill=False)
c.circle(CX, CY, 42, BR0, fill=False)
rune_ring(CX, CY, 46, 20, GL3, GL2, offset=10, swap=3)
ring_ticks(CX, CY, 44, 10, BR1, 1, start=3)

# ---- engraved thin ring
c.circle(CX, CY, 39, OUT, fill=False)
ring_band(34, 38, BR2, BR4, BR0)
c.circle(CX, CY, 40, OUT, fill=False)
c.circle(CX, CY, 33, BR0, fill=False)
ring_ticks(CX, CY, 36, 6, CY2, 1)

# ---- armillary hoops
ellipse_ring(88, 31, -23, 4, BR3, BR5, BR1)
ellipse_ring(63, 21, 57, 3, BR3, BR5, BR1)
ellipse_ring(50, 17, -38, 2, BR2, BR4, BR0)

# ---- off-centre plates
c.circle(CX - 19, CY - 15, 26, OUT, fill=False)
ring_band(21, 25, BR3, BR5, BR1, cx=CX - 19, cy=CY - 15)
c.circle(CX - 19, CY - 15, 27, OUT, fill=False)
c.circle(CX - 19, CY - 15, 20, BR0, fill=False)
rune_ring(CX - 19, CY - 15, 23, 45, CY3, CY2, offset=18)
c.circle(CX + 24, CY + 24, 16, OUT, fill=False)
ring_band(11, 15, BR3, BR5, BR1, cx=CX + 24, cy=CY + 24)
c.circle(CX + 24, CY + 24, 10, BR0, fill=False)
ring_ticks(CX + 24, CY + 24, 13, 20, BR6, 2)

# ---- gears
gear(84, 152, 10, 10)
gear(172, 54, 8, 9)
gear(156, 158, 7, 8)
gear(106, 44, 6, 7)
gear(142, 176, 5, 6, BR2, BR4, BR0)

# ---- dials
dial(30, 124, 10, -55)
dial(226, 118, 9, 205)
dial(114, 184, 6, 40)

# ---- crystals
crystal(68, 52, 7)
crystal(190, 66, 5)
crystal(178, 144, 7)
crystal(58, 138, 4)
crystal(128, 15, 4)
crystal(98, 160, 3)
crystal(152, 62, 3)

# ---- core
c.circle(CX, CY, 32, OUT, fill=False)
ring_band(27, 31, BR3, BR6, BR1)
c.circle(CX, CY, 33, OUT, fill=False)
c.circle(CX, CY, 26, BR0, fill=False)
rune_ring(CX, CY, 29, 45, GL3, BR4, offset=22)
c.circle(CX, CY, 24, BR2)
c.circle(CX, CY, 24, BR5, fill=False)
c.circle(CX, CY, 22, BR3)
c.circle(CX, CY, 20, GL1)
c.circle(CX, CY, 18, GL2)
c.circle(CX, CY, 14, GL3)
c.circle(CX, CY, 10, GL4)
c.circle(CX, CY, 6, "#fffef8")
c.circle(CX, CY, 3, "#ffffff")
# rim light and shadow on the orb
draw_pts(arc_pts(CX, CY, 19, 150, 285), GL3)
draw_pts(arc_pts(CX, CY, 21, 165, 265), GL2)
draw_pts(arc_pts(CX, CY, 19, 20, 115), GL1)
draw_pts(arc_pts(CX, CY, 15, 200, 245), "#fffef8")

# ---- radiant rays
for i in range(16):
    a = math.radians(i * 22.5 + 11.25)
    L = 68 if i % 2 == 0 else 52
    for (r0, r1, col) in [(23, 36, GL3), (36, 50, GL2), (50, L, GL1)]:
        if r0 >= L:
            break
        c.line(int(round(CX + r0 * math.cos(a))), int(round(CY + r0 * math.sin(a))),
               int(round(CX + min(r1, L) * math.cos(a))),
               int(round(CY + min(r1, L) * math.sin(a))), col)
for i in range(8):
    a = math.radians(i * 45)
    for (r0, r1, col) in [(18, 24, GL4), (24, 44, GL2)]:
        c.line(int(round(CX + r0 * math.cos(a))), int(round(CY + r0 * math.sin(a))),
               int(round(CX + r1 * math.cos(a))), int(round(CY + r1 * math.sin(a))), col)

# ---- plumb link to the pedestal
c.circle(CX, 197, 2, BR3)
for y in range(198, 206, 2):
    c.set(CX, y, BR2)
    c.set(CX - 1, y, BR4)
c.circle(CX, 206, 3, BR2)
c.circle(CX, 206, 1, GL3)

# ---- motes
for (x, y, col) in [(46, 62, CY0), (52, 158, CY0), (204, 74, CY0), (198, 170, CY0),
                    (94, 22, CY1), (166, 190, CY1), (20, 92, BG5), (236, 182, BG5),
                    (74, 200, BR1), (182, 198, BR1), (60, 96, BR2), (196, 110, BR2),
                    (36, 44, CY1), (222, 46, CY1)]:
    c.set(x, y, col)

# ---- drifting sparks around the floating instrument
for (x, y, col) in [(88, 92, GL2), (168, 96, GL2), (78, 120, GL1), (176, 122, GL1),
                    (100, 66, GL2), (154, 72, GL1), (92, 186, CY2), (162, 186, CY2),
                    (66, 172, GL1), (188, 160, GL1), (44, 106, CY1), (212, 100, CY1),
                    (110, 196, GL2), (146, 196, GL2), (128, 190, GL3)]:
    c.set(x, y, col)
c.set(126, 189, GL2)
c.set(130, 189, GL2)
c.set(128, 188, GL4)

print(c.stats_text())


def cls(hx):
    if not hx.startswith("#"):
        return "?"
    r, g, b = int(hx[1:3], 16), int(hx[3:5], 16), int(hx[5:7], 16)
    mx = max(r, g, b)
    if mx < 26:
        return " "
    if mx < 60:
        return "."
    if b >= r + 15:
        return "C" if mx > 110 else "c"
    if r >= 240 and g >= 200:
        return "W"
    if r > g > b:
        return "B" if mx > 160 else "b"
    if abs(r - g) < 26 and abs(g - b) < 26:
        return "s" if mx < 110 else "S"
    return "?"


if DEBUG:
    print("PALETTE", len(c.palette()))
    print(c.matrix_text(region=(106, 80, 149, 123)))
    for y in range(0, 256, 3):
        row = ""
        for x in range(0, 256, 3):
            row += cls(c.color_name(c.get(x, y)))
        print("%3d %s" % (y, row))

save("arcane", c)
finish(c)
