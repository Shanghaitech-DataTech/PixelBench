from pixelbench_api import *

c = new_canvas(32, 32, name="factory")

# ---------------------------------------------------------------- palette ---
K  = c.color("#191d2e", "outline")
D  = c.color("#7b3427", "brick_dark")
B  = c.color("#a84832", "brick")
L  = c.color("#c9694a", "brick_light")
H  = c.color("#e08d63", "brick_hi")
Rd = c.color("#2b3450", "roof_dark")
Rm = c.color("#44517a", "roof_mid")
Rl = c.color("#6a79a4", "roof_light")
Md = c.color("#3d4a68", "metal_dark")
Mm = c.color("#74849f", "metal")
Ml = c.color("#b9c7dd", "metal_light")
Yl = c.color("#ffd75e", "glow")
Or = c.color("#ef9330", "glow_deep")
Gm = c.color("#4a5470", "ground_mid")
Gd = c.color("#252b3d", "ground_dark")
Sm = c.color("#7e8aa3", "smoke_mid")
Sl = c.color("#b6c1d4", "smoke_light")


# ---------------------------------------------------------------- helpers ---
def block(x0, y0, x1, y1):
    """Dark silhouette block used to build the outline of a volume."""
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, K)


def brick_wall(x0, y0, x1, y1, top_shadow=True):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, B)
    for y in range(y0, y1 + 1):
        row = y - y0
        if row % 4 == 3:
            c.line(x0, y, x1, y, D)
        else:
            off = 2 if (row // 4) % 2 else 0
            for x in range(x0 + off, x1 + 1, 4):
                c.set(x, y, D)
    if top_shadow:
        c.line(x0, y0, x1, y0, Rd)
    c.line(x0, y0, x0, y1, L)
    c.line(x1, y0, x1, y1, D)


def roof_slab(x0, y0, x1, y1):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, Rm)
    c.line(x0, y0, x1, y0, Rl)
    c.line(x0, y1, x1, y1, Rd)


def window(x0, y0, x1, y1):
    """Glowing window; dark frame already provided by the silhouette block."""
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, Or)
    c.rect(x0, y0, x1 - x0 + 1, max(1, (y1 - y0 + 1) // 2), Yl)


def grille(x0, y0, x1, y1):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, Md)
    for y in range(y0, y1 + 1):
        c.line(x0, y, x1, y, Mm if (y - y0) % 2 == 0 else K)


# ------------------------------------------------------------------ smoke ---
SMOKE = {
    0: (8, 10),
    1: (6, 12),
    2: (5, 14),
    3: (6, 11),
}
for y, (x0, x1) in SMOKE.items():
    c.line(x0, y, x1, y, Sm)
for px, py in ((8, 0), (9, 0), (6, 1), (7, 1), (9, 1)):
    c.set(px, py, Sl)

# --------------------------------------------------------------- chimney ----
block(2, 4, 11, 7)                       # cap silhouette
c.rect(3, 5, 8, 2, Mm)                   # cap body
c.line(3, 5, 10, 5, Ml)                  # cap highlight
c.line(3, 6, 10, 6, Md)
block(3, 7, 10, 14)                      # shaft silhouette
c.rect(4, 8, 6, 7, B)                    # shaft brick
c.line(4, 10, 9, 10, D)                  # mortar course
c.line(4, 8, 4, 14, L)                   # lit left edge
c.line(9, 8, 9, 14, D)                   # shaded right edge
c.set(6, 9, H); c.set(7, 11, D); c.set(5, 12, L)

# ------------------------------------------------------------- main hall ----
block(1, 13, 18, 27)
roof_slab(2, 14, 17, 16)
brick_wall(2, 17, 17, 27)

# roof vent box on the low hall
block(11, 10, 17, 13)
c.rect(12, 11, 5, 2, Md)
c.line(12, 11, 16, 11, Ml)
c.set(13, 12, K); c.set(15, 12, K)

# ----------------------------------------------------------- right block ----
block(18, 8, 30, 27)
roof_slab(19, 9, 29, 11)
brick_wall(19, 12, 29, 27)

# twin roof ventilators on the tall block
for vx in (20, 25):
    block(vx, 4, vx + 4, 8)
    c.rect(vx + 1, 5, 3, 3, Md)
    c.line(vx + 1, 5, vx + 3, 5, Ml)
    c.line(vx + 1, 6, vx + 1, 7, Mm)
    c.line(vx + 3, 6, vx + 3, 7, Mm)
    c.set(vx + 2, 6, K); c.set(vx + 2, 7, K)

# ------------------------------------------------------------ wall detail ---
# low hall: roll-up gate + window + wall grille
block(3, 19, 10, 27)
c.rect(4, 20, 6, 6, Md)
for y in range(20, 26):
    c.line(4, y, 9, y, Mm if y % 2 == 0 else Md)
c.line(4, 20, 4, 25, Ml)
c.line(9, 20, 9, 25, K)
c.rect(4, 26, 6, 1, Yl)                  # light spilling from under the gate

block(12, 18, 16, 22)
window(13, 19, 15, 21)

block(11, 23, 17, 27)
grille(12, 24, 16, 26)

# tall block: two lit windows, service door, louvered vent
block(21, 13, 24, 18)
window(22, 14, 23, 17)
c.line(22, 16, 23, 16, K)

block(26, 13, 29, 18)
window(27, 14, 28, 17)
c.line(27, 16, 28, 16, K)

block(20, 20, 24, 27)
c.rect(21, 21, 3, 6, Md)
c.line(21, 21, 23, 21, Mm)
c.set(23, 24, Yl)

block(25, 20, 29, 24)
grille(26, 21, 28, 23)

# --------------------------------------------------------------- plinth -----
block(1, 27, 30, 30)
c.rect(2, 28, 28, 1, Gm)
c.rect(2, 29, 28, 1, Gd)
for x in (5, 11, 17, 23, 28):
    c.set(x, 28, Gd)

view(c)
print(c.matrix_text(region=(18, 8, 30, 28)))
save("factory", c, indexed=True)
finish(c)
