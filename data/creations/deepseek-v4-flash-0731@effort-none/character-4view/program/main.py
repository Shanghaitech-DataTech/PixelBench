from pixelbench_api import *

c = new_canvas(64, 64)

OUTLINE = (8, 8, 8)
SKIN = (255, 205, 170)
HAIR = (252, 205, 70)
HAIR_DL = (228, 174, 42)
TOP = (252, 66, 96)
TOP_DL = (214, 40, 70)
WHITE = (255, 255, 255)
CHEEK = (255, 170, 170)

# Shared body base for front/back views (facing viewer/away)
def draw_body_base(ox, oy):
    # Torso (crop top)
    c.rect(ox+7, oy+11, 14, 7, TOP, fill=True)
    c.rect(ox+6, oy+11, 16, 8, OUTLINE, fill=False)
    # White stripe
    c.rect(ox+12, oy+11, 1, 6, WHITE, fill=True)
    # Midriff
    c.set(ox+8, oy+17, SKIN)
    c.set(ox+9, oy+17, SKIN)
    c.set(ox+18, oy+17, SKIN)
    c.set(ox+19, oy+17, SKIN)
    # Skirt (pleated)
    c.rect(ox+6, oy+18, 16, 4, TOP, fill=True)
    c.rect(ox+5, oy+18, 18, 5, OUTLINE, fill=False)
    c.rect(ox+6, oy+18, 16, 2, TOP_DL, fill=True)
    c.set(ox+9, oy+20, TOP_DL)
    c.set(ox+13, oy+20, TOP_DL)
    c.set(ox+17, oy+20, TOP_DL)
    # Legs
    c.rect(ox+9, oy+23, 3, 4, SKIN, fill=True)
    c.rect(ox+16, oy+23, 3, 4, SKIN, fill=True)
    c.rect(ox+9, oy+26, 3, 2, WHITE, fill=True)
    c.rect(ox+16, oy+26, 3, 2, WHITE, fill=True)
    c.rect(ox+8, oy+28, 5, 1, OUTLINE, fill=True)
    c.rect(ox+15, oy+28, 5, 1, OUTLINE, fill=True)

def draw_front(ox, oy):
    # Hair top
    c.rect(ox+6, oy+0, 16, 2, HAIR, fill=True)
    c.rect(ox+5, oy+0, 18, 3, OUTLINE, fill=False)
    c.rect(ox+6, oy+0, 16, 1, HAIR_DL, fill=True)
    # Face
    c.rect(ox+6, oy+2, 16, 8, SKIN, fill=True)
    c.rect(ox+5, oy+2, 18, 9, OUTLINE, fill=False)
    c.rect(ox+6, oy+2, 16, 2, HAIR, fill=True)
    c.rect(ox+6, oy+3, 16, 1, HAIR_DL, fill=True)
    c.rect(ox+5, oy+4, 1, 5, HAIR, fill=True)
    c.rect(ox+22, oy+4, 1, 5, HAIR, fill=True)
    # face details
    c.set(ox+10, oy+5, OUTLINE)
    c.set(ox+10, oy+6, OUTLINE)
    c.set(ox+17, oy+5, OUTLINE)
    c.set(ox+17, oy+6, OUTLINE)
    c.set(ox+13, oy+8, OUTLINE)
    c.set(ox+14, oy+8, OUTLINE)
    c.set(ox+7, oy+8, CHEEK)
    c.set(ox+20, oy+8, CHEEK)
    # Neck
    c.set(ox+12, oy+10, SKIN)
    c.set(ox+13, oy+10, SKIN)
    c.set(ox+14, oy+10, SKIN)
    # Arms + pompoms
    c.set(ox+6, oy+12, TOP)
    c.set(ox+6, oy+13, TOP)
    c.set(ox+22, oy+12, TOP)
    c.set(ox+22, oy+13, TOP)
    draw_body_base(ox, oy)
    c.circle(ox+4, oy+14, 2, WHITE, fill=True)
    c.circle(ox+3, oy+13, 3, OUTLINE, fill=False)
    c.circle(ox+24, oy+14, 2, WHITE, fill=True)
    c.circle(ox+25, oy+13, 3, OUTLINE, fill=False)

def draw_back(ox, oy):
    # Back of head - hair
    c.rect(ox+6, oy+0, 16, 2, HAIR, fill=True)
    c.rect(ox+5, oy+0, 18, 11, OUTLINE, fill=False)
    # Back of head hair mass
    c.rect(ox+6, oy+2, 16, 8, HAIR, fill=True)
    c.rect(ox+6, oy+2, 16, 2, HAIR_DL, fill=True)
    # Long hair streaming down the sides
    c.rect(ox+5, oy+7, 2, 13, HAIR, fill=True)
    c.rect(ox+21, oy+7, 2, 13, HAIR, fill=True)
    # neck
    c.set(ox+12, oy+10, SKIN)
    c.set(ox+13, oy+10, SKIN)
    c.set(ox+14, oy+10, SKIN)
    # Back body (no face)
    draw_body_base(ox, oy)
    # Sides of hair behind shoulders
    c.rect(ox+4, oy+10, 2, 8, HAIR, fill=True)
    c.rect(ox+22, oy+10, 2, 8, HAIR, fill=True)
    # Pompoms from behind
    c.circle(ox+4, oy+15, 2, WHITE, fill=True)
    c.circle(ox+3, oy+14, 3, OUTLINE, fill=False)
    c.circle(ox+24, oy+15, 2, WHITE, fill=True)
    c.circle(ox+25, oy+14, 3, OUTLINE, fill=False)

def draw_left(ox, oy):
    # Top hair
    c.rect(ox+5, oy+0, 17, 2, HAIR, fill=True)
    c.rect(ox+4, oy+0, 19, 11, OUTLINE, fill=False)
    # Back-of-head hair
    c.rect(ox+6, oy+2, 14, 8, HAIR, fill=True)
    c.rect(ox+6, oy+2, 14, 2, HAIR_DL, fill=True)
    # Face (profile, facing left)
    c.rect(ox+6, oy+2, 10, 8, SKIN, fill=True)
    # face features
    c.set(ox+7, oy+5, OUTLINE)
    c.set(ox+7, oy+6, OUTLINE)
    c.set(ox+8, oy+7, OUTLINE)
    c.set(ox+10, oy+5, OUTLINE)
    c.set(ox+10, oy+6, OUTLINE)
    c.set(ox+8, oy+8, OUTLINE)
    c.set(ox+9, oy+8, CHEEK)
    # neck
    c.set(ox+12, oy+10, SKIN)
    c.set(ox+13, oy+10, SKIN)
    # Long hair behind
    c.rect(ox+14, oy+5, 6, 16, HAIR, fill=True)
    c.rect(ox+14, oy+5, 2, 15, HAIR_DL, fill=True)
    # Torso + pompom
    c.rect(ox+8, oy+11, 11, 7, TOP, fill=True)
    c.rect(ox+7, oy+11, 12, 8, OUTLINE, fill=False)
    c.rect(ox+13, oy+11, 1, 6, WHITE, fill=True)
    # front arm
    c.rect(ox+4, oy+12, 3, 5, TOP, fill=True)
    c.rect(ox+4, oy+12, 3, 6, OUTLINE, fill=False)
    c.circle(ox+3, oy+15, 2, WHITE, fill=True)
    c.circle(ox+3, oy+14, 3, OUTLINE, fill=False)
    # skirt
    c.rect(ox+6, oy+18, 14, 4, TOP, fill=True)
    c.rect(ox+5, oy+18, 16, 5, OUTLINE, fill=False)
    c.rect(ox+6, oy+18, 14, 2, TOP_DL, fill=True)
    # legs
    c.rect(ox+11, oy+23, 4, 4, SKIN, fill=True)
    c.rect(ox+11, oy+26, 4, 2, WHITE, fill=True)
    c.rect(ox+10, oy+28, 5, 1, OUTLINE, fill=True)

def draw_right(ox, oy):
    # Top hair
    c.rect(ox+6, oy+0, 17, 2, HAIR, fill=True)
    c.rect(ox+5, oy+0, 19, 11, OUTLINE, fill=False)
    c.rect(ox+8, oy+2, 14, 8, HAIR, fill=True)
    c.rect(ox+8, oy+2, 14, 2, HAIR_DL, fill=True)
    # Face (profile, facing right)
    c.rect(ox+12, oy+2, 10, 8, SKIN, fill=True)
    c.set(ox+21, oy+5, OUTLINE)
    c.set(ox+21, oy+6, OUTLINE)
    c.set(ox+20, oy+7, OUTLINE)
    c.set(ox+17, oy+5, OUTLINE)
    c.set(ox+17, oy+6, OUTLINE)
    c.set(ox+20, oy+8, OUTLINE)
    c.set(ox+18, oy+8, CHEEK)
    c.set(ox+14, oy+10, SKIN)
    c.set(ox+15, oy+10, SKIN)
    # Long hair behind
    c.rect(ox+8, oy+5, 6, 16, HAIR, fill=True)
    c.rect(ox+12, oy+5, 2, 15, HAIR_DL, fill=True)
    # Torso + pompom
    c.rect(ox+9, oy+11, 11, 7, TOP, fill=True)
    c.rect(ox+9, oy+11, 12, 8, OUTLINE, fill=False)
    c.rect(ox+14, oy+11, 1, 6, WHITE, fill=True)
    c.rect(ox+21, oy+12, 3, 5, TOP, fill=True)
    c.rect(ox+21, oy+12, 3, 6, OUTLINE, fill=False)
    c.circle(ox+25, oy+15, 2, WHITE, fill=True)
    c.circle(ox+25, oy+14, 3, OUTLINE, fill=False)
    c.rect(ox+8, oy+18, 14, 4, TOP, fill=True)
    c.rect(ox+7, oy+18, 16, 5, OUTLINE, fill=False)
    c.rect(ox+8, oy+18, 14, 2, TOP_DL, fill=True)
    c.rect(ox+13, oy+23, 4, 4, SKIN, fill=True)
    c.rect(ox+13, oy+26, 4, 2, WHITE, fill=True)
    c.rect(ox+13, oy+28, 5, 1, OUTLINE, fill=True)

# Arrange in 2x2 grid
draw_front(2, 2)
draw_back(34, 2)
draw_left(2, 34)
draw_right(34, 34)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))
print("palette count:", len(c.palette()))
finish(c)
