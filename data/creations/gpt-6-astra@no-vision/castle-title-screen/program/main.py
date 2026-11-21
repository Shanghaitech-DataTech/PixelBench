from pixelbench_api import new_canvas, finish

# 128x128 cinematic pixel-art title screen.
c = new_canvas(128, 128, background="#17152b", name="castle_title")

# Palette: a restrained dusk range keeps the image readable and under the colour cap.
SKY0 = "#17152b"
SKY1 = "#282044"
SKY2 = "#49305a"
SKY3 = "#75405f"
SKY4 = "#a9545c"
HORIZON = "#dc7554"
GLOW = "#f39a59"
SUN = "#ffc15d"
SUN_HI = "#ffe08a"
CLOUD_DARK = "#3b2c4c"
CLOUD_MID = "#68405a"
CLOUD_LIT = "#b85c5b"
SEA0 = "#162a43"
SEA1 = "#1b3c54"
SEA2 = "#245468"
SEA_HI = "#3b7180"
OUT = "#16182a"
ROCK0 = "#202238"
ROCK1 = "#2c2b43"
ROCK2 = "#44324a"
ROCK_LIT = "#604050"
STONE_D = "#413149"
STONE = "#76504d"
STONE_L = "#a76a56"
STONE_HI = "#d18a60"
ROOF = "#25213a"
WOOD = "#59383d"
FLAG = "#d9574e"
FLAG_HI = "#f17a59"
WINDOW = "#f5ae5c"
WINDOW_HI = "#ffe08a"

# Layered, banded sunset sky.
for y, col in [(0, SKY0), (16, SKY1), (32, SKY2), (48, SKY3), (64, SKY4), (77, HORIZON)]:
    c.rect(0, y, 128, 16 if y < 77 else 14, col)
# Thin pixel bands soften the transition without anti-aliasing.
c.rect(0, 29, 128, 2, "#38284b")
c.rect(0, 61, 128, 2, "#8b485b")
c.rect(0, 75, 128, 2, "#c56257")

# Small title lettering anchors the otherwise cinematic splash-screen sky.
c.text(40, 5, "DUSK KEEP", SUN_HI)

# Sun, intentionally large and slightly off-center for a cinematic frame.
c.circle(93, 39, 18, SUN)
c.rect(80, 26, 26, 3, SUN_HI)
c.rect(77, 32, 3, 13, SUN_HI)
c.rect(107, 35, 3, 9, GLOW)
c.rect(84, 53, 18, 3, GLOW)

# Far cloud banks behind the castle.
c.poly([(0, 26), (11, 26), (11, 22), (24, 22), (24, 26), (36, 26), (36, 31), (0, 31)], CLOUD_DARK)
c.poly([(92, 19), (103, 19), (103, 15), (116, 15), (116, 19), (127, 19), (127, 25), (92, 25)], CLOUD_DARK)
c.poly([(4, 53), (15, 53), (15, 48), (27, 48), (27, 51), (39, 51), (39, 57), (4, 57)], CLOUD_MID)
c.poly([(99, 57), (110, 57), (110, 52), (121, 52), (121, 55), (127, 55), (127, 62), (99, 62)], CLOUD_MID)
# Broad middle cloud, stepped like hand-placed pixels.
c.poly([(0, 67), (9, 67), (9, 63), (20, 63), (20, 59), (35, 59), (35, 63), (48, 63), (48, 69), (59, 69), (59, 74), (0, 74)], CLOUD_LIT)
c.poly([(127, 67), (118, 67), (118, 62), (106, 62), (106, 65), (95, 65), (95, 71), (84, 71), (84, 76), (127, 76)], CLOUD_LIT)
# Bright cloud undersides around the sun.
c.rect(9, 73, 31, 3, "#e47759")
c.rect(16, 70, 15, 3, "#e47759")
c.rect(103, 72, 24, 3, "#e47759")
c.rect(109, 69, 12, 3, "#e47759")

# Distant ocean horizon and bands.
c.rect(0, 83, 128, 45, SEA0)
c.rect(0, 84, 128, 3, "#31445a")
c.rect(0, 91, 128, 2, SEA1)
c.rect(9, 96, 44, 2, SEA2)
c.rect(4, 101, 33, 2, SEA_HI)
c.rect(75, 95, 48, 2, SEA2)
c.rect(93, 102, 35, 2, SEA_HI)
c.rect(57, 108, 27, 2, SEA1)
c.rect(3, 113, 43, 2, SEA2)
# Small glints, sparse so the castle remains the focal point.
for x, y, w in [(2, 88, 12), (19, 88, 8), (101, 88, 15), (111, 92, 9), (6, 105, 15), (84, 100, 7), (48, 96, 8), (96, 110, 16)]:
    c.rect(x, y, w, 1, SEA_HI)

# Seaside cliff silhouette behind and below the castle.
c.poly([(13, 89), (23, 86), (31, 83), (45, 84), (57, 87), (72, 83), (86, 84), (98, 81), (111, 85), (119, 88), (124, 100), (119, 110), (110, 116), (13, 116)], ROCK0)
c.poly([(24, 89), (37, 86), (47, 89), (62, 87), (74, 88), (85, 86), (98, 85), (108, 90), (104, 98), (95, 103), (83, 102), (71, 107), (51, 103), (38, 108), (23, 104)], ROCK1)
# Cliff face facets and ledges.
c.poly([(17, 98), (29, 91), (41, 93), (37, 100), (31, 101), (29, 111), (20, 115)], ROCK2)
c.poly([(50, 94), (62, 89), (74, 92), (69, 99), (62, 100), (58, 109), (48, 110)], ROCK2)
c.poly([(83, 91), (96, 87), (108, 91), (103, 98), (96, 99), (92, 108), (80, 111)], ROCK2)
c.poly([(30, 103), (42, 100), (47, 104), (41, 108), (35, 108)], ROCK_LIT)
c.poly([(70, 102), (79, 97), (88, 100), (82, 105), (74, 107)], ROCK_LIT)
c.rect(20, 91, 17, 2, ROCK_LIT)
c.rect(91, 89, 12, 2, ROCK_LIT)

# Castle keep: dark outline/back silhouette first.
c.rect(47, 54, 31, 34, OUT)
c.rect(51, 49, 23, 39, OUT)
c.rect(48, 51, 29, 6, OUT)
# Keep stone face.
c.rect(51, 57, 23, 29, STONE)
c.rect(54, 53, 17, 33, STONE_L)
c.rect(56, 56, 15, 30, STONE)
# Keep battlements and roofline.
c.rect(49, 49, 27, 6, ROOF)
for x in [51, 59, 67, 73]:
    c.rect(x, 46, 5, 6, OUT)
for x in [52, 60, 68, 74]:
    c.rect(x, 47, 4, 5, STONE_L)
c.rect(55, 53, 16, 2, STONE_HI)
# Keep warm masonry pixels.
for x, y, w in [(52, 60, 6), (64, 61, 7), (57, 68, 5), (67, 72, 5), (52, 78, 7), (63, 82, 8), (57, 85, 4)]:
    c.rect(x, y, w, 2, STONE_L)
for x, y in [(53, 64), (69, 66), (59, 76), (67, 80), (53, 84)]:
    c.rect(x, y, 2, 2, STONE_D)
# Keep arched doorway and slit windows.
c.rect(60, 76, 9, 10, OUT)
c.rect(62, 74, 5, 4, OUT)
c.rect(63, 77, 3, 9, WOOD)
c.rect(64, 78, 2, 2, WINDOW)
for x, y in [(58, 61), (67, 61), (58, 69), (67, 69)]:
    c.rect(x, y, 3, 5, OUT)
    c.rect(x + 1, y + 1, 1, 3, WINDOW)

# Left tower, taller and slimmer, with outline and stepped cap.
c.rect(34, 39, 19, 50, OUT)
c.rect(37, 43, 13, 45, STONE)
c.rect(36, 40, 15, 7, ROOF)
for x in [37, 44, 49]:
    c.rect(x, 36, 4, 7, OUT)
c.rect(38, 38, 3, 5, STONE_HI)
c.rect(45, 38, 3, 5, STONE_L)
c.rect(39, 47, 9, 3, STONE_HI)
# left tower stone and window.
c.rect(40, 52, 7, 33, STONE_L)
c.rect(37, 55, 3, 28, STONE_D)
c.rect(47, 55, 3, 30, STONE_D)
for x, y, w in [(38, 59, 5), (44, 65, 4), (38, 74, 6), (44, 80, 5)]:
    c.rect(x, y, w, 2, STONE)
c.rect(41, 57, 5, 8, OUT)
c.rect(42, 58, 3, 5, WINDOW_HI)
c.rect(42, 58, 3, 1, SUN)
# left flagpole and pennant.
c.rect(42, 25, 2, 16, OUT)
c.rect(44, 25, 10, 5, FLAG)
c.poly([(54, 25), (54, 34), (44, 30)], FLAG_HI)
c.rect(43, 24, 2, 2, SUN_HI)

# Right tower, broad and dominant, slightly lower than left.
c.rect(73, 34, 21, 55, OUT)
c.rect(77, 39, 13, 48, STONE)
c.rect(75, 36, 17, 7, ROOF)
for x in [76, 83, 89]:
    c.rect(x, 32, 4, 7, OUT)
c.rect(77, 34, 3, 5, STONE_HI)
c.rect(84, 34, 3, 5, STONE_L)
c.rect(78, 43, 11, 3, STONE_HI)
# right tower face details.
c.rect(77, 48, 3, 37, STONE_D)
c.rect(87, 48, 3, 37, STONE_D)
c.rect(80, 49, 7, 36, STONE_L)
for x, y, w in [(78, 55, 6), (83, 61, 5), (78, 69, 5), (83, 77, 5), (78, 82, 6)]:
    c.rect(x, y, w, 2, STONE)
c.rect(81, 52, 5, 9, OUT)
c.rect(82, 53, 3, 6, WINDOW_HI)
c.rect(82, 53, 3, 1, SUN)
c.rect(81, 68, 5, 9, OUT)
c.rect(82, 69, 3, 6, WINDOW)
# right flagpole and larger flag.
c.rect(84, 18, 2, 18, OUT)
c.rect(86, 19, 13, 6, FLAG)
c.poly([(99, 19), (99, 30), (86, 25)], FLAG_HI)
c.rect(85, 17, 2, 2, SUN_HI)

# Foreground sea-side rocks, framing the bottom edge and adding depth.
c.poly([(0, 106), (8, 104), (15, 108), (21, 106), (29, 111), (37, 109), (45, 114), (54, 112), (63, 118), (72, 115), (81, 119), (91, 115), (101, 118), (110, 113), (119, 115), (128, 110), (128, 128), (0, 128)], OUT)
c.poly([(0, 116), (12, 112), (22, 116), (32, 113), (43, 118), (53, 116), (65, 122), (77, 119), (88, 123), (101, 118), (112, 121), (121, 117), (128, 120), (128, 128), (0, 128)], ROCK0)
# Large angular foreground boulders.
c.poly([(0, 110), (8, 106), (16, 109), (19, 117), (14, 124), (0, 126)], ROCK1)
c.poly([(27, 111), (36, 108), (45, 113), (46, 122), (39, 127), (25, 125)], ROCK1)
c.poly([(84, 115), (94, 111), (104, 115), (108, 124), (101, 128), (84, 126)], ROCK1)
c.poly([(111, 113), (120, 109), (128, 112), (128, 126), (118, 124)], ROCK1)
# Rock planes and tiny edge glints.
c.poly([(4, 111), (10, 109), (15, 111), (9, 115)], ROCK_LIT)
c.poly([(30, 113), (37, 110), (42, 114), (36, 117)], ROCK_LIT)
c.poly([(88, 116), (95, 113), (101, 116), (94, 119)], ROCK_LIT)
c.rect(2, 121, 9, 2, ROCK2)
c.rect(48, 119, 8, 2, ROCK2)
c.rect(70, 124, 10, 2, ROCK2)
c.rect(115, 119, 8, 2, ROCK2)

# A few atmospheric birds, kept as deliberate two-pixel marks.
c.line(14, 39, 17, 38, OUT)
c.line(17, 38, 19, 40, OUT)
c.line(22, 45, 25, 44, OUT)
c.line(25, 44, 27, 46, OUT)

print(c.stats_text())
finish(c)
