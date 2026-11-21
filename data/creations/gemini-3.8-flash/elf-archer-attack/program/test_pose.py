from pixelbench_api import *

W, H = 48, 48
dx, dy = 5, 0

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, dx, dy)

f2 = new_canvas(W, H, name="f2")

# Palette constants
TRANSPARENT = 0
C0  = 1   # #422110 dark outline
C1  = 2   # #7b4231 brown/skin shadow
C2  = 3   # #c5956a mid skin
C3  = 4   # #ffffff white
C4  = 5   # #949473 dark blonde
C5  = 6   # #f3f4b6 light blonde
C6  = 7   # #ffe75a bright yellow
C7  = 8   # #c30074 magenta
C8  = 9   # #df9859 peach
C9  = 10  # #55002a deep purple
C10 = 11  # #ef5ba1 bright pink
C11 = 12  # #f6d39b light skin/string
C12 = 13  # #e0c89e cream/string
C13 = 14  # #faf3c9 pale blonde
C14 = 15  # #f1d8b3 skin highlight
C15 = 16  # #a9794f leather
C16 = 17  # #8e7058 boot shadow
C17 = 18  # #907859 leather
C18 = 19  # #fcc44c gold
C19 = 20  # #121311 black outline
C20 = 21  # #9e005d dark magenta
C21 = 22  # #529439 green
C22 = 23  # #f6adcd pale pink
C23 = 24  # #304915 deep green
C24 = 25  # #14110e warm black outline
C25 = 26  # #9cde5a light green
C26 = 27  # #bc6c0c dark gold
C27 = 28  # #252a23 dark grey
C28 = 29  # #f1f7f7 light grey/white
C29 = 30  # #4f7229 dark green
C30 = 31  # #3c3c3c dark grey
C31 = 32  # #687862 mid grey
C32 = 33  # #a4b496 light sage
C33 = 34  # #e1d4c2 pale leather
C34 = 35  # #ffffce cream
C35 = 36  # #534338 boot brown
C36 = 37  # #74341c boot red-brown
C37 = 38  # #48382f boot shadow
C38 = 39  # #313b31 dark green-grey
C39 = 40  # #5d422f boot leather
C40 = 41  # #d1b6a2 boot light leather
C41 = 42  # #17003599 translucent purple shadow

# 1. Start f2 with base pixels from f1
for y in range(H):
    for x in range(W):
        f2.set(x, y, f1.get(x, y))

# 2. Erase old bow, string, resting arm, and old left arm
for y in range(1, 40):
    for x in range(27 + dx, W):
        f2.set(x, y, TRANSPARENT)

for y in range(35, 40):
    for x in range(22 + dx, 28 + dx):
        f2.set(x, y, TRANSPARENT)

for y in range(4, 35):
    for x in range(24 + dx, 29 + dx):
        # Don't erase the body/legs if any
        if y < 20 or y > 25:
            if x >= 27:
                f2.set(x, y, TRANSPARENT)

# Erase old resting arm
for y in range(16, 25):
    for x in range(5 + dx, 12 + dx):
        f2.set(x, y, TRANSPARENT)
# Erase old ribbon end at x=11, y=24..25
f2.set(11, 24, TRANSPARENT)
f2.set(11, 25, TRANSPARENT)
f2.set(10, 24, TRANSPARENT)
f2.set(12, 24, TRANSPARENT)

# Erase old left arm
for y in range(20, 26):
    for x in range(18 + dx, 28 + dx):
        f2.set(x, y, TRANSPARENT)

# 3. Fill in torso side where old resting arm was (rows 17-25, cols 11-15)
# Torso flank: green harness, tanned skin, gold belt
torso_flank = [
    # y, x, color
    # y=17: shoulder transition
    (17, 12, C19), (17, 13, C1), (17, 14, C2), (17, 15, C11),
    # y=18: chest halter top
    (18, 12, C19), (18, 13, C23), (18, 14, C29), (18, 15, C21), (18, 16, C25),
    # y=19: chest halter top with gold border
    (19, 12, C19), (19, 13, C23), (19, 14, C21), (19, 15, C25), (19, 16, C25),
    # y=20: midriff (bare tanned skin)
    (20, 12, C19), (20, 13, C1), (20, 14, C2), (20, 15, C11), (20, 16, C14),
    # y=21: midriff
    (21, 12, C19), (21, 13, C1), (21, 14, C2), (21, 15, C14), (21, 16, C14),
    # y=22: lower midriff
    (22, 12, C19), (22, 13, C1), (22, 14, C2), (22, 15, C11), (22, 16, C2),
    # y=23: gold belt top
    (23, 11, C19), (23, 12, C26), (23, 13, C18), (23, 14, C18), (23, 15, C26), (23, 16, C19),
    # y=24: gold belt / green sash knot
    (24, 11, C19), (24, 12, C26), (24, 13, C18), (24, 14, C21), (24, 15, C23), (24, 16, C19),
    # y=25: belt bottom into hakama
    (25, 11, C19), (25, 12, C27), (25, 13, C38), (25, 14, C38), (25, 15, C27), (25, 16, C19),
]
for y, x, c in torso_flank:
    f2.set(x, y, c)

# 4. Draw Right Arm (Raised Draw Arm):
# Shoulder around x=14..16, y=16..18
# Upper arm going up-left to elbow at x=8..10, y=14..16
# Forearm coming forward to hand at x=23, y=19
right_arm = [
    # Right shoulder:
    (15, 14, C19), (15, 15, C1), (15, 16, C2),
    (16, 13, C19), (16, 14, C2), (16, 15, C11), (16, 16, C14),

    # Upper arm extending up-left:
    (16, 10, C19), (16, 11, C1), (16, 12, C2),
    (15, 8, C19), (15, 9, C1), (15, 10, C2), (15, 11, C11), (15, 12, C14), (15, 13, C1),
    # Elbow joint at x=7..9, y=14..15
    (14, 7, C19), (14, 8, C1), (14, 9, C2), (14, 10, C11), (14, 11, C2), (14, 12, C19),
    (13, 8, C19), (13, 9, C19), (13, 10, C19),

    # Magenta arm band wrapped around upper arm:
    (15, 10, C9), (15, 11, C7), (15, 12, C10), (15, 13, C22),
    (16, 11, C9), (16, 12, C7),
    # Ribbon flowing slightly behind elbow:
    (16, 7, C19), (16, 8, C9), (16, 9, C7),
    (17, 6, C19), (17, 7, C7), (17, 8, C10), (17, 9, C19),
    (18, 6, C19), (18, 7, C9), (18, 8, C19),

    # Forearm from elbow (x=9..11, y=14..15) towards hand (x=23, y=19):
    (15, 14, C2), (15, 15, C11), (15, 16, C14),
    (16, 16, C19), (16, 17, C11), (16, 18, C14), (16, 19, C14),
    (17, 17, C19), (17, 18, C2), (17, 19, C11), (17, 20, C14), (17, 21, C14), (17, 22, C19),
    (18, 19, C19), (18, 20, C2), (18, 21, C11), (18, 22, C14), (18, 23, C11), (18, 24, C19),

    # Draw hand anchored at cheek (x=22..24, y=18..20):
    (19, 21, C19), (19, 22, C2), (19, 23, C14), (19, 24, C11), (19, 25, C19),
    # Curled fingers hooked on string:
    (20, 22, C19), (20, 23, C1), (20, 24, C2), (20, 25, C19),
]
for y, x, c in right_arm:
    f2.set(x, y, c)

# 5. Draw Left Arm (Straight extended bow arm):
# Reaches from shoulder (x=24..26, y=19..20) straight forward to x=39..41
left_arm = [
    # Shoulder / chest connection:
    (19, 25, C19), (19, 26, C25), (19, 27, C21), (19, 28, C19),
    (20, 25, C1),  (20, 26, C2),  (20, 27, C11), (20, 28, C14),

    # Forearm with bracer / gauntlet:
    # Top highlight line:
    (19, 29, C19), (19, 30, C19), (19, 31, C19), (19, 32, C19), (19, 33, C19), (19, 34, C19), (19, 35, C19), (19, 36, C19), (19, 37, C19), (19, 38, C19),
    # Row 20 (upper bracer):
    (20, 29, C32), (20, 30, C28), (20, 31, C32), (20, 32, C28), (20, 33, C32), (20, 34, C28), (20, 35, C32), (20, 36, C28), (20, 37, C32), (20, 38, C31),
    # Row 21 (mid bracer):
    (21, 27, C19), (21, 28, C31), (21, 29, C31), (21, 30, C32), (21, 31, C31), (21, 32, C32), (21, 33, C31), (21, 34, C32), (21, 35, C31), (21, 36, C32), (21, 37, C31), (21, 38, C30),
    # Row 22 (lower bracer):
    (22, 26, C19), (22, 27, C30), (22, 28, C30), (22, 29, C31), (22, 30, C30), (22, 31, C31), (22, 32, C30), (22, 33, C31), (22, 34, C30), (22, 35, C31), (22, 36, C30), (22, 37, C30), (22, 38, C19),
    # Bottom outline:
    (23, 27, C19), (23, 28, C19), (23, 29, C19), (23, 30, C19), (23, 31, C19), (23, 32, C19), (23, 33, C19), (23, 34, C19), (23, 35, C19), (23, 36, C19), (23, 37, C19),

    # Left hand gripping bow handle (x=39..42, y=19..23):
    # Thumb over top of handle:
    (19, 39, C19), (19, 40, C11), (19, 41, C2), (19, 42, C19),
    # Fingers wrapped around handle:
    (20, 39, C14), (20, 40, C11), (20, 41, C2), (20, 42, C1), (20, 43, C19),
    (21, 39, C14), (21, 40, C11), (21, 41, C2), (21, 42, C1), (21, 43, C19),
    (22, 39, C11), (22, 40, C2),  (22, 41, C1), (22, 42, C19),
    (23, 39, C19), (23, 40, C1),  (23, 41, C19),
]
for y, x, c in left_arm:
    f2.set(x, y, c)

# 6. Draw Deeply Bent Recurve Bow:
# Handle at x=41..43, y=19..24
# Upper limb curves out to x=44..45 at y=13..15, then flexes back to x=37..38, y=5..6
# Lower limb curves out to x=43..44 at y=28..30, then flexes back to x=35..36, y=37..38
bow_pixels = [
    # --- UPPER LIMB ---
    # Tip (y=4..5)
    (4, 37, C0),  (4, 38, C1),
    (5, 36, C0),  (5, 37, C18), (5, 38, C6),  (5, 39, C0),
    (6, 36, C0),  (6, 37, C26), (6, 38, C18), (6, 39, C6),  (6, 40, C0),
    (7, 37, C0),  (7, 38, C26), (7, 39, C18), (7, 40, C6),  (7, 41, C0),
    (8, 38, C0),  (8, 39, C26), (8, 40, C18), (8, 41, C6),  (8, 42, C0),
    (9, 39, C0),  (9, 40, C26), (9, 41, C18), (9, 42, C6),  (9, 43, C0),
    (10, 40, C0), (10, 41, C26),(10, 42, C18),(10, 43, C6), (10, 44, C0),
    (11, 41, C0), (11, 42, C26),(11, 43, C18),(11, 44, C6), (11, 45, C0),
    # Magenta wrap on upper limb:
    (12, 41, C0), (12, 42, C9), (12, 43, C7), (12, 44, C10),(12, 45, C0),
    (13, 42, C0), (13, 43, C20),(13, 44, C7), (13, 45, C22),(13, 46, C0),
    (14, 42, C0), (14, 43, C9), (14, 44, C7), (14, 45, C10),(14, 46, C0),
    # Upper limb entering handle:
    (15, 42, C0), (15, 43, C26),(15, 44, C18),(15, 45, C6), (15, 46, C0),
    (16, 42, C0), (16, 43, C26),(16, 44, C18),(16, 45, C6), (16, 46, C0),
    (17, 41, C0), (17, 42, C26),(17, 43, C18),(17, 44, C6), (17, 45, C0),
    (18, 41, C0), (18, 42, C26),(18, 43, C18),(18, 44, C6), (18, 45, C0),

    # --- HANDLE (Wrapped in white leather) ---
    (19, 41, C19),(19, 42, C33),(19, 43, C28),(19, 44, C3), (19, 45, C19),
    (20, 42, C19),(20, 43, C33),(20, 44, C28),(20, 45, C19),
    (21, 42, C19),(21, 43, C33),(21, 44, C28),(21, 45, C19),
    (22, 42, C19),(22, 43, C33),(22, 44, C28),(22, 45, C19),
    (23, 42, C19),(23, 43, C33),(23, 44, C28),(23, 45, C19),
    (24, 41, C19),(24, 42, C33),(24, 43, C28),(24, 44, C3), (24, 45, C19),

    # --- LOWER LIMB ---
    (25, 41, C0), (25, 42, C26),(25, 43, C18),(25, 44, C6), (25, 45, C0),
    (26, 41, C0), (26, 42, C26),(26, 43, C18),(26, 44, C6), (26, 45, C0),
    (27, 41, C0), (27, 42, C26),(27, 43, C18),(27, 44, C6), (27, 45, C0),
    (28, 41, C0), (28, 42, C26),(28, 43, C18),(28, 44, C6), (28, 45, C0),
    (29, 40, C0), (29, 41, C26),(29, 42, C18),(29, 43, C6), (29, 44, C0),
    # Magenta wrap on lower limb:
    (30, 40, C0), (30, 41, C9), (30, 42, C7), (30, 43, C10),(30, 44, C0),
    (31, 39, C0), (31, 40, C20),(31, 41, C7), (31, 42, C22),(31, 43, C0),
    (32, 39, C0), (32, 40, C9), (32, 41, C7), (32, 42, C10),(32, 43, C0),
    # Lower limb curving back:
    (33, 38, C0), (33, 39, C26),(33, 40, C18),(33, 41, C6), (33, 42, C0),
    (34, 37, C0), (34, 38, C26),(34, 39, C18),(34, 40, C6), (34, 41, C0),
    (35, 36, C0), (35, 37, C26),(35, 38, C18),(35, 39, C6), (35, 40, C0),
    (36, 35, C0), (36, 36, C26),(36, 37, C18),(36, 38, C6), (36, 39, C0),
    (37, 34, C0), (37, 35, C26),(37, 36, C18),(37, 37, C6), (37, 38, C0),
    # Tip (y=38..39)
    (38, 33, C0), (38, 34, C18),(38, 35, C6),  (38, 36, C0),
    (39, 33, C0), (39, 34, C1),
]
for y, x, c in bow_pixels:
    f2.set(x, y, c)

# 7. Draw Bowstring:
# Top string from (37, 5) to (23, 19)
# Bottom string from (34, 38) to (23, 19)
# NO ARROW!
def draw_string_line(canvas, x0, y0, x1, y1, color):
    # Bresenham's line algorithm
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        # Don't overwrite the archer's hand or bow limb tips
        current = canvas.get(x, y)
        if current == TRANSPARENT or current in [C11, C12, C3]:
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

# Draw top string
draw_string_line(f2, 36, 5, 23, 19, C12)
# Draw bottom string
draw_string_line(f2, 34, 38, 23, 19, C12)

# Make string highlights with C3 (white) alternating
# Top string highlight
for p in [(33, 8), (30, 11), (27, 14), (24, 18)]:
    if f2.get(p[0], p[1]) == C12:
        f2.set(p[0], p[1], C3)
# Bottom string highlight
for p in [(32, 35), (29, 30), (26, 25), (24, 21)]:
    if f2.get(p[0], p[1]) == C12:
        f2.set(p[0], p[1], C3)

# Sighting eye focused right (x=24, y=12..13):
f2.set(23, 12, C19)
f2.set(24, 12, C3)
f2.set(24, 13, C19)

comp = new_canvas(W * 2 + 4, H, name="comp")
comp.blit(f1, 0, 0)
comp.blit(f2, W + 4, 0)

view(comp)
