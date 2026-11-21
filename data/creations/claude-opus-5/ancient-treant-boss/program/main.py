import math, random

W = H = 256

P = {
    "sky_top": "#09170f",
    "sky_mid": "#112416",
    "sky_low": "#18301d",
    "ray1": "#1a3220",
    "ray2": "#25452a",
    "ray3": "#376034",
    "ray4": "#4e8347",
    "ground_dark": "#111b13",
    "ground": "#1b2819",
    "ground_lit": "#273b23",
    "ground_hi": "#36522d",
    "soil": "#1e1a12",
    "bark_black": "#160f0a",
    "bark_dark": "#241a11",
    "bark": "#33251a",
    "bark_mid": "#473223",
    "bark_lit": "#5e422b",
    "bark_hi": "#7d5836",
    "bark_rim": "#9c7044",
    "outline": "#0c0806",
    "moss_dk": "#1d3519",
    "moss": "#2f5522",
    "moss_lt": "#477a2e",
    "moss_hi": "#63a040",
    "vine": "#27421f",
    "vine_lt": "#3f6a29",
    "eye_glow": "#86ff92",
    "eye_core": "#e8ffe2",
    "eye_halo": "#2c7536",
    "eye_halo2": "#48a94c",
    "maw": "#0a0705",
    "maw2": "#1a1008",
    "tooth": "#b8a87f",
    "tooth_dk": "#8a7b57",
}

bg = new_canvas(W, H, name="bg")
for k, v in P.items():
    bg.color(v, k)
back = new_canvas(W, H, name="back")
tr = new_canvas(W, H, name="trunk")
fr = new_canvas(W, H, name="front")
glow = new_canvas(W, H, name="glow")


def lerp(a, b, t):
    return a + (b - a) * t


# ================= background =================
def background():
    for y in range(H):
        t = y / H
        col = "sky_top" if t < 0.34 else ("sky_mid" if t < 0.6 else "sky_low")
        bg.line(0, y, W - 1, y, col)
    bg.dither(0, 74, W, 24, ["sky_top", "sky_mid"], pattern="bayer4")
    bg.dither(0, 140, W, 28, ["sky_mid", "sky_low"], pattern="bayer4")
    # canopy mass at the very top
    random.seed(99)
    for i in range(260):
        x = random.randrange(0, W)
        y = random.randrange(0, 26)
        r = random.randrange(2, 7)
        bg.circle(x, y, r, random.choice(("sky_top", "ground_dark", "moss_dk")))
    # distant trunks
    for x, w, top in [(4, 8, 48), (26, 5, 86), (244, 9, 56), (228, 5, 96),
                      (120, 4, 118), (66, 4, 126), (176, 3, 130)]:
        bg.rect(x, top, w, 200 - top, "ground_dark")
        bg.line(x, top, x, 198, "ground")


def ray(cv, x_top, half_top, half_bot, drift, y0, y1, cols):
    for y in range(y0, y1):
        t = (y - y0) / max(1, (y1 - y0))
        cx = x_top + drift * t
        half = lerp(half_top, half_bot, t)
        fade = max(0.0, 1.0 - t * 1.2)
        for i, (frac, col, step) in enumerate(cols):
            hw = half * frac
            if hw < 0.5 or (i >= 1 and fade < 0.22 + 0.2 * i):
                continue
            if step > 1 and (y % step) != 0:
                continue
            cv.line(int(cx - hw), y, int(cx + hw), y, col)


BACK_RAYS = [(10, 4, 15, 32, 0, 202), (52, 5, 18, 40, 0, 196),
             (148, 3, 12, 28, 0, 198), (204, 5, 18, 24, 0, 194),
             (238, 4, 12, 18, 0, 188)]


def god_rays():
    for i, (x, ht, hb, dr, y0, y1) in enumerate(BACK_RAYS):
        bright = i in (0, 1, 3, 4)
        cols = [(1.0, "ray1", 2), (0.68, "ray2", 1), (0.38, "ray3", 1), (0.14, "ray4", 1)] \
            if bright else [(1.0, "ray1", 2), (0.62, "ray1", 1), (0.34, "ray2", 1), (0.12, "ray3", 1)]
        ray(bg, x, ht, hb, dr, y0, y1, cols)


def ground():
    hz = 186
    for y in range(hz, H):
        t = (y - hz) / (H - hz)
        col = "ground_dark" if t < 0.2 else ("ground" if t < 0.72 else "ground_dark")
        bg.line(0, y, W - 1, y, col)
    bg.dither(0, hz, W, 9, ["ground_dark", "ground"], pattern="bayer4")
    random.seed(12)
    for cx, cy, rx, ry in [(34, 210, 28, 8), (96, 238, 42, 10), (198, 204, 24, 6),
                           (236, 230, 22, 7), (146, 198, 18, 5), (60, 250, 30, 8)]:
        bg.ellipse(cx, cy, rx, ry, "ground_lit")
        bg.dither(cx - rx, cy - ry, rx * 2, ry * 2, ["ground_lit", "ground"], "bayer4")
        bg.ellipse(cx, cy, rx // 2, max(1, ry // 2), "ground_lit")
        bg.ellipse(cx, cy, rx // 4, max(1, ry // 4), "ground_hi")
    for i in range(190):
        x = random.randrange(0, W)
        y = hz + random.randrange(-4, 7)
        h = random.randrange(2, 8)
        bg.line(x, y, x + random.choice((-1, 0, 1)), y - h,
                random.choice(("moss_dk", "ground_lit", "vine", "moss")))


background()
god_rays()
ground()

# ================= trunk silhouette =================
# tall, tapering, hunched; narrow at the head, flaring into the root base
TRUNK = [
    (106, 18), (100, 30), (98, 42), (88, 50), (76, 60), (72, 74),
    (80, 90), (84, 106), (82, 122), (88, 138), (86, 154), (80, 168),
    (70, 182), (56, 196), (44, 208), (38, 218),
    (218, 218), (212, 206), (200, 192), (190, 178), (184, 164),
    (178, 148), (182, 132), (176, 116), (180, 100), (186, 84),
    (180, 70), (168, 58), (156, 50), (150, 34), (146, 18),
]
tr.poly(TRUNK, "bark_dark")
tr.ellipse(80, 62, 14, 12, "bark_dark")      # left shoulder lump
tr.ellipse(178, 60, 15, 13, "bark_dark")     # right shoulder lump
tr.ellipse(126, 28, 22, 12, "bark_dark")     # crown mass
tr.ellipse(128, 204, 70, 20, "bark_dark")    # base flare
tr.ellipse(130, 152, 44, 26, "bark_dark")    # belly

pal = {p["index"]: p["rgba"] for p in tr.palette()}
inside = [[pal[tr.get(x, y)][3] > 0 for x in range(W)] for y in range(H)]
rows = []
for y in range(H):
    xs = [x for x in range(W) if inside[y][x]]
    rows.append((xs[0], xs[-1]) if xs else None)

# ================= bark: vertical gnarl bands =================
FACE = (82, 58, 176, 140)


def bark_shade():
    for y in range(H):
        if rows[y] is None:
            continue
        xl, xr = rows[y]
        wid = max(1, xr - xl)
        wob = 2.6 * math.sin(y * 0.055) + 1.4 * math.sin(y * 0.17)
        for x in range(xl, xr + 1):
            if not inside[y][x]:
                continue
            u = (x - xl) / wid                     # 0 = lit left edge
            band = (x + wob) % 9.0
            seam = band < 1.1 or band > 8.4
            ridge = 1.0 - abs(band - 4.7) / 3.8    # bright middle of each band
            k = u * 1.02 - 0.17 * ridge + 0.05 * math.sin(y * 0.23 + x * 0.1)
            if seam:
                col = "bark_black" if u > 0.5 else "bark_dark"
            elif k < 0.07:
                col = "bark_hi"
            elif k < 0.20:
                col = "bark_lit"
            elif k < 0.38:
                col = "bark_mid"
            elif k < 0.60:
                col = "bark"
            elif k < 0.82:
                col = "bark_dark"
            else:
                col = "bark_black"
            tr.set(x, y, col)
    # deep gnarl cracks
    random.seed(17)
    for x0, y0, y1, amp, ph in [(96, 56, 212, 3, 0.4), (116, 86, 214, 4, 1.2),
                                (140, 60, 210, 3, 2.1), (160, 80, 206, 4, 0.8),
                                (106, 140, 214, 2, 1.7), (152, 136, 214, 3, 2.6),
                                (176, 104, 202, 2, 0.2), (84, 100, 198, 2, 1.1),
                                (128, 150, 212, 2, 3.0)]:
        for y in range(y0, y1):
            x = int(x0 + amp * math.sin(y * 0.085 + ph))
            if 0 <= x < W and inside[y][x]:
                tr.set(x, y, "bark_black")
                if inside[y][x + 1]:
                    tr.set(x + 1, y, "bark_dark")
    # knot holes
    for cx, cy, r in [(96, 128, 4), (166, 158, 5), (116, 184, 3), (158, 110, 3),
                      (88, 162, 3), (142, 196, 4)]:
        tr.ellipse(cx, cy, r, r - 1, "bark_dark")
        tr.ellipse(cx, cy, max(1, r - 2), max(1, r - 3), "maw")
        tr.line(cx - r, cy - r + 1, cx + r, cy - r + 1, "bark_lit")
    # rim light / shadow edges
    for y in range(H):
        if rows[y] is None:
            continue
        xl, xr = rows[y]
        tr.set(xl, y, "bark_rim")
        if y % 4:
            tr.set(xl + 1, y, "bark_hi")
        tr.set(xr, y, "bark_black")
        tr.set(xr - 1, y, "bark_dark")


bark_shade()

# ================= limbs =================
def spine(pts, rads):
    out = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        r0, r1 = rads[i], rads[i + 1]
        seg = int(max(abs(x1 - x0), abs(y1 - y0))) * 2 + 2
        for s in range(seg + 1):
            t = s / seg
            out.append((lerp(x0, x1, t), lerp(y0, y1, t), lerp(r0, r1, t)))
    return out


def limb(cv, pts, rads, lit=True, knuckles=True):
    sm = spine(pts, rads)
    for x, y, r in sm:
        cv.circle(int(round(x)), int(round(y)), max(0, int(round(r))), "bark_black")
    if knuckles:
        for i in range(0, len(sm), max(6, len(sm) // 5)):
            x, y, r = sm[i]
            if r >= 4:
                cv.circle(int(x), int(y), int(r) + 1, "bark_black")
    if not lit:
        return
    for dx, dy, dr, col in ((0, 0, -1, "bark_dark"), (-1, -1, -2, "bark"),
                            (-1, -2, -3, "bark_mid"), (-2, -3, -5, "bark_lit")):
        for x, y, r in sm:
            rr = int(round(r)) + dr
            if rr >= 0:
                cv.circle(int(round(x)) + dx, int(round(y)) + dy, rr, col)
    # bark grain running along the limb
    for i, (x, y, r) in enumerate(sm):
        if r >= 3 and (i // 3) % 3 == 0:
            cv.set(int(x) + 1, int(y + r * 0.3), "bark_dark")
        if r >= 5 and i % 11 == 0:
            cv.set(int(x) - 1, int(y - r * 0.55), "bark_hi")


def twig(cv, x, y, ang, length, r=2, col="bark_black", tipcol="bark_mid", splits=3):
    pts = [(x, y)]
    a = ang
    for i in range(splits):
        a += random.uniform(-0.32, 0.32)
        L = length / splits
        x += math.cos(a) * L
        y += math.sin(a) * L
        pts.append((x, y))
    rads = [r, r * 0.65, r * 0.35, 0][: splits + 1]
    sm = spine(pts, rads)
    for px, py, pr in sm:
        cv.circle(int(round(px)), int(round(py)), max(0, int(round(pr))), col)
    for px, py, pr in sm[: int(len(sm) * 0.6)]:
        rr = int(round(pr)) - 1
        if rr >= 0:
            cv.circle(int(round(px)) - 1, int(round(py)) - 1, rr, tipcol)
    return x, y


def claw_hand(cv, x, y, base_ang, spread, n=5, length=26, r=3):
    for i in range(n):
        a = base_ang + (i - (n - 1) / 2) * spread
        tx, ty = x + math.cos(a) * 3, y + math.sin(a) * 3
        twig(cv, tx, ty, a, length * random.uniform(0.8, 1.2), r, splits=3)


# far arm: raised high to the viewer's right, elbow kinked outward
random.seed(11)
limb(back, [(182, 62), (202, 54), (216, 40), (222, 28), (228, 22)], [15, 12, 9, 7, 6])
claw_hand(back, 228, 22, -1.25, 0.46, 5, 17, 3)
back.ellipse(188, 60, 13, 11, "bark_dark")
back.ellipse(216, 40, 8, 8, "bark_dark")
# rim light along the top of the raised arm so it reads against the canopy
for pts, rads in [([(182, 62), (202, 54), (216, 40), (222, 28), (228, 22)], [15, 12, 9, 7, 6])]:
    for i, (x, y, r) in enumerate(spine(pts, rads)):
        top = int(round(y - r))
        xi = int(round(x))
        if 0 <= xi < W and 0 <= top < H:
            back.set(xi, top, "bark_hi")
            back.set(xi, top + 1, "bark_lit" if i % 3 else "bark_hi")

# near arm: heavy, swung low and forward to the viewer's left
random.seed(5)
limb(fr, [(74, 70), (52, 82), (32, 104), (26, 130), (30, 152)], [17, 14, 11, 9, 8])
fr.ellipse(50, 82, 11, 10, "bark_dark")     # shoulder joint
fr.ellipse(28, 128, 10, 9, "bark_dark")     # elbow knot
claw_hand(fr, 30, 154, 1.4, 0.36, 5, 30, 4)

# crown branches
random.seed(3)
for x, y, a, L in [(102, 26, -2.6, 36), (112, 18, -2.0, 42), (128, 16, -1.55, 44),
                   (142, 19, -1.1, 40), (152, 28, -0.6, 34), (94, 38, -2.95, 28),
                   (160, 38, -0.2, 30)]:
    twig(tr, x, y, a, L, 3)
for x, y, a, L in [(108, 14, -2.3, 22), (146, 14, -0.9, 24), (128, 10, -1.6, 20),
                   (118, 12, -1.9, 18), (138, 12, -1.3, 18)]:
    twig(tr, x, y, a, L, 2)

# ================= face =================
# brow ridge, heavy and overhanging
tr.poly([(78, 78), (98, 66), (128, 60), (158, 66), (180, 80),
         (178, 90), (156, 76), (128, 71), (100, 77), (80, 92)], "bark_black")
tr.poly([(80, 75), (100, 63), (128, 57), (158, 63), (180, 77),
         (179, 83), (156, 70), (128, 65), (100, 71), (81, 85)], "bark_mid")
tr.poly([(82, 73), (102, 61), (128, 55), (158, 61), (179, 75),
         (179, 78), (156, 66), (128, 61), (100, 68), (83, 80)], "bark_hi")
# recessed sockets: two hollows with a bark ridge between them
for ex, sgn in ((104, -1), (152, 1)):
    tr.poly([(ex - 18, 90), (ex - 12, 80), (ex + 2, 78), (ex + 15, 84),
             (ex + 14, 96), (ex + 2, 103), (ex - 12, 100)], "bark_black")
    tr.poly([(ex - 15, 90), (ex - 10, 82), (ex + 1, 80), (ex + 12, 85),
             (ex + 11, 95), (ex + 1, 100), (ex - 10, 98)], "maw")
# nose/brow ridge column between the eyes
tr.poly([(126, 76), (131, 76), (134, 104), (122, 104)], "bark_mid")
tr.line(128, 78, 128, 103, "bark_lit")
tr.line(133, 80, 134, 103, "bark_dark")
for ex in (104, 152):
    tr.ellipse(ex, 90, 7, 5, "eye_halo")
    tr.ellipse(ex, 90, 5, 4, "eye_halo2")
    tr.ellipse(ex, 90, 3, 2, "eye_glow")
    tr.set(ex, 89, "eye_core")
    tr.set(ex + 1, 89, "eye_core")
# jagged maw
MAW = [(102, 120), (114, 116), (128, 115), (143, 117), (155, 121),
       (151, 134), (140, 141), (128, 143), (113, 139), (104, 130)]
tr.poly(MAW, "maw")
tr.poly([(106, 122), (128, 118), (151, 123), (147, 131), (128, 128), (108, 128)], "maw2")
random.seed(8)
upper = [(103, 121), (109, 119), (115, 117), (121, 116), (128, 116),
         (135, 117), (141, 118), (147, 120), (153, 122)]
for i in range(len(upper) - 1):
    (x0, y0), (x1, y1) = upper[i], upper[i + 1]
    hgt = random.choice((4, 5, 6))
    tr.poly([(x0, y0), (x1, y1), ((x0 + x1) // 2, (y0 + y1) // 2 + hgt)], "tooth")
    tr.line((x0 + x1) // 2, (y0 + y1) // 2 + hgt, x1, y1, "tooth_dk")
lower = [(106, 132), (112, 136), (119, 139), (128, 140), (137, 138), (144, 135), (150, 131)]
for i in range(len(lower) - 1):
    (x0, y0), (x1, y1) = lower[i], lower[i + 1]
    hgt = random.choice((4, 5, 6))
    tr.poly([(x0, y0), (x1, y1), ((x0 + x1) // 2, (y0 + y1) // 2 - hgt)], "tooth")
    tr.line((x0 + x1) // 2, (y0 + y1) // 2 - hgt, x0, y0, "tooth_dk")
# shadow under the overhanging brow and inside the maw corners
tr.line(104, 119, 152, 121, "maw")
tr.ellipse(104, 131, 3, 3, "maw")
tr.ellipse(152, 132, 3, 3, "maw")
# cheek plates
tr.path("M84 100 Q92 122 86 142", "bark_black", fill=False)
tr.path("M178 98 Q170 120 176 142", "bark_black", fill=False)
tr.path("M86 102 Q94 122 88 142", "bark_lit", fill=False)
# shadow cast by the brow onto the eye band, and under the jaw
for x in range(82, 178):
    for dy in range(0, 3):
        y = 74 + dy + int(2 * math.sin((x - 82) * 0.03))
        if 0 <= y < H and inside[y][x]:
            tr.set(x, y, "bark_black")
tr.path("M98 150 Q128 160 158 148", "bark_black", fill=False)
tr.path("M100 153 Q128 163 156 151", "bark_dark", fill=False)
# chest plate ridges below the jaw
for i, (yy, half) in enumerate([(164, 36), (176, 40), (188, 44)]):
    tr.path(f"M{128-half} {yy} Q128 {yy+9} {128+half} {yy}", "bark_black", fill=False)
    tr.path(f"M{128-half} {yy-1} Q128 {yy+8} {128+half} {yy-1}", "bark_mid", fill=False)

# ================= roots =================
random.seed(21)
for pts, rads in [([(74, 190), (48, 202), (22, 210), (4, 212)], [12, 9, 6, 4]),
                  ([(186, 190), (214, 202), (238, 208), (252, 210)], [12, 9, 6, 4]),
                  ([(128, 200), (132, 212), (128, 222), (120, 228)], [13, 9, 6, 4])]:
    limb(back, pts, rads)
# soil mound
fr.ellipse(128, 226, 104, 20, "soil")
fr.dither(24, 206, 208, 24, ["soil", "ground_dark"], "bayer4")
fr.ellipse(128, 236, 96, 14, "ground_dark")
ROOTS_FRONT = [([(64, 202), (44, 216), (22, 228), (4, 234)], [14, 10, 7, 4]),
               ([(94, 212), (78, 228), (56, 242), (34, 250)], [13, 10, 7, 4]),
               ([(118, 216), (110, 232), (98, 248), (86, 255)], [12, 9, 6, 4]),
               ([(146, 216), (156, 232), (170, 246), (188, 254)], [12, 9, 6, 4]),
               ([(172, 208), (194, 222), (216, 234), (238, 240)], [14, 10, 7, 4]),
               ([(128, 220), (132, 238), (126, 252), (120, 255)], [11, 8, 5, 3]),
               ([(100, 204), (84, 212), (62, 218), (40, 220)], [9, 7, 5, 3]),
               ([(158, 204), (178, 210), (200, 216), (220, 220)], [9, 7, 5, 3])]
for pts, rads in ROOTS_FRONT:
    limb(fr, pts, rads)
for x, y, a, L in [(6, 234, 3.0, 18), (34, 250, 2.7, 15), (86, 254, 2.3, 12),
                   (188, 254, 0.85, 14), (238, 240, 0.35, 18), (220, 220, 0.18, 13),
                   (40, 220, 3.1, 14)]:
    twig(fr, x, y, a, L, 3, "bark_black", "bark")

# ================= moss and vines =================
def moss_patch(cv, x, y, w, h, dense=0.5):
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            if 0 <= xx < W and 0 <= yy < H:
                t = (yy - y) / max(1, h - 1)
                if random.random() < dense * (1.0 - t * 0.85):
                    cv.set(xx, yy, random.choice(("moss", "moss_dk", "moss_lt", "moss", "moss_hi")))


random.seed(33)
for x, y, w, h, d in [(60, 54, 32, 15, 0.6), (166, 52, 30, 15, 0.55),
                      (106, 48, 44, 11, 0.5), (76, 110, 18, 16, 0.35),
                      (172, 124, 16, 15, 0.3), (92, 166, 28, 12, 0.35),
                      (144, 172, 30, 12, 0.32), (48, 190, 44, 14, 0.45),
                      (176, 190, 44, 14, 0.4), (20, 110, 18, 13, 0.5),
                      (208, 24, 24, 14, 0.45), (30, 214, 34, 12, 0.4),
                      (196, 214, 36, 12, 0.38), (118, 200, 30, 10, 0.3)]:
    moss_patch(fr, x, y, w, h, d)


def hang_vine(cv, x, y, length, amp=5, freq=0.16):
    for i in range(length):
        yy = y + i
        xx = int(x + amp * math.sin(i * freq))
        if not (0 <= xx < W and 0 <= yy < H):
            continue
        cv.set(xx, yy, "vine")
        cv.set(xx + 1, yy, "vine_lt" if i % 4 else "vine")
        if i % 8 == 3:
            cv.set(xx - 1, yy, "vine_lt")
            cv.set(xx + 2, yy + 1, "moss_lt")
        if i == length - 1:
            cv.set(xx, yy + 1, "moss_lt")


random.seed(44)
# vines hang from shoulders, branch stubs and the crown only
for x, y, L in [(78, 66, 54), (90, 56, 40), (118, 52, 26), (156, 56, 38),
                (176, 64, 58), (188, 76, 34), (206, 26, 42), (104, 32, 22),
                (150, 32, 24), (228, 14, 38), (170, 148, 26), (90, 142, 22),
                (36, 108, 30), (24, 132, 24), (196, 190, 20), (56, 190, 22),
                (128, 44, 16), (166, 94, 22)]:
    hang_vine(fr, x, y, L, amp=random.randint(2, 4), freq=random.uniform(0.07, 0.13))

# foreground grass
random.seed(55)
for i in range(300):
    x = random.randrange(0, W)
    y = random.randrange(208, H)
    h = random.randrange(3, 10)
    fr.line(x, y, x + random.choice((-1, 0, 1)), y - h,
            random.choice(("moss_dk", "moss", "vine", "moss_lt", "ground_lit")))

# ================= composite =================
sprite = flatten([back, tr, fr], name="sprite")

# depth pass: push the lower body and the right side down the value ramp,
# so the treant reads as a dark mass against the lit clearing
DOWN = {"bark_rim": "bark_hi", "bark_hi": "bark_lit", "bark_lit": "bark_mid",
        "bark_mid": "bark", "bark": "bark_dark", "bark_dark": "bark_black",
        "moss_hi": "moss_lt", "moss_lt": "moss", "moss": "moss_dk",
        "moss_dk": "vine", "vine_lt": "vine", "vine": "moss_dk",
        "ground_lit": "ground", "ground": "ground_dark"}
names = {p["index"]: (p["name"] or "") for p in sprite.palette()}
for y in range(H):
    for x in range(W):
        nm = names.get(sprite.get(x, y), "")
        if nm not in DOWN:
            continue
        steps = 0
        if y > 212:
            steps += 1                     # roots sink into shadow
        if x > 178 and y > 70:
            steps += 1                     # light comes from the left
        if x > 220 and y > 70:
            steps += 1
        for _ in range(steps):
            nm2 = DOWN.get(nm)
            if not nm2:
                break
            nm = nm2
        sprite.set(x, y, nm)

sprite.outline("outline")
result = flatten([bg, sprite], name="result")

# cast shadow pooling between and behind the roots
result.ellipse(126, 248, 92, 10, "ground_dark")
result.dither(34, 232, 188, 20, ["ground_dark", "soil"], "bayer4")

# relight the root tops so the base keeps its form inside the shadow
for pts, rads in ROOTS_FRONT:
    sm = spine(pts, rads)
    for i, (x, y, r) in enumerate(sm):
        if r < 3:
            continue
        top = int(round(y - r + 1))
        xi = int(round(x))
        col = "bark_lit" if xi < 150 else "bark_mid"
        if 0 <= xi < W and 0 <= top < H:
            result.set(xi, top, col)
            if i % 4 == 0 and top + 1 < H:
                result.set(xi, top + 1, "bark_hi" if xi < 120 else "bark_lit")

random.seed(66)
for i in range(140):
    x = random.randrange(20, 236)
    y = random.randrange(226, H)
    result.line(x, y, x + random.choice((-1, 0, 1)), y - random.randrange(2, 7),
                random.choice(("moss_dk", "vine", "moss")))

# front light shafts over everything, plus eye bloom
for x, ht, hb, dr, y0, y1 in [(44, 3, 12, 34, 0, 190), (196, 3, 11, 22, 0, 186)]:
    ray(glow, x, ht, hb, dr, y0, y1, [(0.5, "ray2", 3), (0.2, "ray3", 4)])
for ex in (106, 150):
    for r, col, step in ((17, "eye_halo", 3), (12, "eye_halo", 2)):
        for a in range(0, 360, 7):
            rad = math.radians(a)
            gx, gy = int(ex + math.cos(rad) * r), int(93 + math.sin(rad) * r * 0.78)
            if a % (step * 7) == 0 and 0 <= gx < W and 0 <= gy < H:
                glow.set(gx, gy, col)
result = flatten([result, glow], name="final")

# foreground fern silhouettes frame the clearing
random.seed(77)


def fern(cv, x, y, L, ang, col="bark_black"):
    for i in range(L):
        t = i / L
        px = int(x + math.cos(ang) * i * 0.9 - 0 * t)
        py = int(y - math.sin(-ang) * i * 0.9) if False else int(y + math.sin(ang) * i * 0.9)
        if not (0 <= px < W and 0 <= py < H):
            break
        cv.set(px, py, col)
        if i % 3 == 0:
            leaf = int(6 * (1 - t)) + 2
            n = ang + 1.1
            m = ang - 1.1
            cv.line(px, py, int(px + math.cos(n) * leaf), int(py + math.sin(n) * leaf), col)
            cv.line(px, py, int(px + math.cos(m) * leaf), int(py + math.sin(m) * leaf), col)


for x, y, L, a in [(6, 254, 30, -1.05), (24, 255, 26, -1.3), (40, 255, 20, -1.45),
                   (250, 254, 30, -2.1), (232, 255, 26, -1.85), (216, 255, 20, -1.7)]:
    fern(result, x, y, L, a)
for i in range(70):
    x = random.choice((random.randrange(0, 42), random.randrange(214, W)))
    y = random.randrange(238, H)
    result.line(x, y, x + random.choice((-1, 0, 1)), y - random.randrange(4, 14), "bark_black")

# lit moss caps on the shoulders and upper branches
random.seed(88)
for cx, cy, w, h in [(82, 54, 26, 7), (176, 52, 24, 6), (122, 22, 30, 5),
                     (44, 100, 14, 5), (30, 126, 12, 4)]:
    for xx in range(cx - w // 2, cx + w // 2):
        for yy in range(cy, cy + h):
            if random.random() < 0.55 - (yy - cy) * 0.09:
                result.set(xx, yy, random.choice(("moss_lt", "moss_hi", "moss")))

# dust motes drifting in the shafts
random.seed(90)
for i in range(120):
    x = random.randrange(0, W)
    y = random.randrange(10, 200)
    if (x < 96 and y < 190) or (x > 196 and y < 190):
        result.set(x, y, random.choice(("ray4", "ray3", "moss_lt")))

view(result)
print(result.stats_text())
finish(result)
