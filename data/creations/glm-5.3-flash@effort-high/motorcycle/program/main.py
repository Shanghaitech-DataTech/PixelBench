import math

c = new_canvas(128, 128, background=None, name="moto")

# ---- palette ----
TIRE   = c.color("#101014", "tire")
TIRE_H = c.color("#26262c", "tire_hi")
BODY   = c.color("#2c2c33", "body_dark")
BODY_H = c.color("#43434c", "body_mid")
SIL    = c.color("#bcc1ca", "silver")
SIL_D  = c.color("#838994", "silver_dk")
HUB    = c.color("#5c616b", "hub")
RED    = c.color("#d21f2e", "red")
RED_D  = c.color("#8e1220", "red_dk")
WHITE  = c.color("#eef0f4", "white")

def tline(x0, y0, x1, y1, col, w=2):
    """thick line: w parallel 1px lines offset perpendicular"""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    for i in range(w):
        o = i - (w - 1) / 2.0
        c.line(int(round(x0 + nx * o)), int(round(y0 + ny * o)),
               int(round(x1 + nx * o)), int(round(y1 + ny * o)), col)

def wheel(cx, cy):
    c.circle(cx, cy, 16, TIRE)                    # thick black tire
    c.circle(cx, cy, 16, TIRE_H, fill=False)      # tire outer edge
    c.circle(cx, cy, 13, TIRE, fill=False)        # tire inner shoulder
    c.circle(cx, cy, 10, BODY)                    # rim well / dark interior
    c.circle(cx, cy, 10, SIL_D, fill=False)       # rim ring
    c.circle(cx, cy, 9, SIL_D, fill=False)        # brake disc
    for k in range(6):                            # white spokes
        a = math.pi / 6 + k * math.pi / 3
        c.line(cx, cy, int(round(cx + 9 * math.cos(a))),
               int(round(cy + 9 * math.sin(a))), WHITE)
    c.circle(cx, cy, 4, HUB)                      # gray hub
    c.circle(cx, cy, 2, SIL)

RW = (34, 88)   # rear wheel centre
FW = (98, 88)   # front wheel centre

# ================= wheels =================
wheel(*RW)
wheel(*FW)

# ================= swingarm (silver tubular) =================
tline(34, 88, 62, 81, SIL_D, 3)
tline(34, 88, 62, 81, SIL, 1)
c.circle(62, 81, 2, SIL_D)                        # pivot boss

# subframe tube under the tail
tline(56, 59, 42, 68, SIL_D, 2)

# ================= exhaust (upswept muffler) =================
tline(60, 78, 44, 68, SIL_D, 5)
tline(60, 77, 45, 68, SIL, 2)
c.circle(43, 67, 3, SIL)
c.set(42, 66, TIRE)                                # pipe opening

# ================= front fender =================
pts = []
for deg in range(30, 151, 8):
    a = math.radians(deg)
    pts.append((FW[0] + 21 * math.cos(a), FW[1] - 21 * math.sin(a)))
for deg in range(150, 29, -8):
    a = math.radians(deg)
    pts.append((FW[0] + 17 * math.cos(a), FW[1] - 17 * math.sin(a)))
c.poly(pts, BODY)

# ================= front fork (silver) =================
tline(98, 86, 89, 48, SIL_D, 3)
tline(97, 86, 88, 48, SIL, 1)
# lower fork slider
tline(97, 78, 94, 62, SIL, 2)
# triple clamp + handlebar
c.rect(85, 45, 8, 3, SIL_D)
tline(85, 45, 79, 42, TIRE, 2)                     # grip
c.set(84, 44, SIL)

# ================= main body / fairing (dark gray) =================
body = [(101, 60), (97, 52), (90, 47), (82, 46), (74, 48), (66, 52),
        (60, 55), (55, 58), (54, 66), (57, 74), (62, 79), (70, 80),
        (80, 79), (88, 76), (94, 71), (98, 66)]
c.poly(body, BODY)
# belly panel in black
c.poly([(58, 70), (62, 79), (70, 80), (80, 79), (86, 76), (80, 74),
        (70, 75), (62, 72)], TIRE)
# top highlight along the fairing
tline(97, 53, 90, 48, BODY_H, 1)
tline(88, 47, 76, 49, BODY_H, 1)

# ================= main frame (silver tubular) =================
tline(88, 50, 63, 80, SIL_D, 2)
tline(88, 50, 63, 80, SIL, 1)
# downtube behind the nose
tline(93, 56, 86, 70, SIL_D, 2)

# ================= tail (upswept) =================
tail = [(60, 54), (40, 47), (27, 44), (23, 46), (25, 51), (34, 55),
        (46, 60), (58, 64), (60, 58)]
c.poly(tail, BODY)
# black seat
tline(58, 55, 30, 47, TIRE, 2)
# tail highlight
tline(56, 56, 38, 50, BODY_H, 1)
# red tail light
c.rect(23, 46, 3, 4, RED)
c.set(24, 47, WHITE)
# red stripe along the tail top edge
tline(52, 51, 30, 45, RED, 1)
tline(30, 45, 26, 45, RED, 1)

# ================= red accents =================
# stripe sweeping along the fairing
tline(99, 58, 91, 50, RED, 2)
tline(91, 50, 80, 48, RED, 1)
tline(80, 48, 68, 52, RED, 1)
# red edge on the tail underside
tline(56, 62, 40, 55, RED_D, 1)
# red accent on the front fender
tline(88, 71, 96, 68, RED, 1)
# nose accent
c.rect(99, 58, 2, 3, RED_D)

# ================= engine cover (round, silver gray) =================
c.circle(70, 70, 8, SIL)
c.circle(70, 70, 8, SIL_D, fill=False)
c.circle(70, 70, 5, SIL_D)
c.circle(70, 70, 3, SIL)
c.set(70, 70, HUB)
# clutch cover arcs
c.circle(70, 70, 6, SIL_D, fill=False)

# ================= windscreen (small, tilted, black) =================
c.poly([(85, 45), (92, 42), (88, 34), (81, 37)], TIRE)
tline(83, 43, 87, 36, TIRE_H, 1)

# ================= mirrors =================
c.line(86, 43, 82, 39, SIL_D)
c.rect(79, 36, 4, 2, SIL_D)

# ================= headlight sliver =================
c.set(100, 59, WHITE)
c.set(101, 60, WHITE)
c.set(101, 61, SIL)

# footpeg
c.set(64, 80, SIL_D)
c.set(63, 81, SIL_D)

# ---- inspection: downsampled ascii ----
import numpy as np
W, H, rgba = c.to_rgba()
rgba = np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(H, W, 4)
# color-coded downsample (2x2 blocks, dominant colour)
names = {}
for entry in c.palette():
    names[entry["index"]] = entry["name"]
sym = {"tire": "#", "tire_hi": "%", "body_dark": "o", "body_mid": "O",
       "silver": "=", "silver_dk": "-", "hub": "h", "red": "R",
       "red_dk": "r", "white": "*"}
for yy in range(0, H, 2):
    row = ""
    for xx in range(0, W, 2):
        best, cnt = None, 0
        for dy in (0, 1):
            for dx in (0, 1):
                if xx+dx < W and yy+dy < H:
                    a = int(rgba[yy+dy, xx+dx, 3])
                    if a > 0:
                        idx = int(rgba[yy+dy, xx+dx, 0])
                        cnt += 1
                        if best is None:
                            best = idx
print(c.stats_text())

result = c
finish(result)


