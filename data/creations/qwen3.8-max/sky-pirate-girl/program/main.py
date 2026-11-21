# Sky Pirate Girl - 64x64 anime style character portrait
W = H = 64

# ---------------- palette ----------------
INK    = "#1b1424"
INK2   = "#3a2c46"

SKIN   = "#f7d0aa"
SKIN_L = "#ffe7cd"
SKIN_S = "#dda87f"
SKIN_D = "#b3785a"
BLUSH  = "#e88f7a"

HAIR_L = "#f8c479"
HAIR   = "#d3843c"
HAIR_S = "#a05a26"
HAIR_D = "#6d3714"

NAVY   = "#2e4076"
NAVY_L = "#4a63a8"
NAVY_S = "#1d2a4e"
NAVY_D = "#121a33"

GOLD   = "#e6b34c"
GOLD_S = "#a97a2b"

RED    = "#d8403a"
RED_L  = "#f4705f"
RED_S  = "#9d2521"
RED_D  = "#6d1715"

GLASS  = "#8fdcea"
GLASS_L= "#e2fbff"
GLASS_S= "#4a9cb6"

EYE_W  = "#f6fbff"
IRIS   = "#3aa3bd"
IRIS_L = "#8fe2ee"
IRIS_D = "#1b5f79"

SKY    = ["#10264a", "#193763", "#234d7e", "#33699c", "#4d88b6",
          "#72a9cf", "#9dc9e2", "#c6e2f1"]
CLOUD  = "#e6f2fa"
CLOUD_S= "#a8c9e2"
HAZE   = "#8fb8d8"


def poly(c, pts, col):
    d = "M " + " L ".join("%d,%d" % (x, y) for x, y in pts) + " Z"
    return c.path(d, col, fill=True)


def pline(c, pts, col):
    d = "M " + " L ".join("%d,%d" % (x, y) for x, y in pts)
    return c.path(d, col, fill=False)


# ================= BACKGROUND =================
bg = new_canvas(W, H, name="bg")
step = H // len(SKY)
for i, col in enumerate(SKY):
    y0 = i * step
    y1 = (i + 1) * step if i + 1 < len(SKY) else H
    bg.rect(0, y0, W, y1 - y0, col)
for i in range(len(SKY) - 1):
    y = (i + 1) * step
    bg.dither(0, y - 1, W, 2, [SKY[i], SKY[i + 1]], "bayer4")

# clouds
def cloud(c, cx, cy, rx, ry):
    c.ellipse(cx, cy, rx, ry, CLOUD_S)
    c.ellipse(cx, cy - 1, rx, ry, CLOUD)
    c.ellipse(cx - rx // 2, cy - 2, max(1, rx // 2), max(1, ry), CLOUD)
    c.ellipse(cx + rx // 2, cy - 1, max(1, rx // 2), max(1, ry - 1), CLOUD)
    c.rect(cx - rx, cy + ry - 1, rx * 2 + 1, 2, CLOUD_S)

cloud(bg, 53, 9, 8, 3)
cloud(bg, 7, 40, 7, 3)
cloud(bg, 57, 46, 6, 2)
cloud(bg, 12, 14, 5, 2)

# distant airship silhouette
bg.ellipse(8, 28, 6, 2, HAZE)
poly(bg, [(1, 27), (3, 25), (3, 31), (1, 29)], HAZE)
poly(bg, [(7, 25), (10, 25), (9, 26), (8, 26)], HAZE)
bg.rect(6, 30, 4, 1, HAZE)

# ================= CHARACTER =================
ch = new_canvas(W, H, name="char")

# ---- back hair mass (behind everything) ----
ch.ellipse(30, 21, 16, 15, HAIR_S)
poly(ch, [(16, 26), (18, 38), (23, 46), (30, 49), (37, 46), (42, 38), (44, 26)], HAIR_S)

# ---- wind-swept mass streaming to the right ----
ch.path("M 34,6 Q 48,2 58,8 Q 64,14 62,22 Q 60,30 52,36 Q 45,41 38,43 "
        "L 36,24 Z", HAIR_S, fill=True)
poly(ch, [(56, 7), (63, 4), (60, 11)], HAIR_S)
poly(ch, [(60, 16), (63, 15), (61, 21)], HAIR_S)
poly(ch, [(56, 30), (63, 32), (55, 35)], HAIR_S)
poly(ch, [(48, 38), (56, 44), (46, 42)], HAIR_S)
ch.path("M 40,8 Q 52,6 58,12 Q 50,10 42,12 Z", HAIR, fill=True)
ch.path("M 44,16 Q 54,16 60,20 Q 52,20 45,20 Z", HAIR, fill=True)
ch.path("M 44,26 Q 53,27 58,31 Q 51,30 44,30 Z", HAIR, fill=True)
pline(ch, [(40, 12), (52, 10)], HAIR_D)
pline(ch, [(42, 21), (56, 19)], HAIR_D)
pline(ch, [(42, 29), (54, 31)], HAIR_D)
pline(ch, [(40, 36), (48, 40)], HAIR_D)
# loose flying strands
ch.path("M 50,4 Q 58,2 63,6", HAIR, fill=False)
ch.path("M 52,40 Q 58,44 62,50", HAIR_S, fill=False)

# ---- collar behind neck ----
poly(ch, [(19, 52), (20, 40), (26, 37), (34, 37), (40, 40), (41, 52)], NAVY_S)

# ---- neck ----
poly(ch, [(25, 36), (35, 36), (36, 48), (24, 48)], SKIN_S)
poly(ch, [(25, 36), (35, 36), (35, 42), (25, 42)], SKIN_D)

# ---- coat body ----
poly(ch, [(4, 64), (6, 56), (11, 50), (18, 46), (26, 44), (34, 44),
          (43, 47), (51, 51), (56, 57), (58, 64)], NAVY)
poly(ch, [(11, 50), (18, 46), (26, 44), (27, 48), (18, 52), (12, 57), (8, 64), (4, 64), (6, 56)], NAVY_L)
poly(ch, [(43, 47), (51, 51), (56, 57), (58, 64), (48, 64), (46, 55)], NAVY_S)
poly(ch, [(30, 56), (34, 64), (26, 64), (28, 58)], NAVY_S)   # centre opening shadow
# epaulette on lit shoulder
poly(ch, [(7, 54), (14, 50), (18, 53), (11, 57)], GOLD)
for (x, y) in [(8, 57), (10, 58), (12, 59)]:
    ch.set(x, y, GOLD_S)
# buttons
ch.set(25, 61, GOLD)
ch.set(33, 62, GOLD)
ch.set(25, 62, GOLD_S)
ch.set(33, 63, GOLD_S)

# ---- scarf ----
poly(ch, [(20, 45), (26, 50), (34, 50), (40, 45), (43, 49), (42, 55),
          (34, 58), (25, 57), (19, 52)], RED)
poly(ch, [(20, 45), (26, 50), (34, 50), (40, 45), (41, 47), (34, 52), (25, 52), (19, 48)], RED_L)
poly(ch, [(19, 52), (25, 57), (34, 58), (42, 55), (42, 57), (33, 60), (23, 58), (18, 54)], RED_S)
# scarf tails streaming in the wind
ch.path("M 40,48 Q 52,46 63,52 Q 53,54 45,54 Q 41,53 39,51 Z", RED, fill=True)
ch.path("M 40,48 Q 52,46 63,52 Q 55,52 47,51 Q 42,50 40,49 Z", RED_L, fill=True)
ch.path("M 38,54 Q 50,55 60,61 Q 50,60 43,60 Q 39,58 37,56 Z", RED_S, fill=True)
ch.path("M 38,54 Q 48,55 57,59 Q 48,58 42,58 Q 39,57 37,55 Z", RED, fill=True)
# scarf knot
poly(ch, [(36, 47), (42, 46), (44, 52), (38, 54)], RED)
poly(ch, [(36, 47), (42, 46), (42, 49), (37, 50)], RED_L)
poly(ch, [(38, 51), (44, 52), (38, 54)], RED_S)

# ---- face ----
FACE = [(19, 14), (30, 12), (39, 14), (42, 21), (42, 28), (40, 34),
        (35, 40), (29, 42), (24, 41), (20, 37), (18, 31), (18, 22)]
poly(ch, FACE, SKIN)
# right side (far from light) shading
poly(ch, [(38, 15), (42, 21), (42, 28), (40, 34), (35, 40), (29, 42),
          (31, 39), (36, 33), (38, 26)], SKIN_S)
poly(ch, [(40, 26), (42, 27), (41, 32), (38, 37), (36, 36), (39, 31)], SKIN_D)
# left highlight
poly(ch, [(19, 22), (22, 17), (26, 15), (24, 20), (21, 26), (19, 30)], SKIN_L)
# chin / jaw line
pline(ch, [(20, 37), (24, 41), (29, 42), (34, 40)], INK2)

# ---- ear ----
poly(ch, [(41, 28), (44, 27), (45, 31), (42, 34)], SKIN_S)

# ---- eyes ----
# far eye (viewer left)
poly(ch, [(19, 24), (26, 23), (27, 25), (26, 29), (20, 29)], EYE_W)
ch.ellipse(23, 26, 2, 2, IRIS)
ch.set(23, 26, INK)
ch.set(23, 27, IRIS_D)
ch.set(21, 24, GLASS_L)
poly(ch, [(18, 23), (27, 22), (27, 23), (18, 24)], INK)
pline(ch, [(20, 29), (26, 29)], INK2)
# near eye (viewer right)
poly(ch, [(30, 24), (38, 23), (39, 26), (38, 30), (31, 30)], EYE_W)
ch.ellipse(34, 26, 3, 3, IRIS)
poly(ch, [(31, 26), (37, 26), (37, 29), (31, 29)], IRIS_D)
ch.set(34, 26, INK)
ch.set(33, 26, INK)
ch.set(32, 24, GLASS_L)
ch.set(33, 23, GLASS_L)
ch.set(36, 28, IRIS_L)
poly(ch, [(29, 22), (40, 21), (40, 22), (29, 23)], INK)
pline(ch, [(31, 30), (38, 30)], INK2)
ch.set(40, 25, INK)
# lash flicks
ch.set(18, 22, INK)
ch.set(40, 23, INK)

# ---- brows drawn later, over the bangs ----

# ---- nose ----
ch.set(19, 32, SKIN_D)
ch.set(20, 33, SKIN_D)
ch.set(21, 33, SKIN_S)
ch.set(19, 31, SKIN_L)

# ---- mouth: confident smirk ----
pline(ch, [(22, 36), (25, 37), (28, 36)], INK2)
ch.set(29, 35, INK2)
poly(ch, [(23, 37), (27, 37), (26, 38), (24, 38)], BLUSH)
ch.set(24, 39, SKIN_S)
ch.set(25, 39, SKIN_S)

# ---- blush ----
for (x, y) in [(20, 33), (22, 34), (24, 34)]:
    ch.set(x, y, BLUSH)

# ---- front hair: cap + swept bangs ----
ch.path("M 14,30 Q 12,13 22,6 Q 31,1 41,6 Q 49,12 47,28 L 45,38 L 41,31 "
        "Q 43,24 40,19 L 37,15 L 35,20 L 32,15 L 29,20 L 26,15 L 23,20 "
        "L 20,16 L 18,22 Q 16,27 18,33 L 15,38 Z", HAIR, fill=True)
# hair shadow under the cap edge
ch.path("M 18,22 L 20,16 L 23,20 L 26,15 L 29,20 L 32,15 L 35,20 L 37,15 "
        "L 40,19 L 41,22 L 38,19 L 35,22 L 32,18 L 29,22 L 26,18 L 23,22 "
        "L 20,19 Z", HAIR_S, fill=True)
# side locks in front of ears
poly(ch, [(14, 28), (18, 26), (19, 36), (17, 44), (14, 46), (13, 38)], HAIR)
poly(ch, [(15, 30), (17, 30), (17, 40), (15, 44)], HAIR_S)
poly(ch, [(43, 26), (47, 28), (46, 38), (43, 44), (41, 40), (42, 32)], HAIR)
poly(ch, [(44, 30), (46, 32), (45, 40), (43, 43)], HAIR_S)
# hair highlights
ch.path("M 20,10 Q 27,4 36,6 Q 28,7 23,12 Z", HAIR_L, fill=True)
ch.path("M 17,17 Q 19,11 24,8 Q 20,13 19,19 Z", HAIR_L, fill=True)
ch.path("M 40,10 Q 45,15 45,23 Q 43,16 39,12 Z", HAIR_L, fill=True)
# strand lines
pline(ch, [(24, 8), (30, 6), (37, 8)], HAIR_S)
pline(ch, [(41, 14), (44, 20)], HAIR_S)
# ahoge
ch.path("M 29,5 Q 27,0 21,0 Q 26,3 27,7 Z", HAIR, fill=True)

# ---- front wind locks over the shoulder ----
ch.path("M 40,32 Q 52,36 62,46 Q 52,44 45,45 Q 41,40 39,36 Z", HAIR, fill=True)
ch.path("M 40,32 Q 52,36 62,46 Q 54,42 47,39 Q 42,36 40,33 Z", HAIR_L, fill=True)
ch.path("M 42,40 Q 50,42 58,45 Q 50,44 45,44 Q 43,42 42,41 Z", HAIR_S, fill=True)
ch.path("M 36,40 Q 46,45 53,54 Q 45,50 39,50 Q 37,45 35,43 Z", HAIR_S, fill=True)

# ---- goggles on the forehead ----
# strap
poly(ch, [(12, 15), (18, 12), (18, 16), (12, 19)], HAIR_D)
poly(ch, [(39, 11), (48, 13), (48, 16), (39, 14)], HAIR_D)
poly(ch, [(45, 12), (47, 12), (47, 15), (45, 15)], GOLD_S)
ch.set(46, 13, GOLD)
# far lens rim
ch.ellipse(37, 12, 5, 4, GOLD_S)
ch.ellipse(37, 12, 4, 3, GLASS_S)
ch.ellipse(37, 11, 3, 2, GLASS)
ch.set(36, 10, GLASS_L)
# bridge
poly(ch, [(28, 11), (33, 11), (33, 14), (28, 14)], GOLD_S)
# near lens rim
ch.ellipse(24, 12, 7, 6, GOLD)
ch.ellipse(24, 13, 7, 5, GOLD_S)
ch.ellipse(24, 12, 6, 5, GOLD)
ch.ellipse(24, 12, 5, 4, GLASS_S)
ch.ellipse(24, 11, 4, 3, GLASS)
poly(ch, [(20, 10), (24, 8), (26, 9), (22, 13)], GLASS_L)
ch.set(27, 14, GLASS_L)
# rim shading + outline hints
ch.path("M 18,10 A 7 6 0 0 1 30,10", GOLD_S, fill=False)
pline(ch, [(17, 13), (18, 16), (21, 18)], INK2)
pline(ch, [(31, 13), (30, 16)], INK2)

# ---- brows over the bangs (confident: near brow raised) ----
pline(ch, [(19, 21), (23, 20), (26, 21)], HAIR_D)
pline(ch, [(30, 20), (35, 18), (39, 19)], HAIR_D)

# ---- gold earring ----
ch.set(43, 34, GOLD)
ch.set(43, 35, GOLD_S)

# ================= COMPOSITE =================
ch.outline(INK)
result = flatten([bg, ch], name="sky_pirate_girl")

view(result)
view(result, margin=0)
save("sky_pirate_girl", result)
print(result.stats_text())
finish(result)
