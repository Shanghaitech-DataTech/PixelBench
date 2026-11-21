from pixelbench_api import *

W = 16
H = 16
c = new_canvas(W, H, name="output")

# Palette
wood_light  = c.color("#9a7046")   # light board base
wood_med    = c.color("#7a5636")   # medium board base  
wood_dark   = c.color("#5a3d26")   # dark board base
seam        = c.color("#241708")   # dark seam groove
grain_dark  = c.color("#4a2f1b")   # grain line (dark)
grain_hl    = c.color("#b08054")   # light grain highlight
knot_core   = c.color("#1c1105")   # knot center
knot_ring   = c.color("#3d2814")   # knot ring

# Board layout: 4 boards of 3px, seams at x in {3,7,11,15} -> tiles horizontally.
# Alternative board coloring: light, dark, light, dark
board_col = {0: wood_light, 1: wood_dark, 2: wood_med, 3: wood_light}
seam_cols = {3, 7, 11, 15}

# Add a lighter and slightly darker light-board variant
wood_light2 = c.color("#a57a4c")
board_col = {0: wood_light2, 1: wood_dark, 2: wood_med, 3: c.color("#6e492b")}

# 1. Base fill
for y in range(H):
    for x in range(W):
        if x in seam_cols:
            c.set(x, y, seam)
        else:
            c.set(x, y, board_col[x // 4])

# 2. Vertical grain strokes per board, subtle wavy lines
def grain(bidx, gc, rows, color):
    xoff = 0
    for i in range(H):
        if i in rows:
            xoff = 1 if xoff == 0 else 0
        gx = bidx * 4 + gc + xoff
        if gx < W and (gx % 4) != 3:
            c.set(gx, i, color)

# light boards (0,2): one grain line each
grain(0, 1, {4, 8, 12}, grain_dark)
grain(2, 2, {4, 8, 12}, grain_dark)
# dark boards (1,3): one grain line each
grain(1, 1, {3, 7, 11}, grain_dark)
grain(3, 1, {5, 9, 13}, grain_dark)

# Light grain highlights beside dark grain lines
for y in [3, 8, 12]:
    if y < H:
        c.set(4 + 2, y, grain_hl)
        c.set(12 + 2, y, grain_hl)
        c.set(0 + 2, y, grain_hl)

# 3. Knots - a couple of small dark knots with ring
def knot(cx, cy):
    c.set(cx, cy, knot_core)
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= cx+dx < W and 0 <= cy+dy < H and (cx+dx) % 4 != 3:
            c.set(cx+dx, cy+dy, knot_ring)

knot(1, 4)
knot(13, 9)
knot(9, 13)

# 4. Board-end highlighting: rows 0 and 15 show alternating tone per board
for x in range(W):
    if x in seam_cols:
        continue
    bidx = x // 4
    if bidx in (0, 2):
        c.set(x, 0, c.color("#b08054"))
        c.set(x, 15, c.color("#8a603c"))
    else:
        c.set(x, 0, c.color("#6b4729"))
        c.set(x, 15, c.color("#4a2f1b"))

# 5. Subtle per-board speckle for material texture (low density)
for y in range(H):
    for x in range(W):
        if x in seam_cols:
            continue
        v = (x * 37 + y * 17 + 5) % 40
        if v == 0 and y not in (0, 15):
            c.set(x, y, grain_hl)
        elif v == 13:
            c.set(x, y, grain_dark)

finish(c)
