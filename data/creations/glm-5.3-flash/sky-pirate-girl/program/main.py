# ============================================================
#  sky-pirate-girl  --  64x64 pixel art portrait (bust)
#  layers: bg < hair_back < body < head < hair_front < scarf < goggles
# ============================================================
W = H = 64

# ---------------- palette ----------------
OUT      = "#201830"
SKY      = ["#b3e6fb", "#7fc8f0", "#58a8e2", "#3f8bd0", "#2f6fb5"]
CLOUD    = "#ffffff"
CLOUD_SH = "#cfe6f7"
SUN_A    = "#fff0bc"
SUN_B    = "#fffbe2"
SHIP_B   = "#bcd9f2"
SHIP_D   = "#2c4a78"

SKIN    = "#ffd9b6"
SKIN_SH = "#e0a67e"
BLUSH   = "#f7a08c"
MOUTH   = "#a04a48"

HAIR    = "#d99a4e"
HAIR_SH = "#a86b30"
HAIR_HI = "#f6cd85"

EYE    = "#2fa89a"
EYE_D  = "#14524c"
EYE_HI = "#e6fffa"
SCLERA = "#ffffff"

COAT    = "#2c3e6b"
COAT_SH = "#1e2b4d"
COAT_HI = "#42598f"
SHIRT   = "#c2cede"
BRASS   = "#e0b64a"
BRASS_SH = "#a97e2a"

SCARF    = "#d43a3a"
SCARF_SH = "#a02424"
SCARF_HI = "#f06a5a"

STRAP   = "#4a3226"
LENS    = "#8fd8d0"
LENS_HI = "#e8fffb"


# ---------------- background ----------------
def draw_bg(c):
    ys = [0, 14, 26, 38, 50]
    for i, y0 in enumerate(ys):
        y1 = ys[i + 1] if i + 1 < len(ys) else H
        c.rect(0, y0, W, y1 - y0, SKY[i])
    for i in range(len(ys) - 1):
        c.dither(0, ys[i + 1] - 2, W, 4, [SKY[i], SKY[i + 1]], pattern="bayer4")
    c.circle(7, 6, 5, SUN_A)
    c.circle(7, 6, 3, SUN_B)
    # clouds
    c.ellipse(6, 44, 5, 2, CLOUD); c.rect(2, 44, 10, 2, CLOUD); c.rect(3, 46, 8, 1, CLOUD_SH)
    c.ellipse(59, 32, 4, 2, CLOUD); c.rect(55, 32, 9, 2, CLOUD); c.rect(56, 34, 7, 1, CLOUD_SH)
    c.ellipse(53, 59, 6, 3, CLOUD); c.ellipse(59, 57, 4, 3, CLOUD)
    c.rect(47, 58, 16, 3, CLOUD); c.rect(48, 61, 14, 1, CLOUD_SH)
    # distant airship
    c.ellipse(7, 28, 4, 2, SHIP_B)
    c.rect(5, 30, 5, 1, SHIP_D)
    c.poly([(3, 28), (1, 27), (1, 29)], SHIP_D)
    # birds
    for bx, by in ((4, 17), (8, 15)):
        c.set(bx, by, SHIP_D); c.set(bx + 1, by - 1, SHIP_D); c.set(bx + 2, by, SHIP_D)


# ---------------- hair, back (one clean silhouette) ----------------
def draw_hair_back(c):
    c.poly([(16, 24), (16, 17), (20, 10), (27, 5), (35, 4), (43, 5), (50, 9),
            (55, 14), (57, 20), (58, 26), (55, 32), (51, 28), (47, 36), (43, 31),
            (39, 40), (35, 34), (31, 42), (27, 37), (23, 44), (19, 39), (16, 45),
            (14, 38)], HAIR)
    # strand torn loose by the wind
    c.poly([(52, 10), (58, 5), (60, 6), (55, 11)], HAIR)
    # shine + flow shading
    c.path("M 26,10 C 34,8 42,8 49,12", HAIR_HI, fill=False)
    c.path("M 22,13 C 27,11 32,10 37,11", HAIR_HI, fill=False)
    c.path("M 40,12 C 46,13 51,16 54,20", HAIR_SH, fill=False)
    c.path("M 30,14 C 36,15 41,17 45,20", HAIR_SH, fill=False)
    c.path("M 44,22 C 47,24 49,26 50,28", HAIR_SH, fill=False)
    c.path("M 36,26 C 38,30 38,34 38,37", HAIR_SH, fill=False)
    c.path("M 20,18 C 18,24 18,30 20,36", HAIR_SH, fill=False)
    c.path("M 24,20 C 27,24 28,29 28,33", HAIR_SH, fill=False)
    c.outline(OUT)
    # ahoge, drawn after the outline so it keeps its colour
    c.line(30, 5, 34, 1, HAIR)
    c.line(31, 5, 35, 2, HAIR)


# ---------------- body: shoulders, short navy coat ----------------
def draw_body(c):
    c.poly([(10, 63), (11, 56), (14, 51), (19, 48), (24, 47), (32, 47),
            (37, 48), (42, 51), (45, 56), (46, 63)], COAT)
    c.poly([(12, 57), (14, 51), (18, 49), (18, 62), (13, 62)], COAT_HI)
    c.poly([(40, 52), (43, 56), (44, 62), (39, 62), (38, 54)], COAT_SH)
    c.poly([(25, 47), (30, 47), (29, 55), (26, 55)], SHIRT)
    c.poly([(22, 47), (26, 48), (25, 56), (20, 54)], COAT_SH)
    c.poly([(33, 47), (29, 48), (30, 56), (35, 54)], COAT_SH)
    for bx in (22, 31):
        for by in (57, 60):
            c.rect(bx, by, 2, 2, BRASS)
            c.set(bx + 1, by + 1, BRASS_SH)
    c.outline(OUT)
    # the canvas edge counts as transparency, so re-fill the cut rows
    c.rect(10, 62, 37, 2, COAT)
    for px in (10, 46):
        c.set(px, 62, OUT); c.set(px, 63, OUT)


# ---------------- head: neck, face, features ----------------
def draw_head(c):
    c.rect(25, 38, 6, 10, SKIN)                    # neck
    c.ellipse(28, 27, 9, 11, SKIN)                 # face
    c.poly([(21, 32), (26, 39), (32, 33)], SKIN)   # chin
    c.outline(OUT)
    c.rect(22, 23, 14, 1, SKIN_SH)                 # shadow cast by the bangs
    c.rect(36, 26, 1, 6, SKIN_SH)                  # far-side form shadow
    c.rect(26, 40, 4, 1, SKIN_SH)                  # under the chin
    c.set(25, 33, SKIN_SH)                         # nose
    # brows
    c.line(20, 24, 26, 25, HAIR_SH)
    c.line(30, 25, 34, 24, HAIR_SH)
    # left eye (near side, 7 px)
    for x in range(20, 27):
        c.set(x, 27, OUT)
    c.set(20, 28, SCLERA); c.set(21, 28, EYE_HI); c.set(22, 28, EYE)
    c.set(23, 28, EYE_D); c.set(24, 28, EYE_D)
    c.set(25, 28, SCLERA); c.set(26, 28, SCLERA)
    c.set(20, 29, SCLERA); c.set(21, 29, EYE); c.set(22, 29, EYE)
    c.set(23, 29, EYE_D); c.set(24, 29, EYE_D)
    c.set(25, 29, SCLERA); c.set(26, 29, SCLERA)
    c.set(20, 30, SCLERA); c.set(21, 30, EYE); c.set(22, 30, EYE)
    c.set(23, 30, EYE); c.set(24, 30, EYE_D)
    c.set(25, 30, SCLERA); c.set(26, 30, SCLERA)
    for x in range(20, 27):
        c.set(x, 31, SKIN_SH)
    # right eye (far side, 5 px)
    for x in range(30, 35):
        c.set(x, 27, OUT)
    c.set(30, 28, SCLERA); c.set(31, 28, EYE_HI); c.set(32, 28, EYE); c.set(33, 28, EYE_D)
    c.set(34, 28, SCLERA)
    c.set(30, 29, SCLERA); c.set(31, 29, EYE); c.set(32, 29, EYE_D); c.set(33, 29, EYE_D)
    c.set(34, 29, SCLERA)
    c.set(30, 30, SCLERA); c.set(31, 30, EYE); c.set(32, 30, EYE); c.set(33, 30, EYE_D)
    c.set(34, 30, SCLERA)
    for x in range(30, 35):
        c.set(x, 31, SKIN_SH)
    # blush + confident smile
    c.set(21, 34, BLUSH); c.set(22, 34, BLUSH)
    c.set(33, 34, BLUSH); c.set(34, 34, BLUSH)
    c.set(24, 36, MOUTH); c.set(28, 36, MOUTH)
    c.set(25, 37, MOUTH); c.set(26, 37, MOUTH); c.set(27, 37, MOUTH)


# ---------------- hair, front (fringe + locks) ----------------
def draw_hair_front(c):
    # fringe over the forehead; its top edge hides inside the back mass
    c.poly([(19, 13), (23, 10), (29, 9), (35, 11), (38, 15), (38, 20),
            (37, 23), (36, 23), (35, 19), (33, 22), (31, 22), (30, 18),
            (28, 22), (26, 22), (25, 18), (23, 21), (21, 21), (20, 17),
            (18, 16)], HAIR)
    # side locks
    c.poly([(15, 17), (21, 17), (20, 30), (18, 33), (15, 28)], HAIR)
    c.poly([(36, 17), (41, 17), (42, 28), (39, 33), (36, 27)], HAIR)
    # explicit dark edges (no outline() here: it would seam the mass)
    zig = [(38, 20), (37, 23), (36, 23), (35, 19), (33, 22), (31, 22), (30, 18),
           (28, 22), (26, 22), (25, 18), (23, 21), (21, 21), (20, 17)]
    for (ax, ay), (bx, by) in zip(zig, zig[1:]):
        c.line(ax, ay, bx, by, OUT)
    c.line(21, 17, 20, 30, OUT)      # left lock, inner edge
    c.line(36, 17, 36, 27, OUT)      # right lock, inner edge
    # shine
    c.path("M 21,15 C 26,13 32,12 36,14", HAIR_HI, fill=False)
    c.path("M 16,20 C 17,24 18,28 18,31", HAIR_SH, fill=False)
    c.path("M 39,20 C 40,23 40,26 39,30", HAIR_SH, fill=False)


# ---------------- scarf ----------------
def draw_scarf(c):
    c.poly([(21, 46), (24, 43), (32, 43), (35, 46), (34, 50), (22, 50)], SCARF)
    c.rect(25, 44, 8, 1, SCARF_HI)
    c.rect(23, 48, 12, 1, SCARF_SH)
    c.poly([(20, 45), (26, 45), (25, 52), (18, 51)], SCARF)
    c.poly([(23, 45), (26, 45), (25, 52), (22, 51)], SCARF_SH)
    c.poly([(26, 47), (36, 48), (45, 51), (41, 54), (30, 52)], SCARF)
    c.line(29, 51, 40, 52, SCARF_SH)
    c.poly([(43, 53), (52, 56), (58, 61), (50, 59), (42, 56)], SCARF)
    c.line(45, 55, 52, 58, SCARF_SH)
    c.outline(OUT)


# ---------------- goggles ----------------
def draw_goggles(c):
    c.rect(15, 16, 26, 2, STRAP)                 # strap round the head
    for cx in (22, 31):
        c.circle(cx, 14, 3, OUT)                 # rim
        c.circle(cx, 14, 2, BRASS)               # brass ring
        c.rect(cx - 1, 13, 3, 3, LENS)           # teal lens
        c.set(cx - 1, 13, LENS_HI)               # catchlight
    c.set(16, 16, BRASS); c.set(39, 16, BRASS)   # rivets


# ---------------- assemble ----------------
def build():
    bg = new_canvas(W, H, name="bg")
    draw_bg(bg)
    hair_back = new_canvas(W, H, name="hair_back")
    draw_hair_back(hair_back)
    body = new_canvas(W, H, name="body")
    draw_body(body)
    head = new_canvas(W, H, name="head")
    draw_head(head)
    hair_front = new_canvas(W, H, name="hair_front")
    draw_hair_front(hair_front)
    scarf = new_canvas(W, H, name="scarf")
    draw_scarf(scarf)
    acc = new_canvas(W, H, name="goggles")
    draw_goggles(acc)
    return flatten([bg, hair_back, body, head, hair_front, scarf, acc],
                   name="sky-pirate-girl")


# ---------------- text inspection ----------------
SYM = {}


def _rgb(e):
    v = e["rgba"]
    if isinstance(v, dict):
        return v.get("r"), v.get("g"), v.get("b")
    return v[0], v[1], v[2]


def build_syms(canvas):
    m = {}
    for e in canvas.palette():
        r, g, b = _rgb(e)
        m[e["index"]] = SYM.get("#%02x%02x%02x" % (r, g, b), "??")
    return m


def rle(canvas, x0, x1, y0, y1, label=""):
    m = build_syms(canvas)
    print("=== %s ===" % label)
    for y in range(y0, y1 + 1):
        runs = []
        prev = "START"
        start = x0
        for x in range(x0, x1 + 1):
            i = canvas.get(x, y)
            if i != prev:
                if prev != "START":
                    runs.append((start, x - 1, prev))
                prev, start = i, x
        runs.append((start, x1, prev))
        parts = []
        for a, b, i in runs:
            nm = ".." if i is None else m.get(i, "??")
            parts.append(("%d" % a if a == b else "%d-%d" % (a, b)) + nm)
        print("y%02d " % y + " ".join(parts))


for _nm, _hx in list(globals().items()):
    if isinstance(_hx, str) and _hx.startswith("#"):
        SYM[_hx.lower()] = _nm
for _i, _hx in enumerate(SKY):
    SYM[_hx.lower()] = "SK%d" % _i
SYM["#ffffff"] = "WH"      # white is shared by clouds and eye whites

result = build()
print(result.stats_text())
view(result, scale=6)
finish(result)
