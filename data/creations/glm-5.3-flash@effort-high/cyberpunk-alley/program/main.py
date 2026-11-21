import random

random.seed(11)

W = H = 128
c = new_canvas(W, H, background="#06060e", name="cyberpunk-alley")

# ---------------- palette ----------------
SKY_MID  = c.color("#0c1022", name="sky_mid")
SKY_LOW  = c.color("#151c39", name="sky_low")
WALL     = c.color("#171728", name="wall")
WALL_L   = c.color("#21213a", name="wall_lit")
WALL_D   = c.color("#101020", name="wall_dark")
BACK     = c.color("#0d0d1a", name="back_wall")
FLOOR    = c.color("#0c0c16", name="floor")
FLOOR_L  = c.color("#141424", name="floor_line")
PUDDLE   = c.color("#05050c", name="puddle")
PINK     = c.color("#ff2d78", name="neon_pink")
PINK_M   = c.color("#7a1a44", name="pink_mid")
PINK_D   = c.color("#43122e", name="pink_dim")
CYAN     = c.color("#00e5ff", name="neon_cyan")
CYAN_D   = c.color("#0a3542", name="cyan_dim")
ORANGE   = c.color("#ff9e2c", name="neon_orange")
ORANGE_D = c.color("#43260c", name="orange_dim")
PURPLE   = c.color("#9b5cff", name="neon_purple")
PURPLE_D = c.color("#281a44", name="purple_dim")
YELLOW   = c.color("#ffd75e", name="warm_light")
YELLOW_D = c.color("#3a2c10", name="warm_dim")
WHITE    = c.color("#eaf6ff", name="white")
INK      = c.color("#04040a", name="silhouette")
CABLE    = c.color("#08080f", name="cable")
RAIN     = c.color("#222b47", name="rain")
RAIN_B   = c.color("#5d74a8", name="rain_bright")
VM_BODY  = c.color("#101022", name="vm_body")
VM_EDGE  = c.color("#23233c", name="vm_edge")
VM_PANEL = c.color("#071019", name="vm_panel")
DOOR     = c.color("#241608", name="door")
UMB      = c.color((150, 172, 208, 105), name="umbrella")
UMB_R    = c.color("#a9bdd9", name="umbrella_rim")
UMB_P    = c.color((255, 45, 120, 90), name="umb_pink")
UMB_C    = c.color((0, 229, 255, 80), name="umb_cyan")

# ---------------- sky ----------------
c.rect(0, 16, 128, 16, SKY_MID)
c.rect(0, 32, 128, 12, SKY_LOW)

# distant skyline inside the sky wedge
for (bx, by, bw, bh) in [(44, 30, 7, 12), (54, 24, 6, 18), (68, 28, 8, 14), (79, 33, 6, 9)]:
    c.rect(bx, by, bw, bh, "#0a0c18")
c.set(56, 26, YELLOW_D); c.set(57, 29, YELLOW_D)
c.set(70, 31, CYAN_D); c.set(72, 34, YELLOW_D)
c.line(57, 24, 57, 18, CABLE); c.set(57, 17, PINK)  # antenna beacon

# ---------------- walls ----------------
c.poly([(0, 0), (40, 42), (40, 96), (0, 128)], WALL)            # left wall
c.poly([(128, 0), (88, 42), (88, 96), (128, 128)], WALL)        # right wall
c.rect(40, 42, 48, 54, BACK)                                    # back wall
c.line(40, 42, 40, 96, WALL_L)                                  # inner corners
c.line(88, 42, 88, 96, WALL_L)
c.poly([(40, 96), (88, 96), (128, 128), (0, 128)], FLOOR)       # alley floor

# wall panel seams
for y in (52, 66, 82):
    c.line(0, y, 40, min(96, y + 14), "#12121f")
    c.line(128, y, 88, min(96, y + 14), "#12121f")

# ---------------- back-wall details ----------------
c.rect(46, 58, 4, 5, YELLOW_D); c.set(47, 60, YELLOW)
c.rect(76, 54, 4, 5, YELLOW_D); c.set(78, 56, YELLOW)
c.rect(52, 70, 3, 4, CYAN_D)
# distant purple sign
c.rect(56, 48, 16, 16, PURPLE_D)
c.rect(58, 50, 12, 12, BACK)
c.rect(58, 50, 12, 12, PURPLE, fill=False)
c.rect(61, 53, 3, 6, PURPLE); c.rect(65, 53, 3, 6, PURPLE)
# glowing doorway at the alley end (backlight for the figure)
c.rect(54, 78, 14, 20, ORANGE_D)
c.rect(56, 80, 10, 18, DOOR)
c.rect(58, 84, 6, 12, ORANGE)
c.rect(60, 86, 2, 8, YELLOW)

# ---------------- power cables + lamps ----------------
c.path("M -2 14 Q 64 34 127 10", CABLE, fill=False)
c.path("M -2 30 Q 64 46 127 26", CABLE, fill=False)
c.path("M 34 46 Q 64 58 96 44", CABLE, fill=False)
# hanging lamp on cable 1
c.line(64, 25, 64, 31, CABLE)
c.rect(62, 31, 4, 5, "#0a0a12")
c.circle(64, 34, 4, YELLOW_D)
c.set(63, 33, YELLOW); c.set(64, 33, YELLOW); c.set(64, 34, YELLOW)
# second small lamp
c.line(44, 39, 44, 44, CABLE)
c.circle(44, 46, 3, YELLOW_D)
c.set(44, 45, YELLOW)

# ---------------- LEFT WALL NEON ----------------
# vertical pink sign with CJK glyphs
c.rect(4, 24, 18, 44, PINK_D)
c.rect(6, 26, 14, 40, "#191928")
c.rect(6, 26, 14, 40, PINK, fill=False)
c.text(7, 30, "\u9152", PINK, font="12px")   # sake
c.text(7, 44, "\u5734", PINK, font="12px")   # place
c.rect(9, 62, 8, 1, PINK)
# cyan OPEN sign
c.rect(1, 72, 34, 11, CYAN_D)
c.rect(2, 74, 32, 8, "#06202a")
c.rect(2, 74, 32, 8, CYAN, fill=False)
c.text(8, 75, "OPEN", CYAN, font="5x7")
# AC unit dripping
c.rect(24, 48, 9, 6, WALL_D)
c.rect(24, 48, 9, 6, VM_EDGE, fill=False)
for dy in range(4):
    c.set(28, 55 + dy * 2, CYAN_D)
# pipe along wall base
c.line(0, 68, 40, 94, "#0a0a14")
c.set(10, 75, "#0a0a14"); c.set(24, 84, "#0a0a14")

# ---------------- RIGHT WALL NEON ----------------
# vertical orange sign with CJK glyphs
c.rect(102, 24, 18, 44, ORANGE_D)
c.rect(104, 26, 14, 40, "#1c1420")
c.rect(104, 26, 14, 40, ORANGE, fill=False)
c.text(105, 30, "\u591c", ORANGE, font="12px")  # night
c.text(105, 44, "\u98df", ORANGE, font="12px")  # food
c.rect(107, 62, 8, 1, ORANGE)
# purple LIVE sign
c.rect(93, 70, 34, 11, PURPLE_D)
c.rect(94, 72, 32, 8, "#150f26")
c.rect(94, 72, 32, 8, PURPLE, fill=False)
c.text(102, 73, "LIVE", PURPLE, font="5x7")
# AC unit
c.rect(96, 44, 8, 6, WALL_D)
c.rect(96, 44, 8, 6, VM_EDGE, fill=False)
c.line(127, 62, 88, 92, "#0a0a14")

# ---------------- vending machine (left foreground) ----------------
c.rect(7, 81, 24, 36, CYAN_D)                 # glow halo
c.poly([(27, 84), (30, 86), (30, 114), (27, 114)], WALL_D)   # side face
c.rect(10, 84, 18, 30, VM_BODY)
c.rect(10, 84, 18, 30, VM_EDGE, fill=False)
c.rect(12, 85, 14, 2, CYAN_D)
c.set(13, 85, CYAN); c.set(18, 85, CYAN); c.set(23, 85, CYAN)
c.rect(13, 88, 12, 15, VM_PANEL)
items = [PINK, CYAN, ORANGE, CYAN, PINK, PURPLE, ORANGE, CYAN, PINK]
i = 0
for row in (90, 95, 100):
    for col in (14, 18, 22):
        c.rect(col, row, 3, 3, items[i]); i += 1
c.rect(13, 105, 12, 5, INK)
c.line(13, 106, 24, 106, CYAN)
c.ellipse(19, 116, 12, 2, INK)                # base shadow

# ---------------- wet floor ----------------
c.rect(44, 98, 40, 1, FLOOR_L)
c.rect(34, 103, 60, 1, FLOOR_L)
c.rect(22, 109, 84, 1, FLOOR_L)
c.rect(8, 117, 112, 1, FLOOR_L)
c.rect(0, 125, 128, 1, FLOOR_L)

# neon smear reflections on the wet asphalt
for y in range(98, 112, 3):
    c.rect(10, y, 20, 1, CYAN_D)
for y in range(96, 106, 3):
    c.rect(92, y, 14, 1, PURPLE_D)
for y in range(98, 110, 3):
    c.rect(104, y, 12, 1, ORANGE_D)
for y in range(110, 122, 3):
    c.rect(8, y, 12, 1, PINK_D)

# ---------------- puddles + reflections ----------------
# puddle A (left, under pink/cyan signs)
c.ellipse(34, 118, 20, 5, PUDDLE)
for y in range(114, 123, 2):
    c.rect(16, y, 10, 1, PINK_M)
for y in range(115, 122, 2):
    c.rect(28, y, 16, 1, CYAN_D)
c.set(18, 114, PINK); c.set(21, 116, PINK)
c.set(30, 116, CYAN); c.set(36, 118, CYAN)
# puddle B (right, under orange/purple signs)
c.ellipse(98, 112, 15, 4, PUDDLE)
for y in range(109, 116, 2):
    c.rect(102, y, 11, 1, ORANGE_D)
for y in range(109, 114, 2):
    c.rect(88, y, 11, 1, PURPLE_D)
c.set(104, 110, ORANGE); c.set(109, 112, ORANGE)
c.set(90, 110, PURPLE)
# glow pool + puddle C behind the figure
c.ellipse(60, 118, 14, 5, PINK_D)
c.ellipse(60, 118, 8, 3, PINK_M)
c.ellipse(60, 124, 12, 3, PUDDLE)
c.set(54, 123, PINK); c.set(66, 124, PINK_M); c.set(60, 126, PINK_M)

# ---------------- rain ----------------
for _ in range(110):
    x = random.randint(-4, 128)
    y = random.randint(-4, 118)
    ln = random.randint(3, 8)
    c.line(x, y, x - max(1, ln // 3), y + ln, RAIN)
# bright streaks catching the neon
for (x, y, ln, col) in [(12, 20, 6, PINK), (18, 34, 5, PINK), (9, 52, 6, PINK),
                        (26, 60, 5, CYAN), (16, 78, 6, CYAN), (30, 70, 5, CYAN),
                        (110, 22, 6, ORANGE), (116, 38, 5, ORANGE), (106, 54, 6, ORANGE),
                        (98, 66, 5, PURPLE), (120, 74, 6, PURPLE), (70, 18, 6, RAIN_B),
                        (52, 30, 5, RAIN_B), (84, 26, 6, RAIN_B)]:
    c.line(x, y, x - max(1, ln // 3), y + ln, col)

# ---------------- the figure with a transparent umbrella ----------------
# canopy (translucent fill, lit rim, ribs)
c.ellipse(60, 89, 15, 6, UMB)
c.set(48, 88, UMB_P); c.set(50, 90, UMB_P); c.set(52, 87, UMB_P)
c.set(70, 88, UMB_C); c.set(72, 90, UMB_C)
c.path("M 45 89 A 15 6 0 0 1 75 89", UMB_R, fill=False)
c.line(60, 84, 47, 90, UMB_R)
c.line(60, 84, 73, 90, UMB_R)
c.line(60, 84, 60, 95, UMB_R)
# pole + arm
c.line(60, 90, 66, 101, INK)
c.line(64, 106, 66, 101, INK)
c.set(66, 101, INK)
# body silhouette
c.circle(60, 98, 3, INK)
c.poly([(55, 103), (65, 103), (64, 112), (63, 118), (57, 118), (56, 112)], INK)
c.rect(56, 116, 3, 6, INK)
c.rect(61, 116, 3, 6, INK)
c.rect(55, 121, 5, 1, INK)
c.rect(61, 121, 5, 1, INK)
# neon rim light on the silhouette
for (x, y) in [(55, 104), (54, 106), (54, 108), (54, 110), (55, 112), (57, 97)]:
    c.set(x, y, PINK)
for (x, y) in [(65, 104), (65, 107), (64, 111), (63, 97), (62, 95)]:
    c.set(x, y, CYAN)
# reflection of the figure in puddle C
for y in range(122, 127, 2):
    c.rect(56, y, 9, 1, "#06060e")
c.set(58, 122, INK); c.set(62, 124, INK)

# rain splashes on the puddles
for (x, y) in [(28, 117), (46, 120), (92, 111), (104, 113), (70, 123), (36, 121)]:
    c.set(x - 1, y, RAIN_B); c.set(x, y - 1, RAIN_B); c.set(x + 1, y, RAIN_B)

print(c.stats_text())
finish(c)
