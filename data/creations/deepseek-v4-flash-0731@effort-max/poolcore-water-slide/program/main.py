import math
from pixelbench_api import *

P = {
    "w0": "#ffffff",
    "p1": "#eef4f9", "p2": "#dce7f0", "p3": "#c8d9e6", "p4": "#aec6d8",
    "wt2": "#c0d7e7", "wt3": "#a4c3d9", "wt4": "#8aacc6", "wt5": "#7195b2",
    "q1": "#e4f8fd", "q2": "#c0eef7", "q3": "#97dcee", "q4": "#6bc4e0",
    "q5": "#46a9c9", "q6": "#2d8fb0", "q7": "#217695", "q8": "#1b5f7c",
    "s1": "#ffffff", "s2": "#dfeaf2", "s3": "#bed3e2",
    "r1": "#ffe97f", "r2": "#f4cd26",
    "sk": "#f1c79d",
    "hr": "#5a4430", "hr2": "#715840",
    "su": "#f0a9c2",
    "dr": "#101b26", "dr2": "#243a4d",
}


def edged(pts, off):
    n = len(pts)
    out = []
    for i, p in enumerate(pts):
        pr = pts[i - 1]
        nx = pts[i + 1 if i + 1 < n else n - 1]
        dx = nx[0] - pr[0]
        dy = nx[1] - pr[1]
        L = math.hypot(dx, dy) or 1.0
        out.append((p[0] - dy / L * off, p[1] + dx / L * off))
    return out


def band(pts, hw):
    a = edged(pts, hw)
    b = edged(pts, -hw)
    return [(round(x), round(y)) for x, y in a] + [(round(x), round(y)) for x, y in b[::-1]]


def bez(p0, p1, p2, p3, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


c = new_canvas(128, 128, name="poolroom")

# ---------------- side columns ----------------
c.rect(0, 0, 16, 128, P["p1"])
for x in (4, 8, 12):
    c.line(x, 0, x, 127, P["wt5"])
for y in (6, 12, 19, 27, 36, 46, 57, 69, 82, 96, 111, 127):
    c.line(0, y, 15, y, P["wt5"])
c.line(15, 0, 15, 127, P["wt4"])

c.rect(112, 0, 16, 128, P["p1"])
for x in (115, 119, 123):
    c.line(x, 0, x, 127, P["wt5"])
for y in (6, 12, 19, 27, 36, 46, 57, 69, 82, 96, 111, 127):
    c.line(112, y, 127, y, P["wt5"])
c.line(112, 0, 112, 127, P["wt4"])

# ---------------- ceiling ----------------
c.rect(16, 0, 96, 34, P["p2"])
for (yt, y2) in [(2, 5), (6, 10), (11, 15), (16, 20), (21, 25), (26, 30), (31, 33)]:
    for (x0, x1) in [(18, 40), (42, 64), (66, 88), (90, 110)]:
        w = x1 - x0 + 1
        h = y2 - yt + 1
        c.rect(x0, yt, w, h, P["p3"])
        c.rect(x0 + 1, yt + 1, w - 2, h - 2, P["w0"])
for x in (16, 40, 64, 88, 110):
    c.rect(x, 0, 2, 34, P["p4"])

# ---------------- back wall ----------------
c.rect(16, 34, 96, 16, P["wt2"])
for x in range(22, 112, 6):
    c.line(x, 34, x, 49, P["wt3"])
for y in (38, 42, 46):
    c.line(16, y, 111, y, P["wt3"])
c.line(16, 50, 111, 50, P["wt4"])

# dark doorway (left)
c.rect(27, 34, 20, 16, P["wt4"])
c.rect(29, 36, 16, 14, P["dr"])
c.rect(29, 36, 16, 3, P["dr2"])
c.rect(29, 50, 16, 3, P["wt3"])

# bright window (right)
c.rect(70, 34, 14, 12, P["wt4"])
c.rect(72, 36, 10, 8, P["q3"])
c.line(77, 36, 77, 44, P["wt4"])
c.line(72, 40, 82, 40, P["wt4"])
c.line(75, 36, 75, 44, P["q1"])

# slide platform on wall (right)
c.rect(90, 36, 22, 9, P["wt2"])
c.line(90, 41, 111, 41, P["wt4"])

# ---------------- floor ----------------
c.rect(16, 50, 96, 78, P["wt2"])
for y in (56, 63, 71, 80, 90, 101, 113):
    c.line(16, y, 111, y, P["wt3"])
for x in (18, 20, 22):
    c.line(x, 50, x, 127, P["wt3"])
for x in (106, 108, 110):
    c.line(x, 50, x, 127, P["wt3"])
c.line(16, 125, 111, 125, P["wt4"])

# ---------------- pool water ----------------
c.rect(24, 56, 80, 69, P["q6"])
for (y0, y1, kk) in [(56, 58, "q4"), (59, 63, "q5"), (64, 67, "q6"), (68, 75, "q5"),
                    (76, 83, "q6"), (84, 92, "q7"), (93, 101, "q6"), (102, 109, "q7"),
                    (110, 117, "q6"), (118, 124, "q7")]:
    c.rect(24, y0, 80, y1 - y0 + 1, P[kk])
# faint underwater tile diagonals
for y0 in range(60, 120, 8):
    c.line(24, y0, 24 + (124 - y0), 124, P["q8"])
    c.line(103, y0, 103 - (124 - y0), 124, P["q8"])
# pool rims
c.line(24, 55, 103, 55, P["wt4"])
c.line(24, 124, 103, 124, P["wt4"])
c.line(24, 56, 24, 124, P["wt4"])
c.line(103, 56, 103, 124, P["wt4"])

# light reflections (ceiling panels)
for (cx, y0) in [(28, 58), (52, 56), (76, 55), (99, 57)]:
    c.rect(cx, y0, 1, 3, P["q1"])
    c.rect(cx - 1, y0 + 1, 1, 2, P["q2"])
    c.rect(cx + 1, y0 + 1, 1, 2, P["q2"])
    c.rect(cx, y0 + 4, 1, 7, P["q1"])
    c.rect(cx, y0 + 10, 1, 5, P["q2"])

# window reflection
c.rect(80, 57, 12, 2, P["q2"])
c.rect(83, 58, 6, 2, P["q1"])

# gentle ripple dashes
for yb in range(60, 124, 3):
    row = yb + int(2.0 * math.sin(yb * 1.1))
    for x0 in range(24, 100, 6):
        if 46 <= x0 <= 82:
            continue
        c.rect(x0, row, 3, 1, P["q2"])

# ---------------- slide ----------------
pts = bez((96, 40), (109, 62), (112, 84), (96, 107))
# slide visible through clear water (+ shadow nearby)
c.poly(band([(x + 2, y + 3) for x, y in pts], 6.0), P["q5"])
c.poly(band([(x + 5, y + 9) for x, y in pts], 6.0), P["q8"])
# the slide itself (white flume)
c.poly(band(pts, 6.0), P["s1"])
c.poly(band(pts, 3.4), P["s2"])
Ls = edged(pts, 6.0)
Rs = edged(pts, -6.0)
for i in range(3, len(pts), 4):
    c.line(round(Ls[i][0]), round(Ls[i][1]), round(Rs[i][0]), round(Rs[i][1]), P["s3"])
# splash around slide entrance (soft froth)
c.ellipse(96, 108, 9, 4, P["q3"])
c.ellipse(96, 112, 13, 5, P["q3"])
c.rect(84, 109, 24, 4, P["q2"])
c.rect(88, 106, 16, 2, P["q4"])
c.rect(86, 113, 20, 3, P["q1"])

# ---------------- girl in swim ring ----------------
# soft reflection under her
c.rect(60, 94, 8, 6, P["q4"])
c.ellipse(64, 98, 14, 6, P["q2"], fill=False)
c.ellipse(64, 103, 17, 8, P["q1"], fill=False)
# the ring
c.ellipse(64, 88, 10, 5, P["r2"], fill=True)
c.ellipse(64, 88, 8, 3, P["q5"], fill=True)
c.ellipse(64, 86, 8, 3, P["r1"], fill=False)
# body (from behind)
c.rect(60, 81, 8, 6, P["su"])
c.ellipse(64, 78, 5, 3, P["sk"])
c.ellipse(64, 69, 5, 5, P["hr"])
c.rect(61, 66, 6, 1, P["hr2"])
# near-side ring edge over water
c.ellipse(64, 90, 10, 4, P["r1"], fill=False)
c.ellipse(64, 91, 10, 4, P["r2"], fill=False)

print(c.stats_text())
finish(c)
