from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')

# === REGISTER COLORS ===
# Vines - use existing green palette colors where possible
vine_stem = c.color((67, 110, 90), name='vine_stem')       # medium green (exists at 52)
vine_deep = c.color((35, 68, 51), name='vine_deep')        # deep green (exists at 113)
vine_light = c.color((81, 111, 101), name='vine_light')    # light green (exists at 56)
vine_leaf = c.color((51, 75, 75), name='vine_leaf')        # muted green (exists at 5)
vine_dark_leaf = c.color((22, 41, 37), name='vine_dark_leaf')  # very dark green (new)

# Mage - cloaked figure colors
cloak_dark = c.color((9, 20, 24), name='cloak_dark')       # deepest cloak shadow
cloak_main = c.color((13, 33, 40), name='cloak_main')      # main cloak color (matches 58)
cloak_mid = c.color((30, 50, 55), name='cloak_mid')         # mid-tone
cloak_hi = c.color((57, 87, 89), name='cloak_hi')           # highlight (matches 25)

# Staff and glow
staff_c = c.color((72, 52, 30), name='staff')               # brown staff
staff_d = c.color((45, 32, 18), name='staff_dark')          # dark staff
glow_core = c.color((255, 240, 200), name='glow_core')      # bright glow
glow_mid = c.color((246, 218, 178), name='glow_mid')         # warm glow (matches 84)
glow_soft = c.color((200, 170, 130), name='glow_soft')      # soft glow (new)
glow_dim = c.color((160, 140, 110), name='glow_dim')        # dim glow (new)

# ============================================================
# 1. VINES ON LEFT TOWER WALL
# Left wall is approximately x=28-45, y=50-130
# ============================================================

# Main vine winding up the left wall
vine_pts_left = []
for y in range(48, 130, 2):
    wave = (y // 2) % 4
    if wave == 0 or wave == 2:
        x_stem = 36
    elif wave == 1:
        x_stem = 38
    else:
        x_stem = 34
    vine_pts_left.append((x_stem, y))

for x, y in vine_pts_left:
    out.set(x, y, vine_stem)
    out.set(x, y + 1, vine_deep)  # stem thickness

# Secondary thin vines on left wall
for y in range(52, 125, 5):
    out.set(40, y, vine_stem)
    out.set(41, y + 1, vine_deep)
    if y % 10 == 0:
        out.set(42, y, vine_leaf)
    if y % 10 == 5:
        out.set(39, y, vine_leaf)

# Leaf clusters in clusters around the left wall
leaf_cl_left = []
for cy in [55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115, 121]:
    lx = 33 + (cy % 4)
    leaf_cl_left.append((lx, cy))
    leaf_cl_left.append((lx+1, cy+1))
    leaf_cl_left.append((lx-1, cy+1))
    leaf_cl_left.append((lx, cy-1))
    leaf_cl_left.append((lx+1, cy))
    leaf_cl_left.append((lx-1, cy))

for x, y in leaf_cl_left:
    out.set(x, y, vine_leaf)
for i, (x, y) in enumerate(leaf_cl_left):
    if i % 3 == 0:
        out.set(x, y, vine_dark_leaf)
    if i % 3 == 1:
        out.set(x, y, vine_light)

# Hanging vines at top-left of wall
for x in range(30, 43):
    h_len = 3 + (x % 5)
    for dy in range(h_len):
        out.set(x, 50 + dy, vine_stem)
        if dy == h_len - 1:
            out.set(x, 50 + dy, vine_leaf)
    
# Additional scattered smaller leaves
for y in range(60, 125, 5):
    out.set(31, y, vine_leaf)
    out.set(44, y, vine_dark_leaf)

# ============================================================
# 2. VINES ON RIGHT TOWER WALL
# Right wall is approximately x=80-94, y=50-125
# ============================================================

vine_pts_right = []
for y in range(50, 128, 2):
    wave = (y // 2) % 4
    if wave == 0 or wave == 2:
        x_stem = 83
    elif wave == 1:
        x_stem = 85
    else:
        x_stem = 81
    vine_pts_right.append((x_stem, y))

for x, y in vine_pts_right:
    out.set(x, y, vine_stem)
    out.set(x, y + 1, vine_deep)

# Secondary vine on right wall
for y in range(56, 124, 5):
    out.set(88, y, vine_stem)
    out.set(87, y + 1, vine_deep)
    if y % 10 == 0:
        out.set(89, y, vine_leaf)
    if y % 10 == 5:
        out.set(86, y, vine_leaf)

# Leaf clusters on right
leaf_cl_right = []
for cy in [56, 62, 68, 74, 80, 86, 92, 98, 104, 110, 116, 122]:
    lx = 89 + (cy % 4)
    leaf_cl_right.append((lx, cy))
    leaf_cl_right.append((lx-1, cy+1))
    leaf_cl_right.append((lx+1, cy+1))
    leaf_cl_right.append((lx, cy-1))
    leaf_cl_right.append((lx+1, cy))
    leaf_cl_right.append((lx-1, cy))

for x, y in leaf_cl_right:
    out.set(x, y, vine_leaf)
for i, (x, y) in enumerate(leaf_cl_right):
    if i % 3 == 0:
        out.set(x, y, vine_dark_leaf)
    if i % 3 == 1:
        out.set(x, y, vine_light)

# Hanging vines at right wall top
for x in range(80, 93):
    h_len = 4 + (x % 5)
    for dy in range(h_len):
        out.set(x, 52 + dy, vine_stem)
        if dy == h_len - 1:
            out.set(x, 52 + dy, vine_leaf)

for y in range(58, 122, 5):
    out.set(91, y, vine_leaf)
    out.set(78, y, vine_dark_leaf)

# ============================================================
# 3. VINES OVER ARCHWAY FRAME EDGES
# ============================================================
# Left arch column (x=47-49)
for y in range(62, 115, 2):
    out.set(48, y, vine_stem)
    if y % 4 == 0:
        out.set(47, y, vine_deep)
    if y % 5 == 1:
        out.set(46, y, vine_leaf)
    if y % 5 == 2:
        out.set(49, y, vine_leaf)

# Right arch column (x=72-75)  
for y in range(64, 112, 2):
    out.set(73, y, vine_stem)
    if y % 4 == 0:
        out.set(74, y, vine_deep)
    if y % 5 == 1:
        out.set(75, y, vine_leaf)
    if y % 5 == 2:
        out.set(72, y, vine_leaf)

# Additional vine strands at arch top
for x in range(47, 76):
    if x < 50 or x > 72:
        out.set(x, 60 + (x % 8), vine_stem)
    if x % 3 == 0:
        out.set(x, 61, vine_leaf)

# ============================================================
# 4. CLOAKED MAGE AT THE ARCHWAY ENTRANCE
# Seen from behind, walking into the tower
# Mage center at mcx=60, positioned in the archway opening
# ============================================================

mcx = 60  # horizontal center of the mage

# === Glowing staff ===
# Staff position: at mage's right side
sx = mcx + 5  # x=65
for y in range(92, 118):
    out.set(sx, y, staff_c)
    if y % 4 == 0:
        out.set(sx, y, staff_d)

# === Staff glow at the top ===
gx, gy = sx, 88

# Outer glow ring (dim)
for dy in range(-5, 6):
    for dx in range(-5, 6):
        if dx*dx + dy*dy <= 20:
            out.set(gx + dx, gy + dy, glow_dim)

# Soft glow
for dy in range(-4, 5):
    for dx in range(-4, 5):
        if dx*dx + dy*dy <= 13:
            out.set(gx + dx, gy + dy, glow_soft)

# Warm glow
for dy in range(-3, 4):
    for dx in range(-3, 4):
        if dx*dx + dy*dy <= 8:
            out.set(gx + dx, gy + dy, glow_mid)

# Bright core
for dy in range(-2, 3):
    for dx in range(-2, 3):
        if dx*dx + dy*dy <= 4:
            out.set(gx + dx, gy + dy, glow_core)

# === Mage figure (back of figure, walking into archway) ===

# Hood/head (seen from behind) - at top of the body
for y in range(96, 106):
    # Hood is rounded at the top of the cloak
    r = 3 if y <= 98 else 4
    for x in range(mcx - r, mcx + r + 1):
        out.set(x, y, cloak_main)

# Hood shading
out.set(mcx, 96, cloak_dark)
out.set(mcx - 2, 95, cloak_dark)
out.set(mcx + 2, 95, cloak_dark)
out.set(mcx - 1, 96, cloak_dark)

# Hood opening visible from behind - the back of the hood
out.set(mcx - 3, 99, cloak_dark)
out.set(mcx + 3, 99, cloak_dark)
out.set(mcx - 3, 100, cloak_dark)
out.set(mcx + 3, 100, cloak_dark)

# Back of the hood/head highlight
out.set(mcx - 1, 97, cloak_mid)
out.set(mcx + 1, 97, cloak_mid)

# === Cloak body (back view) ===
# Shoulders - broad at the top of the cloak
for y in range(105, 114):
    r = 5 if y <= 106 else 6
    for x in range(mcx - r, mcx + r + 1):
        out.set(x, y, cloak_main)

# Shoulder highlights
for y in range(106, 109):
    out.set(mcx - 4, y, cloak_mid)
    out.set(mcx + 4, y, cloak_mid)
out.set(mcx - 5, 107, cloak_hi)
out.set(mcx + 5, 107, cloak_hi)

# Cloak body - descends and narrows
for y in range(114, 136):
    if y < 118:
        r = 5
    elif y < 124:
        r = 4
    elif y < 131:
        r = 3
    else:
        r = 3
    for x in range(mcx - r, mcx + r + 1):
        out.set(x, y, cloak_main)

# Cloak side shading
for y in range(105, 136):
    r = 5 if y <= 106 else 6
    r = r if y < 114 else (5 if y < 118 else (4 if y < 124 else 3))
    out.set(mcx - r, y, cloak_dark)
    out.set(mcx + r, y, cloak_dark)

# Center back crease line
for y in range(102, 132, 2):
    out.set(mcx, y, cloak_dark)

# Cloak folds
for y in range(105, 130, 8):
    out.set(mcx - 2, y, cloak_mid)
    out.set(mcx + 2, y, cloak_mid)

# === Hand holding the staff ===
hy = 112  # hand at hip level, holding the staff
out.set(sx - 1, hy, cloak_mid)
out.set(sx, hy, cloak_hi)
out.set(sx + 1, hy, cloak_mid)
out.set(sx, hy + 1, cloak_mid)

# === Feet at the bottom ===
out.set(mcx - 2, 135, cloak_dark)
out.set(mcx - 1, 136, cloak_dark)
out.set(mcx + 1, 136, cloak_dark)
out.set(mcx + 2, 135, cloak_dark)
out.set(mcx, 136, cloak_dark)

# === Warm light from staff reflecting on nearby surfaces ===
# Light cast on the mage's shoulder from the staff
for dy in range(103, 108):
    out.set(mcx + 4, dy, cloak_mid)
    out.set(mcx + 3, dy, cloak_hi)

# Light glow reflecting on the ground/wall
for dx in range(-2, 4):
    out.set(sx + dx, 124, glow_dim)
    out.set(sx, 120, glow_soft)
    out.set(sx - 1, 121, glow_dim)

# === Final output ===
print(out.stats_text())

# Quick verification of key features
# Verify mage exists at archway center
mage_pixels = 0
for y in range(95, 137):
    for x in range(53, 68):
        if out.get(x, y) not in (0,) and out.get(x, y) in (cloak_dark, cloak_main, cloak_mid, cloak_hi):
            mage_pixels += 1
print(f"Mage pixels in archway: {mage_pixels}")

finish(out)
