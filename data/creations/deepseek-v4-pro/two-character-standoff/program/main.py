from pixelbench_api import *
import math

W = H = 128

# ---------------------------------------------------------------------------
# palettes (shared across all canvases in the drawing)
# ---------------------------------------------------------------------------
bg0       = new_canvas(W, H, background=None, name="bg0")  # just to register colours; real bg below
bg0.color("#131226", "bg0")
bg0.color("#1a1730", "bg1")
bg0.color("#281b3a", "bg2")
bg0.color("#382140", "bg3")
bg0.color("#4a2b46", "horizon")
bg0.color("#0d0c15", "ground")
bg0.color("#181724", "ground_hi")
bg0.color("#07060b", "shadow")
bg0.color("#584163", "moon_halo")
bg0.color("#e9dcc3", "moon")
bg0.color("#141019", "outline")

bg0.color("#c22a2f", "k_red")
bg0.color("#7c161c", "k_red_d")
bg0.color("#e05a5a", "k_red_l")
bg0.color("#a9afba", "k_metal")
bg0.color("#5b616c", "k_metal_d")
bg0.color("#dfe4ec", "k_metal_l")
bg0.color("#d8b25a", "k_gold")
bg0.color("#1d1f26", "k_dark")
bg0.color("#5a3a28", "k_leather")

bg0.color("#2f7d3a", "r_green")
bg0.color("#1c4a24", "r_green_d")
bg0.color("#5cbf68", "r_green_l")
bg0.color("#171a16", "r_dark")
bg0.color("#4a3226", "r_leather")
bg0.color("#e8c4a0", "r_skin")
bg0.color("#ccd2dc", "r_silver")
bg0.color("#8ff0d8", "r_eye")
bg0.color("#c9cbdd", "star")
bg0.color("#e8a04a", "spark")


def thick_line(c, x0, y0, x1, y1, w, col):
    """Draw a thick straight segment as a rotated filled rectangle."""
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy)
    if L < 0.001:
        c.circle(int(x0), int(y0), max(1, int(w)//2), col)
        return
    nx = -dy / L * w / 2.0
    ny = dx / L * w / 2.0
    pts = [
        (round(x0 + nx), round(y0 + ny)),
        (round(x1 + nx), round(y1 + ny)),
        (round(x1 - nx), round(y1 - ny)),
        (round(x0 - nx), round(y0 - ny)),
    ]
    c.poly(pts, col)


def draw_background(c):
    c.rect(0, 0, W, 24, "bg0")
    c.rect(0, 24, W, 24, "bg1")
    c.rect(0, 48, W, 24, "bg2")
    c.rect(0, 72, W, 24, "bg3")
    c.rect(0, 92, W, 4, "horizon")
    c.rect(0, 96, W, 32, "ground")

    # big backlight moon in the central gap
    c.circle(64, 54, 27, "moon_halo")
    c.circle(64, 54, 20, "moon")

    # sparse night-sky stars (kept off the central moon and fighters)
    stars = [
        (12, 8), (26, 6), (40, 10), (52, 6), (76, 8), (88, 5),
        (104, 10), (118, 7), (124, 14), (68, 4), (6, 46), (124, 50),
        (118, 70), (8, 60),
    ]
    for (sx, sy) in stars:
        c.set(sx, sy, "star")
    # a few brighter two-pixel glints
    c.set(26, 7, "star")
    c.set(104, 11, "star")
    c.set(76, 9, "star")

    # small embers/sparks floating in the tense gap between the rivals
    sparks = [(58, 64), (68, 58), (62, 74), (72, 70), (54, 80), (66, 82)]
    for (sx, sy) in sparks:
        c.set(sx, sy, "spark")
        c.set(sx + 1, sy, "spark")

    # perspective lines on the floor
    c.rect(0, 100, W, 2, "ground_hi")
    c.rect(0, 108, W, 2, "ground_hi")
    c.rect(0, 116, W, 2, "ground_hi")

    # contact shadows under the fighters
    c.ellipse(28, 99, 21, 4, "shadow")
    c.ellipse(98, 99, 21, 4, "shadow")


def draw_knight(c):
    # ---- flowing cape (back) ----
    c.poly([(18, 56), (28, 58), (20, 94), (10, 88)], "k_red_d")

    # ---- back leg + boot ----
    c.rect(17, 78, 9, 18, "k_metal_d")
    c.rect(16, 92, 11, 4, "k_red_d")

    # ---- shield on the far (left) side ----
    c.poly([(5, 52), (21, 48), (25, 66), (17, 80), (5, 76)], "k_metal_d")
    c.poly([(7, 54), (19, 50), (22, 64), (15, 76), (7, 73)], "k_metal")
    c.line(10, 56, 18, 66, "k_red")
    c.line(18, 56, 10, 66, "k_red")
    c.circle(14, 61, 2, "k_gold")

    # ---- left arm toward shield ----
    thick_line(c, 20, 58, 12, 62, 4, "k_red_d")

    # ---- torso armour ----
    c.poly([(15, 58), (43, 58), (45, 80), (13, 80)], "k_red")
    c.poly([(19, 60), (39, 60), (41, 72), (17, 72)], "k_red_l")

    # ---- belt ----
    c.rect(13, 78, 32, 4, "k_gold")

    # ---- front leg + boot ----
    c.rect(28, 78, 10, 18, "k_metal")
    c.rect(27, 92, 12, 4, "k_red_d")

    # ---- pauldrons ----
    c.circle(15, 56, 6, "k_red_l")
    c.circle(43, 56, 6, "k_red_l")

    # ---- raised sword arm ----
    thick_line(c, 43, 60, 48, 50, 5, "k_red")
    c.poly([(45, 47), (51, 47), (51, 51), (45, 51)], "k_metal")  # gauntlet

    # ---- sword ----
    c.poly([(46, 16), (50, 16), (50, 46), (46, 46)], "k_metal")
    c.poly([(46, 16), (50, 16), (48, 11)], "k_metal_l")          # tip
    c.rect(43, 46, 10, 3, "k_gold")                              # crossguard
    c.rect(47, 49, 2, 7, "k_leather")                            # grip
    c.circle(48, 57, 2, "k_gold")                                # pommel

    # ---- helmet ----
    c.rect(22, 34, 18, 22, "k_red")
    c.rect(24, 34, 12, 3, "k_red_l")                             # top highlight
    c.rect(34, 42, 7, 5, "k_dark")                               # visor slit
    c.rect(37, 43, 3, 3, "k_metal")                              # visor glint

    # ---- plume ----
    c.poly([(22, 34), (33, 34), (25, 12), (17, 20)], "k_red_l")
    c.poly([(24, 34), (30, 34), (25, 16), (20, 22)], "k_red")


def draw_rogue(c):
    # ---- legs / boots peeking from under cloak ----
    c.rect(88, 78, 9, 18, "r_dark")
    c.rect(99, 78, 9, 18, "r_dark")
    c.rect(87, 91, 11, 5, "r_leather")
    c.rect(98, 91, 11, 5, "r_leather")

    # ---- body cloak ----
    c.poly([(78, 50), (104, 48), (114, 86), (94, 92), (72, 88)], "r_green")
    c.poly([(82, 52), (102, 50), (110, 82), (92, 88), (76, 84)], "r_green_d")
    c.line(104, 50, 112, 84, "r_green_l")
    c.line(78, 52, 74, 86, "r_green_l")

    # ---- arms (crossed, ready) ----
    thick_line(c, 88, 56, 78, 68, 5, "r_green_d")
    thick_line(c, 100, 54, 82, 76, 5, "r_green_d")

    # ---- hands ----
    c.circle(78, 68, 3, "r_skin")
    c.circle(82, 76, 3, "r_skin")

    # ---- twin daggers ----
    thick_line(c, 78, 66, 71, 55, 2, "r_silver")
    thick_line(c, 82, 76, 90, 85, 2, "r_silver")

    # ---- hood ----
    c.circle(94, 38, 15, "r_green")
    c.circle(94, 38, 15, "r_green_d", fill=False)   # thin inner rim
    c.line(83, 27, 104, 26, "r_green_l")            # top sheen

    # ---- face opening + glowing eyes ----
    c.poly([(80, 34), (98, 46), (78, 50)], "r_dark")
    c.rect(82, 42, 5, 4, "r_eye")
    c.rect(90, 42, 5, 4, "r_eye")


def coarse(c, step=2, x0=0, y0=0, x1=127, y1=127):
    """Tiny text observation map: a letter per sampled pixel."""
    pal = c.palette()
    trans = {p["index"] for p in pal if p["rgba"][3] == 0}
    name_to_char = {
        "bg0": ".", "bg1": ".", "bg2": ".", "bg3": ".", "horizon": ".",
        "ground": "=", "ground_hi": "-", "shadow": ".",
        "moon_halo": "o", "moon": "O", "outline": "#",
        "k_red": "R", "k_red_d": "r", "k_red_l": "L",
        "k_metal": "M", "k_metal_d": "m", "k_metal_l": "W",
        "k_gold": "Y", "k_dark": "D", "k_leather": "K",
        "r_green": "G", "r_green_d": "g", "r_green_l": "E",
        "r_dark": "d", "r_leather": "T", "r_skin": "S",
        "r_silver": "M", "r_eye": "e", "star": "*", "spark": "+",
    }
    for y in range(y0, y1 + 1, step):
        row = []
        for x in range(x0, x1 + 1, step):
            idx = c.get(x, y)
            if idx in trans:
                row.append(".")
            else:
                nm = c.color_name(idx)
                row.append(name_to_char.get(nm, "?"))
        print(f"{y:03d} " + "".join(row))


# ---------------------------------------------------------------------------
# compose
# ---------------------------------------------------------------------------
bg = new_canvas(W, H, background=None, name="bg")
chars = new_canvas(W, H, background=None, name="chars")

draw_background(bg)
draw_knight(chars)
draw_rogue(chars)

# anime-cel style dark outline around both fighters
chars.outline("outline")

result = flatten([bg, chars], name="result")

print(result.stats_text())
finish(result)
