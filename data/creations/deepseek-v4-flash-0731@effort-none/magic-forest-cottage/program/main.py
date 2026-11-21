from pixelbench_api import new_canvas, finish

W, H = 128, 128
c = new_canvas(W, H)

# === Define palette colors ===
# Sky - deep purple night
sky = c.color((18, 12, 42))
sky2 = c.color((26, 18, 56))
sky3 = c.color((38, 28, 72))
sky4 = c.color((52, 40, 90))
star = c.color((235, 230, 255))

# Moon
moon = c.color((245, 240, 220))
moon_glow = c.color((210, 200, 180))

# Mist
mist = c.color((90, 80, 130, 110))
mist2 = c.color((70, 62, 105, 90))
mist3 = c.color((50, 44, 80, 80))

# Ground / dirt
ground = c.color((22, 18, 34))
ground2 = c.color((30, 24, 42))
path_stone = c.color((60, 52, 74))
path_stone2 = c.color((48, 42, 62))
path_stone3 = c.color((72, 64, 88))

# Cottage wood
wood = c.color((52, 32, 24))
wood2 = c.color((68, 44, 32))
wood3 = c.color((84, 56, 40))
wood4 = c.color((38, 24, 18))

# Stone parts
stone = c.color((70, 66, 82))
stone2 = c.color((56, 52, 68))
stone3 = c.color((86, 80, 96))

# Roof - mossy
roof = c.color((36, 40, 30))
roof2 = c.color((48, 54, 38))
roof3 = c.color((56, 62, 44))
moss = c.color((42, 52, 34))
moss2 = c.color((60, 68, 44))
moss3 = c.color((74, 84, 54))

# Window light - warm orange
win_light = c.color((255, 180, 80))
win_light2 = c.color((255, 160, 60))
win_light3 = c.color((230, 130, 50))
win_frame = c.color((30, 20, 16))

# Trees
trunk = c.color((40, 26, 30))
trunk2 = c.color((54, 36, 42))
trunk3 = c.color((30, 20, 24))
branch = c.color((46, 30, 34))

# Leaves - dark red brown purple
leaf1 = c.color((58, 24, 44))
leaf2 = c.color((72, 30, 52))
leaf3 = c.color((46, 20, 38))
leaf4 = c.color((86, 42, 62))
leaf5 = c.color((64, 28, 48))

# Well
well_stone = c.color((64, 60, 78))
well_stone2 = c.color((50, 46, 62))
well_wood = c.color((56, 36, 28))

# Stone slab path
slab = c.color((66, 58, 80))
slab2 = c.color((52, 46, 66))

# === Fill sky ===
c.rect(0, 0, W, H, sky)

# Sky gradient bands
for y in range(0, 40):
    c.rect(0, y, W, 1, sky)
for y in range(40, 60):
    c.rect(0, y, W, 1, sky2)
for y in range(60, 76):
    c.rect(0, y, W, 1, sky3)
for y in range(76, 88):
    c.rect(0, y, W, 1, sky4)

# === Stars ===
stars = [(10, 12), (22, 5), (35, 18), (48, 8), (60, 15), (72, 6), (85, 20),
         (98, 10), (110, 22), (118, 8), (15, 30), (40, 35), (65, 28), (90, 32),
         (105, 40), (5, 45), (55, 48), (95, 50), (120, 55), (28, 55),
         (75, 42), (112, 30), (8, 20), (44, 12), (88, 6)]
for sx, sy in stars:
    c.set(sx, sy, star)
# A few dimmer stars
dimmer = [(18, 40), (32, 25), (52, 30), (68, 35), (80, 45), (100, 28), (115, 40),
           (25, 8), (95, 15), (50, 42), (8, 52), (120, 18)]
for sx, sy in dimmer:
    c.set(sx, sy, c.color((180, 175, 210)))

# === Moon ===
moon_cx, moon_cy = 96, 30
# Glow
c.circle(moon_cx, moon_cy, 12, moon_glow)
# Moon body
c.circle(moon_cx, moon_cy, 8, moon)
# Moon crater details
c.set(moon_cx - 3, moon_cy - 2, c.color((230, 220, 200)))
c.set(moon_cx + 2, moon_cy + 1, c.color((230, 220, 200)))
c.set(moon_cx + 1, moon_cy + 3, c.color((225, 215, 195)))
c.set(moon_cx + 4, moon_cy - 2, c.color((230, 220, 200)))

# === Ground ===
c.rect(0, 88, W, H - 88, ground)
c.rect(0, 88, W, 2, ground2)

# === Background trees (twisted ancient) ===
# Left large tree trunk
c.poly([(18, 88), (22, 60), (26, 45), (28, 35), (32, 28), (36, 22), (34, 14),
        (30, 18), (30, 30), (24, 42), (20, 55), (16, 70), (10, 88)], trunk)
# Branches
c.line(32, 28, 42, 18, trunk)
c.line(30, 35, 18, 30, trunk)
c.line(24, 42, 14, 38, trunk)
c.line(22, 60, 40, 50, trunk)
c.line(20, 55, 8, 48, trunk)

# Right tree trunk
c.poly([(100, 88), (98, 70), (96, 55), (94, 40), (92, 30), (90, 24), (92, 18),
        (96, 24), (98, 36), (100, 50), (102, 65), (104, 78), (108, 88)], trunk)
c.line(92, 24, 82, 16, trunk)
c.line(94, 35, 80, 30, trunk)
c.line(96, 50, 84, 42, trunk)
c.line(98, 65, 110, 55, trunk)
c.line(94, 40, 108, 34, trunk)

# === Cottage ===
cw_left, cw_right = 44, 84
cottage_top = 52

# Stone base of cottage
c.rect(cw_left - 2, cottage_top + 6, cw_right - cw_left + 4, 10, stone)
# Stone detail
for sy in range(cottage_top + 6, cottage_top + 16, 5):
    for sx in range(cw_left - 2, cw_right + 2, 8):
        c.set(sx, sy, stone2)
        c.set(sx + 4, sy + 2, stone3)

# Wooden body
c.rect(cw_left, cottage_top + 2, cw_right - cw_left, 28, wood)
# Wood plank lines (horizontal)
for wy in range(cottage_top + 2, cottage_top + 30, 4):
    c.line(cw_left, wy, cw_right, wy, wood4)
# Wood shading
c.rect(cw_left, cottage_top + 2, cw_right - cw_left, 6, wood2)
c.rect(cw_left, cottage_top + 8, cw_right - cw_left, 4, wood3)

# == Roof - steep mossy ==
roof_left = cw_left - 8
roof_right = cw_right + 8
ridge_y = cottage_top - 12
eave_y = cottage_top + 2

c.poly([(roof_left, eave_y), ((cw_left + cw_right) // 2, ridge_y), (roof_right, eave_y)], roof)
# Moss patches
c.poly([(roof_left + 4, eave_y - 4), (roof_left + 15, eave_y - 12), (roof_left + 22, eave_y - 3)], roof2)
c.poly([(roof_right - 5, eave_y - 4), (roof_right - 17, eave_y - 12), (roof_right - 24, eave_y - 3)], roof3)
c.poly([(cw_left, eave_y - 6), (cw_left + 8, eave_y - 8), (cw_left + 14, eave_y - 4), (cw_left + 6, eave_y - 2)], moss2)
c.poly([(cw_right, eave_y - 6), (cw_right - 8, eave_y - 8), (cw_right - 14, eave_y - 4), (cw_right - 6, eave_y - 2)], moss3)
c.poly([(cw_left + 18, eave_y - 5), (cw_left + 28, eave_y - 10), (cw_left + 35, eave_y - 4)], moss)
c.poly([(cw_right - 18, eave_y - 5), (cw_right - 28, eave_y - 10), (cw_right - 35, eave_y - 4)], moss2)
c.poly([(cw_left + 6, eave_y - 8), (cw_left + 20, eave_y - 12), (cw_left + 30, eave_y - 7), (cw_left + 15, eave_y - 4)], moss3)

# == Windows (warm light) ==
# Window 1
win1_x, win1_y = cw_left + 6, cottage_top + 8
win1_w, win1_h = 8, 10
c.rect(win1_x, win1_y, win1_w, win1_h, win_light)
c.rect(win1_x + 1, win1_y + 1, win1_w - 2, win1_h - 2, win_light2)
c.line(win1_x + 4, win1_y, win1_x + 4, win1_y + win1_h, win_frame)
c.line(win1_x, win1_y + 5, win1_x + win1_w, win1_y + 5, win_frame)
c.rect(win1_x, win1_y, win1_w, win1_h, win_frame, fill=False)

# Window 2
win2_x, win2_y = cw_left + 24, cottage_top + 8
c.rect(win2_x, win2_y, 8, 10, win_light)
c.rect(win2_x + 1, win2_y + 1, 6, 8, win_light2)
c.line(win2_x + 4, win2_y, win2_x + 4, win2_y + 10, win_frame)
c.line(win2_x, win2_y + 5, win2_x + 8, win2_y + 5, win_frame)
c.rect(win2_x, win2_y, 8, 10, win_frame, fill=False)

# Window light spill on ground
warm_spill = c.color((255, 170, 70, 60))
c.poly([(win1_x - 2, cottage_top + 16), (win1_x - 4, cottage_top + 32), (win1_x + 12, cottage_top + 32), (win1_x + 10, cottage_top + 16)], warm_spill)
c.poly([(win2_x - 2, cottage_top + 16), (win2_x - 4, cottage_top + 32), (win2_x + 12, cottage_top + 32), (win2_x + 10, cottage_top + 16)], warm_spill)

# Chimney
chimney_x, chimney_y = cw_left + 30, cottage_top - 4
c.rect(chimney_x, chimney_y - 10, 6, 10, stone)
c.rect(chimney_x + 1, chimney_y - 10, 4, 10, stone3)
# Chimney cap
c.rect(chimney_x - 1, chimney_y - 12, 8, 3, stone2)
# Smoke wisps
smoke = c.color((90, 80, 120, 70))
c.set(chimney_x + 2, chimney_y - 14, smoke)
c.set(chimney_x + 4, chimney_y - 16, smoke)
c.set(chimney_x + 1, chimney_y - 18, smoke)
c.set(chimney_x + 3, chimney_y - 20, c.color((80, 70, 110, 60)))
c.set(chimney_x + 5, chimney_y - 22, c.color((80, 70, 110, 50)))
c.set(chimney_x + 2, chimney_y - 24, c.color((70, 60, 100, 40)))

# == Door ==
door_x, door_y = (cw_left + cw_right) // 2 - 3, cottage_top + 16
c.rect(door_x, door_y, 7, 14, wood4)
c.rect(door_x + 1, door_y + 1, 5, 12, wood3)
c.set(door_x + 5, door_y + 7, c.color((200, 160, 90)))

# == Stone well ==
well_x, well_y = 34, 92
# Well posts
c.rect(well_x + 1, well_y - 8, 2, 8, well_wood)
c.rect(well_x + 11, well_y - 8, 2, 8, well_wood)
# Cross beam
c.rect(well_x, well_y - 9, 14, 2, well_wood)
# Well body
c.rect(well_x, well_y, 14, 12, well_stone)
c.rect(well_x + 1, well_y + 1, 12, 10, well_stone2)
# Stone detail
for wy in range(well_y, well_y + 12, 3):
    for wx in range(well_x, well_x + 14, 4):
        if (wx + wy) % 2 == 0:
            c.set(wx + 1, wy + 1, well_stone)
# Dark opening
c.rect(well_x + 4, well_y, 6, 4, c.color((16, 12, 24)))
# Winch
c.rect(well_x + 4, well_y - 10, 6, 3, c.color((70, 48, 36)))
# Rope
rope_col = c.color((40, 32, 28))
for ry in range(well_y - 7, well_y - 3):
    c.set(well_x + 7, ry, rope_col)
# Bucket
c.rect(well_x + 5, well_y - 4, 5, 4, c.color((60, 40, 30)))

# === Stone slab path from door ===
for i in range(6):
    px = 63 - i * 3
    py = 102 + i * 4
    if py < H:
        c.ellipse(px, py, 7 - i // 3, 3, slab if i % 2 == 0 else slab2)
        c.ellipse(px, py, 5 - i // 3, 2, path_stone3)

# Extra scattered stones
c.ellipse(46, 100, 3, 2, path_stone)
c.ellipse(72, 104, 3, 2, path_stone2)
c.ellipse(42, 108, 3, 2, path_stone)
c.ellipse(68, 98, 2, 2, path_stone2)

# === Tree canopies ===
def add_cluster(cx, cy, r, col1, col2):
    c.circle(cx, cy, r, col1)
    c.circle(cx - r // 2, cy - r // 3, r - 1, col1)
    c.circle(cx + r // 2, cy - r // 4, r - 1, col1)
    c.circle(cx, cy + r // 2, r - 1, col2)
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if dx * dx + dy * dy <= r * r and (dx + dy) % 5 == 0:
                if 0 <= cx + dx < W and 0 <= cy + dy < H:
                    c.set(cx + dx, cy + dy, col2)

# Upper canopies
add_cluster(30, 16, 12, leaf1, leaf3)
c.circle(22, 18, 9, leaf3)
c.circle(38, 14, 8, leaf2)
c.circle(30, 8, 8, leaf2)

add_cluster(108, 22, 10, leaf1, leaf3)
c.circle(100, 15, 9, leaf3)
c.circle(116, 18, 8, leaf4)
c.circle(106, 10, 7, leaf2)

# Top center canopy
c.circle(70, 10, 8, leaf5)
c.circle(56, 12, 9, leaf3)
c.circle(62, 16, 7, leaf1)
c.circle(6, 60, 5, leaf5)
c.circle(122, 58, 5, leaf3)
# Extra leaf clusters for depth
c.circle(14, 50, 7, leaf5)
c.circle(118, 48, 6, leaf2)
c.circle(28, 8, 6, leaf4)
c.circle(12, 70, 7, leaf1)
c.circle(118, 70, 6, leaf4)

# === Mist bands ===
for mx in range(0, W - 4, 4):
    my = 88 + ((mx * 7) % 6)
    c.rect(mx, my, 4, 1, mist)
for mx in range(0, W - 5, 5):
    my = 92 + ((mx * 5) % 7)
    c.rect(mx, my, 5, 1, mist2)
for mx in range(0, W - 6, 6):
    my = 84 + ((mx * 3) % 5)
    c.rect(mx, my, 6, 1, mist3)

# === Bushes around cottage base ===
c.circle(cw_left - 6, cottage_top + 30, 5, leaf3)
c.circle(cw_left - 10, cottage_top + 32, 4, leaf1)
c.circle(cw_right + 6, cottage_top + 30, 5, leaf3)
c.circle(cw_right + 10, cottage_top + 32, 4, leaf5)
c.circle(cw_left + 10, cottage_top + 32, 4, leaf5)
c.circle(cw_right - 6, cottage_top + 32, 4, leaf1)

# Low bushes near trees
c.circle(8, 92, 5, leaf3)
c.circle(14, 94, 5, leaf1)
c.circle(112, 92, 5, leaf5)
c.circle(120, 94, 4, leaf3)
c.circle(22, 96, 4, leaf5)
c.circle(102, 96, 4, leaf1)

# === Ground texture ===
for gx in range(0, W, 2):
    gy = 92 + ((gx * 13) % 8)
    if 88 <= gy < H:
        c.set(gx, gy, ground2)

# === Foreground framing branches ===
# Left foreground branch
c.line(0, 76, 12, 82, trunk2)
c.line(12, 82, 4, 90, branch)
c.line(0, 70, 8, 75, branch)
# Right foreground branch
c.line(127, 76, 116, 82, trunk2)
c.line(116, 82, 124, 90, branch)
c.line(127, 70, 120, 75, branch)

# Foreground leaf clusters on branches
c.circle(5, 72, 4, leaf3)
c.circle(7, 78, 3, leaf1)
c.circle(124, 72, 3, leaf5)
c.circle(120, 78, 3, leaf1)
c.circle(4, 66, 3, leaf2)
c.circle(124, 66, 3, leaf2)

# === Magic firefly particles ===
firefly = c.color((200, 200, 100, 180))
fireflies = [(48, 50), (50, 44), (78, 42), (86, 52), (38, 58), (70, 56),
             (44, 48), (82, 40), (52, 62), (90, 60), (35, 52), (75, 38)]
for fx, fy in fireflies:
    c.set(fx, fy, firefly)
    c.set(fx + 1, fy, firefly)
# Dimmer fireflies
ff2 = c.color((180, 200, 120, 140))
for fx2, fy2 in [(56, 34), (64, 44), (40, 66), (88, 48), (46, 56), (80, 36)]:
    c.set(fx2, fy2, ff2)

finish(c)
