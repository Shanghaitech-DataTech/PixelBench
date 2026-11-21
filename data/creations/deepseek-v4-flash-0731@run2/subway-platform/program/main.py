from pixelbench_api import new_canvas, flatten, finish

WALL = (18, 18, 30); WALL2 = (24, 24, 38)
LAMP = (255, 236, 178); LAMP_DIM = (188, 168, 124)
SIGN_BG = (12, 14, 24); WHITE = (242, 242, 244); BLUE = (38, 96, 168)
T_BODY = (174, 184, 196); T_SHADE = (136, 146, 160); T_WIN = (26, 34, 60)
T_STREAK = (238, 242, 250); T_RED = (200, 62, 62); T_DARK = (98, 108, 122)
GLASS = (150, 180, 206, 110); GREFL = (208, 224, 240, 64)
FRAME = (162, 172, 186); BASE = (62, 74, 90)
PILLAR = (102, 112, 128); PILLAR_HI = (124, 136, 152); PILLAR_DK = (82, 90, 104)
FLOOR = (74, 74, 88); FLOOR_LT = (94, 94, 110); FLOOR_DK = (56, 56, 70)
YELLOW = (240, 198, 84)
WOOD = (140, 96, 60); WOOD_DK = (94, 62, 36); METAL = (52, 54, 66)
PASS = (26, 26, 38); PASS_HI = (60, 60, 84)

back = new_canvas(64, 64, background=WALL, name="back")
# wall tiling
for x in range(8, 64, 8):
    back.rect(x, 0, 1, 64, WALL2)
# ceiling lamps
for lx in (6, 40):
    back.rect(lx, 2, 12, 3, LAMP_DIM)
    back.rect(lx + 2, 2, 8, 2, LAMP)
# station sign (no brand)
back.rect(3, 5, 50, 9, SIGN_BG)
back.rect(3, 12, 50, 1, WHITE)
back.text(5, 7, "PLATFORM", WHITE, font="5x7")
back.circle(57, 9, 3, BLUE)
back.rect(55, 9, 5, 1, WHITE)

# arriving train passes behind the doors
back.rect(0, 16, 64, 30, T_BODY)
back.rect(21, 16, 2, 30, WALL)   # gap between cars
back.rect(43, 16, 2, 30, WALL)
back.rect(0, 16, 3, 30, T_SHADE)  # nose
back.rect(1, 18, 2, 13, T_WIN)     # windshield
back.rect(0, 39, 64, 2, T_RED)     # stripe
back.rect(0, 41, 64, 5, T_DARK)    # skirt
cars = [(4, 20), (23, 42), (45, 63)]
for ci, (a, b) in enumerate(cars):
    back.rect(a, 22, b - a, 15, T_WIN)
    for y in (24, 28, 32):
        s = a + (ci * 2 + y) % 4
        for x in range(s, b, 5):
            back.rect(x, y, 2, 1, T_STREAK)
back.rect(1, 33, 2, 3, LAMP)       # headlight

# platform screen doors
doors = new_canvas(64, 64, name="doors")
for fx in range(2, 59, 8):
    gw = min(6, 63 - (fx + 2))
    doors.rect(fx + 2, 14, gw, 26, GLASS)
    doors.rect(fx + 3, 15, 1, 9, GREFL)
for fx in range(2, 59, 8):
    doors.rect(fx, 12, 2, 34, FRAME)
doors.rect(2, 40, 61, 6, BASE)

scene = flatten([back, doors], name="scene")

# platform floor with perspective
scene.rect(0, 48, 64, 16, FLOOR)
scene.rect(0, 46, 64, 2, YELLOW)
for y in (50, 53, 57, 62):
    scene.rect(0, y, 64, 1, FLOOR_DK)
for xt, xb in [(10, 5), (24, 18), (44, 40), (56, 62)]:
    scene.line(xt, 47, xb, 63, FLOOR_DK)
scene.rect(4, 51, 12, 2, FLOOR_LT)   # light pools
scene.rect(38, 51, 12, 2, FLOOR_LT)

# pillar in front (depth)
scene.rect(30, 0, 4, 64, PILLAR)
scene.rect(30, 0, 1, 64, PILLAR_HI)
scene.rect(33, 0, 1, 64, PILLAR_DK)

# bench
scene.rect(19, 41, 2, 9, WOOD_DK)
scene.rect(20, 49, 10, 2, WOOD)
scene.rect(20, 51, 2, 8, METAL)
scene.rect(28, 51, 2, 8, METAL)

# passenger 1: sitting (bench, facing right)
scene.rect(23, 36, 5, 5, PASS)
scene.rect(22, 41, 5, 8, PASS)
scene.rect(24, 43, 4, 6, PASS)
scene.rect(26, 49, 2, 6, PASS)
scene.rect(24, 54, 4, 1, PASS)

# passenger 2: standing, close (left)
scene.rect(5, 32, 6, 6, PASS)
scene.rect(4, 37, 8, 11, PASS)
scene.rect(3, 38, 2, 9, PASS)
scene.rect(2, 44, 1, 3, LAMP)      # phone in hand
scene.rect(9, 40, 2, 6, PASS)
scene.rect(6, 47, 2, 10, PASS)
scene.rect(9, 47, 2, 9, PASS)
scene.rect(5, 56, 3, 2, PASS)
scene.rect(9, 56, 3, 2, PASS)
scene.rect(4, 37, 1, 8, PASS_HI)

# passenger 3: walking, farther (right)
scene.rect(47, 39, 5, 4, PASS)
scene.rect(46, 42, 7, 6, PASS)
scene.rect(45, 43, 2, 7, PASS)
scene.rect(51, 43, 2, 7, PASS)
scene.rect(44, 47, 2, 7, PASS)
scene.rect(50, 47, 2, 7, PASS)
scene.rect(43, 53, 3, 1, PASS)
scene.rect(50, 53, 3, 1, PASS)
scene.rect(46, 43, 1, 6, PASS_HI)

print(scene.stats_text())
finish(scene)
