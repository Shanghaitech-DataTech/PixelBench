# Neighborhood laundromat interior - 64x64 pixel art
c = new_canvas(64, 64, background=None, name="laundromat")

# ---- palette ----
WALL    = "#d9e1e8"   # cool light wall
WALL_HI = "#e7edf2"   # lit band under the ceiling light
BASE    = "#8e9aa8"   # baseboard
FLOOR   = "#b7c0ca"   # tile floor
FLOORL  = "#9ba5b1"   # tile grout lines
SHADOW  = "#a6b0bb"   # soft shadow on floor
LIGHT   = "#f4fbff"   # fluorescent tube (cool white)
LIGHTFR = "#7f8b99"   # light housing

BODY    = "#f0f5f9"   # machine body
OUT     = "#5d6875"   # machine outline
PANEL   = "#c2cbd5"   # control panel
PANELD  = "#6e7986"   # panel slot
DISP    = "#4fc3d9"   # little display
BTN_G   = "#7fc98f"   # green button
BTN_R   = "#d97b7b"   # red button
RING    = "#97a3b1"   # door ring
GLASS   = "#2b3646"   # door glass
GLASS_H = "#8fd6e6"   # glass highlight

TABLE   = "#f4f7fa"   # folding table top
TABLE_E = "#aab4c0"   # table edge
LEG     = "#77828f"   # table legs
TOW_P   = "#e8a7a7"   # towel pink
TOW_B   = "#a7c8e8"   # towel blue
TOW_Y   = "#efe0a3"   # towel yellow
TOW_G   = "#b8dcc0"   # towel green

BASKET  = "#6fa8d8"   # laundry basket
BASKET_D= "#4f86b8"   # basket shade
CL_P    = "#dba0b4"   # clothes pink
CL_W    = "#eef3f7"   # clothes white
CL_Y    = "#e6d489"   # clothes yellow

FACE    = "#f6fafc"   # clock face
RIM     = "#55606d"   # clock rim
HAND    = "#333c48"   # clock hands

# ---- room shell ----
c.rect(0, 0, 64, 39, WALL)          # wall
c.rect(0, 3, 64, 1, WALL_HI)        # lit band under the light
c.rect(0, 38, 64, 2, BASE)          # baseboard
c.rect(0, 40, 64, 24, FLOOR)        # floor
for yy in (46, 52, 58):             # floor grout, horizontal
    c.line(0, yy, 63, yy, FLOORL)
for xx in (10, 26, 42, 58):         # floor grout, vertical
    c.line(xx, 40, xx, 63, FLOORL)

# ---- ceiling fluorescent light ----
c.rect(9, 1, 46, 2, LIGHT)
c.set(8, 1, LIGHTFR); c.set(8, 2, LIGHTFR)
c.set(55, 1, LIGHTFR); c.set(55, 2, LIGHTFR)

# ---- wall clock ----
c.circle(32, 9, 4, RIM, fill=True)
c.circle(32, 9, 3, FACE, fill=True)
c.line(32, 9, 32, 6, HAND)          # minute hand
c.line(32, 9, 34, 10, HAND)         # hour hand

# ---- wall sign (right wall, above the table) ----
c.rect(50, 16, 11, 10, FACE)                 # sign board
c.rect(50, 16, 11, 10, OUT, fill=False)
c.circle(55, 21, 3, BASKET, fill=True)       # wash swirl
c.circle(55, 21, 1, FACE, fill=True)
c.set(53, 19, GLASS_H)

# ---- detergent bottle on the floor ----
c.rect(21, 50, 4, 1, CL_W)                   # cap
c.rect(22, 48, 2, 2, CL_W)                   # neck
c.rect(20, 51, 6, 8, TOW_B)                  # bottle body
c.rect(20, 51, 6, 8, OUT, fill=False)
c.rect(21, 53, 4, 3, CL_W)                   # label
c.set(22, 54, BASKET_D)

# ---- washing machines ----
def machine(x, y, w, h, r, cy):
    c.rect(x, y, w, h, BODY)
    c.rect(x, y, w, h, OUT, fill=False)          # crisp outline
    c.rect(x + 1, y + 1, w - 2, 3, PANEL)        # control panel
    c.rect(x + 2, y + 2, 3, 1, DISP)             # display
    c.set(x + w - 3, y + 2, BTN_G)               # buttons
    c.set(x + w - 5, y + 2, BTN_R)
    c.line(x + 1, y + 4, x + w - 2, y + 4, PANELD)  # panel slot
    cx = x + w // 2
    c.circle(cx, cy, r, RING, fill=True)         # door ring
    c.circle(cx, cy, r - 1, GLASS, fill=True)    # glass
    c.set(cx - 1, cy - 1, GLASS_H)               # highlight
    c.set(cx + 1, cy - 1, GLASS_H)

# back row (against the wall): 4 machines
for x in (5, 19, 33, 47):
    machine(x, 13, 12, 14, 3, 22)     # y=13..26, door centre y=22

# front row (larger, closer): 3 machines
for x in (4, 19, 34):
    machine(x, 30, 13, 17, 4, 41)     # y=30..46, door centre y=41
    c.rect(x, 47, 13, 1, SHADOW)      # floor shadow

# ---- folding table (right side) ----
# folded towel stacks on top
c.rect(50, 35, 5, 3, TOW_P)
c.rect(50, 34, 5, 1, TOW_B)
c.rect(56, 33, 6, 2, TOW_Y)
c.rect(56, 35, 6, 3, TOW_G)
# table top
c.rect(48, 38, 15, 3, TABLE)
c.line(48, 41, 62, 41, TABLE_E)
# legs
c.rect(49, 41, 2, 9, LEG)
c.rect(60, 41, 2, 9, LEG)

# ---- laundry basket (front left) ----
# clothes poking out
c.rect(6, 48, 4, 3, CL_P)
c.rect(10, 47, 4, 4, CL_W)
c.rect(7, 49, 7, 2, CL_Y)
# basket
c.rect(5, 51, 12, 2, BASKET)          # rim
c.rect(6, 53, 10, 6, BASKET)          # body
c.line(6, 53, 6, 58, BASKET_D)
c.line(15, 53, 15, 58, BASKET_D)
c.line(6, 58, 15, 58, BASKET_D)
for gx in (8, 11):                    # grid texture
    c.line(gx, 53, gx, 57, BASKET_D)

print(c.stats_text())
finish(c)
