from pixelbench_api import *

W, H = 48, 48
dx, dy = 5, 0

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, dx, dy)

f2 = new_canvas(W, H, name="f2")

# Palette constants
TRANSPARENT = 0
C0  = 1   # #422110 dark brown outline
C1  = 2   # #7b4231 dark warm brown / skin shadow
C2  = 3   # #c5956a mid skin / tan
C3  = 4   # #ffffff white highlight / string / grip
C4  = 5   # #949473 dark blonde / olive shadow
C5  = 6   # #f3f4b6 light blonde
C6  = 7   # #ffe75a bright yellow / gold
C7  = 8   # #c30074 bright magenta
C8  = 9   # #df9859 warm peach
C9  = 10  # #55002a deep purple / magenta shadow
C10 = 11  # #ef5ba1 pink / magenta midtone
C11 = 12  # #f6d39b light skin / hair highlight / string
C12 = 13  # #e0c89e warm cream / string
C13 = 14  # #faf3c9 pale blonde
C14 = 15  # #f1d8b3 skin highlight
C15 = 16  # #a9794f leather
C16 = 17  # #8e7058 boot shadow
C17 = 18  # #907859 leather
C18 = 19  # #fcc44c gold
C19 = 20  # #121311 darkest black outline
C20 = 21  # #9e005d dark magenta
C21 = 22  # #529439 mid green
C22 = 23  # #f6adcd pale pink
C23 = 24  # #304915 deep green shadow
C24 = 25  # #14110e warm black outline
C25 = 26  # #9cde5a bright lime green
C26 = 27  # #bc6c0c dark gold / bronze
C27 = 28  # #252a23 dark grey fabric
C28 = 29  # #f1f7f7 light grey/white bracer
C29 = 30  # #4f7229 dark green fabric
C30 = 31  # #3c3c3c dark grey bracer
C31 = 32  # #687862 mid grey bracer
C32 = 33  # #a4b496 light sage bracer
C33 = 34  # #e1d4c2 pale leather / grip
C34 = 35  # #ffffce cream highlight
C35 = 36  # #534338 boot brown
C36 = 37  # #74341c boot red-brown
C37 = 38  # #48382f boot shadow
C38 = 39  # #313b31 dark green-grey fabric
C39 = 40  # #5d422f boot leather
C40 = 41  # #d1b6a2 boot light leather
C41 = 42  # #17003599 translucent purple shadow

# 1. Base copy from f1
for y in range(H):
    for x in range(W):
        f2.set(x, y, f1.get(x, y))

# Clear old bow, string, resting arm, and left arm
for y in range(0, 40):
    for x in range(32, W):
        f2.set(x, y, TRANSPARENT)

for y in range(33, 40):
    for x in range(26, 32):
        f2.set(x, y, TRANSPARENT)

for y in range(4, 34):
    for x in range(28, 33):
        if y < 20 or y > 25:
            f2.set(x, y, TRANSPARENT)

# Clear old resting arm (rows 15-26, cols 6-17)
for y in range(15, 27):
    for x in range(6, 17):
        f2.set(x, y, TRANSPARENT)

# Clear old left arm (rows 19-26, cols 22-38)
for y in range(19, 27):
    for x in range(22, 38):
        f2.set(x, y, TRANSPARENT)

# 2. Torso side, chest, halter top, midriff, and belt
torso_pixels = [
    # y=16: neckline
    (16, 14, C19), (16, 15, C1),  (16, 16, C2),  (16, 17, C11), (16, 18, C26), (16, 19, C18), (16, 20, C18), (16, 21, C26), (16, 22, C19),
    # y=17: green halter top
    (17, 13, C19), (17, 14, C23), (17, 15, C29), (17, 16, C21), (17, 17, C25), (17, 18, C25), (17, 19, C25), (17, 20, C21), (17, 21, C29), (17, 22, C19),
    # y=18: halter top with gold border
    (18, 13, C19), (18, 14, C23), (18, 15, C21), (18, 16, C25), (18, 17, C26), (18, 18, C18), (18, 19, C18), (18, 20, C26), (18, 21, C23), (18, 22, C19),
    # y=19: midriff (bare skin)
    (19, 13, C19), (19, 14, C1),  (19, 15, C2),  (19, 16, C11), (19, 17, C14), (19, 18, C14), (19, 19, C11), (19, 20, C2),  (19, 21, C1),  (19, 22, C19),
    # y=20: midriff
    (20, 12, C19), (20, 13, C1),  (20, 14, C2),  (20, 15, C11), (20, 16, C14), (20, 17, C14), (20, 18, C14), (20, 19, C11), (20, 20, C2),  (20, 21, C1),  (20, 22, C19),
    # y=21: lower midriff
    (21, 12, C19), (21, 13, C1),  (21, 14, C2),  (21, 15, C11), (21, 16, C11), (21, 17, C14), (21, 18, C14), (21, 19, C11), (21, 20, C2),  (21, 21, C1),  (21, 22, C19),
    # y=22: gold belt top
    (22, 11, C19), (22, 12, C26), (22, 13, C18), (22, 14, C18), (22, 15, C26), (22, 16, C26), (22, 17, C18), (22, 18, C18), (22, 19, C26), (22, 20, C26), (22, 21, C19),
    # y=23: gold belt body & sash knot
    (23, 11, C19), (23, 12, C26), (23, 13, C18), (23, 14, C6),  (23, 15, C18), (23, 16, C21), (23, 17, C25), (23, 18, C21), (23, 19, C18), (23, 20, C26), (23, 21, C19),
    # y=24: gold belt bottom
    (24, 11, C19), (24, 12, C26), (24, 13, C26), (24, 14, C18), (24, 15, C26), (24, 16, C23), (24, 17, C29), (24, 18, C23), (24, 19, C26), (24, 20, C26), (24, 21, C19),
    # y=25: hakama waist
    (25, 11, C19), (25, 12, C27), (25, 13, C38), (25, 14, C38), (25, 15, C38), (25, 16, C27), (25, 17, C27), (25, 18, C38), (25, 19, C38), (25, 20, C27), (25, 21, C19),
    # y=26: connect hakama
    (26, 11, C19), (26, 12, C27), (26, 13, C38), (26, 14, C38), (26, 15, C38), (26, 16, C27),
]
for y, x, c in torso_pixels:
    f2.set(x, y, c)

# 3. Draw Arm (Right Arm):
# Raised high elbow at x=5..8, y=14..17
# Forearm coming forward to chin at x=21..24, y=15..18
# Solid 4-5px thick arm!
right_arm_pixels = [
    # Elbow joint (outermost point on left):
    (14, 6, C19),  (14, 7, C19),  (14, 8, C19),
    (15, 5, C19),  (15, 6, C1),   (15, 7, C2),   (15, 8, C11),  (15, 9, C14),
    (16, 5, C19),  (16, 6, C0),   (16, 7, C1),   (16, 8, C2),   (16, 9, C11),  (16, 10, C14),
    (17, 6, C19),  (17, 7, C0),   (17, 8, C1),   (17, 9, C2),   (17, 10, C19),

    # Upper arm connecting shoulder to elbow:
    (14, 9, C11),  (14, 10, C14), (14, 11, C19),
    (15, 10, C11), (15, 11, C14), (15, 12, C19),
    (16, 11, C2),  (16, 12, C11), (16, 13, C19),

    # Magenta arm band on upper arm (prominent like Frame 1):
    (14, 9, C7),   (14, 10, C10),
    (15, 8, C9),   (15, 9, C7),   (15, 10, C10), (15, 11, C22),
    (16, 8, C9),   (16, 9, C7),   (16, 10, C7),

    # Magenta ribbon fluttering behind elbow:
    (17, 4, C19),  (17, 5, C9),   (17, 6, C7),
    (18, 4, C19),  (18, 5, C7),   (18, 6, C10),  (18, 7, C19),
    (19, 5, C19),  (19, 6, C9),   (19, 7, C19),

    # Forearm extending forward to cheek/anchor point (rows 15-18, cols 10-22):
    # Top edge of forearm:
    (14, 12, C19), (14, 13, C19), (14, 14, C19), (14, 15, C19), (14, 16, C19), (14, 17, C19),
    # Forearm body (highlights and midtones):
    (15, 12, C14), (15, 13, C14), (15, 14, C14), (15, 15, C14), (15, 16, C14), (15, 17, C14), (15, 18, C14), (15, 19, C19),
    (16, 11, C11), (16, 12, C11), (16, 13, C11), (16, 14, C11), (16, 15, C11), (16, 16, C11), (16, 17, C11), (16, 18, C14), (16, 19, C14), (16, 20, C19),
    # Forearm underside shadow:
    (17, 10, C1),  (17, 11, C1),  (17, 12, C2),  (17, 13, C2),  (17, 14, C2),  (17, 15, C2),  (17, 16, C2),  (17, 17, C2),  (17, 18, C11), (17, 19, C11), (17, 20, C14), (17, 21, C19),
    # Bottom outline of forearm:
    (18, 11, C19), (18, 12, C19), (18, 13, C19), (18, 14, C19), (18, 15, C19), (18, 16, C19), (18, 17, C19), (18, 18, C19), (18, 19, C19), (18, 20, C19), (18, 21, C19),

    # Hand hooked around string at cheek (x=21..24, y=15..18):
    (15, 20, C19), (15, 21, C14), (15, 22, C11), (15, 23, C19),
    (16, 21, C14), (16, 22, C14), (16, 23, C11), (16, 24, C19),
    (17, 21, C11), (17, 22, C2),  (17, 23, C1),  (17, 24, C19),
    (18, 21, C19), (18, 22, C19), (18, 23, C19),
]
for y, x, c in right_arm_pixels:
    f2.set(x, y, c)

# 4. Bow Arm (Left Arm):
# Straight locked forward arm with grey leather/metal bracer
bow_arm_pixels = [
    # Shoulder connection:
    (16, 24, C19), (16, 25, C21), (16, 26, C25), (16, 27, C19),
    (17, 24, C1),  (17, 25, C2),  (17, 26, C11), (17, 27, C14),

    # Bracer top outline:
    (16, 28, C19), (16, 29, C19), (16, 30, C19), (16, 31, C19), (16, 32, C19), (16, 33, C19), (16, 34, C19), (16, 35, C19), (16, 36, C19), (16, 37, C19),
    # Bracer highlight:
    (17, 28, C32), (17, 29, C28), (17, 30, C32), (17, 31, C28), (17, 32, C32), (17, 33, C28), (17, 34, C32), (17, 35, C28), (17, 36, C32), (17, 37, C31),
    # Bracer midtone:
    (18, 27, C19), (18, 28, C31), (18, 29, C31), (18, 30, C32), (18, 31, C31), (18, 32, C32), (18, 33, C31), (18, 34, C32), (18, 35, C31), (18, 36, C32), (18, 37, C30),
    # Bracer shadow:
    (19, 27, C19), (19, 28, C30), (19, 29, C30), (19, 30, C31), (19, 31, C30), (19, 32, C31), (19, 33, C30), (19, 34, C31), (19, 35, C30), (19, 36, C30), (19, 37, C19),
    # Bracer bottom outline:
    (20, 27, C19), (20, 28, C19), (20, 29, C19), (20, 30, C19), (20, 31, C19), (20, 32, C19), (20, 33, C19), (20, 34, C19), (20, 35, C19), (20, 36, C19),

    # Hand gripping bow handle (x=38..42, y=16..20):
    (16, 38, C19), (16, 39, C11), (16, 40, C2),  (16, 41, C19),
    (17, 38, C14), (17, 39, C11), (17, 40, C2),  (17, 41, C1),  (17, 42, C19),
    (18, 38, C14), (18, 39, C11), (18, 40, C2),  (18, 41, C1),  (18, 42, C19),
    (19, 38, C11), (19, 39, C2),  (19, 40, C1),  (19, 41, C19),
    (20, 38, C19), (20, 39, C1),  (20, 40, C19),
]
for y, x, c in bow_arm_pixels:
    f2.set(x, y, c)

# 5. Bow (Graceful, deeply flexed golden recurve):
# Grip at x=40..43, y=16..21
# Upper limb: curves forward to x=43 at y=9..11, flexes back to x=36, y=2
# Lower limb: curves forward to x=42 at y=25..27, flexes back to x=34, y=36
bow_pixels = [
    # Tip (y=1..3)
    (1, 36, C0),  (1, 37, C1),
    (2, 35, C0),  (2, 36, C18), (2, 37, C6),  (2, 38, C0),
    (3, 35, C0),  (3, 36, C26), (3, 37, C18), (3, 38, C6),  (3, 39, C0),
    (4, 36, C0),  (4, 37, C26), (4, 38, C18), (4, 39, C6),  (4, 40, C0),
    (5, 37, C0),  (5, 38, C26), (5, 39, C18), (5, 40, C6),  (5, 41, C0),
    (6, 38, C0),  (6, 39, C26), (6, 40, C18), (6, 41, C6),  (6, 42, C0),
    (7, 39, C0),  (7, 40, C26), (7, 41, C18), (7, 42, C6),  (7, 43, C0),
    (8, 40, C0),  (8, 41, C26), (8, 42, C18), (8, 43, C6),  (8, 44, C0),
    # Magenta wrap on upper limb:
    (9, 40, C0),  (9, 41, C9),  (9, 42, C7),  (9, 43, C10), (9, 44, C0),
    (10, 41, C0), (10, 42, C20),(10, 43, C7), (10, 44, C22),(10, 45, C0),
    (11, 41, C0), (11, 42, C9), (11, 43, C7), (11, 44, C10),(11, 45, C0),
    # Entering handle:
    (12, 41, C0), (12, 42, C26),(12, 43, C18),(12, 44, C6), (12, 45, C0),
    (13, 41, C0), (13, 42, C26),(13, 43, C18),(13, 44, C6), (13, 45, C0),
    (14, 40, C0), (14, 41, C26),(14, 42, C18),(14, 43, C6), (14, 44, C0),
    (15, 40, C0), (15, 41, C26),(15, 42, C18),(15, 43, C6), (15, 44, C0),

    # Grip (white wrapped):
    (16, 40, C19),(16, 41, C33),(16, 42, C28),(16, 43, C3), (16, 44, C19),
    (17, 41, C19),(17, 42, C33),(17, 43, C28),(17, 44, C19),
    (18, 41, C19),(18, 42, C33),(18, 43, C28),(18, 44, C19),
    (19, 41, C19),(19, 42, C33),(19, 43, C28),(19, 44, C19),
    (20, 41, C19),(20, 42, C33),(20, 43, C28),(20, 44, C19),
    (21, 40, C19),(21, 41, C33),(21, 42, C28),(21, 43, C3), (21, 44, C19),

    # Lower limb:
    (22, 40, C0), (22, 41, C26),(22, 42, C18),(22, 43, C6), (22, 44, C0),
    (23, 40, C0), (23, 41, C26),(23, 42, C18),(23, 43, C6), (23, 44, C0),
    (24, 40, C0), (24, 41, C26),(24, 42, C18),(24, 43, C6), (24, 44, C0),
    (25, 40, C0), (25, 41, C26),(25, 42, C18),(25, 43, C6), (25, 44, C0),
    # Magenta wrap on lower limb:
    (26, 39, C0), (26, 40, C9), (26, 41, C7), (26, 42, C10),(26, 43, C0),
    (27, 39, C0), (27, 40, C20),(27, 41, C7), (27, 42, C22),(27, 43, C0),
    (28, 38, C0), (28, 39, C9), (28, 40, C7), (28, 41, C10),(28, 42, C0),
    # Lower limb flex:
    (29, 38, C0), (29, 39, C26),(29, 40, C18),(29, 41, C6), (29, 42, C0),
    (30, 37, C0), (30, 38, C26),(30, 39, C18),(30, 40, C6), (30, 41, C0),
    (31, 37, C0), (31, 38, C26),(31, 39, C18),(31, 40, C6), (31, 41, C0),
    (32, 36, C0), (32, 37, C26),(32, 38, C18),(32, 39, C6), (32, 40, C0),
    (33, 35, C0), (33, 36, C26),(33, 37, C18),(33, 38, C6), (33, 39, C0),
    (34, 35, C0), (34, 36, C26),(34, 37, C18),(34, 38, C6), (34, 39, C0),
    (35, 34, C0), (35, 35, C26),(35, 36, C18),(35, 37, C6), (35, 38, C0),
    # Tip (y=36..37)
    (36, 33, C0), (36, 34, C18),(36, 35, C6),  (36, 36, C0),
    (37, 33, C0), (37, 34, C1),
]
for y, x, c in bow_pixels:
    f2.set(x, y, c)

# 6. Bowstring (Solid, taut line drawn IN FRONT of body directly to draw hand):
# Anchor point: (x=23, y=16)
# Upper tip: (x=36, y=2)
# Lower tip: (x=34, y=36)
def draw_bowstring(canvas, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    step = 0
    while True:
        # Don't overwrite the tips or the draw hand itself
        if (x, y) != (x0, y0) and (x, y) != (x1, y1):
            # Alternating white and cream for shimmering taut string
            color = C3 if (step % 3 == 0) else C12
            canvas.set(x, y, color)
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
        step += 1

draw_bowstring(f2, 36, 2, 23, 16)
draw_bowstring(f2, 34, 36, 23, 16)

# 7. Sighting Eye & Expression:
# Sharp gaze focused forward towards target
f2.set(23, 12, C19)
f2.set(24, 12, C3)
f2.set(24, 13, C19)

comp = new_canvas(W * 2 + 4, H, name="comp")
comp.blit(f1, 0, 0)
comp.blit(f2, W + 4, 0)

view(comp)
