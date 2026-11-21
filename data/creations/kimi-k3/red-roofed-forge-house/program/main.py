# Red-roofed forge house - 128x128 isometric RTS tileset sprite
b = new_canvas(128, 128, name="building")
sh = new_canvas(128, 128, name="shadow")

# ---------------- ground shadow ----------------
sh.ellipse(61, 100, 50, 12, (0, 0, 0, 28))
sh.ellipse(61, 100, 41, 9, (0, 0, 0, 42))

# ---------------- walls ----------------
b.poly([(24, 86), (64, 106), (64, 78), (24, 58)], "#d9b182")    # left wall (lit)
b.poly([(64, 106), (104, 86), (104, 58), (64, 78)], "#b28a5c")  # right wall (shade)

# stone foundation bands
b.poly([(24, 80), (64, 100), (64, 106), (24, 86)], "#8d857a")
b.poly([(64, 100), (104, 80), (104, 86), (64, 106)], "#7f786d")
b.line(25, 83, 63, 103, "#6f685d")
b.line(65, 103, 103, 83, "#6f685d")
b.line(28, 82, 28, 88, "#6f685d")
b.line(56, 96, 56, 102, "#6f685d")
b.line(68, 98, 68, 104, "#6f685d")
b.line(96, 84, 96, 90, "#6f685d")

# under-eave shadow bands
b.poly([(24, 62), (64, 82), (64, 84), (24, 64)], "#a3805c")
b.poly([(64, 82), (104, 64), (104, 66), (64, 84)], "#8f6f47")

# subtle wall texture
b.line(27, 70, 35, 74, "#c9a06f")
b.line(46, 78, 52, 81, "#c9a06f")
b.line(90, 64, 98, 60, "#a37c4f")
b.line(92, 76, 100, 72, "#a37c4f")

# timber corner posts
b.rect(22, 62, 4, 26, "#6e4a2f")
b.line(25, 62, 25, 87, "#54371f")
b.rect(102, 62, 4, 26, "#54371f")
b.line(102, 62, 102, 87, "#6e4a2f")
b.rect(62, 80, 3, 25, "#6e4a2f")
b.rect(65, 80, 2, 25, "#54371f")

# ---------------- window (left wall) ----------------
b.rect(53, 80, 7, 7, "#6e4a2f")
b.rect(54, 81, 5, 5, "#ffc65c")
b.line(56, 81, 56, 85, "#6e4a2f")
b.line(54, 83, 58, 83, "#6e4a2f")
b.set(51, 84, "#c9854a")
b.set(61, 83, "#c9854a")
b.set(55, 88, "#c9854a")

# ---------------- furnace (left wall) ----------------
b.circle(42, 81, 8, "#4a3428")                                  # stone rim
b.poly([(34, 81), (50, 81), (50, 99), (34, 91)], "#4a3428")
b.circle(42, 82, 6, "#2a160c")                                  # dark interior
b.poly([(36, 82), (48, 82), (48, 97), (36, 91)], "#2a160c")
b.circle(42, 84, 5, "#e36414")                                  # glow: outer
b.poly([(37, 84), (47, 84), (47, 97), (37, 92)], "#e36414")
b.circle(42, 86, 4, "#ff9f1c")                                  # glow: mid
b.poly([(38, 86), (46, 86), (46, 96), (38, 92)], "#ff9f1c")
b.circle(42, 88, 3, "#ffd23f")                                  # glow: core
b.poly([(39, 88), (45, 88), (45, 96), (39, 93)], "#ffd23f")
b.circle(42, 90, 2, "#fff3b0")                                  # white-hot heart
b.poly([(40, 90), (44, 90), (44, 95), (40, 94)], "#fff3b0")
b.line(39, 80, 39, 93, "#2a160c")                               # grate bars
b.line(42, 79, 42, 94, "#2a160c")
b.line(45, 80, 45, 96, "#2a160c")
b.set(36, 74, "#6b5a4a")                                        # rim highlight
b.set(35, 76, "#6b5a4a")
b.set(38, 73, "#6b5a4a")
b.set(31, 85, "#c9854a")                                        # glow spill on wall
b.set(32, 90, "#c9854a")
b.set(53, 87, "#c9854a")
b.set(52, 92, "#c9854a")
b.set(37, 72, "#c9854a")

# ---------------- door (right wall) ----------------
b.poly([(71, 81), (85, 75), (85, 97), (71, 103)], "#7a5228")    # frame
b.poly([(72, 82), (84, 76), (84, 96), (72, 102)], "#4f3018")    # planks
b.line(75, 81, 75, 101, "#3a2310")
b.line(79, 79, 79, 99, "#3a2310")
b.line(83, 77, 83, 97, "#3a2310")
b.set(81, 89, "#bb8950")
b.set(82, 89, "#bb8950")

# hanging lantern
b.line(67, 80, 67, 82, "#3a2a1a")
b.rect(65, 82, 6, 7, "#4a2f18")
b.rect(66, 83, 4, 4, "#ffb347")
b.rect(67, 84, 2, 2, "#ffd23f")
b.set(63, 85, "#c9854a")
b.set(72, 86, "#c9854a")
b.set(68, 91, "#c9854a")

# small window (right wall, shadow side)
b.rect(88, 71, 7, 7, "#54371f")
b.rect(89, 72, 5, 5, "#e8a94a")
b.line(91, 72, 91, 76, "#54371f")
b.line(89, 74, 93, 74, "#54371f")

# ---------------- stacked barrels ----------------
def barrel(x, y):
    b.circle(x + 6, y + 6, 6, "#9c6b3d")
    b.ellipse(x + 6, y + 2, 5, 2, "#b08050")
    b.line(x + 2, y + 4, x + 10, y + 4, "#5f3f22")
    b.line(x + 1, y + 5, x + 11, y + 5, "#5f3f22")
    b.line(x + 1, y + 9, x + 11, y + 9, "#5f3f22")
    b.line(x + 3, y + 11, x + 9, y + 11, "#5f3f22")
    b.line(x + 3, y + 3, x + 3, y + 10, "#bb8950")

barrel(86, 96)
barrel(99, 96)
barrel(92, 86)

# ---------------- wooden sign ----------------
b.rect(15, 90, 4, 20, "#6e4a2f")
b.line(18, 90, 18, 109, "#54371f")
b.rect(6, 80, 22, 12, "#a0713f")
b.rect(6, 80, 22, 12, "#7a5228", fill=False)
b.line(7, 81, 26, 81, "#bb8950")
b.rect(12, 84, 10, 2, "#3a2a1a")                                # anvil pictogram
b.rect(15, 86, 4, 2, "#3a2a1a")
b.rect(13, 88, 8, 2, "#3a2a1a")
b.set(8, 82, "#5f4126")
b.set(25, 82, "#5f4126")
b.set(8, 89, "#5f4126")
b.set(25, 89, "#5f4126")

# ---------------- back roof (shadowed slopes) ----------------
b.poly([(64, 34), (108, 60), (78, 49), (50, 35)], "#9e3226")    # back slope
b.poly([(64, 34), (20, 60), (50, 35)], "#9e3226")               # back-left hip

# ---------------- chimney ----------------
b.rect(84, 26, 8, 28, "#9a938a")
b.line(84, 26, 84, 53, "#b5aea3")
b.line(91, 26, 91, 53, "#6f6a61")
b.line(85, 33, 90, 33, "#6f6a61")
b.line(85, 40, 90, 40, "#6f6a61")
b.line(85, 47, 90, 47, "#6f6a61")
b.rect(83, 23, 10, 3, "#b5aea3")
b.rect(86, 23, 4, 2, "#3a3430")

# ---------------- front roof slope ----------------
b.poly([(20, 60), (64, 82), (78, 49), (50, 35)], "#c0452f")
b.poly([(28, 54), (68, 74), (71, 66), (35, 48)], "#b23a28")     # shaded tile bands
b.poly([(43, 41), (75, 57), (78, 49), (50, 35)], "#b23a28")
b.line(50, 37, 78, 51, "#d95f43")                               # ridge highlight
b.line(28, 54, 68, 74, "#9e3226")                               # tile rows
b.line(35, 48, 71, 66, "#9e3226")
b.line(43, 41, 75, 57, "#9e3226")
b.line(36, 58, 36, 60, "#9e3226")                               # tile joints
b.line(48, 64, 48, 66, "#9e3226")
b.line(60, 70, 60, 72, "#9e3226")
b.line(42, 51, 42, 53, "#9e3226")
b.line(54, 57, 54, 59, "#9e3226")
b.line(66, 63, 66, 65, "#9e3226")
b.line(50, 44, 50, 46, "#9e3226")
b.line(62, 50, 62, 52, "#9e3226")
b.line(26, 63, 26, 65, "#9e3226")                               # eave tile ends
b.line(34, 67, 34, 69, "#9e3226")
b.line(42, 71, 42, 73, "#9e3226")
b.line(50, 75, 50, 77, "#9e3226")
b.line(58, 79, 58, 81, "#9e3226")

# ---------------- right hip slope ----------------
b.poly([(64, 82), (108, 60), (78, 49)], "#a83827")
b.line(69, 71, 98, 56, "#932f20")
b.line(73, 60, 88, 53, "#932f20")
b.line(80, 65, 80, 67, "#932f20")
b.line(84, 54, 84, 56, "#932f20")
b.line(64, 82, 78, 49, "#8f2f20")                               # hip seam
b.line(72, 78, 72, 80, "#932f20")                               # hip eave tile ends
b.line(80, 74, 80, 76, "#932f20")
b.line(88, 70, 88, 72, "#932f20")
b.line(96, 66, 96, 68, "#932f20")
b.line(104, 62, 104, 64, "#932f20")

# ---------------- smoke ----------------
b.circle(88, 17, 3, (168, 168, 172, 95))
b.circle(92, 12, 2, (175, 175, 178, 60))
b.circle(86, 9, 2, (180, 180, 183, 40))
b.circle(88, 21, 1, (160, 160, 165, 120))

# ---------------- crisp RTS outline ----------------
b.outline("#241509")

result = flatten([sh, b], name="forge_house")
print(result.stats())
view(result)
finish(result)
