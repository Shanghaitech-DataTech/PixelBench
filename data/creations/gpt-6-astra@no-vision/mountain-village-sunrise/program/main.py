from pixelbench_api import *

# Mountain village at sunrise: a compact, high-contrast pixel landscape.
c = new_canvas(128, 128, background="#f6c98f", name="mountain_village_sunrise")

# Palette: dawn sky bands.
c.rect(0, 0, 128, 14, "#22264f")
c.rect(0, 14, 128, 13, "#383064")
c.rect(0, 27, 128, 12, "#5a3d76")
c.rect(0, 39, 128, 11, "#8d527d")
c.rect(0, 50, 128, 11, "#c36d7c")
c.rect(0, 61, 128, 11, "#e48d7b")
c.rect(0, 72, 128, 10, "#f4b184")

# Tiny pixel clouds, keeping the horizon airy.
c.rect(7, 33, 19, 2, "#725077")
c.rect(12, 31, 10, 2, "#725077")
c.rect(91, 25, 22, 2, "#4a386c")
c.rect(97, 23, 9, 2, "#4a386c")
c.rect(37, 58, 14, 2, "#d77b7b")
c.rect(42, 56, 7, 2, "#d77b7b")

# Sunrise: square pixel glow behind the focal valley.
c.rect(48, 31, 32, 25, "#eea06f")
c.rect(53, 34, 22, 20, "#f6bd76")
c.circle(64, 45, 11, "#ffe09a")
c.rect(51, 44, 26, 3, "#ffe09a")
c.rect(56, 37, 16, 16, "#ffe09a")
# restore a crisp sun disk over the stepped glow
c.circle(64, 45, 9, "#ffe9a8")

# Far mountain silhouettes and snowy ridges.
c.poly([(0, 71), (15, 59), (23, 66), (36, 48), (49, 65), (62, 54), (77, 67), (91, 50), (108, 67), (120, 57), (128, 64), (128, 88), (0, 88)], "#655078")
c.poly([(0, 72), (15, 59), (23, 66), (36, 48), (49, 65), (62, 54), (77, 67), (91, 50), (108, 67), (120, 57), (128, 64), (128, 69), (112, 68), (103, 60), (92, 73), (79, 71), (62, 60), (51, 72), (37, 56), (25, 72), (15, 65), (5, 76)], "#f6cda0")
# cut the snow backs with the mountain body for chunky ridges
c.poly([(0, 72), (15, 61), (23, 68), (36, 51), (49, 68), (62, 57), (77, 70), (91, 53), (108, 70), (120, 60), (128, 67), (128, 88), (0, 88)], "#73547b")

# Middle blue-violet mountain range adds depth.
c.poly([(0, 84), (13, 73), (25, 78), (39, 62), (54, 79), (69, 66), (83, 82), (98, 67), (113, 78), (128, 70), (128, 103), (0, 103)], "#4a5272")
c.poly([(0, 84), (13, 73), (25, 78), (39, 62), (54, 79), (69, 66), (83, 82), (98, 67), (113, 78), (128, 70), (128, 77), (114, 82), (99, 73), (84, 88), (69, 74), (55, 87), (40, 70), (26, 85), (13, 80), (0, 90)], "#68708a")
# dark foothills
c.poly([(0, 91), (16, 82), (31, 91), (46, 78), (62, 89), (79, 80), (95, 91), (111, 80), (128, 89), (128, 112), (0, 112)], "#30445b")

# Ground plane, layered like broad pixel bands.
c.rect(0, 96, 128, 32, "#273d3b")
c.poly([(0, 102), (19, 96), (39, 104), (59, 97), (77, 106), (99, 96), (128, 103), (128, 128), (0, 128)], "#304c3e")
c.poly([(0, 113), (25, 106), (46, 114), (67, 105), (87, 114), (108, 106), (128, 112), (128, 128), (0, 128)], "#3b5742")

# Distant tree line behind the homes.
def pine(x, top, w, h, dark, light):
    base = top + h
    c.rect(x - 1, base - 12, 3, 13, dark)
    c.poly([(x, top), (x - 3, top + 9), (x - w//4, top + 12),
            (x - w//2, top + 25), (x - w//3, top + 25),
            (x - w//2, top + 39), (x + w//2, top + 39),
            (x + w//3, top + 25), (x + w//2, top + 25),
            (x + w//4, top + 12), (x + 3, top + 9)], dark)
    c.poly([(x, top + 4), (x - 4, top + 18), (x - 1, top + 17),
            (x - 8, top + 30), (x - 3, top + 29),
            (x - 11, top + 38), (x, top + 34),
            (x + 6, top + 38), (x + 3, top + 29),
            (x + 8, top + 30), (x + 2, top + 17), (x + 5, top + 18)], light)

for args in [(8, 73, 12, 31), (21, 71, 11, 28), (108, 72, 13, 31), (122, 68, 12, 36), (40, 77, 8, 23), (91, 75, 9, 25)]:
    pine(*args, "#20393a", "#355343")

# Large framing pines at the edges establish depth.
pine(7, 43, 27, 65, "#172d35", "#28473d")
pine(120, 48, 29, 61, "#172d35", "#28473d")
# needle edge highlights
c.rect(4, 68, 3, 15, "#3f6148")
c.rect(116, 72, 3, 13, "#3f6148")

# Smoke stacks and stepped smoke, behind roofs.
c.rect(68, 55, 5, 16, "#26383d")
c.rect(69, 53, 4, 4, "#3a414e")
c.rect(72, 45, 5, 5, "#5d5369")
c.rect(75, 38, 6, 6, "#705b70")
c.rect(78, 31, 7, 6, "#8b6476")
c.rect(81, 25, 5, 5, "#ae747c")
c.rect(84, 21, 4, 4, "#ca837f")
# left and right chimney smoke, smaller silhouettes
c.rect(23, 68, 4, 11, "#343c49")
c.rect(24, 60, 6, 6, "#5a5267")
c.rect(21, 54, 6, 5, "#756078")
c.rect(18, 48, 5, 5, "#9a6e7b")
c.rect(104, 65, 4, 11, "#313a46")
c.rect(105, 58, 6, 5, "#5a5267")
c.rect(108, 51, 5, 5, "#816378")

# Houses: rear left, rear right, then the central focal home.
# Left cottage shadow and walls
c.rect(10, 81, 29, 24, "#3a2f36")
c.rect(13, 82, 23, 20, "#9b5b45")
c.rect(15, 84, 19, 18, "#b56c4c")
# left gable roof and dark eaves
c.poly([(7, 83), (23, 71), (41, 83), (38, 87), (23, 77), (11, 87)], "#342d3b")
c.poly([(11, 82), (23, 74), (36, 83), (34, 84), (23, 78), (14, 85)], "#6a3e43")
c.rect(10, 84, 29, 4, "#342d3b")
# left windows/door
c.rect(16, 89, 7, 8, "#26353a")
c.rect(17, 90, 5, 6, "#e7a765")
c.rect(27, 89, 6, 6, "#29383b")
c.rect(28, 90, 4, 4, "#e9b16e")
c.rect(25, 97, 7, 8, "#49353a")
c.rect(28, 98, 2, 2, "#c77a4e")
c.rect(12, 101, 25, 3, "#6f433e")
# left roof snow lip
c.rect(13, 80, 7, 2, "#e7b17d")
c.rect(29, 80, 6, 2, "#e7b17d")

# Right cottage
c.rect(89, 80, 28, 24, "#352e36")
c.rect(92, 81, 22, 21, "#8d5546")
c.rect(94, 84, 18, 18, "#aa6749")
c.poly([(86, 83), (103, 69), (120, 83), (117, 87), (103, 76), (90, 87)], "#302c3a")
c.poly([(90, 82), (103, 72), (116, 82), (114, 84), (103, 77), (93, 85)], "#633d45")
c.rect(89, 84, 28, 4, "#302c3a")
c.rect(95, 89, 6, 6, "#27373c")
c.rect(96, 90, 4, 4, "#edb46e")
c.rect(105, 89, 6, 8, "#29383b")
c.rect(106, 90, 4, 6, "#e0a05e")
c.rect(101, 97, 7, 8, "#49353a")
c.rect(104, 98, 2, 2, "#c77a4e")
c.rect(91, 101, 25, 3, "#684039")
c.rect(93, 79, 7, 2, "#e5ad79")
c.rect(108, 80, 6, 2, "#e5ad79")

# Central house is larger and brighter, the clear focal point.
c.rect(45, 72, 38, 34, "#332d35")
c.rect(49, 75, 30, 29, "#a85e43")
c.rect(52, 77, 24, 27, "#c8784d")
# timber beams
c.rect(49, 82, 30, 3, "#724337")
c.rect(49, 96, 30, 3, "#724337")
c.rect(62, 75, 3, 29, "#774538")
# central roof with snow-lit slope
c.poly([(40, 76), (64, 57), (87, 76), (83, 82), (64, 65), (45, 82)], "#292b38")
c.poly([(44, 75), (64, 60), (83, 75), (80, 77), (64, 65), (48, 78)], "#70424a")
c.poly([(46, 72), (64, 59), (75, 68), (70, 67), (64, 63), (54, 72)], "#c58a68")
c.rect(43, 77, 42, 5, "#292b38")
# central warm windows, door, and cross frames
c.rect(53, 86, 9, 8, "#26373b")
c.rect(54, 87, 7, 6, "#f6c275")
c.rect(57, 87, 2, 6, "#b85f47")
c.rect(54, 89, 7, 2, "#b85f47")
c.rect(68, 86, 9, 8, "#26373b")
c.rect(69, 87, 7, 6, "#f6c275")
c.rect(72, 87, 2, 6, "#b85f47")
c.rect(69, 89, 7, 2, "#b85f47")
c.rect(61, 96, 8, 9, "#46343a")
c.rect(63, 98, 4, 7, "#7f4b3e")
c.set(66, 100, "#c77a4e")
# central house foundation and snow edge
c.rect(47, 103, 35, 4, "#4a3838")
c.rect(51, 74, 10, 2, "#e7b27b")
c.rect(69, 74, 10, 2, "#e7b27b")

# Stone path, narrowing toward the front door (drawn over ground, under little foreground tufts).
c.poly([(61, 103), (69, 103), (88, 128), (39, 128)], "#6d6258")
c.poly([(62, 104), (68, 104), (82, 128), (45, 128)], "#9a8269")
# individual pixel stones and dark seams
for x, y, w, h in [(61,106,7,3), (58,111,12,3), (54,117,10,3), (69,117,12,3), (48,123,13,3), (65,124,15,3), (79,124,7,3)]:
    c.rect(x, y, w, h, "#c09a73")
for x, y, w in [(60,109,9), (55,115,14), (69,121,11), (45,127,15)]:
    c.rect(x, y, w, 1, "#6d6258")

# Foreground grass clusters frame the path without obscuring the village.
for x, y in [(3,111), (14,116), (27,109), (94,110), (111,114), (124,107), (35,123), (100,126)]:
    c.line(x, y+8, x+2, y, "#1d3833")
    c.line(x+2, y+8, x+6, y+2, "#27453a")
    c.line(x+2, y+8, x-2, y+3, "#27453a")
# a few lit grass tips
c.rect(16, 111, 2, 5, "#5d7049")
c.rect(109, 108, 2, 5, "#5d7049")
c.rect(94, 119, 2, 5, "#5d7049")

# Small birds add scale in the sunrise, using deliberate 1px stair-steps.
c.set(30, 28, "#302d50")
c.set(31, 29, "#302d50")
c.set(32, 28, "#302d50")
c.set(95, 40, "#463559")
c.set(96, 41, "#463559")
c.set(97, 40, "#463559")

print(c.stats_text())
print(c.matrix_text(region=(38, 52, 89, 110)))
finish(c)
