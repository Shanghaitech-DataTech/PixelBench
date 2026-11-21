from pixelbench_api import *

# ---- palette (registered on the main drawing) ----
c = new_canvas(64, 64)
OUT   = c.color("#241e2c")   # dark outline
SKIN  = c.color("#f8d0a8")   # skin
HAIR  = c.color("#8a4a2a")   # brown hair
HAIR2 = c.color("#6b3518")   # dark hair accent
TOP   = c.color("#e23a4a")   # cheer top red
SKIRT = c.color("#d82a3a")   # skirt red
WHITE = c.color("#ffffff")   # white trim / shoes
POM   = c.color("#f4f0f0")   # pom-poms
BLUSH = c.color("#f2a0a8")   # blush
SHOE  = c.color("#e8e8f0")   # shoe white

def rct(cv, ox, oy, x, y, w, h, col):
    cv.rect(ox + x, oy + y, w, h, col)

def crc(cv, ox, oy, cx, cy, r, col, fill=True):
    cv.circle(ox + cx, oy + cy, r, col, fill)

def elp(cv, ox, oy, cx, cy, rx, ry, col, fill=True):
    cv.ellipse(ox + cx, oy + cy, rx, ry, col, fill)

def pol(cv, ox, oy, pts, col, fill=True):
    cv.poly([(ox + x, oy + y) for x, y in pts], col, fill)

def lin(cv, ox, oy, x0, y0, x1, y1, col):
    cv.line(ox + x0, oy + y0, ox + x1, oy + y1, col)

# ---------------- FRONT ----------------
def draw_front(cv, ox, oy):
    # head
    crc(cv, ox, oy, 16, 8, 7, OUT)
    elp(cv, ox, oy, 16, 7, 7, 6, HAIR)
    elp(cv, ox, oy, 16, 12, 6, 5, OUT)
    elp(cv, ox, oy, 16, 12, 5, 4, SKIN)
    # face
    rct(cv, ox, oy, 12, 11, 2, 1, OUT)
    rct(cv, ox, oy, 18, 11, 2, 1, OUT)
    rct(cv, ox, oy, 14, 14, 4, 1, OUT)
    rct(cv, ox, oy, 11, 13, 1, 1, BLUSH)
    rct(cv, ox, oy, 20, 13, 1, 1, BLUSH)
    # neck
    rct(cv, ox, oy, 14, 18, 4, 2, SKIN)
    # arms
    rct(cv, ox, oy, 8, 20, 4, 5, OUT)
    rct(cv, ox, oy, 9, 21, 2, 3, SKIN)
    rct(cv, ox, oy, 20, 20, 4, 5, OUT)
    rct(cv, ox, oy, 21, 21, 2, 3, SKIN)
    # torso / top
    rct(cv, ox, oy, 11, 20, 10, 4, OUT)
    rct(cv, ox, oy, 12, 21, 8, 2, TOP)
    rct(cv, ox, oy, 14, 21, 4, 1, WHITE)
    # pom-poms
    crc(cv, ox, oy, 10, 24, 3, OUT)
    crc(cv, ox, oy, 10, 24, 2, POM)
    crc(cv, ox, oy, 22, 24, 3, OUT)
    crc(cv, ox, oy, 22, 24, 2, POM)
    # skirt
    pol(cv, ox, oy, [(11, 23), (21, 23), (24, 28), (8, 28)], OUT)
    pol(cv, ox, oy, [(12, 24), (20, 24), (23, 27), (9, 27)], SKIRT)
    lin(cv, ox, oy, 15, 24, 14, 27, WHITE)
    lin(cv, ox, oy, 17, 24, 18, 27, WHITE)
    # legs
    rct(cv, ox, oy, 11, 28, 5, 3, OUT)
    rct(cv, ox, oy, 12, 29, 3, 2, SKIN)
    rct(cv, ox, oy, 16, 28, 5, 3, OUT)
    rct(cv, ox, oy, 17, 29, 3, 2, SKIN)
    # shoes
    rct(cv, ox, oy, 10, 30, 5, 2, OUT)
    rct(cv, ox, oy, 11, 30, 3, 1, SHOE)
    rct(cv, ox, oy, 17, 30, 5, 2, OUT)
    rct(cv, ox, oy, 18, 30, 3, 1, SHOE)

# ---------------- BACK ----------------
def draw_back(cv, ox, oy):
    # head (all hair)
    crc(cv, ox, oy, 16, 8, 7, OUT)
    crc(cv, ox, oy, 16, 8, 6, HAIR)
    # high ponytail / puff
    elp(cv, ox, oy, 16, 4, 4, 4, OUT)
    elp(cv, ox, oy, 16, 4, 3, 3, HAIR)
    rct(cv, ox, oy, 14, 5, 4, 1, HAIR2)
    # neck
    rct(cv, ox, oy, 14, 16, 4, 3, SKIN)
    # arms
    rct(cv, ox, oy, 8, 20, 4, 5, OUT)
    rct(cv, ox, oy, 9, 21, 2, 3, SKIN)
    rct(cv, ox, oy, 20, 20, 4, 5, OUT)
    rct(cv, ox, oy, 21, 21, 2, 3, SKIN)
    # torso / top back
    rct(cv, ox, oy, 11, 19, 10, 4, OUT)
    rct(cv, ox, oy, 12, 20, 8, 3, TOP)
    rct(cv, ox, oy, 13, 20, 6, 1, WHITE)
    # pom-poms
    crc(cv, ox, oy, 10, 24, 3, OUT)
    crc(cv, ox, oy, 10, 24, 2, POM)
    crc(cv, ox, oy, 22, 24, 3, OUT)
    crc(cv, ox, oy, 22, 24, 2, POM)
    # skirt
    pol(cv, ox, oy, [(11, 23), (21, 23), (24, 28), (8, 28)], OUT)
    pol(cv, ox, oy, [(12, 24), (20, 24), (23, 27), (9, 27)], SKIRT)
    lin(cv, ox, oy, 15, 24, 14, 27, WHITE)
    lin(cv, ox, oy, 17, 24, 18, 27, WHITE)
    # legs
    rct(cv, ox, oy, 11, 28, 5, 3, OUT)
    rct(cv, ox, oy, 12, 29, 3, 2, SKIN)
    rct(cv, ox, oy, 16, 28, 5, 3, OUT)
    rct(cv, ox, oy, 17, 29, 3, 2, SKIN)
    # shoes
    rct(cv, ox, oy, 10, 30, 5, 2, OUT)
    rct(cv, ox, oy, 11, 30, 3, 1, SHOE)
    rct(cv, ox, oy, 17, 30, 5, 2, OUT)
    rct(cv, ox, oy, 18, 30, 3, 1, SHOE)

# ---------------- SIDE (facing left) ----------------
def draw_side_left(cv, ox, oy):
    # head
    crc(cv, ox, oy, 16, 8, 7, OUT)
    elp(cv, ox, oy, 18, 7, 7, 6, HAIR)
    elp(cv, ox, oy, 13, 12, 6, 5, OUT)
    elp(cv, ox, oy, 13, 12, 5, 4, SKIN)
    # nose
    rct(cv, ox, oy, 8, 10, 2, 2, SKIN)
    # face features
    rct(cv, ox, oy, 11, 11, 2, 1, OUT)
    rct(cv, ox, oy, 10, 14, 2, 1, OUT)
    rct(cv, ox, oy, 9, 13, 1, 1, BLUSH)
    # ponytail at back
    elp(cv, ox, oy, 20, 6, 4, 6, OUT)
    elp(cv, ox, oy, 20, 6, 3, 5, HAIR)
    # neck
    rct(cv, ox, oy, 12, 16, 3, 3, SKIN)
    # back pom (partially hidden)
    crc(cv, ox, oy, 20, 24, 3, OUT)
    crc(cv, ox, oy, 20, 24, 2, POM)
    # torso side
    rct(cv, ox, oy, 10, 19, 12, 4, OUT)
    rct(cv, ox, oy, 11, 20, 10, 3, TOP)
    rct(cv, ox, oy, 12, 20, 4, 1, WHITE)
    # front arm + pom
    rct(cv, ox, oy, 7, 20, 4, 5, OUT)
    rct(cv, ox, oy, 8, 21, 2, 3, SKIN)
    crc(cv, ox, oy, 9, 24, 3, OUT)
    crc(cv, ox, oy, 9, 24, 2, POM)
    # skirt
    pol(cv, ox, oy, [(10, 22), (20, 22), (21, 28), (9, 28)], OUT)
    pol(cv, ox, oy, [(11, 23), (19, 23), (20, 27), (10, 27)], SKIRT)
    lin(cv, ox, oy, 14, 23, 13, 27, WHITE)
    lin(cv, ox, oy, 16, 23, 17, 27, WHITE)
    # legs
    rct(cv, ox, oy, 11, 28, 4, 3, OUT)
    rct(cv, ox, oy, 12, 29, 2, 2, SKIN)
    rct(cv, ox, oy, 17, 28, 4, 3, OUT)
    rct(cv, ox, oy, 18, 29, 2, 2, SKIN)
    # shoes
    rct(cv, ox, oy, 10, 30, 5, 2, OUT)
    rct(cv, ox, oy, 11, 30, 3, 1, SHOE)
    rct(cv, ox, oy, 16, 30, 5, 2, OUT)
    rct(cv, ox, oy, 17, 30, 3, 1, SHOE)

# draw three quadrants directly
draw_front(c, 0, 0)
draw_back(c, 32, 0)

# side views: draw left-facing into a temp canvas, then mirror for the right view
side = new_canvas(32, 32)
draw_side_left(side, 0, 0)
c.blit(side, 0, 32)
side.mirror("h")
c.blit(side, 32, 32)

finish(c)
