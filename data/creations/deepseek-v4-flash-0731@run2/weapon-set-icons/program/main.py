from pixelbench_api import *

OUT = "#171a21"
STEEL = "#aeb9c7"
STEEL_L = "#e8eef5"
STEEL_D = "#77849a"
GOLD = "#e3b04a"
GOLD_D = "#a87f2e"
GOLD_L = "#f4cf7e"
GRIP = "#6b4726"
GRIP_D = "#422b14"
WOOD = "#8a5a2e"
WOOD_L = "#b57c41"
WOOD_D = "#5c3a1c"
STRING = "#efe6d8"
RED = "#c24a33"
RED_D = "#8e2f1e"
RED_L = "#e07058"

c = new_canvas(64, 64, name="weapon-set")

def draw_sword(qx, qy):
    # blade
    c.poly([(qx+14, qy+5), (qx+18, qy+5), (qx+16, qy+1)], STEEL)
    c.rect(qx+14, qy+6, 4, 13, STEEL)
    c.rect(qx+15, qy+3, 2, 14, STEEL_L)
    # guard
    c.rect(qx+8, qy+19, 16, 3, GOLD)
    c.rect(qx+9, qy+20, 3, 1, GOLD_D)
    c.rect(qx+17, qy+20, 3, 1, GOLD_D)
    # grip + pommel
    c.rect(qx+14, qy+22, 4, 7, GRIP)
    c.rect(qx+15, qy+24, 2, 3, GRIP_D)
    c.circle(qx+16, qy+29, 2, GOLD)
    c.set(qx+16, qy+30, GOLD_D)

def draw_bow(qx, qy):
    # thick recurve limb (outer edge left, inner edge right)
    c.path(f"M {qx+16},{qy+4} Q {qx+3},{qy+16} {qx+16},{qy+28} Q {qx+8},{qy+16} {qx+16},{qy+4} Z", WOOD)
    # wood shading along the inner edge
    c.path(f"M {qx+16},{qy+7} Q {qx+9},{qy+16} {qx+16},{qy+25}", WOOD_L, False)
    # nocks
    c.circle(qx+16, qy+3, 1, GOLD)
    c.circle(qx+16, qy+29, 1, GOLD)
    # grip wrap
    for i, off in enumerate([0, 1, 0, 1, 0]):
        c.rect(qx+3+off, qy+13+i, 2, 1, GRIP)

def draw_bow_string(qx, qy):
    c.line(qx+16, qy+3, qx+16, qy+29, STRING)

def draw_shield(qx, qy):
    outer = f"M {qx+9},{qy+7} Q {qx+16},{qy+3} {qx+23},{qy+7} L {qx+21},{qy+21} L {qx+16},{qy+27} L {qx+11},{qy+21} Z"
    inner = f"M {qx+11},{qy+8} Q {qx+16},{qy+5} {qx+21},{qy+8} L {qx+19},{qy+20} L {qx+16},{qy+25} L {qx+13},{qy+20} Z"
    c.path(outer, RED_D)
    c.path(inner, RED)          # even-odd hole -> dark rim band
    c.path(f"M {qx+12},{qy+9} Q {qx+16},{qy+6} {qx+19},{qy+9}", RED_L, False)
    c.circle(qx+16, qy+17, 4, RED_D)
    c.circle(qx+16, qy+17, 3, GOLD)
    c.rect(qx+14, qy+16, 5, 1, GOLD_L)

def draw_axe(qx, qy):
    # head
    c.path(f"M {qx+10},{qy+4} L {qx+25},{qy+3} L {qx+25},{qy+11} L {qx+13},{qy+14} Q {qx+4},{qy+8} {qx+10},{qy+4} Z", STEEL)
    c.circle(qx+25, qy+7, 3, STEEL)
    c.rect(qx+18, qy+9, 7, 1, STEEL_D)
    c.path(f"M {qx+10},{qy+5} Q {qx+6},{qy+8} {qx+13},{qy+12}", STEEL_L, False)
    # haft
    c.rect(qx+21, qy+12, 4, 16, WOOD)
    c.rect(qx+22, qy+14, 1, 12, WOOD_L)
    c.rect(qx+24, qy+14, 1, 12, WOOD_D)
    # collars
    c.rect(qx+20, qy+10, 6, 2, GOLD)
    c.rect(qx+20, qy+28, 6, 2, GOLD)
    c.set(qx+22, qy+29, GOLD_D)

draw_sword(0, 0)
draw_bow(32, 0)
draw_shield(0, 32)
draw_axe(32, 32)
c.outline(OUT)
draw_bow_string(32, 0)

print(c.stats_text())
for name, r in [("sword", (0, 0, 31, 31)), ("bow", (32, 0, 63, 31)),
               ("shield", (0, 32, 31, 63)), ("axe", (32, 32, 63, 63))]:
    print("==", name)
    print(c.matrix_text(region=r, indices=True))

finish(c)
