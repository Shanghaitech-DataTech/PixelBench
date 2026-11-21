from pixelbench_api import *

c = new_canvas(64, 64)

# ---- Palette definitions (deduplicated) ----
water = [
    (14, 48, 98),
    (11, 45, 103),
    (9, 42, 110),
    (7, 40, 118),
    (5, 38, 125),
    (4, 36, 130),
]
sand_dark = (70, 60, 40)
sand = (100, 88, 55)
sand_light = (140, 125, 80)

wood_dark = (55, 38, 25)
wood = (85, 55, 32)
wood_light = (115, 75, 40)
wood_green = (60, 70, 45)

metal_dark = (45, 50, 45)
metal = (70, 80, 70)
rust = (90, 60, 30)

fish = (210, 160, 60)
fish_dark = (170, 120, 40)
fish_light = (235, 195, 120)
fish2 = (150, 200, 220)
fish2_dark = (110, 160, 190)

coral = (200, 90, 70)
coral_dark = (160, 60, 50)
coral_light = (230, 130, 110)

seaweed = (40, 120, 60)
seaweed_dark = (25, 85, 45)
seaweed_light = (60, 155, 85)

purple = (150, 70, 160)
purple_dark = (110, 50, 120)

bubble = (180, 220, 255)
ray = (40, 105, 160)
shimmer = (170, 210, 245)

# ---- Background water gradient ----
for y in range(64):
    c.line(0, y, 63, y, water[min(y // 12, 5)])

# ---- Sun rays from surface ----
for (x0, x1, w) in [(4, 22, 2), (10, 26, 2), (46, 36, 2), (52, 42, 3)]:
    for i in range(30):
        y = i
        x = x0 + int((x1 - x0) * i / 30) + (i % 3 - 1)
        c.set(x, y, ray)

# ---- Shipwreck hull ----
# Big tilted hull, positioned so bottom is buried. Deck ~y30&34, bottom ~y50&54.
# Draw hull as several filled layers (top deck, then sides), then sand over bottom.

# Hull main body (side toward viewer, tilted)
hull = [
    (12, 34), (52, 26), (56, 36), (20, 55), (10, 50),
]
c.poly(hull, wood, fill=True)

# Deck top surface (a strip along the top edge)
deck = [
    (12, 34), (52, 26), (56, 36), (12, 38),
]
c.poly(deck, wood_light, fill=True)

# Hull plank lines running along
c.line(14, 38, 53, 30, wood_dark)
c.line(16, 42, 54, 34, wood_dark)
c.line(18, 46, 55, 38, wood_dark)
c.line(14, 50, 52, 42, wood_dark)

# Missing planks / broken gaps (holes)
# big hole on left side of hull
for (hx, hy) in [
    (16, 39), (17, 39), (18, 40), (16, 40),
    (22, 45), (23, 46), (24, 47),
    (34, 44), (35, 45), (48, 34), (45, 44),
    (40, 39), (41, 40), (28, 41),
]:
    c.set(hx, hy, None)

# Corrosion / algae patches
for (px, py) in [(24, 33), (34, 30), (43, 28), (29, 43), (38, 40), (18, 48), (44, 39)]:
    c.set(px, py, wood_green)
    c.set(px, py+1, wood_green)
for (px, py) in [(30, 35), (40, 32), (47, 40), (20, 44), (33, 47)]:
    c.set(px, py, rust)
    c.set(px, py+1, rust)

# Metal plates / bolts along hull
for (mx, my) in [(26, 36), (36, 33), (46, 41), (30, 45)]:
    c.set(mx, my, metal)
    c.set(mx+1, my, metal_dark)

# ---- Cabin / broken superstructure ----
cabin = [(34, 22), (45, 20), (45, 27), (34, 29)]
c.poly(cabin, wood, fill=True)
c.line(34, 22, 34, 29, wood_dark)
c.line(45, 20, 45, 27, wood_diff := wood_dark)
c.line(34, 29, 45, 27, wood_dark)
# roof
c.poly([(33, 21), (46, 19), (46, 22), (33, 24)], wood_green, fill=True)
# window holes
c.set(38, 23, None)
c.set(39, 23, None)
c.set(42, 22, None)
c.set(43, 22, None)
# roof broken/fallen off partially on right end

# ---- Broken mast ----
# Mast near x=27 rising up to deck
c.rect(27, 10, 3, 20, wood_dark)
# jagged break at top
c.set(27, 10, wood_light)
c.set(29, 11, wood)
c.set(26, 11, wood)
# wood grain
c.line(28, 14, 28, 22, wood)
# ragged torn sail/rope lines
c.line(29, 12, 34, 10, wood_green)
c.line(30, 12, 30, 16, wood_light)

# ---- Sand floor that buries the hull bottom ----
# Sand base fill
for y in range(48, 64):
    c.line(0, y, 63, y, sand)
# wavy sand texture + gradient
for y in range(47, 64):
    for x in range(64):
        v = (x * 13 + y * 7) % 10
        if v < 2:
            col = sand_dark
        elif v < 4:
            col = sand_light
        else:
            col = sand
        c.set(x, y, col)

# Dune bumps and hollows on sand surface ~y47-52, varying
for x in range(64):
    h = 47 + ((x * 17) % 5)
    if h % 3 == 0:
        c.set(x, h, sand_light)
        c.set(x, h+1, sand_light)
    if h % 4 == 1:
        c.set(x, h, sand_dark)
# scatter darker sand at the buried-hull junction for depth
for x in range(8, 58):
    c.set(x, 49, sand_dark)
for x in range(12, 54):
    c.set(x, 50, sand_light if x % 2 else sand_dark)

# Small shell / pebble details on sand
for (sx, sy) in [(6, 54), (30, 60), (46, 58), (22, 62), (52, 63), (40, 61)]:
    c.set(sx, sy, (170, 150, 100))
for (sx, sy) in [(12, 62), (34, 59), (56, 57)]:
    c.set(sx, sy, sand_light)

# ---- Anchor lying half-buried ----
c.line(8, 50, 16, 52, metal)
c.line(8, 50, 8, 49, metal_dark)
c.line(16, 52, 16, 51, metal_dark)
c.line(11, 51, 11, 58, metal)
c.line(12, 51, 12, 58, metal_dark)
c.line(9, 57, 14, 59, metal_dark)
c.set(10, 53, rust)
c.set(11, 55, rust)

# ---- Seaweed ----
def draw_seaweed(x0, y0, h, color, dark, light):
    for i in range(h):
        sway = int((i * 0.9) % 4) - 1
        x = x0 + sway + (0 if i < h // 2 else (1 if i % 3 == 0 else 0))
        x = max(0, min(63, x))
        y = max(0, y0 - i)
        col = dark if i < 3 else (light if i > h - 4 else color)
        c.set(x, y, col)

# Left seaweed cluster
for sx in [1, 3]:
    draw_seaweed(sx, 56, 20 + sx, seaweed, seaweed_dark, seaweed_light)
draw_seaweed(4, 57, 14, seaweed_light, seaweed_dark, seaweed_light)
draw_seaweed(0, 55, 24, seaweed, seaweed_dark, seaweed_light)

# Right seaweed cluster
for sx in [59, 61, 63]:
    draw_seaweed(sx, 56, 22 - sx % 3, seaweed_dark, seaweed_dark, seaweed_light)
draw_seaweed(60, 58, 16, seaweed, seaweed_dark, seaweed_light)

# ---- Coral ----
# Red branching coral, left
c.line(6, 55, 9, 47, coral)
c.line(9, 47, 11, 43, coral_light)
c.line(7, 57, 10, 50, coral)
c.line(10, 50, 12, 46, coral)
c.line(3, 56, 5, 49, coral_dark)
c.line(5, 49, 6, 46, coral)
# small coral tips
c.set(11, 42, coral_light)
c.set(12, 45, coral)
c.set(6, 45, coral_light)

# Purple brain/sponge coral, right
c.circle(56, 52, 4, purple)
c.circle(56, 52, 4, purple)
c.circle(56, 52, 3, (175, 95, 185))
c.set(56, 52, (195, 125, 205))
c.set(54, 50, purple_dark)
c.set(58, 50, purple_dark)
c.set(56, 53, (120, 60, 130))

# ---- School of fish ----
def draw_fish(x, y, color, cdark, clight):
    c.set(x, y, color)
    c.set(x+1, y, color)
    c.set(x+2, y, color)
    c.set(x+3, y, cdark)
    c.set(x+1, y-1, clight)
    c.set(x+2, y+1, clight)
    c.set(x+1, y, (250, 250, 240))

fish_positions = [
    (6, 12), (10, 10), (14, 14), (18, 11), (22, 16), (26, 10),
    (30, 15), (35, 9), (39, 13), (44, 11), (48, 16), (53, 10),
    (8, 18), (12, 20), (16, 15), (21, 19), (25, 23), (30, 20),
    (34, 23), (38, 17), (43, 21), (47, 18), (51, 22), (57, 16),
    (4, 25), (14, 24), (24, 8), (33, 27), (58, 7),
]
for (fx, fy) in fish_positions:
    draw_fish(fx, fy, fish, fish_dark, fish_light)

# scattered blue fish
for (fx, fy) in [(3, 31), (26, 28), (51, 39), (58, 28), (7, 43), (60, 44)]:
    draw_fish(fx, fy, fish2, fish2_dark, (185, 230, 248))

# ---- Bubbles ----
for (bx, by) in [(9, 5), (12, 2), (31, 4), (15, 8), (40, 3), (49, 5), (56, 2), (22, 6)]:
    c.set(bx, by, bubble)
    c.set(bx+1, by+1, (140, 190, 235))

# ---- Foreground tint seaweed right of hull for depth ----
draw_seaweed(18, 56, 20, seaweed, seaweed_dark, seaweed_light)

print(c.stats_text())
finish(c)
