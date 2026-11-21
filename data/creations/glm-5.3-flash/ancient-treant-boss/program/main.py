# ============================================================
#  ANCIENT TREANT BOSS - 256x256 pixel art
#  layers: bg (forest floor/sky) -> glow -> rays -> treant -> fg
# ============================================================
import math, random

try:
    from pixelbench_api import *
except Exception:
    pass

random.seed(11)
W = H = 256

# ---------------- palette ----------------
SKY_TOP = "#0a140f"
SKY_MID = "#122016"
SKY_LOW = "#1b2d19"
SKY_GLOW = "#2a3f22"

DIST1 = "#0f1a12"
DIST2 = "#152417"

GRO_D = "#141d0f"
GRO_M = "#223016"
GRO_L = "#32421e"
GRO_HL = "#42562a"

GRASS1 = "#4c6b28"
GRASS2 = "#63853a"
GRASS3 = "#2c4218"

ROCK_M = "#3d453c"
ROCK_L = "#525c50"

RAY_A = (213, 238, 168, 46)
RAY_B = (188, 222, 150, 32)
GLOW_C = (206, 232, 150, 22)
GLOW_B = (206, 232, 150, 14)
SPORE = (216, 240, 172, 130)
SPORE2 = (216, 240, 172, 70)

CAN_D = "#1a2f14"
CAN_M = "#25451b"
CAN_L = "#336024"
CAN_HL = "#467e2d"

BARK = "#4a2f1c"
BARK_M = "#5b3b23"
BARK_L = "#6f4b2a"
BARK_HL = "#8a6238"
BARK_D = "#33200f"
BARK_DD = "#20130a"
OUTLINE = "#0c0a06"

ROOT = "#3e2817"
ROOT_D = "#291a0d"

MOSS_M = "#3d6b25"
MOSS_L = "#578f32"
MOSS_HL = "#73b243"

EYE_HALO = "#223c16"
EYE_S = "#140d05"
EYE_O = "#3f7a22"
EYE_M = "#6fdb37"
EYE_C = "#a9f25c"
EYE_H = "#dcff96"

VINE = "#3a6324"
VINE_D = "#1c3315"
LEAF = "#4f8a2e"
SHROOM_CAP = "#2f6b4f"
SHROOM_HL = "#5fae8a"
SHROOM_STEM = "#a8b494"
SHROOM_GLOW = "#c8ffd8"

RIM = "#b9cf6a"
SHADOW = "#0a0f08"


# ---------------- helpers ----------------
def taper(cv, pts, r0, r1, col):
    """blobby tapered limb along a polyline"""
    segs = [math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
            for i in range(len(pts) - 1)]
    total = sum(segs) or 1.0
    acc = 0.0
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        L = segs[i]
        steps = max(1, int(L * 2))
        for s in range(steps + 1):
            u = s / steps
            d = (acc + L * u) / total
            r = r0 + (r1 - r0) * d
            cv.circle(int(round(x0 + (x1 - x0) * u)), int(round(y0 + (y1 - y0) * u)),
                      max(1, int(round(r))), col)
        acc += L


def spike(cv, x0, y0, x1, y1, w0, col):
    """tapered triangle from base to a point"""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    px, py = -dy / L, dx / L
    cv.poly([(int(round(x0 + px * w0)), int(round(y0 + py * w0))),
             (x1, y1),
             (int(round(x0 - px * w0)), int(round(y0 - py * w0)))], col)


def bark_tex(cv, x0, x1, y0, y1, step, col, amp=2, seg=8):
    x = x0
    while x <= x1:
        xx, yy = x, y0
        while yy < y1:
            ny = min(yy + seg, y1)
            nx = xx + random.choice([-amp, 0, amp])
            cv.line(xx, yy, nx, ny, col)
            xx, yy = nx, ny
        x += step


def vine(cv, x, y0, y1, col, leaf, sway=3, phase=0.0):
    segs, yy, xx, k = [], y0, x, 0
    while yy < y1:
        ny = min(yy + 4, y1)
        nx = x + int(round(sway * math.sin(k * 0.9 + phase)))
        segs.append((xx, yy, nx, ny))
        xx, yy = nx, ny
        k += 1
    for (a, b, c, d) in segs:
        cv.line(a + 1, b, c + 1, d, VINE_D)
    for (a, b, c, d) in segs:
        cv.line(a, b, c, d, col)
    for i, (a, b, c, d) in enumerate(segs):
        if i % 2 == 0:
            cv.set(c + 1, d, leaf)
            cv.set(c - 1, d - 1, leaf)


def moss(cv, x, y, rx, ry):
    cv.ellipse(x, y, rx, ry, MOSS_M)
    cv.ellipse(x - rx // 3, y - ry // 3, max(1, rx // 2), max(1, ry // 2), MOSS_L)
    cv.set(x - rx // 2, y - max(1, ry // 2), MOSS_HL)


def dist_tree(cv, x, base, h, w, col):
    cv.rect(x - 1, base - h // 2, 3, h // 2, col)
    cv.ellipse(x, base - h + 4, w // 2, h // 3, col)
    cv.ellipse(x - w // 3, base - h // 2 - 6, w // 3, h // 4, col)
    cv.ellipse(x + w // 3, base - h // 2 - 4, w // 3, h // 4, col)


def tuft(cv, x, y, col, h=5):
    for dx in (-2, -1, 0, 1, 2):
        hh = max(1, h - abs(dx))
        lean = 1 if dx > 0 else (-1 if dx < 0 else 0)
        cv.line(x + dx, y, x + dx + lean, y - hh, col)


def rock(cv, x, y, w, h):
    cv.poly([(x, y), (x + w // 3, y - h), (x + 2 * w // 3, y - h + 1), (x + w, y),
             (x + w - 1, y + h // 3), (x + 1, y + h // 3)], ROCK_M)
    cv.poly([(x + 1, y), (x + w // 3, y - h + 1), (x + w // 2, y - h + 2), (x + w // 2, y)], ROCK_L)


def overview(cv, step=8):
    pal = {p["index"]: p["rgba"] for p in cv.palette()}
    chars = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    m = {}
    nxt = [1]
    out = []
    for y in range(0, H, step):
        row = ""
        for x in range(0, W, step):
            i = cv.get(x, y)
            if i is None:
                row += "?"
                continue
            rgba = pal.get(i, (0, 0, 0, 0))
            if rgba[3] == 0:
                row += "."
                continue
            if i not in m:
                m[i] = chars[nxt[0] % len(chars)]
                nxt[0] += 1
            row += m[i]
        out.append(row)
    print("\n".join(out))
    for i, ch in sorted(m.items(), key=lambda kv: kv[1]):
        print(ch, cv.color_name(i), pal[i])


# ================= BACKGROUND =================
bg = new_canvas(W, H, background=SKY_TOP, name="bg")
bg.rect(0, 0, W, 92, SKY_TOP)
bg.rect(0, 88, W, 54, SKY_MID)
bg.rect(0, 138, W, 44, SKY_LOW)
bg.rect(0, 178, W, 26, SKY_GLOW)
bg.dither(0, 84, W, 10, [SKY_TOP, SKY_MID], pattern="bayer4")
bg.dither(0, 132, W, 10, [SKY_MID, SKY_LOW], pattern="bayer4")
bg.dither(0, 172, W, 10, [SKY_LOW, SKY_GLOW], pattern="bayer4")

# distant treeline
for (x, h, w) in [(6, 52, 26), (30, 66, 30), (58, 46, 24), (86, 58, 28), (114, 42, 22),
                  (146, 50, 24), (174, 62, 30), (204, 48, 26), (232, 60, 30), (252, 44, 22)]:
    dist_tree(bg, x, 204, h, w, DIST1)
for (x, h, w) in [(0, 74, 34), (26, 88, 38), (228, 92, 40), (254, 70, 32)]:
    dist_tree(bg, x, 208, h, w, DIST2)

# ground
bg.rect(0, 200, W, 56, GRO_D)
bg.rect(0, 204, W, 52, GRO_M)
bg.dither(0, 197, W, 8, [SKY_GLOW, GRO_D], pattern="bayer4")
bg.dither(0, 201, W, 8, [GRO_D, GRO_M], pattern="bayer4")
bg.ellipse(128, 226, 88, 24, GRO_L)
bg.ellipse(126, 224, 60, 16, GRO_HL)
for i in range(130):
    x, y = random.randint(0, 255), random.randint(203, 255)
    bg.set(x, y, random.choice([GRO_D, GRO_M, GRO_L, GRO_HL]))

# grass + rocks + shadow
for (x, y) in [(18, 214), (34, 222), (52, 208), (70, 232), (96, 240), (150, 242),
               (176, 230), (200, 238), (222, 220), (240, 210), (12, 242), (60, 250),
               (120, 252), (190, 254), (248, 246), (44, 236), (210, 248)]:
    tuft(bg, x, y, random.choice([GRASS1, GRASS3]), random.randint(4, 7))
rock(bg, 28, 238, 16, 8)
rock(bg, 214, 232, 20, 9)
rock(bg, 98, 248, 12, 6)
bg.ellipse(128, 218, 76, 13, SHADOW)
bg.ellipse(128, 216, 54, 9, "#0d1409")

# ================= LIGHT LAYERS =================
glow = new_canvas(W, H, name="glow")
glow.poly([(0, 0), (104, 0), (214, H), (56, H)], GLOW_B)
glow.ellipse(128, 224, 86, 20, GLOW_C)

rays = new_canvas(W, H, name="rays")


def beam(cv, xt, wt, shift, colr):
    cv.poly([(xt, 0), (xt + wt, 0), (xt + wt + shift, H), (xt + shift, H)], colr)


beam(rays, 14, 22, 74, RAY_A)
beam(rays, 58, 12, 80, RAY_B)
beam(rays, 104, 26, 70, RAY_A)
beam(rays, 158, 14, 76, RAY_B)
beam(rays, 196, 22, 72, RAY_A)
beam(rays, 112, 10, 70, (232, 250, 196, 58))
beam(rays, 20, 8, 74, (232, 250, 196, 40))
rays.ellipse(26, 8, 20, 11, (226, 246, 186, 50))
rays.ellipse(26, 8, 11, 6, (242, 252, 214, 72))
rays.ellipse(120, 222, 54, 13, GLOW_C)

# ================= TREANT =================
t = new_canvas(W, H, name="treant")

# --- crown (back mass) ---
t.ellipse(128, 40, 64, 26, CAN_D)
t.ellipse(84, 36, 30, 18, CAN_D)
t.ellipse(172, 38, 30, 18, CAN_D)
t.ellipse(128, 28, 42, 18, CAN_D)
t.ellipse(70, 50, 20, 11, CAN_D)
t.ellipse(186, 52, 22, 12, CAN_D)
# bare branch tips above the crown
for (x0, y0, x1, y1) in [(76, 26, 62, 8), (96, 20, 90, 4), (150, 18, 146, 2),
                         (176, 26, 192, 10), (120, 14, 118, 2), (206, 44, 218, 30)]:
    t.line(x0, y0, x1, y1, BARK_D)
    t.line(x1, y1, x1 + (x1 - x0) // 3, y1 - 3, BARK_D)
# crown front clumps
t.ellipse(104, 40, 30, 16, CAN_M)
t.ellipse(152, 42, 30, 16, CAN_M)
t.ellipse(128, 30, 34, 14, CAN_M)
t.ellipse(112, 34, 18, 9, CAN_L)
t.ellipse(146, 36, 16, 8, CAN_L)
t.ellipse(126, 26, 14, 7, CAN_L)
t.ellipse(106, 30, 8, 4, CAN_HL)
t.ellipse(140, 30, 7, 4, CAN_HL)
t.ellipse(122, 24, 6, 3, CAN_HL)
# clump separation shadows + lit tops (scalloped canopy)
for (cx, cy, r) in [(88, 36, 9), (118, 28, 10), (148, 32, 9), (172, 42, 8),
                    (100, 48, 8), (140, 50, 8), (160, 54, 7), (78, 48, 6), (128, 44, 9)]:
    t.ellipse(cx, cy + 3, r, 3, CAN_D)
    t.ellipse(cx - 2, cy - 2, max(2, r - 4), 3, CAN_L)
for (dx, dy) in [(96, 28), (110, 22), (126, 20), (142, 24), (158, 32), (170, 44),
                 (86, 40), (104, 40), (134, 38), (150, 46), (118, 34), (164, 36),
                 (92, 46), (124, 30), (138, 44), (108, 46)]:
    t.set(dx, dy, CAN_HL)
    t.set(dx + 1, dy, CAN_HL)
# scalloped dark underside of the crown
for x in range(66, 194, 7):
    t.line(x, 56, x + 4, 64, CAN_D)

# --- roots rising from the ground (behind legs) ---
t.path("M 54 224 Q 42 204 56 186 Q 62 202 64 220 Z", ROOT)
t.path("M 202 224 Q 216 206 204 188 Q 198 204 196 220 Z", ROOT)
t.path("M 34 226 Q 26 214 34 202 Q 38 214 40 224 Z", ROOT_D)
t.path("M 222 226 Q 232 216 224 204 Q 220 216 218 224 Z", ROOT_D)
t.path("M 96 218 Q 88 200 98 188 Q 102 202 102 214 Z", ROOT_D)

# --- root legs ---
taper(t, [(104, 150), (94, 174), (86, 194), (82, 206)], 10, 6, BARK)
taper(t, [(152, 150), (162, 174), (170, 194), (174, 206)], 10, 6, BARK)
taper(t, [(118, 158), (112, 180), (108, 200)], 7, 4, BARK)
taper(t, [(138, 158), (144, 180), (148, 200)], 7, 4, BARK)
taper(t, [(128, 160), (127, 182), (126, 202)], 6, 4, BARK)
# claw toes
spike(t, 82, 204, 60, 214, 4, BARK)
spike(t, 84, 206, 76, 222, 4, BARK)
spike(t, 90, 206, 100, 218, 4, BARK)
spike(t, 174, 204, 196, 214, 4, BARK)
spike(t, 172, 206, 180, 222, 4, BARK)
spike(t, 166, 206, 156, 218, 4, BARK)
spike(t, 108, 198, 96, 212, 3, BARK)
spike(t, 110, 200, 112, 216, 3, BARK)
spike(t, 148, 198, 160, 212, 3, BARK)
spike(t, 146, 200, 144, 216, 3, BARK)
spike(t, 126, 200, 116, 214, 3, BARK)
spike(t, 128, 200, 130, 218, 3, BARK)
spike(t, 128, 200, 140, 212, 3, BARK)
# leg shading + texture
t.line(100, 156, 88, 198, BARK_L)
t.line(156, 156, 168, 198, BARK_D)
t.line(104, 160, 94, 200, BARK_D)
t.line(150, 160, 162, 200, BARK_D)

# --- torso ---
t.poly([(102, 62), (154, 62), (162, 86), (168, 110), (173, 134), (176, 158),
        (166, 166), (90, 166), (80, 158), (83, 134), (88, 110), (94, 86)], BARK)
t.poly([(102, 62), (112, 64), (106, 92), (102, 122), (100, 166), (90, 166),
        (80, 158), (83, 134), (88, 110), (94, 86)], BARK_L)
t.poly([(154, 62), (144, 64), (150, 92), (154, 122), (156, 166), (166, 166),
        (176, 158), (173, 134), (168, 110), (162, 86)], BARK_D)
# bark texture (kept inside the silhouette)
bark_tex(t, 108, 148, 64, 78, 7, BARK_D)
bark_tex(t, 92, 166, 112, 164, 7, BARK_D)
bark_tex(t, 112, 146, 116, 162, 13, BARK_M, amp=1, seg=9)
bark_tex(t, 97, 103, 84, 112, 4, BARK_D, amp=1, seg=7)
bark_tex(t, 153, 159, 84, 112, 4, BARK_D, amp=1, seg=7)
# knots and cracks
t.ellipse(120, 128, 7, 5, BARK_D)
t.ellipse(120, 128, 4, 3, BARK_DD)
t.set(120, 128, BARK_D)
t.ellipse(150, 144, 6, 4, BARK_D)
t.ellipse(150, 144, 3, 2, BARK_DD)
t.ellipse(112, 150, 4, 3, BARK_D)
t.line(108, 118, 124, 116, BARK_D)
t.line(134, 152, 152, 150, BARK_D)
t.line(140, 120, 156, 122, BARK_D)
# glowing energy seam in the bark
t.line(132, 120, 128, 140, BARK_DD)
t.line(128, 140, 132, 156, BARK_DD)
t.set(130, 128, EYE_O)
t.set(129, 136, EYE_O)
t.set(131, 146, EYE_M)
t.set(130, 152, EYE_O)

# --- face ---
# brow slabs
t.poly([(99, 76), (123, 83), (123, 89), (99, 82)], BARK_D)
t.line(99, 82, 123, 89, BARK_DD)
t.poly([(157, 76), (133, 83), (133, 89), (157, 82)], BARK_D)
t.line(157, 82, 133, 89, BARK_DD)
# eyes (glowing, slanted)
t.poly([(98, 84), (123, 90), (123, 103), (101, 98)], EYE_HALO)
t.poly([(101, 87), (121, 92), (121, 101), (103, 96)], EYE_S)
t.poly([(104, 89), (119, 93), (119, 99), (106, 95)], EYE_O)
t.poly([(106, 90), (117, 94), (117, 98), (108, 94)], EYE_M)
t.poly([(108, 91), (116, 94), (116, 96), (108, 93)], EYE_C)
t.set(111, 93, EYE_H)
t.set(113, 94, EYE_H)
t.poly([(158, 84), (133, 90), (133, 103), (155, 98)], EYE_HALO)
t.poly([(155, 87), (135, 92), (135, 101), (153, 96)], EYE_S)
t.poly([(152, 89), (137, 93), (137, 99), (150, 95)], EYE_O)
t.poly([(150, 90), (139, 94), (139, 98), (148, 94)], EYE_M)
t.poly([(148, 91), (140, 94), (140, 96), (148, 93)], EYE_C)
t.set(145, 93, EYE_H)
t.set(143, 94, EYE_H)
# nose ridge
t.poly([(125, 92), (132, 92), (130, 108), (127, 108)], BARK_D)
t.line(131, 93, 129, 107, BARK_DD)
# jagged mouth crack
t.poly([(106, 110), (114, 107), (120, 112), (128, 107), (134, 112), (142, 108),
        (150, 110), (148, 118), (140, 115), (134, 120), (126, 114), (118, 120),
        (110, 116), (106, 114)], BARK_DD)
spike(t, 114, 108, 114, 114, 2, BARK_D)
spike(t, 128, 108, 128, 113, 2, BARK_D)
spike(t, 142, 109, 142, 114, 2, BARK_D)
spike(t, 120, 119, 120, 113, 2, BARK_D)
spike(t, 134, 119, 134, 114, 2, BARK_D)
t.set(121, 112, EYE_O)
t.set(131, 113, EYE_O)
t.set(139, 111, EYE_O)

# --- arms (raised, clawed) ---
taper(t, [(102, 76), (84, 66), (64, 52), (48, 42)], 7, 4, BARK)
taper(t, [(154, 76), (172, 64), (192, 50), (208, 42)], 7, 4, BARK)
t.line(99, 70, 52, 42, BARK_L)
t.line(157, 70, 204, 42, BARK_L)
t.line(103, 80, 58, 48, BARK_D)
t.line(151, 80, 196, 48, BARK_D)
# claw twigs
spike(t, 48, 42, 32, 20, 3, BARK)
spike(t, 50, 40, 42, 12, 3, BARK)
spike(t, 52, 44, 56, 16, 3, BARK)
spike(t, 46, 46, 26, 34, 2, BARK)
spike(t, 208, 42, 224, 20, 3, BARK)
spike(t, 206, 40, 214, 12, 3, BARK)
spike(t, 204, 44, 200, 16, 3, BARK)
spike(t, 210, 46, 230, 34, 2, BARK)
t.line(46, 40, 34, 22, BARK_D)
t.line(206, 40, 222, 22, BARK_D)
# elbow thorns
spike(t, 66, 58, 58, 68, 2, BARK_D)
spike(t, 190, 56, 198, 66, 2, BARK_D)
spike(t, 84, 64, 80, 74, 2, BARK_D)
spike(t, 172, 62, 176, 72, 2, BARK_D)

# --- moss patches ---
moss(t, 96, 64, 11, 4)
moss(t, 160, 64, 11, 4)
moss(t, 128, 60, 14, 4)
moss(t, 74, 56, 8, 3)
moss(t, 182, 58, 8, 3)
moss(t, 56, 46, 6, 3)
moss(t, 200, 46, 6, 3)
moss(t, 92, 170, 9, 3)
moss(t, 164, 170, 9, 3)
moss(t, 86, 190, 6, 3)
moss(t, 170, 190, 6, 3)
moss(t, 118, 66, 7, 3)

# --- dark outline around the whole creature ---
t.outline(OUTLINE)

# --- hanging vines (after the outline so they keep their green) ---
vine(t, 62, 58, 104, VINE, LEAF, sway=3, phase=0.3)
vine(t, 196, 56, 96, VINE, LEAF, sway=3, phase=1.8)
vine(t, 84, 60, 88, VINE, LEAF, sway=2, phase=2.6)
vine(t, 172, 60, 84, VINE, LEAF, sway=2, phase=0.9)
vine(t, 112, 62, 78, VINE, LEAF, sway=2, phase=1.4)

# --- rim light from the god rays (upper-left) ---
for (x0, y0, x1, y1) in [(99, 69, 87, 61), (87, 61, 73, 51), (73, 51, 59, 43),
                         (159, 69, 173, 59), (173, 59, 189, 47), (189, 47, 203, 41),
                         (95, 88, 90, 110), (90, 110, 85, 134), (85, 134, 83, 154),
                         (104, 64, 118, 63), (88, 160, 100, 158), (86, 180, 82, 196),
                         (78, 200, 66, 210), (172, 64, 158, 63)]:
    t.line(x0, y0, x1, y1, RIM)

# ================= FOREGROUND =================
fg = new_canvas(W, H, name="fg")
fg.path("M 66 236 Q 54 226 64 212 Q 70 224 72 234 Z", ROOT_D)
fg.path("M 192 238 Q 204 228 194 214 Q 188 226 186 236 Z", ROOT_D)
for x in list(range(0, 56, 5)) + list(range(204, 256, 5)):
    if random.random() < 0.8:
        h = random.randint(4, 11)
        fg.line(x, 256, x + random.randint(-2, 2), 256 - h,
                random.choice([GRASS1, GRASS3, GRASS2]))
for (x, y) in [(70, 250), (120, 254), (180, 252), (230, 250)]:
    tuft(fg, x, y, GRASS1, 6)
# drifting spores in the light
for i in range(30):
    x, y = random.randint(20, 236), random.randint(30, 200)
    fg.set(x, y, SPORE if random.random() < 0.5 else SPORE2)
    if random.random() < 0.4:
        fg.set(x + 1, y, SPORE2)
# falling leaves
fg.poly([(150, 120), (155, 123), (150, 127), (146, 123)], "#5d8a33")
fg.poly([(90, 160), (95, 163), (90, 167), (86, 163)], "#4c7a2b")
fg.poly([(178, 88), (183, 91), (178, 95), (174, 91)], "#54812f")
# corner shading
fg.poly([(0, 256), (0, 214), (34, 256)], (0, 0, 0, 45))
fg.poly([(256, 256), (256, 214), (222, 256)], (0, 0, 0, 45))
# glowing mushrooms in the roots' shade
for (x, y) in [(64, 234), (188, 240), (36, 246), (222, 250)]:
    fg.rect(x - 1, y - 3, 2, 3, SHROOM_STEM)
    fg.ellipse(x, y - 4, 3, 2, SHROOM_CAP)
    fg.line(x - 2, y - 5, x + 2, y - 5, SHROOM_HL)
    fg.set(x, y - 6, SHROOM_GLOW)
    fg.set(x - 1, y - 6, SHROOM_GLOW)

def reduce_colors(cv, limit=100):
    """Merge near-identical blended colours into their most frequent neighbour."""
    from collections import Counter
    w, h, buf = cv.to_rgba()
    n = w * h
    cnt = Counter()
    for i in range(n):
        a = buf[i * 4 + 3]
        if a == 0:
            continue
        cnt[(buf[i * 4], buf[i * 4 + 1], buf[i * 4 + 2], a)] += 1
    order = [c for c, _ in cnt.most_common()]

    def dist(c1, c2):
        dr, dg, db = c1[0] - c2[0], c1[1] - c2[1], c1[2] - c2[2]
        return 0.9 * dr * dr + 1.3 * dg * dg + 0.6 * db * db

    kept, mapping = [], {}
    for thresh in (10, 13, 16, 20, 24, 28, 34, 42):
        kept, mapping = [], {}
        for c in order:
            best, bd = None, thresh * thresh
            for k in kept:
                d = dist(c, k)
                if d < bd:
                    bd, best = d, k
            if best is None:
                kept.append(c)
            mapping[c] = best if best is not None else c
        if len(kept) <= limit:
            break
    out = new_canvas(w, h, name="result")
    for y in range(h):
        base = y * w
        for x in range(w):
            i = (base + x) * 4
            a = buf[i + 3]
            if a == 0:
                continue
            out.set(x, y, mapping[(buf[i], buf[i + 1], buf[i + 2], a)])
    print("reduced to", len(kept), "colours (thresh", thresh, ")")
    return out


def region_overview(cv, x0, y0, x1, y1, step=2):
    pal = {p["index"]: p["rgba"] for p in cv.palette()}
    chars = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    m, nxt, out = {}, [1], []
    for y in range(y0, y1 + 1, step):
        row = ""
        for x in range(x0, x1 + 1, step):
            i = cv.get(x, y)
            rgba = pal.get(i, (0, 0, 0, 0))
            if i is None or rgba[3] == 0:
                row += "."
                continue
            if i not in m:
                m[i] = chars[nxt[0] % len(chars)]
                nxt[0] += 1
            row += m[i]
        out.append(row)
    print("\n".join(out))
    for i, ch in sorted(m.items(), key=lambda kv: kv[1]):
        print(ch, cv.color_name(i), pal[i])


# ================= COMPOSITE =================
result = reduce_colors(flatten([bg, glow, rays, t, fg], name="flat"))
print(result.stats_text())
overview(result, step=4)
print("--- left arm / claw (24-112, 10-84) step2 ---")
region_overview(result, 24, 10, 112, 84, 2)
print("--- full silhouette step8 ---")
overview(result, step=8)
finish(result)
