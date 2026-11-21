# Two-character standoff, 128x128
# Red-armored knight (left) vs green-cloaked rogue (right), moonlit night.

# ---------------- background ----------------
bg = new_canvas(128, 128, name="bg")

# sky gradient bands
bands = [
    (0, 20, "#0f0a20"),
    (20, 36, "#171030"),
    (36, 52, "#201440"),
    (52, 68, "#2b1a4e"),
    (68, 82, "#382258"),
    (82, 92, "#462a66"),
]
for y0, y1, col in bands:
    bg.rect(0, y0, 128, y1 - y0, col)
bg.dither(0, 35, 128, 2, ["#171030", "#201440"], pattern="bayer4")
bg.dither(0, 67, 128, 2, ["#2b1a4e", "#382258"], pattern="bayer4")

# stars
for x, y in [(6, 8), (18, 14), (30, 6), (44, 10), (52, 16), (78, 8), (90, 14),
             (104, 6), (118, 12), (124, 20), (10, 26), (38, 20), (112, 26)]:
    bg.set(x, y, "#cfc4ea")
for x, y in [(14, 4), (26, 18), (58, 6), (70, 14), (86, 4), (98, 18),
             (122, 8), (34, 28), (8, 40)]:
    bg.set(x, y, "#6a5c9a")

# moon halo + moon + craters
bg.circle(64, 22, 19, "#6a5a80")
bg.circle(64, 22, 15, "#f2e8c9")
bg.circle(58, 17, 3, "#dccaa0")
bg.circle(70, 27, 4, "#dccaa0")
bg.circle(61, 29, 2, "#dccaa0")
bg.circle(71, 15, 2, "#e8d8b0")

# birds
for x, y in [(86, 30), (93, 34), (100, 28)]:
    bg.set(x - 1, y + 1, "#0d0a12")
    bg.set(x, y, "#0d0a12")
    bg.set(x + 1, y + 1, "#0d0a12")

# cloud wisps
bg.ellipse(24, 28, 15, 3, "#1d1236")
bg.ellipse(102, 22, 13, 3, "#1d1236")
bg.ellipse(64, 34, 18, 2, "#2a1a44")
bg.ellipse(28, 62, 13, 2, "#241640")
bg.ellipse(106, 56, 12, 2, "#241640")

# mountains
bg.poly([(0, 90), (14, 74), (26, 84), (40, 70), (54, 86), (66, 76), (80, 88),
         (94, 72), (110, 86), (127, 78), (127, 100), (0, 100)], "#1c1233")

# wind lines
bg.line(8, 46, 24, 46, "#3c2a5e")
bg.line(98, 40, 116, 40, "#3c2a5e")
bg.line(16, 70, 30, 70, "#46306a")
bg.line(92, 62, 108, 62, "#46306a")

# ground
bg.rect(0, 92, 128, 36, "#2b2040")
bg.dither(0, 96, 128, 22, ["#2b2040", "#33264a"], pattern="bayer4")
bg.rect(0, 92, 128, 3, "#3e2d55")
bg.rect(0, 120, 128, 8, "#1a1226")
bg.ellipse(64, 99, 24, 5, "#41305c")          # moonlit pool in the gap
bg.ellipse(38, 112, 13, 3, "#170f24")          # knight shadow
bg.ellipse(90, 112, 13, 3, "#170f24")          # rogue shadow

# stones + grass tufts
for x, y in [(12, 100), (13, 100), (40, 118), (71, 122), (100, 102), (118, 116), (56, 114)]:
    bg.set(x, y, "#4a3860")
for x, y in [(20, 112), (60, 118), (90, 120), (112, 106)]:
    bg.set(x, y, "#1c1430")
for x, y in [(8, 95), (48, 94), (80, 95), (112, 94), (30, 96), (98, 96)]:
    bg.set(x, y - 2, "#1c4a3a")
    bg.set(x - 1, y - 1, "#1c4a3a")
    bg.set(x + 1, y - 1, "#1c4a3a")

# ---------------- knight (left, facing right) ----------------
kn = new_canvas(128, 128, name="knight")

# cape
kn.poly([(36, 60), (24, 62), (14, 68), (18, 74), (8, 82), (18, 86), (12, 96),
         (24, 94), (30, 86), (34, 76)], "#560e1a")
kn.poly([(33, 64), (24, 66), (17, 72), (21, 78), (13, 84), (21, 88), (17, 93),
         (26, 91), (31, 84), (33, 76)], "#8c1626")

# legs
kn.rect(33, 88, 8, 9, "#8c1420")        # back thigh
kn.rect(41, 88, 8, 9, "#c01e28")        # front thigh
kn.circle(36, 98, 2, "#8a93a8")         # back knee
kn.circle(46, 98, 2, "#dde4ee")         # front knee
kn.rect(32, 100, 8, 9, "#c01e28")       # back greave
kn.rect(32, 100, 2, 9, "#8c1420")
kn.rect(43, 100, 8, 9, "#c01e28")       # front greave
kn.rect(43, 100, 1, 9, "#e84838")
kn.poly([(32, 108), (41, 108), (41, 112), (27, 112)], "#8c1420")   # back foot
kn.poly([(44, 108), (52, 108), (57, 112), (44, 112)], "#8c1420")   # front foot
kn.line(27, 111, 30, 111, "#8a93a8")
kn.line(54, 111, 57, 111, "#dde4ee")

# torso
kn.poly([(35, 62), (47, 62), (49, 74), (47, 86), (36, 86), (34, 74)], "#c01e28")
kn.rect(34, 64, 4, 20, "#8c1420")
kn.rect(44, 64, 3, 20, "#e84838")
kn.line(36, 63, 46, 63, "#e0a83c")               # gold collar trim
kn.rect(35, 84, 13, 3, "#9c6f24")                # belt
kn.rect(39, 84, 4, 3, "#e0a83c")                 # buckle

# tassets
kn.poly([(36, 87), (41, 87), (40, 94), (35, 93)], "#8c1420")
kn.poly([(43, 87), (48, 87), (49, 93), (44, 94)], "#8c1420")

# pauldrons
kn.circle(33, 66, 5, "#8c1420")
kn.circle(33, 65, 4, "#c01e28")
kn.circle(47, 67, 5, "#c01e28")
kn.circle(46, 65, 4, "#e84838")
kn.set(44, 63, "#ff8a68")
kn.set(31, 62, "#e84838")

# neck
kn.rect(37, 60, 6, 2, "#8c1420")

# back arm (to lower grip)
kn.poly([(35, 67), (40, 71), (51, 80), (48, 86), (37, 76), (33, 72)], "#8c1420")
# grip
kn.line(54, 79, 50, 87, "#3a2a16")
kn.set(49, 88, "#e0a83c")                        # pommel
kn.circle(51, 84, 3, "#8a93a8")                  # back gauntlet
# front arm
kn.poly([(44, 66), (50, 67), (56, 75), (54, 80), (47, 73), (42, 70)], "#c01e28")
kn.circle(54, 78, 3, "#dde4ee")                  # front gauntlet

# sword: guard then broad blade raised across the moon
kn.line(49, 74, 59, 78, "#e0a83c")
kn.line(49, 75, 59, 79, "#9c6f24")
kn.poly([(52, 78), (55, 79), (72, 36), (69, 34)], "#dde4ee")
kn.line(55, 78, 72, 36, "#565d70")
kn.set(71, 35, "#dde4ee")

# helmet
kn.circle(40, 55, 6, "#c01e28")
kn.poly([(34, 51), (37, 49), (37, 61), (34, 59)], "#8c1420")
kn.poly([(40, 50), (45, 50), (47, 54), (46, 60), (40, 60)], "#8a93a8")   # faceplate
kn.line(45, 51, 46, 59, "#dde4ee")
kn.rect(41, 53, 6, 2, "#0d0a12")                 # visor slit
kn.set(45, 54, "#ff5040")                        # eye glow
kn.set(43, 57, "#565d70")
kn.set(45, 57, "#565d70")

# plume
kn.poly([(40, 50), (33, 42), (21, 37), (27, 45), (13, 45), (27, 51), (39, 53)], "#f2ecdc")
kn.line(39, 53, 27, 51, "#b0a68c")
kn.line(27, 51, 15, 46, "#b0a68c")

kn.outline("#0d0a12")

# ---------------- rogue (right, facing left) ----------------
rg = new_canvas(128, 128, name="rogue")

# cloak (behind)
rg.poly([(92, 60), (104, 62), (116, 68), (111, 76), (120, 84), (110, 92),
         (117, 100), (104, 100), (95, 92), (90, 78)], "#123f22")
rg.poly([(94, 64), (103, 66), (112, 71), (108, 78), (115, 85), (107, 91),
         (112, 97), (103, 96), (96, 89), (93, 78)], "#1e6b38")

# legs
rg.poly([(89, 87), (98, 93), (96, 100), (87, 94)], "#1e6b38")      # back thigh
rg.poly([(96, 98), (103, 107), (108, 112), (98, 112), (93, 103)], "#3a2a16")  # back boot
rg.poly([(88, 87), (80, 91), (77, 97), (86, 96)], "#1e6b38")       # front thigh
rg.poly([(77, 95), (76, 108), (81, 108), (82, 97)], "#6b4a2a")     # front shin
rg.poly([(74, 108), (82, 108), (82, 112), (72, 112)], "#3a2a16")   # front foot

# torso
rg.poly([(84, 62), (93, 64), (92, 86), (82, 86), (80, 72)], "#1e6b38")
rg.poly([(82, 66), (85, 65), (84, 85), (81, 84)], "#37a057")
rg.line(83, 66, 91, 80, "#3a2a16")               # chest strap
rg.rect(81, 83, 11, 3, "#3a2a16")                # belt
rg.rect(85, 83, 3, 3, "#e0a83c")                 # buckle

# back arm + second dagger (lowered)
rg.poly([(90, 69), (95, 76), (94, 84), (89, 82), (88, 74)], "#123f22")
rg.circle(94, 85, 2, "#e8b58c")
rg.poly([(95, 86), (97, 87), (102, 95)], "#8a93a8")
rg.set(101, 94, "#565d70")

# front arm extended with dagger
rg.poly([(84, 67), (78, 71), (72, 78), (75, 82), (81, 76), (87, 71)], "#1e6b38")
rg.circle(74, 79, 2, "#e8b58c")
rg.line(71, 80, 75, 76, "#e0a83c")               # dagger guard
rg.poly([(72, 78), (74, 76), (64, 68)], "#dde4ee")
rg.line(74, 77, 65, 69, "#565d70")

# shoulders
rg.circle(88, 67, 5, "#1e6b38")
rg.circle(83, 69, 4, "#37a057")

# hood + face
rg.poly([(86, 47), (95, 50), (97, 58), (93, 63), (82, 63), (77, 59), (79, 51)], "#1e6b38")
rg.poly([(84, 49), (93, 52), (94, 57), (91, 60), (89, 53), (83, 51)], "#37a057")
rg.poly([(80, 54), (88, 53), (90, 60), (82, 60)], "#0a120c")       # face shadow
rg.rect(82, 59, 5, 2, "#b8845c")                                    # chin hint
rg.set(82, 56, "#b8f0a0"); rg.set(83, 56, "#b8f0a0")                # glowing eyes
rg.set(86, 56, "#b8f0a0"); rg.set(87, 56, "#b8f0a0")
rg.line(79, 51, 77, 58, "#6fd08a")               # hood rim light

# scarf trailing
rg.poly([(86, 62), (96, 60), (106, 57), (101, 63), (110, 63), (99, 68), (89, 66)], "#37a057")

rg.outline("#0d0a12")

# ---------------- effects ----------------
fx = new_canvas(128, 128, name="fx")
# tension spark in the gap (star burst)
fx.line(67, 57, 67, 61, "#ffd84a"); fx.line(67, 63, 67, 67, "#ffd84a")
fx.line(62, 62, 66, 62, "#ffd84a"); fx.line(68, 62, 72, 62, "#ffd84a")
fx.set(64, 59, "#e8a838"); fx.set(70, 59, "#e8a838")
fx.set(64, 65, "#e8a838"); fx.set(70, 65, "#e8a838")
fx.set(67, 62, "#fff6d8"); fx.set(66, 61, "#fff6d8"); fx.set(68, 63, "#fff6d8")
# drifting petals / leaves
fx.set(58, 64, "#e84838"); fx.set(59, 64, "#e84838")
fx.set(60, 55, "#c01e28"); fx.set(57, 76, "#e84838")
fx.set(74, 58, "#37a057"); fx.set(73, 72, "#1e6b38")
fx.set(75, 84, "#37a057"); fx.set(72, 50, "#1e6b38")
# ground crack
fx.line(59, 101, 64, 103, "#0d0a12")
fx.line(64, 103, 70, 105, "#0d0a12")
fx.line(64, 103, 61, 108, "#0d0a12")
fx.line(67, 104, 71, 109, "#0d0a12")
# dust puffs
for x, y in [(25, 106), (29, 104), (52, 105), (55, 106), (80, 105), (99, 104), (103, 106)]:
    fx.set(x, y, "#4a3a5e")

# ---------------- composite ----------------
final = flatten([bg, kn, rg, fx], name="standoff")

view(final)
print(final.stats_text())
finish(final)
