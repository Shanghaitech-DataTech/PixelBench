from pixelbench_api import *

c = new_canvas(64, 64, name="result")

# ---------- palette ----------
sky = c.color("#0d1130", "sky")
cloud = c.color("#1a2046", "cloud")
rain = c.color("#6e8fd4", "rain")
rain_l = c.color("#9db8e8", "rain_l")
roof = c.color("#241f33", "roof")
roof_edge = c.color("#37304a", "roof_edge")
sign_glow = c.color("#cfd8f0", "sign_glow")
sign_bg = c.color("#f6efd8", "sign_bg")
wall = c.color("#4c4258", "wall")
wall_dark = c.color("#393146", "wall_dark")
frame = c.color("#241e2e", "frame")
glass = c.color("#ffd968", "glass")
glass_hi = c.color("#ffeaa8", "glass_hi")
shelf = c.color("#8a5230", "shelf")
shelf_d = c.color("#6b3d22", "shelf_d")
prod_red = c.color("#d84b3a", "prod_red")
prod_blue = c.color("#4b7fd8", "prod_blue")
prod_green = c.color("#57a05a", "prod_green")
prod_orange = c.color("#e88a3a", "prod_orange")
prod_white = c.color("#f0e9d8", "prod_white")
prod_purple = c.color("#8a5fd0", "prod_purple")
awning_red = c.color("#c8433a", "awning_red")
awning_white = c.color("#ece1cf", "awning_white")
awning_shadow = c.color("#5e2426", "awning_shadow")
door = c.color("#3c2f40", "door")
door_glass = c.color("#ffdf80", "door_glass")
ground = c.color("#23273f", "ground")
ground_dk = c.color("#1a1e32", "ground_dk")
curb = c.color("#15182a", "curb")
road = c.color("#121526", "road")
puddle = c.color("#171c33", "puddle")
puddle_l = c.color("#ffd068", "puddle_l")
puddle_o = c.color("#ff8e4a", "puddle_o")
puddle_b = c.color("#3a4d8c", "puddle_b")
glow_ground = c.color("#4a3d55", "glow_ground")
raincoat = c.color("#f2c94c", "raincoat")
raincoat_d = c.color("#c9a227", "raincoat_d")
raincoat_hi = c.color("#f8e28a", "raincoat_hi")
person_dk = c.color("#1a1626", "person_dk")
bike_s = c.color("#c8ccd8", "bike_s")
bike_d = c.color("#5a6178", "bike_d")
tire = c.color("#22263a", "tire")
rack = c.color("#5a4a3a", "rack")
umb_red = c.color("#e05a4a", "umb_red")
umb_blue = c.color("#4a7dbd", "umb_blue")
umb_green = c.color("#4f9d52", "umb_green")
umb_handle = c.color("#3a2c24", "umb_handle")

# ---------- background ----------
c.rect(0, 0, 64, 42, sky)
c.rect(0, 42, 64, 16, ground)   # sidewalk
c.rect(0, 58, 64, 2, curb)
c.rect(0, 60, 64, 4, road)
c.rect(0, 2, 64, 1, cloud)

# ---------- building ----------
# roof
c.rect(2, 5, 60, 4, roof)        # x2..61 y5..8
c.rect(2, 9, 60, 1, roof_edge)   # eave

# blank glowing sign (no brand / logo)
c.rect(13, 8, 38, 7, sign_glow)
c.rect(15, 9, 34, 4, sign_bg)
c.rect(15, 9, 34, 1, sign_glow)

# wall
c.rect(4, 13, 56, 29, wall)      # x4..59 y13..41
c.rect(4, 13, 1, 29, wall_dark)  # left edge
c.rect(58, 13, 2, 29, wall_dark) # right edge
c.rect(4, 41, 56, 1, wall_dark)  # base line

# striped awning
c.rect(2, 17, 60, 5, awning_red)
for sx in range(2, 62, 6):
    c.rect(sx, 17, 3, 5, awning_white)
c.rect(2, 22, 60, 1, awning_shadow)

# ---------- windows and door ----------
# left window
c.rect(9, 23, 19, 16, frame)     # x9..27 y23..38
c.rect(10, 24, 17, 14, glass)    # x10..26 y24..37
c.rect(10, 24, 17, 3, glass_hi)
# right window
c.rect(30, 23, 17, 16, frame)    # x30..46
c.rect(31, 24, 15, 14, glass)    # x31..45
c.rect(31, 24, 15, 3, glass_hi)
# door
c.rect(48, 19, 10, 23, frame)    # x48..57 y19..41
c.rect(49, 20, 8, 21, door_glass)
c.rect(49, 30, 8, 1, frame)

# interior shelves
for wy in (27, 31, 35):
    c.rect(10, wy, 17, 1, shelf)
    c.rect(31, wy, 15, 1, shelf)

# products - left window
c.rect(11, 24, 2, 3, prod_red)
c.rect(14, 24, 2, 3, prod_blue)
c.rect(17, 24, 2, 3, prod_green)
c.rect(20, 24, 2, 3, prod_orange)
c.rect(23, 24, 2, 3, prod_white)
c.rect(12, 28, 2, 3, prod_blue)
c.rect(15, 28, 2, 3, prod_red)
c.rect(18, 28, 2, 3, prod_orange)
c.rect(21, 28, 2, 3, prod_green)
c.rect(24, 28, 2, 3, prod_purple)
c.rect(11, 32, 2, 3, prod_orange)
c.rect(14, 32, 2, 3, prod_white)
c.rect(17, 32, 2, 3, prod_red)
c.rect(20, 32, 2, 3, prod_blue)
c.rect(23, 32, 2, 3, prod_green)

# products - right window
c.rect(32, 24, 2, 3, prod_white)
c.rect(35, 24, 2, 3, prod_red)
c.rect(38, 24, 2, 3, prod_blue)
c.rect(41, 24, 2, 3, prod_green)
c.rect(33, 28, 2, 3, prod_green)
c.rect(36, 28, 2, 3, prod_orange)
c.rect(39, 28, 2, 3, prod_red)
c.rect(42, 28, 2, 3, prod_white)
c.rect(32, 32, 2, 3, prod_blue)
c.rect(35, 32, 2, 3, prod_white)
c.rect(38, 32, 2, 3, prod_orange)
c.rect(41, 32, 2, 3, prod_green)

# ---------- light spilling on sidewalk ----------
c.poly([(10, 42), (28, 42), (32, 50), (7, 50)], glow_ground)
c.poly([(31, 42), (46, 42), (50, 50), (29, 50)], glow_ground)
c.poly([(48, 42), (57, 42), (61, 50), (46, 50)], glow_ground)

# ---------- reflective puddles ----------
c.poly([(8, 46), (28, 45), (30, 52), (24, 57), (10, 55), (6, 49)], puddle)
c.poly([(31, 45), (45, 44), (47, 52), (42, 56), (33, 54), (30, 49)], puddle)
c.poly([(48, 46), (59, 45), (60, 54), (53, 58), (47, 52)], puddle)

# warm window reflections in puddles
for (rx, ry, rh) in [(10, 46, 6), (13, 45, 8), (16, 46, 5), (19, 45, 7), (22, 46, 4), (25, 46, 6)]:
    c.rect(rx, ry, 2, rh, puddle_l)
c.rect(12, 50, 2, 3, puddle_o)
c.rect(18, 49, 2, 3, puddle_o)
c.rect(24, 50, 2, 2, puddle_o)

for (rx, ry, rh) in [(32, 45, 6), (35, 44, 8), (38, 45, 5), (41, 44, 7), (44, 45, 4)]:
    c.rect(rx, ry, 2, rh, puddle_l)
c.rect(34, 49, 2, 3, puddle_o)
c.rect(40, 48, 2, 3, puddle_o)

for (rx, ry, rh) in [(49, 46, 5), (52, 45, 7), (55, 46, 4)]:
    c.rect(rx, ry, 2, rh, puddle_l)
c.rect(51, 49, 2, 3, puddle_o)
# raincoat figure reflected in the door-side puddle
c.rect(53, 51, 2, 3, raincoat)
c.rect(55, 53, 2, 2, raincoat_d)

# ripple lines
c.line(10, 51, 16, 51, puddle_b)
c.line(20, 52, 26, 52, puddle_b)
c.line(33, 50, 40, 50, puddle_b)
c.line(36, 53, 43, 53, puddle_b)
c.line(50, 51, 56, 51, puddle_b)

# ---------- umbrella rack ----------
c.rect(2, 38, 7, 4, rack)
c.rect(2, 38, 7, 1, umb_handle)
c.rect(3, 41, 5, 1, umb_handle)
c.rect(2, 42, 8, 1, person_dk)

c.poly([(0, 26), (6, 26), (3, 21)], umb_red)
c.line(3, 26, 3, 39, umb_handle)
c.set(3, 20, umb_handle)

c.poly([(2, 27), (8, 27), (5, 22)], umb_blue)
c.line(5, 27, 5, 39, umb_handle)
c.set(5, 21, umb_handle)

c.poly([(3, 28), (9, 28), (6, 23)], umb_green)
c.line(6, 28, 6, 39, umb_handle)
c.set(6, 22, umb_handle)

# ---------- parked bicycle ----------
for wx in (12, 21):
    c.circle(wx, 53, 4, tire)
    c.circle(wx, 53, 2, bike_s)
    c.set(wx, 53, tire)
    c.line(wx, 53, wx - 2, 51, bike_s)
    c.line(wx, 53, wx + 2, 51, bike_s)
    c.line(wx, 53, wx - 2, 55, bike_s)
    c.line(wx, 53, wx + 2, 55, bike_s)

c.line(12, 53, 16, 52, bike_s)
c.line(16, 52, 14, 46, bike_s)
c.line(12, 53, 14, 46, bike_s)
c.line(14, 46, 19, 45, bike_s)
c.line(16, 52, 19, 45, bike_s)
c.line(19, 45, 21, 53, bike_s)
c.line(19, 45, 20, 44, bike_s)
c.rect(12, 45, 4, 1, bike_s)   # seat
c.rect(19, 43, 4, 1, bike_s)   # handlebar grip
c.rect(15, 52, 2, 1, bike_s)   # pedal

# ---------- person in raincoat entering ----------
c.circle(54, 29, 2, raincoat)
c.set(52, 29, person_dk)
c.set(52, 30, person_dk)
c.set(54, 28, raincoat_hi)
c.set(55, 29, raincoat_hi)
c.poly([(51, 32), (56, 32), (57, 41), (50, 41)], raincoat)
c.line(56, 32, 57, 41, raincoat_d)
c.line(50, 41, 57, 41, raincoat_d)
c.line(52, 34, 52, 37, raincoat_hi)
c.rect(48, 33, 3, 2, raincoat)  # reaching arm
c.rect(51, 42, 2, 3, person_dk) # legs
c.rect(54, 42, 2, 3, person_dk)
c.rect(48, 44, 10, 2, person_dk)  # shadow on sidewalk

# ---------- rain ----------
rain_drops = [
    (3, 2), (8, 6), (14, 3), (19, 8), (24, 2), (30, 7), (36, 4), (41, 9),
    (46, 3), (52, 6), (57, 2), (61, 8),
    (5, 12), (11, 15), (17, 11), (23, 16), (28, 12), (34, 17), (39, 13),
    (45, 18), (50, 14), (55, 12), (60, 17),
    (7, 20), (13, 25), (18, 21), (25, 26), (31, 22), (37, 27), (43, 23),
    (49, 28), (54, 24), (59, 22),
    (4, 30), (10, 35), (15, 31), (21, 36), (27, 32), (33, 37), (39, 33),
    (45, 38), (51, 34), (56, 31), (62, 36),
    (6, 40), (12, 45), (17, 41), (23, 46), (29, 42), (35, 47), (41, 43),
    (47, 48), (53, 44), (58, 41), (62, 46),
    (9, 50), (14, 55), (20, 51), (26, 56), (32, 52), (38, 57), (44, 53),
    (50, 58), (56, 54), (61, 51), (3, 58), (18, 58), (42, 60),
]
for i, (x, y) in enumerate(rain_drops):
    col = rain if i % 3 else rain_l
    c.line(x, y, x - 1, y + 3, col)

# tiny rain splashes on the sidewalk
for (sx, sy) in [(10, 44), (16, 43), (22, 44), (34, 43), (40, 44), (46, 43),
                 (52, 44), (58, 43), (5, 45), (27, 45), (49, 45)]:
    c.set(sx, sy, rain)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 22)))
print(c.matrix_text(region=(0, 23, 63, 44)))
print(c.matrix_text(region=(0, 45, 63, 63)))

finish(c)
