# Dim Sum Chef - 32x32 front-facing character sprite
# Chef on the left, bamboo steamer of buns held out at the right.
# Blocky parts get outline(); overlapping foreground parts (apron, hands)
# carry hand-drawn dark separator lines so hands / steamer / food /
# clothing stay crisply separated. Everything is flattened at the end.

W = H = 32

OUT     = "#241c26"
HAT_L   = "#fbfbf3"
HAT_S   = "#d2d2c3"
SKIN    = "#f3c49d"
SKIN_S  = "#d99f74"
SKIN_D  = "#a9744e"
HAIR    = "#322c3a"
BLUSH   = "#e58f78"
MOUTH   = "#8c4a45"
JACK    = "#3b4d78"
JACK_S  = "#2a3857"
JACK_L  = "#5a6da0"
APRON   = "#f4f3ea"
APRON_S = "#d5d2c2"
FLOUR   = "#ffffff"
TIE     = "#b8483c"
TIE_S   = "#8d352c"
BAM_L   = "#eec58c"
BAM     = "#c8914d"
BAM_D   = "#96642e"
BUN     = "#fdf3dd"
BUN_S   = "#e0c79e"
PANTS   = "#2c3050"
PANTS_S = "#20243c"
SHOE    = "#1d2033"
SHOE_L  = "#33384f"
STEAM   = "#cfe0ea"


def R(c, col, spec):
    """spec = list of (y, x0, x1) inclusive."""
    for y, x0, x1 in spec:
        c.rect(x0, y, x1 - x0 + 1, 1, col)
    return c


def P(c, col, pts):
    """pts = list of (x, y)."""
    for x, y in pts:
        c.set(x, y, col)
    return c


# ================================================================ legs
legs = new_canvas(W, H, name="legs")
R(legs, PANTS, [(27, 7, 9), (28, 7, 9), (29, 7, 9),
                (27, 11, 13), (28, 11, 13), (29, 11, 13)])
R(legs, PANTS_S, [(29, 7, 9), (29, 11, 13), (28, 9, 9), (28, 13, 13)])
R(legs, SHOE, [(30, 6, 9), (31, 6, 9), (30, 11, 14), (31, 11, 14)])
R(legs, SHOE_L, [(30, 6, 9), (30, 11, 14)])
legs.outline(OUT)

# ================================================================ torso
torso = new_canvas(W, H, name="torso")
R(torso, JACK, [(17, 7, 13),
                (18, 6, 14),
                (19, 5, 15), (20, 5, 15), (21, 5, 15), (22, 5, 15),
                (23, 6, 14), (24, 6, 14)])
R(torso, JACK_L, [(18, 7, 7), (19, 6, 6), (20, 6, 6)])
R(torso, JACK_S, [(18, 13, 13), (19, 14, 14), (20, 14, 14), (21, 14, 14), (22, 14, 14)])
P(torso, FLOUR, [(6, 19), (13, 21), (7, 23)])        # flour on the jacket
torso.outline(OUT)

# ================================================================ apron
apron = new_canvas(W, H, name="apron")
# bib
R(apron, APRON, [(18, 9, 11), (19, 9, 11), (20, 8, 12), (21, 8, 12)])
# waist tie + knot
R(apron, TIE, [(22, 6, 14)])
R(apron, TIE_S, [(22, 13, 14)])
R(apron, TIE, [(23, 9, 11)])
R(apron, TIE_S, [(23, 11, 11)])
# skirt
R(apron, APRON, [(23, 8, 12), (24, 8, 12), (25, 8, 12), (26, 8, 12)])
R(apron, APRON_S, [(26, 8, 12)])
R(apron, APRON, [(26, 9, 11)])
# flour dust (grey specks read on the white apron)
P(apron, APRON_S, [(9, 19), (11, 20), (9, 24), (11, 25), (10, 23), (8, 25), (12, 24),
                   (10, 18), (12, 21), (8, 23)])
# hand-drawn silhouette separators
P(apron, OUT, [(8, 18), (12, 18), (8, 19), (12, 19),
               (7, 20), (13, 20), (7, 21), (13, 21),
               (7, 23), (13, 23), (7, 24), (13, 24), (7, 25), (13, 25),
               (7, 26), (13, 26)])
# ================================================================ collar
collar = new_canvas(W, H, name="collar")
R(collar, TIE, [(18, 9, 11)])
P(collar, TIE_S, [(11, 18)])

# ================================================================ arms
armL = new_canvas(W, H, name="armL")
R(armL, JACK, [(17, 2, 6), (18, 2, 6), (19, 2, 6)])
R(armL, JACK_L, [(18, 3, 3), (19, 3, 3)])
R(armL, JACK_S, [(20, 2, 6)])                        # sleeve end shadow
R(armL, "#e9e6da", [(21, 2, 6), (22, 2, 6)])         # cuff (wrist line below)
armL.outline(OUT)

armR = new_canvas(W, H, name="armR")
R(armR, JACK, [(17, 14, 16), (18, 14, 16), (19, 14, 16), (20, 14, 16)])
R(armR, JACK_L, [(18, 14, 14), (19, 14, 14)])
R(armR, JACK_S, [(17, 16, 16), (18, 16, 16), (19, 16, 16), (20, 16, 16)])
R(armR, "#e9e6da", [(17, 17, 18), (18, 17, 18), (19, 17, 18), (20, 17, 18)])
P(armR, OUT, [(13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16),
              (13, 21), (14, 21), (15, 21), (16, 21), (17, 21), (18, 21),
              (13, 17), (13, 18), (13, 19), (13, 20)])

# ================================================================ head + hat
head = new_canvas(W, H, name="head")
# chef hat
R(head, HAT_L, [(0, 7, 13), (1, 5, 15), (2, 4, 16), (3, 4, 16), (4, 5, 15),
                (5, 6, 14), (6, 6, 14)])
R(head, HAT_S, [(2, 15, 16), (3, 15, 16), (4, 14, 15), (5, 6, 14), (6, 6, 14),
                (1, 14, 15), (0, 12, 13)])
R(head, HAT_L, [(5, 8, 12)])
R(head, HAT_S, [(1, 8, 8), (2, 8, 8), (3, 8, 8), (1, 12, 12), (2, 12, 12), (3, 12, 12)])
# hair
R(head, HAIR, [(7, 7, 13), (8, 6, 7), (8, 13, 14), (9, 6, 6), (9, 14, 14),
               (10, 6, 6), (10, 14, 14), (11, 6, 6), (11, 14, 14)])
# face
R(head, SKIN, [(8, 8, 12), (9, 7, 13), (10, 7, 13), (11, 7, 13), (12, 7, 13),
               (13, 7, 13), (14, 7, 13), (15, 8, 12)])
R(head, SKIN_S, [(15, 8, 12)])                       # jaw shadow
R(head, HAIR, [(10, 8, 9), (11, 8, 9), (10, 11, 12), (11, 11, 12)])   # eyes
R(head, SKIN_S, [(12, 10, 10)])                      # nose
R(head, MOUTH, [(13, 9, 11)])
P(head, MOUTH, [(8, 12), (12, 12)])                  # smile corners
# neck
R(head, SKIN_D, [(16, 9, 11), (17, 9, 11)])
head.outline(OUT)


# ================================================================ buns
def bun(name, cx, cy):
    b = new_canvas(W, H, name=name)
    b.circle(cx, cy, 2, BUN)
    P(b, BUN_S, [(cx + 1, cy + 1), (cx + 2, cy + 1), (cx, cy + 2), (cx + 1, cy + 2),
                 (cx - 1, cy + 2), (cx + 2, cy)])
    P(b, FLOUR, [(cx - 1, cy - 1)])
    P(b, BUN_S, [(cx, cy - 1), (cx - 1, cy)])         # pleat swirl
    b.outline(OUT)
    return b


bun_l = bun("bun_l", 21, 14)
bun_r = bun("bun_r", 29, 14)
bun_m = bun("bun_m", 25, 13)

# ================================================================ steamer
st = new_canvas(W, H, name="steamer")
R(st, BAM_L, [(16, 20, 30), (17, 19, 31)])
R(st, BAM_D, [(18, 19, 31)])
R(st, BAM,   [(19, 19, 31), (20, 19, 31), (21, 19, 31), (22, 19, 31), (23, 19, 31)])
R(st, BAM_L, [(21, 19, 31)])
R(st, BAM_D, [(23, 19, 31), (24, 19, 31)])
R(st, BAM,   [(24, 20, 30)])
R(st, BAM_D, [(25, 21, 29)])
# vertical bamboo weave ticks
P(st, BAM_D, [(24, 19), (24, 20), (28, 19), (28, 20), (24, 22), (26, 22), (28, 22)])
P(st, BAM_L, [(22, 21), (26, 21), (30, 21)])
st.outline(OUT)

# ================================================================ hands
handL = new_canvas(W, H, name="handL")
R(handL, SKIN, [(23, 3, 5), (24, 3, 5), (25, 3, 5)])
R(handL, SKIN_S, [(23, 5, 5), (24, 5, 5), (25, 4, 5)])
P(handL, OUT, [(2, 23), (2, 24), (2, 25), (6, 23), (6, 24), (6, 25),
               (2, 26), (3, 26), (4, 26), (5, 26), (6, 26)])

handR = new_canvas(W, H, name="handR")
R(handR, SKIN, [(17, 19, 21), (18, 19, 21), (19, 19, 21), (20, 19, 21), (21, 19, 21)])
R(handR, SKIN_S, [(17, 21, 21), (18, 21, 21), (19, 21, 21), (20, 21, 21), (21, 19, 21)])
P(handR, OUT, [(19, 16), (20, 16), (21, 16),
               (18, 17), (18, 18), (18, 19), (18, 20), (18, 21),
               (22, 17), (22, 18), (22, 19), (22, 20), (22, 21),
               (19, 22), (20, 22), (21, 22)])

# ================================================================ steam
steam = new_canvas(W, H, name="steam")
P(steam, STEAM, [(22, 10), (21, 9), (21, 8), (22, 7), (22, 6), (21, 5)])
P(steam, STEAM, [(28, 9), (29, 8), (29, 7), (28, 6), (28, 5), (29, 4)])
P(steam, STEAM, [(25, 8), (25, 7), (26, 6)])

# ================================================================ flatten
layers = [legs, torso, apron, collar, armL, armR, head,
          bun_l, bun_r, bun_m, st, handL, handR, steam]
result = flatten(layers, name="dimsum_chef")

print(result.stats_text())
view(result, scale=12, margin=1)
save("dimsum_chef", result, indexed=True)
finish(result)
