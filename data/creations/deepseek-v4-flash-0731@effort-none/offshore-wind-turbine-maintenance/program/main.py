from pixelbench_api import new_canvas, finish, canvas, input_canvas

W, H = 64, 64
c = new_canvas(W, H, background=None, name="offshore_wind")

# ---- Palette ----
# Sky
SKY_TOP = c.color("#7db4e0", name="sky_top")
SKY_MID = c.color("#a5cce8", name="sky_mid")
SKY_LOW = c.color("#cfe6f2", name="sky_low")
CLOUD_LIGHT = c.color("#f5fbfe", name="cloud_light")
CLOUD_SHADOW = c.color("#d8ecf5", name="cloud_shadow")

# Ocean
SEA_DEEP = c.color("#1c4e7c", name="sea_deep")
SEA_MID = c.color("#2a6a9e", name="sea_mid")
SEA_LIGHT = c.color("#3f86b8", name="sea_light")
WAVE = c.color("#e8f4fa", name="wave_foam")

# Foreground structure (steel)
STEEL_DARK = c.color("#3a4a5a", name="steel_dark")
STEEL_MID = c.color("#5a6e7e", name="steel_mid")
STEEL_LIGHT = c.color("#7d96a6", name="steel_light")
STEEL_HI = c.color("#a9c0cc", name="steel_hi")

# Structure accent (yellow/gray)
ACCENT_DARK = c.color("#8a6d1f", name="accent_dark")
ACCENT = c.color("#d4a834", name="accent")
ACCENT_LIGHT = c.color("#f0d060", name="accent_light")

# Technician
TECH_SUIT = c.color("#e8792a", name="tech_suit")
TECH_SUIT_DARK = c.color("#c0601f", name="tech_suit_dark")
TECH_HELMET = c.color("#2a4a8a", name="tech_helmet")
TECH_SKIN = c.color("#e0a878", name="tech_skin")
TECH_BOOT = c.color("#4a2a12", name="tech_boot")

# Distant turbines
DIST_TURBINE = c.color("#6a8a9a", name="dist_turbine")
DIST_TURBINE_DARK = c.color("#5a7a8a", name="dist_turbine_dark")

# Distant tower color
TOWER_FAR = c.color("#708a99", name="tower_far")

# Turbine main body
TURBINE_WHITE = c.color("#dbe6ee", name="turbine_white")
TURBINE_SHADOW = c.color("#a8bcc8", name="turbine_shadow")

# ---- Sky ----
for y in range(0, 30):
    for x in range(0, W):
        if y < 12:
            c.set(x, y, SKY_TOP)
        elif y < 22:
            c.set(x, y, SKY_MID)
        else:
            c.set(x, y, SKY_LOW)

# ---- Distant turbines (background, behind ocean) ----
# Turbine 1 (farthest, left)
t1_x = 14
t1_base_y = 30
# tower
for i in range(6):
    w_ = 2 if i < 3 else 1
    for dx in range(w_):
        c.set(t1_x - w_ + dx + w_//2, t1_base_y - i, TOWER_FAR)
# blades - simple crosses
for a in range(7):
    c.set(t1_x - 3 + a, t1_base_y - 9, DIST_TURBINE_DARK)
for a in range(5):
    c.set(t1_x - 2 + a, t1_base_y - 8, DIST_TURBINE_DARK)
c.set(t1_x, t1_base_y - 7, DIST_TURBINE_DARK)
# nacelle
c.set(t1_x - 1, t1_base_y - 8, DIST_TURBINE)
c.set(t1_x, t1_base_y - 8, DIST_TURBINE)
c.set(t1_x, t1_base_y - 9, DIST_TURBINE)

# Turbine 2 (mid distance, more right)
t2_x = 48
t2_base_y = 24
# tower
for i in range(8):
    w_ = 3 if i < 4 else 2
    for dx in range(w_):
        c.set(t2_x - w_ + dx + w_//2, t2_base_y - i, TOWER_FAR)
# blades
for a in range(9):
    c.set(t2_x - 4 + a, t2_base_y - 14, TOWER_FAR)
for a in range(7):
    c.set(t2_x - 3 + a, t2_base_y - 12, TOWER_FAR)
for a in range(5):
    c.set(t2_x - 2 + a, t2_base_y - 10, TOWER_FAR)
# nacelle
c.set(t2_x - 1, t2_base_y - 10, DIST_TURBINE)
c.set(t2_x, t2_base_y - 10, DIST_TURBINE)
c.set(t2_x, t2_base_y - 9, DIST_TURBINE)

# ---- Ocean ----
for y in range(31, 50):
    for x in range(0, W):
        if y < 36:
            c.set(x, y, SEA_LIGHT)
        elif y < 43:
            c.set(x, y, SEA_MID)
        else:
            c.set(x, y, SEA_DEEP)

# ---- Main turbine (foreground, tall) ----
# Tower (tapered, from base of platform up)
TOWER_BASE_Y = 42
tower_x = 24
for i in range(26):
    y = TOWER_BASE_Y - i
    if y < 0:
        break
    half_w = 4 - (i // 5)  # taper
    if half_w < 1:
        half_w = 1
    for dx in range(half_w * 2):
        x = tower_x - half_w + dx
        c.set(x, y, TURBINE_SHADOW if x == tower_x - half_w + dx == 0 else TURBINE_WHITE)

# Simplify tower: draw with rects per section
tower_x = 25
TURBINE_WHITE = c.color("#dbe6ee")  # reuse
TURBINE_SHADOW = c.color("#a8bcc8")

c.clear()
# Redraw sky
for y in range(0, 30):
    for x in range(0, W):
        if y < 12:
            c.set(x, y, SKY_TOP)
        elif y < 22:
            c.set(x, y, SKY_MID)
        else:
            c.set(x, y, SKY_LOW)

# Redraw distant turbines
# Turbine 1 (farthest, left)
t1_x = 14
t1_base_y = 30
for i in range(6):
    w_ = 2 if i < 3 else 1
    for dx in range(w_):
        c.set(t1_x - w_ + dx + w_//2, t1_base_y - i, TOWER_FAR)
# blades - small cross/diagonal
for a in range(7):
    c.set(t1_x - 3 + a, t1_base_y - 9, DIST_TURBINE_DARK)
for a in range(5):
    c.set(t1_x - 2 + a, t1_base_y - 8, DIST_TURBINE_DARK)
for a in range(3):
    c.set(t1_x - 1 + a, t1_base_y - 7, DIST_TURBINE_DARK)
# nacelle
c.set(t1_x - 1, t1_base_y - 8, DIST_TURBINE)
c.set(t1_x, t1_base_y - 8, DIST_TURBINE)
c.set(t1_x, t1_base_y - 9, DIST_TURBINE)
# vertical blade
for a in range(5):
    c.set(t1_x, t1_base_y - 12 + a, DIST_TURBINE_DARK)
# down blades
c.set(t1_x - 2, t1_base_y - 6, DIST_TURBINE_DARK)
c.set(t1_x - 1, t1_base_y - 5, DIST_TURBINE_DARK)
c.set(t1_x + 2, t1_base_y - 6, DIST_TURBINE_DARK)

# Turbine 2 (mid, right)
t2_x = 48
t2_base_y = 24
for i in range(10):
    w_ = 3 if i < 5 else 2
    for dx in range(w_):
        c.set(t2_x - w_ + dx + w_//2, t2_base_y - i, TOWER_FAR)
# nacelle (compact)
c.rect(t2_x - 2, t2_base_y - 10, 5, 3, DIST_TURBINE)
c.set(t2_x + 2, t2_base_y - 11, DIST_TURBINE)
# three blades - subtle, visible against sky
c.line(t2_x, t2_base_y - 13, t2_x + 4, t2_base_y - 17, DIST_TURBINE_DARK)
c.line(t2_x - 1, t2_base_y - 1, t2_x - 4, t2_base_y + 2, DIST_TURBINE_DARK)
c.line(t2_x + 2, t2_base_y - 1, t2_x + 5, t2_base_y + 1, DIST_TURBINE_DARK)
# short blade connecting to nacelle
c.set(t2_x + 1, t2_base_y - 11, DIST_TURBINE_DARK)
c.set(t2_x + 2, t2_base_y - 12, DIST_TURBINE_DARK)

# ---- Ocean ----
for y in range(31, 50):
    for x in range(0, W):
        if y < 36:
            c.set(x, y, SEA_LIGHT)
        elif y < 43:
            c.set(x, y, SEA_MID)
        else:
            c.set(x, y, SEA_DEEP)

# ---- Main turbine tower ----
tw = 25
# Tower from y=13 to y=44 (goes below the water line)
for y in range(44, 12, -1):
    # tower width tapers: wider at bottom
    half_w = 3 if y > 30 else 2
    if y > 38:
        half_w = 4
    elif y > 34:
        half_w = 3
    for dx in range(half_w*2):
        x = tw - half_w + dx
        if x >= 0 and x < W:
            # shading: left dark, right light edge
            if dx == 0:
                c.set(x, y, TURBINE_SHADOW)
            elif dx == half_w*2 - 1:
                c.set(x, y, TURBINE_SHADOW)
            else:
                c.set(x, y, TURBINE_WHITE)

# Nacelle and hub for main turbine
for dx in range(6):
    c.set(tw - 3 + dx, 12, TURBINE_WHITE)
for dx in range(6):
    c.set(tw - 3 + dx, 13, TURBINE_WHITE)
# upper part of nacelle
for dx in range(4):
    c.set(tw - 2 + dx, 11, TURBINE_SHADOW)
c.set(tw + 3, 11, TURBINE_SHADOW)
# silouette of the nacelle base
c.set(tw - 4, 12, TURBINE_SHADOW)
c.set(tw + 3, 12, TURBINE_SHADOW)
# hub
c.set(tw - 1, 10, TURBINE_WHITE)
c.set(tw, 10, TURBINE_WHITE)
c.set(tw - 1, 11, TURBINE_WHITE)
c.set(tw, 11, TURBINE_SHADOW)
# small wind vane on top of nacelle
c.set(tw - 1, 10, STEEL_DARK)
c.set(tw, 9, STEEL_DARK)
c.set(tw + 1, 10, STEEL_LIGHT)

# Blades for main turbine - three blades pointing up-right, down-left, down-right
# Blade 1: up-right (main blade) - clean diagonal from hub
for i in range(15):
    bx = tw + 1 + i
    by = 11 - i
    if bx < W and by >= 0:
        if i % 2 == 0:
            c.set(bx, by, TURBINE_SHADOW)
        else:
            c.set(bx, by, TURBINE_WHITE)
        # blade has two-pixel width
        c.set(bx + 1, by, TURBINE_SHADOW) if i < 8 else c.set(bx, by, TURBINE_SHADOW)

# Blade 2: down-left
for i in range(12):
    bx = tw - 2 - i
    by = 13 + i
    if bx >= 0 and by < 42:
        if i % 2 == 0:
            c.set(bx, by, TURBINE_SHADOW)
        else:
            c.set(bx, by, TURBINE_WHITE)

# Blade 3: down-right
for i in range(12):
    bx = tw + 2 + i
    by = 13 + i // 2
    if bx < W and by < 42:
        if i % 2 == 0:
            c.set(bx, by, TURBINE_SHADOW)
        else:
            c.set(bx, by, TURBINE_WHITE)

# ---- Maintenance platform (around tower base, above water) ----
plat_top = 43
plat_w = 24
plat_x = tw - plat_w // 2

# Platform deck - solid structure
c.rect(plat_x, plat_top, plat_w, 2, STEEL_MID)
# platform edge highlight
c.rect(plat_x, plat_top, plat_w, 1, STEEL_LIGHT)
# railing posts
for px in range(plat_x, plat_x + plat_w, 2):
    c.set(px, plat_top - 3, STEEL_MID)
# top handrail
c.rect(plat_x - 1, plat_top - 4, plat_w + 2, 1, STEEL_MID)
c.rect(plat_x - 1, plat_top - 4, plat_w + 2, 1, STEEL_LIGHT)
# mid rail
c.rect(plat_x - 1, plat_top - 1, plat_w + 2, 1, STEEL_DARK)

# Platform support legs (diagonal from tower to platform edge)
for i in range(8):
    c.set(tw - 5 - i, plat_top + i, STEEL_DARK)
for i in range(8):
    c.set(tw + 5 + i, plat_top + i, STEEL_DARK)

# Ladder from platform up the tower
ladder_y = 18
c.line(tw - 5, ladder_y, tw - 5, plat_top - 1, STEEL_MID)
c.line(tw + 5, ladder_y, tw + 5, plat_top - 1, STEEL_MID)
# rungs
for ry in range(ladder_y + 1, plat_top - 2, 3):
    c.line(tw - 5, ry, tw + 5, ry, STEEL_LIGHT)
# safety cage hoops around ladder (every few rungs)
for ry in range(ladder_y + 3, plat_top - 2, 7):
    c.set(tw - 7, ry, STEEL_MID)
    c.set(tw - 6, ry - 1, STEEL_MID)
    c.set(tw + 6, ry - 1, STEEL_MID)
    c.set(tw + 7, ry, STEEL_MID)
    c.set(tw - 7, ry + 1, STEEL_DARK)
    c.set(tw + 7, ry + 1, STEEL_DARK)

# ---- Technician climbing ladder ----
# Position: around y=29 on the ladder, between rails
tech_y = 29
tech_x = tw  # center
# Back of head / helmet
c.set(tech_x - 1, tech_y - 3, TECH_HELMET)
c.set(tech_x, tech_y - 3, TECH_HELMET)
c.set(tech_x + 1, tech_y - 3, TECH_HELMET)
c.set(tech_x - 1, tech_y - 2, TECH_HELMET)
c.set(tech_x, tech_y - 2, TECH_HELMET)
# face (skin) - seen from back/side
c.set(tech_x - 1, tech_y - 1, TECH_SKIN)
c.set(tech_x, tech_y - 1, TECH_SKIN)
# torso - suit
c.set(tech_x - 2, tech_y, TECH_SUIT)
c.set(tech_x - 1, tech_y, TECH_SUIT)
c.set(tech_x, tech_y, TECH_SUIT)
c.set(tech_x + 1, tech_y, TECH_SUIT)
c.set(tech_x - 2, tech_y + 1, TECH_SUIT_DARK)
c.set(tech_x - 1, tech_y + 1, TECH_SUIT_DARK)
c.set(tech_x, tech_y + 1, TECH_SUIT_DARK)
c.set(tech_x + 1, tech_y + 1, TECH_SUIT_DARK)
# safety harness strap (accent)
c.set(tech_x - 2, tech_y, ACCENT)
c.set(tech_x + 1, tech_y, ACCENT)
# right arm reaching up to grab rail
c.set(tech_x + 2, tech_y - 2, TECH_SUIT)
c.set(tech_x + 2, tech_y - 1, TECH_SUIT)
# right hand on ladder rail
c.set(tech_x + 3, tech_y - 2, TECH_SKIN)
# left arm down at side
c.set(tech_x - 3, tech_y, TECH_SUIT)
# legs
c.set(tech_x - 1, tech_y + 2, TECH_SUIT_DARK)
c.set(tech_x, tech_y + 2, TECH_SUIT_DARK)
c.set(tech_x - 1, tech_y + 3, TECH_BOOT)
c.set(tech_x, tech_y + 3, TECH_BOOT)
# second boot on a lower rung
c.set(tech_x - 2, tech_y + 4, TECH_BOOT)
# safety lanyard/harness line going to the ladder
c.line(tech_x + 1, tech_y - 3, tech_x + 4, tech_y - 6, ACCENT_LIGHT)

# ---- Waves / sea surface details ----
# foam lines at water's edge
for fx in range(0, 64, 4):
    fo = (fx // 4) % 3
    c.set(fx, 31, WAVE)
    c.set(fx + 1, 31, WAVE)
for fx in range(2, 64, 5):
    fo = (fx // 5) % 2
    if fo == 0:
        c.set(fx, 33, WAVE)
for fx in range(1, 64, 6):
    c.set(fx, 35, SEA_LIGHT)
for fx in range(3, 64, 7):
    c.set(fx, 38, SEA_MID)
# wave texture
for fx in range(0, 64, 4):
    c.set(fx, 37, SEA_LIGHT)
for fx in range(2, 64, 5):
    c.set(fx, 41, SEA_LIGHT)
# highlight sparkles
for fx in range(0, 64, 8):
    c.set(fx, 40, SEA_MID)
    c.set(fx + 1, 41, SEA_MID)
# wave crest lines (more detailed waves)
for fx in range(0, 64, 3):
    c.set(fx, 32, WAVE) if fx % 6 == 0 else c.set(fx, 32, SEA_LIGHT)
# additional wave ripples
for fx in range(1, 64, 5):
    c.set(fx, 34, SEA_LIGHT)
for fx in range(0, 64, 6):
    c.set(fx, 39, SEA_MID)
# foam near turbine base
for fx in range(14, 38, 2):
    if fx % 4 == 0:
        c.set(fx, 42, WAVE)

# ---- Birds (for scale) ----
# bird 1
c.set(36, 6, STEEL_DARK)
c.set(37, 5, STEEL_DARK)
c.set(38, 6, STEEL_DARK)
# bird 2
c.set(52, 4, STEEL_DARK)
c.set(53, 3, STEEL_DARK)
c.set(54, 4, STEEL_DARK)

# ---- Distant ship on horizon ----
# A small workboat near the turbine
c.rect(5, 32, 4, 1, STEEL_DARK)
c.set(5, 31, STEEL_DARK)
c.set(6, 31, STEEL_DARK)
c.set(5, 30, STEEL_DARK)
c.set(6, 30, STEEL_DARK)
# wake
c.set(3, 32, WAVE)
c.set(9, 32, WAVE)

# ---- Clouds ----
# cloud 1
for dx in range(8):
    c.set(4 + dx, 5, CLOUD_LIGHT) if dx not in (0, 7) else c.set(4 + dx, 5, CLOUD_SHADOW)
c.set(5, 4, CLOUD_LIGHT)
c.set(6, 4, CLOUD_LIGHT)
c.set(9, 4, CLOUD_LIGHT)
c.set(5, 6, CLOUD_SHADOW)
c.set(6, 6, CLOUD_SHADOW)
c.set(7, 6, CLOUD_SHADOW)

# cloud 2
for dx in range(10):
    c.set(44 + dx, 8, CLOUD_LIGHT) if dx not in (0, 9) else c.set(44 + dx, 8, CLOUD_SHADOW)
c.set(45, 7, CLOUD_LIGHT)
c.set(46, 7, CLOUD_LIGHT)
c.set(48, 7, CLOUD_LIGHT)
c.set(49, 9, CLOUD_SHADOW)
c.set(50, 9, CLOUD_SHADOW)

# cloud 3 (small)
c.set(30, 16, CLOUD_SHADOW)
c.set(31, 16, CLOUD_LIGHT)
c.set(32, 16, CLOUD_LIGHT)
c.set(33, 16, CLOUD_LIGHT)
c.set(34, 16, CLOUD_SHADOW)
c.set(31, 15, CLOUD_LIGHT)
# cloud 4 (low, near horizon)
c.set(56, 20, CLOUD_SHADOW)
c.set(57, 20, CLOUD_LIGHT)
c.set(58, 20, CLOUD_LIGHT)
c.set(59, 20, CLOUD_LIGHT)
c.set(60, 20, CLOUD_SHADOW)
c.set(57, 19, CLOUD_LIGHT)

# ---- Ocean reflection of main turbine tower ----
for y in range(45, 50):
    for dx in range(5):
        c.set(tw - 2 + dx, y, SEA_DEEP)

# Tower extends into the water with a base/jacket structure
# The tower narrows to the water surface with a broader base
for y in range(40, 44):
    half_w = 3  # narrower at the top of water
    for dx in range(half_w * 2):
        x = tw - half_w + dx
        if 0 <= x < W:
            if dx == 0 or dx == half_w * 2 - 1:
                c.set(x, y, STEEL_DARK)
            else:
                c.set(x, y, STEEL_MID)

# Jacket/foundation base wider in the water
for y in range(44, 50):
    half_w = 5  # foundation wider
    for dx in range(half_w * 2):
        x = tw - half_w + dx
        if 0 <= x < W:
            if dx == 0 or dx == half_w * 2 - 1:
                c.set(x, y, STEEL_DARK)
            else:
                c.set(x, y, STEEL_MID) if y % 3 == 0 else c.set(x, y, SEA_DEEP)

# Jacket/foundation legs more visible in the water
for dy in range(0, 5):
    c.set(tw - 5, 45 + dy, STEEL_DARK)
    c.set(tw + 5, 45 + dy, STEEL_DARK)

# Cross braces on the jacket
for dy in range(0, 3):
    c.set(tw - 3 + dy, 44 + dy, STEEL_DARK)
for dy in range(0, 3):
    c.set(tw + 3 - dy, 44 + dy, STEEL_DARK)

# Structural platform braces below deck
for i in range(4):
    c.set(plat_x + i, plat_top + 2 + i, STEEL_DARK)
for i in range(4):
    c.set(plat_x + plat_w - 1 - i, plat_top + 2 + i, STEEL_DARK)

# Helper details on platform: small box/equipment crate
c.set(plat_x + 3, plat_top - 1, ACCENT)
c.set(plat_x + 4, plat_top - 1, ACCENT)
c.set(plat_x + 3, plat_top - 2, ACCENT_DARK)
c.set(plat_x + 4, plat_top - 2, ACCENT_DARK)
# another equipment piece near the tower
c.set(plat_x + 9, plat_top - 3, ACCENT_DARK)
c.set(plat_x + 10, plat_top - 3, ACCENT_DARK)
c.set(plat_x + 9, plat_top - 2, ACCENT)
c.set(plat_x + 10, plat_top - 2, ACCENT)
# small crane on the platform edge
c.set(plat_x + 6, plat_top - 6, STEEL_MID)
c.set(plat_x + 6, plat_top - 5, STEEL_MID)
c.set(plat_x + 7, plat_top - 7, STEEL_MID)
c.line(plat_x + 6, plat_top - 7, plat_x + 14, plat_top - 8, STEEL_LIGHT)
# crane cable
c.line(plat_x + 12, plat_top - 8, plat_x + 12, plat_top - 5, STEEL_MID)
# crane hook block
c.set(plat_x + 11, plat_top - 5, STEEL_DARK)
c.set(plat_x + 12, plat_top - 5, STEEL_DARK)

# Bottom darkening of ocean
for y in range(47, 50):
    for x in range(0, W):
        c.set(x, y, SEA_DEEP)

print(c.stats_text())
result = c
finish(result)
