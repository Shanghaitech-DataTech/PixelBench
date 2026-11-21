import math

W, H = 135, 85
dx, dy = 15, 8

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, dx, dy)

f2 = new_canvas(W, H, name="f2")
f2.blit(input_canvas, dx, dy)

BLACK = f2.color('#020202')       # c0
DARK_PURPLE = f2.color('#120d1c') # c1
GI_BLUE = f2.color('#454463')     # c3
GI_DARK = f2.color('#231c2c')     # c4
GI_SHADE = f2.color('#3d2c32')    # c5
HAKAMA_LT = f2.color('#926e6b')   # c6
HAKAMA_MID = f2.color('#8a8385')  # c7
HAKAMA_DK = f2.color('#71444c')   # c8
HILT_DK = f2.color('#1b0202')     # c9
SKIN = f2.color('#f3a473')        # c10
WHITE = f2.color('#eedddd')       # c11
GRAY = f2.color('#9b938d')        # c12
SILVER = f2.color('#b2aeb1')      # c13
LIGHT_BLUE = f2.color('#8ca2e4')  # c14

# =========================================================================
# FRAME 2: COMPLETED DRAWN-SWORD SLASH
# =========================================================================

# --- 1. CLEAN UP FRAME 2 TORSO & WAIST ---
for y in range(25, 45):
    for x in range(46, 62):
        f2.set(x + dx, y + dy, None)
for y in range(39, 43):
    for x in range(41, 48):
        f2.set(x + dx, y + dy, None)

# Torso body fill (solid gi with proper shading)
for y in range(25, 40):
    for x in range(43, 49):
        f2.set(x + dx, y + dy, GI_BLUE)
    f2.set(49 + dx, y + dy, GI_DARK)
    f2.set(50 + dx, y + dy, DARK_PURPLE)

for y in range(32, 40):
    f2.set(46 + dx, y + dy, GI_DARK)
    f2.set(47 + dx, y + dy, GI_DARK)
    f2.set(48 + dx, y + dy, GI_DARK)

# Obi / belt / waist transition
for x in range(41, 49):
    f2.set(x + dx, 40 + dy, DARK_PURPLE)
    f2.set(x + dx, 41 + dy, HAKAMA_MID)
    f2.set(x + dx, 42 + dy, HAKAMA_LT)
    f2.set(x + dx, 43 + dy, HAKAMA_DK)
    f2.set(x + dx, 44 + dy, HAKAMA_DK)

# Empty scabbard mouth (koiguchi) - sword drawn!
f2.set(40 + dx, 41 + dy, HILT_DK)
f2.set(40 + dx, 42 + dy, DARK_PURPLE)
f2.set(41 + dx, 41 + dy, HILT_DK)
f2.set(41 + dx, 42 + dy, DARK_PURPLE)

# Hair trailing slightly
f2.set(31 + dx, 8 + dy, DARK_PURPLE)
f2.set(30 + dx, 9 + dy, DARK_PURPLE)
f2.set(29 + dx, 10 + dy, DARK_PURPLE)

# --- 2. DRAW LEFT ARM & SLEEVE (SWUNG FORWARD-UP) ---
sleeve_poly = [
    (48, 25), (55, 21), (62, 18), (69, 17), (72, 18),
    (73, 23), (69, 28), (64, 30), (58, 31), (52, 30), (48, 28)
]
f2.poly([(x + dx, y + dy) for x, y in sleeve_poly], GI_BLUE)

# Outlines
f2.line(48 + dx, 25 + dy, 69 + dx, 17 + dy, DARK_PURPLE)
f2.line(69 + dx, 17 + dy, 72 + dx, 18 + dy, DARK_PURPLE)
f2.line(48 + dx, 28 + dy, 52 + dx, 30 + dy, DARK_PURPLE)
f2.line(52 + dx, 30 + dy, 58 + dx, 31 + dy, DARK_PURPLE)
f2.line(58 + dx, 31 + dy, 64 + dx, 30 + dy, DARK_PURPLE)
f2.line(64 + dx, 30 + dy, 69 + dx, 28 + dy, DARK_PURPLE)
f2.line(69 + dx, 28 + dy, 73 + dx, 23 + dy, DARK_PURPLE)

# Shading inside sleeve folds
for x in range(53, 64):
    f2.set(x + dx, 29 + dy, GI_DARK)
for x in range(56, 68):
    f2.set(x + dx, 27 + dy, GI_DARK)
    f2.set(x + dx, 28 + dy, GI_DARK)

# Cuff opening
f2.line(70 + dx, 18 + dy, 73 + dx, 23 + dy, DARK_PURPLE)
f2.set(71 + dx, 19 + dy, DARK_PURPLE)
f2.set(72 + dx, 20 + dy, DARK_PURPLE)

# Forearm extending from cuff to hand
for x in range(71, 78):
    f2.set(x + dx, 18 + dy, SKIN)
    f2.set(x + dx, 19 + dy, SKIN)
f2.set(72 + dx, 17 + dy, DARK_PURPLE)
f2.set(73 + dx, 17 + dy, SKIN)
f2.set(74 + dx, 17 + dy, SKIN)
f2.set(75 + dx, 17 + dy, SKIN)
f2.set(76 + dx, 17 + dy, DARK_PURPLE)

# Left hand gripping the hilt
hand_pixels = [
    (77, 17, DARK_PURPLE), (77, 18, SKIN), (77, 19, SKIN), (77, 20, DARK_PURPLE),
    (78, 16, DARK_PURPLE), (78, 17, SKIN), (78, 18, SKIN), (78, 19, SKIN), (78, 20, DARK_PURPLE),
    (79, 15, DARK_PURPLE), (79, 16, SKIN), (79, 17, SKIN), (79, 18, SKIN), (79, 19, DARK_PURPLE),
    (80, 15, SKIN), (80, 16, SKIN), (80, 17, SKIN), (80, 18, DARK_PURPLE),
    (81, 14, DARK_PURPLE), (81, 15, SKIN), (81, 16, SKIN), (81, 17, DARK_PURPLE),
    (82, 14, DARK_PURPLE), (82, 15, DARK_PURPLE)
]
for x, y, c in hand_pixels:
    f2.set(x + dx, y + dy, c)

# Hilt & Pommel
f2.set(73 + dx, 22 + dy, WHITE)
f2.set(74 + dx, 22 + dy, WHITE)
f2.set(74 + dx, 21 + dy, HILT_DK)
f2.set(75 + dx, 21 + dy, HAKAMA_DK)
f2.set(76 + dx, 20 + dy, HILT_DK)
f2.set(77 + dx, 20 + dy, HAKAMA_DK)

# Guard (tsuba)
f2.set(81 + dx, 13 + dy, WHITE)
f2.set(82 + dx, 13 + dy, SILVER)
f2.set(82 + dx, 14 + dy, WHITE)
f2.set(83 + dx, 14 + dy, GRAY)
f2.set(83 + dx, 15 + dy, DARK_PURPLE)

# Katana Blade position:
blade_start_x = 84 + dx # 99
blade_start_y = 13 + dy # 21
blade_end_x = 114 + dx   # 129
blade_end_y = 3 + dy    # 11
blade_len = blade_end_x - blade_start_x + 1

# --- 3. THE BLACK SLASH TRAIL ---
# Sweeping from lower left up to upper right, ending on the completed slash.
outer_pts = []
for t in range(60):
    u = t / 59.0
    x = (1-u)**2 * 18 + 2*(1-u)*u * 68 + u**2 * blade_end_x
    y = (1-u)**2 * 68 + 2*(1-u)*u * 52 + u**2 * blade_end_y
    outer_pts.append((int(round(x)), int(round(y))))

blade_edge_pts = []
for i in range(blade_len):
    bx = blade_end_x - i
    by = blade_end_y + int(round(i * (blade_start_y - blade_end_y) / float(blade_len - 1)))
    blade_edge_pts.append((bx, by))

inner_pts = []
for t in range(60):
    u = t / 59.0
    x = (1-u)**2 * (blade_start_x) + 2*(1-u)*u * 76 + u**2 * 18
    y = (1-u)**2 * (blade_start_y + 3) + 2*(1-u)*u * 66 + u**2 * 68
    inner_pts.append((int(round(x)), int(round(y))))

trail_poly = outer_pts + blade_edge_pts + inner_pts
f2.poly(trail_poly, BLACK)

# Clean, sharp tapered tail at lower left (solid, no floating detached dots):
f2.line(18, 68, 14, 69, BLACK)
f2.line(19, 69, 15, 70, BLACK)
f2.line(22, 70, 18, 71, BLACK)

# Draw the Katana Blade crisp and gleaming on top of the leading edge:
for i in range(blade_len):
    bx = blade_start_x + i
    by = blade_start_y - int(round(i * (blade_start_y - blade_end_y) / float(blade_len - 1)))
    f2.set(bx, by, WHITE)
    f2.set(bx, by + 1, SILVER)
    f2.set(bx, by + 2, DARK_PURPLE)

# Blade tip & kissaki
f2.set(blade_end_x, blade_end_y, WHITE)
f2.set(blade_end_x + 1, blade_end_y - 1, WHITE)
f2.set(blade_end_x + 1, blade_end_y, SILVER)

# Sharp black slash point extending just past blade tip
f2.set(blade_end_x + 2, blade_end_y - 1, BLACK)
f2.set(blade_end_x + 3, blade_end_y - 2, BLACK)

view(f1)
view(f2)
finish([f1, f2])
