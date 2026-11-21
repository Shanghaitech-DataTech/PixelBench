# ===============================================================
#  blue-cloak-girl-mage  -  64x64 anime RPG sprite
#  full body, front facing, relaxed pose, glowing amber staff
#  technique: body layer + 5x offset-stamped silhouette layer
#             flattened  ->  clean 1px outline ring, no eaten detail
# ===============================================================
try:
    from pixelbench_api import *
except Exception:
    pass

from types import SimpleNamespace

SPEC = {
    "OUT":      "#161028",   # silhouette outline
    "SKIN":     "#ffdcc5",
    "SKIN_SH":  "#e8a987",
    "BLUSH":    "#ffb0a0",
    "MOUTH":    "#d97f6f",
    "HAIR":     "#ffd98a",   # blonde
    "HAIR_SH":  "#dca75c",
    "HAIR_HI":  "#fff0c4",
    "EYE":      "#ff9d3c",   # amber eyes (matches staff)
    "EYE_DK":   "#b35a14",
    "WHITE":    "#ffffff",   # boots
    "WHITE_SH": "#c9d2e4",
    "CREAM":    "#f6ecd4",   # dress
    "CREAM_SH": "#dcc9a4",
    "CLOAK":    "#35497f",   # dark blue cloak
    "CLOAK_L":  "#5570b0",
    "CLOAK_D":  "#222e5a",
    "GOLD":     "#f0c05a",
    "GOLD_D":   "#b8862e",
    "WOOD":     "#8a5a33",
    "WOOD_D":   "#5e3a1f",
    "AMBER":    "#ffb347",
    "AMBER_L":  "#ffdf8a",
    "AMBER_C":  "#fff6cf",
    "SHADOW":   "#14102480",
}

body = new_canvas(64, 64, None, "body")
PAL = SimpleNamespace(**{k: body.color(v, k) for k, v in SPEC.items()})


class _Flat:
    """Every colour requested becomes the outline colour."""
    def __getattr__(self, name):
        return PAL.OUT


FLAT = _Flat()


def draw_char(cv, C, dx=0, dy=0):
    X = lambda x: x + dx
    Y = lambda y: y + dy
    R = cv.rect; S = cv.set; L = cv.line; P = cv.poly; E = cv.ellipse

    # ---------- staff (right side, resting on the ground) ----------
    R(X(43), Y(11), 3, 51, C.WOOD)          # shaft x43-45, y11-61
    R(X(45), Y(11), 1, 51, C.WOOD_D)
    R(X(42), Y(59), 5, 3, C.GOLD_D)         # ferrule
    R(X(42), Y(9), 5, 2, C.GOLD)            # gem collar
    # gem: hand-pixelled 7x7 diamond, x41-47 / y2-8
    for y, x0, w in ((2, 44, 1), (3, 43, 3), (4, 42, 5), (5, 41, 7),
                     (6, 42, 5), (7, 43, 3), (8, 44, 1)):
        R(X(x0), Y(y), w, 1, C.AMBER)
    R(X(44), Y(2), 1, 1, C.AMBER_L)         # lit upper-left facet
    R(X(43), Y(3), 2, 1, C.AMBER_L)
    R(X(42), Y(4), 3, 1, C.AMBER_L)
    R(X(41), Y(5), 4, 1, C.AMBER_L)
    R(X(43), Y(4), 2, 2, C.AMBER_C)         # hot core
    S(X(46), Y(6), C.EYE_DK)                # dark lower-right facet
    S(X(45), Y(7), C.EYE_DK)
    S(X(43), Y(3), C.WHITE)                 # sparkle

    # ---------- back hair ----------
    E(X(29), Y(11), 8, 9, C.HAIR)           # x21-37, y2-19
    R(X(24), Y(17), 10, 3, C.HAIR_SH)       # hair behind the neck

    # ---------- cloak (A-line) ----------
    P([(X(22), Y(20)), (X(36), Y(20)), (X(40), Y(44)), (X(18), Y(44))], C.CLOAK)
    L(X(24), Y(23), X(22), Y(42), C.CLOAK_D)   # fold
    L(X(34), Y(23), X(36), Y(42), C.CLOAK_D)   # fold

    # ---------- dress panel ----------
    P([(X(26), Y(20)), (X(32), Y(20)), (X(33), Y(43)), (X(25), Y(43))], C.CREAM)
    R(X(26), Y(22), 1, 19, C.GOLD)          # trim
    R(X(32), Y(22), 1, 19, C.GOLD)
    R(X(25), Y(41), 9, 2, C.GOLD)           # hem
    R(X(25), Y(30), 9, 1, C.CREAM_SH)       # shadow under the belt

    # ---------- belt ----------
    R(X(23), Y(28), 13, 1, C.GOLD)
    R(X(23), Y(29), 13, 1, C.GOLD_D)
    R(X(28), Y(27), 3, 4, C.GOLD)           # buckle
    S(X(29), Y(28), C.GOLD_D)
    S(X(29), Y(29), C.GOLD_D)

    # ---------- sleeves ----------
    P([(X(20), Y(20)), (X(25), Y(20)), (X(23), Y(34)), (X(17), Y(34))], C.CLOAK)
    L(X(25), Y(21), X(23), Y(33), C.CLOAK_D)
    P([(X(33), Y(20)), (X(38), Y(20)), (X(41), Y(34)), (X(35), Y(34))], C.CLOAK)
    L(X(33), Y(21), X(35), Y(33), C.CLOAK_D)
    L(X(37), Y(22), X(39), Y(32), C.CLOAK_L)

    # ---------- cuffs ----------
    R(X(17), Y(35), 7, 2, C.GOLD)
    R(X(35), Y(35), 7, 2, C.GOLD)

    # ---------- hands ----------
    R(X(18), Y(37), 5, 4, C.SKIN)
    R(X(18), Y(40), 5, 1, C.SKIN_SH)
    L(X(20), Y(37), X(20), Y(39), C.SKIN_SH)
    R(X(40), Y(37), 6, 4, C.SKIN)           # grips the staff
    R(X(40), Y(40), 6, 1, C.SKIN_SH)
    L(X(42), Y(37), X(42), Y(39), C.SKIN_SH)
    L(X(44), Y(37), X(44), Y(39), C.SKIN_SH)

    # ---------- legs ----------
    R(X(24), Y(45), 3, 9, C.SKIN)
    R(X(26), Y(45), 1, 9, C.SKIN_SH)
    R(X(32), Y(45), 3, 9, C.SKIN)
    R(X(32), Y(45), 1, 9, C.SKIN_SH)

    # ---------- white boots ----------
    R(X(23), Y(54), 5, 8, C.WHITE)
    R(X(23), Y(55), 5, 1, C.WHITE_SH)
    R(X(27), Y(54), 1, 8, C.WHITE_SH)
    R(X(23), Y(61), 5, 1, C.WHITE_SH)
    R(X(31), Y(54), 5, 8, C.WHITE)
    R(X(31), Y(55), 5, 1, C.WHITE_SH)
    R(X(31), Y(54), 1, 8, C.WHITE_SH)
    R(X(31), Y(61), 5, 1, C.WHITE_SH)

    # ---------- neck ----------
    R(X(27), Y(15), 4, 5, C.SKIN)
    R(X(27), Y(18), 4, 1, C.SKIN_SH)

    # ---------- collar ----------
    P([(X(24), Y(19)), (X(34), Y(19)), (X(37), Y(22)), (X(21), Y(22))], C.CLOAK_L)
    R(X(28), Y(20), 3, 1, C.GOLD)           # clasp

    # ---------- face ----------
    E(X(29), Y(11), 6, 6, C.SKIN)           # x23-35, y5-16

    # ---------- bangs ----------
    P([(X(21), Y(9)), (X(23), Y(5)), (X(26), Y(3)), (X(29), Y(2)), (X(32), Y(3)),
       (X(35), Y(5)), (X(37), Y(9)), (X(35), Y(10)), (X(33), Y(7)), (X(31), Y(10)),
       (X(29), Y(7)), (X(27), Y(10)), (X(25), Y(7)), (X(23), Y(10))], C.HAIR)
    R(X(26), Y(4), 7, 1, C.HAIR_HI)
    R(X(25), Y(5), 9, 1, C.HAIR_HI)

    # ---------- side locks ----------
    R(X(20), Y(6), 4, 16, C.HAIR)
    R(X(23), Y(7), 1, 14, C.HAIR_SH)
    R(X(21), Y(22), 2, 1, C.HAIR)
    R(X(35), Y(6), 4, 16, C.HAIR)
    R(X(35), Y(7), 1, 14, C.HAIR_SH)
    R(X(36), Y(22), 2, 1, C.HAIR)

    # ---------- eyes ----------
    R(X(24), Y(10), 4, 1, C.OUT)            # lash
    R(X(31), Y(10), 4, 1, C.OUT)
    R(X(24), Y(11), 4, 2, C.EYE)
    R(X(31), Y(11), 4, 2, C.EYE)
    R(X(24), Y(13), 4, 1, C.EYE_DK)
    R(X(31), Y(13), 4, 1, C.EYE_DK)
    S(X(26), Y(11), C.WHITE)
    S(X(33), Y(11), C.WHITE)

    # ---------- nose / mouth / blush ----------
    S(X(29), Y(14), C.SKIN_SH)
    R(X(28), Y(15), 3, 1, C.MOUTH)
    R(X(24), Y(14), 2, 1, C.BLUSH)
    R(X(33), Y(14), 2, 1, C.BLUSH)


draw_char(body, PAL)

# ---- silhouette layer: the body stamped at 5 offsets, flat outline ----
sil = new_canvas(64, 64, None, "sil")
for ox, oy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
    draw_char(sil, FLAT, ox, oy)

sprite = flatten([sil, body], name="blue_cloak_girl_mage")

# ---- gem sparkles (1px gap outside the outline ring) ----
for gx, gy in ((41, 2), (47, 2), (38, 5), (50, 5), (41, 8), (47, 8)):
    sprite.set(gx, gy, PAL.AMBER_L)

# ---- warm rim light from the gem, down the figure's right edge ----
W64, H64, BUF = sprite.to_rgba()


def alpha_at(x, y):
    return BUF[(y * W64 + x) * 4 + 3]


def rim(y, x_start, x_end, colour):
    for x in range(x_start, x_end - 1, -1):
        if alpha_at(x, y) == 0:
            continue
        if sprite.get(x, y) == PAL.OUT:
            continue
        sprite.set(x, y, colour)
        return


for y in range(8, 15):          # hair edge, nearest the gem
    rim(y, 39, 35, PAL.AMBER)
for y in range(24, 37):         # sleeve edge
    rim(y, 41, 33, PAL.AMBER_L)
for y in range(37, 41):         # staff hand
    rim(y, 46, 40, PAL.AMBER_L)
for y in range(41, 44):         # cloak skirt edge
    rim(y, 41, 33, PAL.AMBER_L)

# ---- ground shadow ----
sprite.rect(21, 62, 17, 1, PAL.SHADOW)
sprite.rect(41, 62, 7, 1, PAL.SHADOW)

print(sprite.stats_text())
print("--- gem ---")
print(sprite.matrix_text(region=(36, 0, 52, 14), indices=True))
print("--- head ---")
print(sprite.matrix_text(region=(16, 0, 42, 24)))
print("--- torso ---")
print(sprite.matrix_text(region=(14, 18, 50, 46)))
print("--- legs / boots ---")
print(sprite.matrix_text(region=(18, 42, 50, 63)))

save("blue_cloak_girl_mage", sprite)
finish(sprite)
