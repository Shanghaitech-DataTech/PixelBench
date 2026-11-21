W = H = 64

# ---------------- palette ----------------
OUT  = "#2a0a14"
D4   = "#43101a"
D3   = "#5c1623"
D2   = "#79202d"
D1   = "#942a35"
M    = "#ad3540"
L1   = "#c0484d"
L2   = "#d0605f"
L3   = "#de8179"
HL   = "#eeaa9e"
PUR0 = "#431626"
PUR  = "#5e2232"
PUR2 = "#7d2f43"
PUR3 = "#9b4257"
PUR4 = "#b5586a"
FAT  = "#ded0a4"
FAT2 = "#bfa678"
FATD = "#8e7646"
AOR  = "#c87f82"
AORL = "#e0a9a6"
AORH = "#f0c8c2"
AORD = "#9a4e55"
AORX = "#6b2f3a"
PT1  = "#ac6672"
PT2  = "#c68c92"
PT3  = "#dcb0b1"
PT0  = "#7a3b4b"
PTX  = "#542433"
VEN  = "#7285b0"
VENL = "#9db0d0"
VEND = "#4a5c8c"
VENX = "#303d61"
MARK = "#00ff00"

art = new_canvas(W, H, name="output")
sil = new_canvas(W, H, name="sil")

# ---------------- geometry ----------------
BODY = ("M14 30 C13 22 21 19 31 19 C42 19 50 26 51 35 "
        "C52 45 44 54 33 58 C30 59 27 60 25 57 "
        "C19 51 15 40 14 33 Z")
BASE = ("M18 31 C17 24 22 18 29 17 C36 15 45 17 49 20 "
        "C51 23 52 28 52 32 L18 32 Z")

AO_A = ((36, 32), (35, 22), (36, 11), (42, 9))    # ascending aorta + left arch
AO_B = ((42, 9), (49, 9), (50, 15), (50, 27))     # right arch + descending
PT_C = ((30, 34), (28, 26), (27, 18), (34, 16))   # pulmonary trunk
SV_C = ((19, 28), (17, 21), (17, 12), (19, 5))    # superior vena cava
BRANCH = ((36, 3, 3, 7), (40, 1, 3, 8), (45, 3, 3, 7))


def cbez(p0, p1, p2, p3, t):
    mt = 1.0 - t
    x = (mt**3)*p0[0] + 3*mt*mt*t*p1[0] + 3*mt*t*t*p2[0] + (t**3)*p3[0]
    y = (mt**3)*p0[1] + 3*mt*mt*t*p1[1] + 3*mt*t*t*p2[1] + (t**3)*p3[1]
    return x, y


def stroke_c(cv, pts, r, colour, dx=0.0, dy=0.0, t0=0.0, t1=1.0, n=180):
    for i in range(n + 1):
        t = t0 + (t1 - t0)*i/n
        x, y = cbez(*pts, t)
        cv.circle(int(round(x + dx)), int(round(y + dy)), r, colour)


def tube_v(cv, pts, width, colour, dx=0, t0=0.0, t1=1.0, n=220):
    for i in range(n + 1):
        t = t0 + (t1 - t0)*i/n
        x, y = cbez(*pts, t)
        cv.rect(int(round(x + dx - (width - 1)/2.0)), int(round(y)), width, 1, colour)


def tube_h(cv, pts, height, colour, dy=0, t0=0.0, t1=1.0, n=220):
    for i in range(n + 1):
        t = t0 + (t1 - t0)*i/n
        x, y = cbez(*pts, t)
        cv.rect(int(round(x)), int(round(y + dy - (height - 1)/2.0)), 1, height, colour)


# ---------------- silhouette ----------------
sil.path(BODY, MARK)
sil.path(BASE, MARK)
for bx, by, bw, bh in BRANCH:
    sil.rect(bx, by, bw, bh, MARK)
stroke_c(sil, AO_A, 3, MARK)
stroke_c(sil, AO_B, 3, MARK)
stroke_c(sil, PT_C, 3, MARK)
stroke_c(sil, SV_C, 3, MARK)

# ---------------- atrial base (behind everything) ----------------
art.path(BASE, PUR)
# right atrium (viewer left): the SVC empties into it
art.ellipse(23, 25, 7, 8, PUR2)
art.ellipse(22, 24, 5, 5, PUR3)
art.ellipse(21, 22, 3, 3, PUR4)
art.ellipse(20, 21, 1, 1, L3)
# left atrium / appendage (viewer right)
art.ellipse(46, 26, 5, 6, PUR2)
art.ellipse(46, 24, 3, 3, PUR3)
art.ellipse(47, 23, 1, 1, PUR4)
art.dither(32, 17, 10, 15, [PUR0, PUR], pattern="bayer4")
art.dither(28, 19, 4, 13, [PUR, PUR2], pattern="bayer4")
art.path("M18 30 C24 33 43 33 52 30 L52 33 L18 33 Z", PUR0)
# pulmonary vein stubs behind the left atrium
art.path("M49 21 C51 20 52 21 52 23", PUR3, fill=False)
art.path("M48 19 C50 18 52 19 52 20", PUR2, fill=False)

# ---------------- ventricular mass ----------------
art.path(BODY, M)
art.ellipse(25, 41, 12, 14, L1)
art.ellipse(24, 39, 8, 10, L2)
art.ellipse(23, 37, 4, 5, L3)
art.ellipse(23, 36, 2, 2, HL)
art.ellipse(41, 42, 9, 11, L1)
art.ellipse(40, 40, 6, 7, L2)
art.ellipse(39, 38, 3, 3, L3)

art.dither(30, 30, 5, 24, [L1, M], pattern="bayer4")
art.dither(15, 46, 8, 12, [M, D1], pattern="bayer4")
art.dither(41, 48, 9, 9, [D1, D2], pattern="bayer4")
art.dither(21, 33, 6, 4, [L2, L1], pattern="bayer4")

# ---------------- atrial lobes, drawn over the muscle above the groove ----------------
# right atrium (viewer left): the superior vena cava empties into it
art.ellipse(21, 27, 7, 7, PUR2)
art.ellipse(20, 26, 5, 5, PUR3)
art.ellipse(19, 24, 3, 3, PUR4)
art.ellipse(18, 23, 1, 1, L3)
art.dither(25, 22, 4, 11, [PUR2, PUR], pattern="bayer4")
# left atrium and appendage (viewer right)
art.ellipse(47, 28, 5, 6, PUR2)
art.ellipse(47, 26, 3, 3, PUR3)
art.ellipse(48, 25, 1, 1, PUR4)
art.dither(42, 22, 5, 10, [PUR0, PUR], pattern="bayer4")
art.path("M43 23 C45 26 46 30 45 33 L43 33 C44 29 43 26 42 24 Z", PUR)

art.path("M51 40 C51 50 43 57 31 59 L25 59 C36 58 47 52 47 40 Z", D1)
art.path("M26 57 C20 51 16 44 16 38 L13 38 C13 47 17 54 24 59 Z", D1)
art.path("M49 42 C49 50 43 56 34 58 L29 59 C41 57 46 51 46 43 Z", D2)
art.path("M30 56 C27 58 25 58 24 57 C26 59 29 58 32 57 Z", D3)

# ---------------- grooves, fat, coronaries ----------------
IV = ((34, 31), (33, 40), (30, 49), (27, 57))
AV = ((14, 31), (23, 40), (38, 38), (51, 31))

tube_h(art, AV, 4, D3)
tube_h(art, AV, 2, FAT2, dy=-1)
tube_h(art, AV, 1, FAT, dy=-1)
tube_h(art, AV, 1, FATD, dy=1, t0=0.05, t1=0.95)

tube_v(art, IV, 4, D3)
tube_v(art, IV, 2, FAT2, dx=-1)
tube_v(art, IV, 1, FAT, dx=-1)
tube_v(art, IV, 1, FATD, dx=1, t0=0.02, t1=0.9)

art.path("M31 38 C29 42 27 45 22 48", D4, fill=False)
art.path("M32 45 C30 48 28 50 25 53", D4, fill=False)
art.path("M44 39 C46 43 46 48 42 52", D4, fill=False)
art.path("M42 41 C43 45 42 49 38 54", AORX, fill=False)
art.path("M19 40 C17 43 16 46 16 49", D2, fill=False)
art.path("M27 48 C26 51 25 54 24 56", D4, fill=False)

art.path("M18 34 C21 33 24 34 25 36 C22 37 19 36 18 34 Z", FAT2)
art.path("M43 34 C45 35 46 37 45 39 C43 38 42 36 43 34 Z", FAT2)

# ---------------- great vessels ----------------
for bx, by, bw, bh in BRANCH:            # arch branches
    art.rect(bx, by, 1, bh, AORD)
    art.rect(bx + 1, by, 1, bh, AOR)
    art.rect(bx + 2, by, 1, bh, AORL)

stroke_c(art, AO_B, 3, AORD)             # right arch + descending aorta
stroke_c(art, AO_B, 2, AOR, dx=-1, dy=-1)
stroke_c(art, AO_B, 1, AORL, dx=-1.5, dy=-1.5)
stroke_c(art, AO_B, 0, AORH, dx=-2, dy=-2, t0=0.0, t1=0.42)
stroke_c(art, AO_B, 1, AORX, dx=2, dy=1.5, t0=0.3, t1=1.0)

stroke_c(art, SV_C, 3, VEND)                     # superior vena cava
stroke_c(art, SV_C, 2, VEN, dx=-1, dy=0)
stroke_c(art, SV_C, 1, VENL, dx=-1.4, dy=0)
stroke_c(art, SV_C, 0, VENX, dx=2, dy=0, t0=0.0, t1=0.92)
# it sinks into the right atrium rather than stopping flat
art.dither(16, 28, 7, 3, [VEND, PUR2], pattern="bayer4")
art.dither(17, 30, 6, 2, [PUR2, PUR], pattern="checker")

stroke_c(art, AO_A, 3, AORD)             # ascending aorta + arch apex
stroke_c(art, AO_A, 2, AOR, dx=-1, dy=-1)
stroke_c(art, AO_A, 1, AORL, dx=-1.5, dy=-1.5)
stroke_c(art, AO_A, 0, AORH, dx=-2, dy=-2, t0=0.12, t1=0.75)
stroke_c(art, AO_A, 1, AORX, dx=2, dy=1.2, t0=0.0, t1=0.5)

stroke_c(art, PT_C, 4, PTX, dx=1.2, dy=0.8)   # cast shadow on the atrium
stroke_c(art, PT_C, 3, PT0)                   # pulmonary trunk, in front
stroke_c(art, PT_C, 3, PT1, dx=-1, dy=-1)
stroke_c(art, PT_C, 2, PT2, dx=-1.6, dy=-1.4)
stroke_c(art, PT_C, 1, PT3, dx=-2, dy=-2, t0=0.12, t1=0.8)
stroke_c(art, PT_C, 0, PTX, dx=2.4, dy=1.4, t0=0.0, t1=0.68)

# contact shadows
art.path("M25 32 C28 34 31 34 34 33 L34 35 C30 36 26 35 25 34 Z", D4)
art.path("M19 29 C21 31 23 31 25 30 L25 32 C22 33 20 32 19 31 Z", PUR0)

# wet specular flecks on the muscle and the vessels
art.set(22, 35, HL)
art.set(21, 36, HL)
art.set(38, 37, HL)
art.set(20, 22, PUR4)
art.dither(19, 34, 5, 3, [L3, L2], pattern="bayer4")
art.dither(36, 36, 4, 3, [L3, L2], pattern="bayer4")

# ---------------- mask to silhouette ----------------
mark_idx = sil.color(MARK)
inside = [[sil.get(x, y) == mark_idx for x in range(W)] for y in range(H)]
for y in range(H):
    for x in range(W):
        if not inside[y][x]:
            art.set(x, y, None)

# ---------------- rim shading + outline ----------------
pal = {p["index"]: tuple(p["rgba"]) for p in art.palette()}


def shade(x, y, f):
    i = art.get(x, y)
    if i is None:
        return
    r, g, b, a = pal[i]
    if a == 0:
        return
    art.set(x, y, (int(r*f), int(g*f), int(b*f), a))


def out_of(x, y):
    return x < 0 or y < 0 or x >= W or y >= H or not inside[y][x]


for y in range(H):
    for x in range(W):
        if not inside[y][x]:
            continue
        l, r_, u, d = out_of(x-1, y), out_of(x+1, y), out_of(x, y-1), out_of(x, y+1)
        if (l and r_) or (u and d):
            continue                      # too thin to shade, keep the colour
        if l or r_ or u or d:
            shade(x, y, 0.72)
        elif out_of(x+2, y) or out_of(x, y+2) or out_of(x-2, y):
            shade(x, y, 0.88)

art.outline(OUT)

print(art.stats_text())
view(art)
finish(art)
