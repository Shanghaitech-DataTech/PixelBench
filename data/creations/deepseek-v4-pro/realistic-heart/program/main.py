from pixelbench_api import *

c = new_canvas(64, 64, name="output")

# ---------- helpers ----------
def lerp(c1, c2, t):
    return tuple(round(a + (b - a) * t) for a, b in zip(c1, c2))

def scaled(poly, s, cx, cy):
    return [(round(cx + (x - cx) * s), round(cy + (y - cy) * s)) for x, y in poly]

def poly_path(pts, close=False):
    d = f"M {pts[0][0]} {pts[0][1]}"
    for p in pts[1:]:
        d += f" L {p[0]} {p[1]}"
    if close:
        d += " Z"
    return d

# ---------- body silhouette ----------
body = [
    (25, 59),
    (18, 50),
    (13, 40),
    (11, 30),
    (12, 23),
    (17, 18),
    (24, 15),
    (32, 15),
    (38, 16),
    (43, 19),
    (48, 25),
    (49, 33),
    (45, 42),
    (38, 50),
    (30, 56),
]

# ---------- base shading: nested bands ----------
dark = (46, 12, 20)
light = (244, 150, 158)
n_bands = 16
cx, cy = 24, 26
for i in range(n_bands):
    t = i / (n_bands - 1)
    col = c.color(lerp(dark, light, t), name=f"band{i}")
    s = 1.0 - 0.62 * t
    c.poly(scaled(body, s, cx, cy), col, fill=True)

# ---------- details palette ----------
wall_mid = c.color((178, 78, 90), name="wall_mid")
wall_light = c.color((214, 124, 134), name="wall_light")
wall_dark = c.color((120, 44, 56), name="wall_dark")
lumen = c.color((24, 6, 10), name="lumen")
vein_mid = c.color((82, 62, 122), name="vein_mid")
vein_light = c.color((120, 96, 168), name="vein_light")
vein_dark = c.color((48, 34, 74), name="vein_dark")
fat_mid = c.color((190, 150, 80), name="fat_mid")
fat_light = c.color((225, 190, 120), name="fat_light")
fat_dark = c.color((150, 110, 50), name="fat_dark")
artery = c.color((208, 60, 72), name="artery")
artery_light = c.color((232, 96, 108), name="artery_light")
red_light1 = c.color((198, 78, 92), name="red_light1")
red_dark1 = c.color((80, 20, 30), name="red_dark1")
spec1 = c.color((250, 180, 188), name="spec1")
spec2 = c.color((255, 218, 222), name="spec2")

# ---------- great vessels ----------
# pulmonary trunk (front left)
c.rect(27, 5, 7, 13, wall_mid, fill=True)
c.ellipse(30, 6, 3, 2, lumen, fill=True)
c.ellipse(30, 6, 3, 2, wall_light, fill=False)
c.rect(27, 8, 2, 10, wall_light, fill=True)
c.rect(32, 8, 2, 10, wall_dark, fill=True)

# aorta (right)
c.rect(36, 4, 8, 14, wall_mid, fill=True)
c.ellipse(40, 5, 3, 2, lumen, fill=True)
c.ellipse(40, 5, 3, 2, wall_light, fill=False)
c.rect(36, 8, 2, 9, wall_light, fill=True)
c.rect(41, 8, 2, 9, wall_dark, fill=True)

# superior vena cava (far right, bluish)
c.rect(44, 7, 5, 13, vein_mid, fill=True)
c.ellipse(46, 8, 2, 2, lumen, fill=True)
c.ellipse(46, 8, 2, 2, vein_light, fill=False)
c.rect(44, 10, 1, 8, vein_light, fill=True)
c.rect(47, 10, 2, 8, vein_dark, fill=True)

# ---------- coronary (AV) sulcus ----------
av_upper = [(13, 26), (18, 22), (26, 21), (34, 22), (42, 24), (47, 27)]
av_lower = [(48, 30), (43, 26), (35, 24), (27, 24), (19, 26), (14, 29)]
c.poly(av_upper + av_lower[::-1], fat_mid, fill=True)
c.path(poly_path(av_upper), fat_light, fill=False)
c.path(poly_path(av_lower), fat_dark, fill=False)
av_shadow = [(48, 32), (43, 28), (35, 26), (27, 26), (19, 28), (14, 31)]
c.path(poly_path(av_shadow), red_dark1, fill=False)

# ---------- anterior interventricular sulcus ----------
iv_left = [(30, 22), (27, 34), (25, 46), (25, 57)]
iv_right = [(32, 23), (29, 35), (27, 47), (26, 56)]
c.poly(iv_left + iv_right[::-1], red_dark1, fill=True)
# LAD artery in the groove
c.path("M 31 23 Q 29 36 27 48 Q 26 53 26 56", artery, fill=False)
c.path("M 32 23 Q 30 36 28 48 Q 27 53 27 56", artery_light, fill=False)

# diagonal branches
c.path("M 29 32 Q 25 35 22 37", artery, fill=False)
c.path("M 28 40 Q 24 43 20 46", artery, fill=False)
c.path("M 27 46 Q 23 49 20 51", artery, fill=False)

# right coronary artery along right AV sulcus + marginal branches
c.path("M 36 22 Q 42 24 46 28", artery, fill=False)
c.path("M 43 27 Q 44 31 43 34", artery, fill=False)
c.path("M 46 29 Q 47 33 47 36", artery, fill=False)

# left circumflex hint
c.path("M 19 23 Q 15 25 13 28", artery, fill=False)

# coronary veins (bluish)
c.path("M 15 27 Q 13 32 14 37", vein_mid, fill=False)
c.path("M 47 28 Q 48 33 47 38", vein_mid, fill=False)

# ---------- auricles ----------
left_auricle = [(15, 20), (10, 22), (8, 27), (10, 31), (14, 30), (17, 26), (17, 22)]
c.poly(left_auricle, red_light1, fill=True)
c.poly(left_auricle, red_dark1, fill=False)

right_auricle = [(44, 20), (49, 21), (52, 25), (50, 29), (46, 28), (44, 24)]
c.poly(right_auricle, red_light1, fill=True)
c.poly(right_auricle, red_dark1, fill=False)

# ---------- surface texture and specular highlight ----------
# specular highlight on the left ventricle
c.ellipse(21, 35, 4, 3, spec1, fill=True)
c.ellipse(20, 34, 2, 2, spec2, fill=True)

# small fat pads around vessel bases
c.ellipse(25, 17, 2, 2, fat_mid, fill=True)
c.ellipse(35, 17, 2, 2, fat_mid, fill=True)
c.ellipse(44, 19, 2, 2, fat_mid, fill=True)
# fat where the interventricular groove meets the AV sulcus
c.ellipse(30, 23, 2, 2, fat_mid, fill=True)

# vessel base shadows (anchor the tubes into the heart)
c.line(27, 17, 33, 17, red_dark1)
c.line(36, 17, 43, 17, red_dark1)
c.line(44, 19, 48, 19, red_dark1)

print(c.stats_text())
finish(c)
