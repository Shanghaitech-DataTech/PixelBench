from pixelbench_api import new_canvas, view, save, finish

c = new_canvas(32, 32, name="escooter_rider")

# ---------------------------------------------------------------- palette
OUT     = "#1b1526"   # outline / near black
HELM    = "#e0503f"; HELM_L = "#f58a6d"; HELM_D = "#a5322c"
SKIN    = "#f2b489"; SKIN_D = "#c9835c"
SHIRT   = "#3ea9cf"; SHIRT_L = "#82daea"; SHIRT_D = "#2a7595"
PANTS   = "#3d4d84"; PANTS_D = "#2b3763"
SHOE    = "#e6e9f2"; SHOE_D = "#8f97ad"
FRAME   = "#f0b93c"; FRAME_D = "#b8801f"
DECK    = "#3a3f55"; DECK_L = "#707892"
TYRE    = "#23232e"; TYRE_L = "#454659"; HUB = "#aeb6c8"
GRIP    = "#2b2b38"
LIGHT   = "#ffe9a3"
SH_A    = "#1b152638"; SH_B = "#1b15266e"


def P(x, y, col):
    c.set(x, y, col)


def L(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)


def R(x, y, w, h, col):
    c.rect(x, y, w, h, col)


# ---------------------------------------------------------------- shadow
R(4, 29, 5, 1, SH_B)
R(22, 29, 5, 1, SH_B)
R(9, 29, 13, 1, SH_A)

# ---------------------------------------------------------------- wheels
for wx in (6, 24):
    c.circle(wx, 26, 2, TYRE, fill=True)
    P(wx - 1, 24, TYRE_L)
    P(wx, 24, TYRE_L)
    P(wx, 26, HUB)

# ---------------------------------------------------------------- scooter
# rear stay deck -> hub
L(9, 24, 6, 26, FRAME_D)
# rear fender over the wheel, joining the deck line
L(5, 23, 7, 23, FRAME)
P(4, 24, FRAME)

# deck
R(8, 23, 15, 1, DECK_L)
R(8, 24, 15, 1, DECK)

# front fork + stem (raked slightly forward)
L(24, 25, 24, 26, FRAME_D)
L(23, 24, 25, 13, FRAME)
L(24, 24, 26, 13, FRAME_D)

# handlebar + headlight
R(21, 12, 6, 1, GRIP)
P(26, 12, FRAME_D)
P(26, 13, LIGHT)

# ---------------------------------------------------------------- rider
# --- far leg (darker), foot on deck
R(12, 16, 2, 3, PANTS_D)
R(12, 19, 2, 2, PANTS_D)
R(12, 21, 3, 1, SHOE_D)
R(11, 22, 4, 1, SHOE_D)

# --- near leg
R(16, 16, 2, 3, PANTS)
R(17, 19, 2, 2, PANTS)
R(17, 21, 3, 1, SHOE)
R(16, 22, 5, 1, SHOE)
P(20, 22, SHOE_D)

# --- torso, leaning forward
c.poly([(13, 15), (14, 13), (15, 11), (16, 10), (18, 10), (19, 11),
        (19, 13), (18, 15), (18, 17), (13, 17)], SHIRT, fill=True)
L(15, 11, 13, 15, SHIRT_D)          # back shading
P(13, 16, SHIRT_D); P(13, 17, SHIRT_D)
L(19, 11, 19, 12, SHIRT_L)          # chest highlight
P(18, 10, SHIRT_L)
# hips
R(13, 16, 6, 1, PANTS)
L(13, 17, 18, 17, PANTS_D)

# --- near arm reaching the grip
L(17, 11, 19, 12, SHIRT)
L(17, 13, 20, 13, SHIRT_D)          # separation under the arm
P(20, 12, SKIN)
P(20, 13, SKIN)
R(21, 12, 2, 2, SKIN)
P(22, 13, SKIN_D)

# --- head: face under the helmet, sitting on the collar
R(16, 7, 3, 3, SKIN)
P(18, 8, OUT)          # eye
P(18, 9, SKIN_D)       # jaw
P(15, 7, HELM_D)       # helmet rear shell
P(15, 8, HELM_D)
P(16, 9, HELM_D)       # chin strap
# helmet shell
R(17, 3, 2, 1, HELM)
R(16, 4, 4, 1, HELM)
P(16, 4, HELM_L); P(17, 4, HELM_L)
R(15, 5, 6, 1, HELM)
P(15, 5, HELM_L); P(16, 5, HELM_L); P(20, 5, HELM_D)
L(15, 6, 21, 6, HELM_D)   # brim + visor peak

view(c)
save("escooter_rider", c)
finish(c)
