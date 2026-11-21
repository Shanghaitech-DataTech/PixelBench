from pixelbench_api import *

# Create the canvas
c = new_canvas(256, 256, background=None, name="ancient_treant")

# Define color palette
# Background/sky - deep forest with god rays
SKY_TOP = (20, 30, 45)
SKY_MID = (35, 50, 55)
SKY_BOT = (50, 68, 45)
RAY = (255, 240, 190, 110)
RAY_BRIGHT = (255, 250, 210, 160)
GROUND_D1 = (10, 22, 15)
GROUND_D2 = (15, 30, 20)
GROUND_M = (22, 40, 28)
GROUND_L = (30, 52, 36)

# Tree trunk - gnarled bark
BARK_D0 = (10, 12, 10)
BARK_D = (16, 18, 14)
BARK_M = (28, 30, 22)
BARK_L = (45, 48, 35)
BARK_HL = (70, 74, 55)
BARK_BR = (24, 26, 20)

# Green glow
GREEN_GLOW = (60, 255, 100, 160)
GREEN_BRIGHT = (120, 255, 140, 220)
GREEN_CORE = (160, 255, 170, 255)
GREEN_DARK = (30, 120, 50, 180)

# Moss
MOSS_D = (35, 90, 40)
MOSS_M = (55, 130, 60)
MOSS_L = (80, 170, 90)

# Vines
VINE_D = (60, 85, 40)
VINE_M = (85, 120, 60)

# Roots
ROOT_D = (12, 16, 12)
ROOT_M = (20, 26, 18)

# Sky gradient (drawn as horizontal bands)
for y in range(256):
    t = y / 255
    if t < 0.35:
        # top - dark
        col = SKY_TOP
    elif t < 0.65:
        # transition
        f = (t - 0.35) / 0.30
        col = tuple(int(SKY_TOP[i] + (SKY_MID[i] - SKY_TOP[i]) * f) for i in range(3))
    else:
        f = (t - 0.65) / 0.35
        col = tuple(int(SKY_MID[i] + (SKY_BOT[i] - SKY_MID[i]) * f) for i in range(3))
    c.rect(0, y, 256, 1, col)

# Draw ground - lower area
from pixelbench_api import *
# ground from y=180 down
for y in range(185, 256):
    c.rect(0, y, 256, 1, GROUND_D2)

# Ground texture variations
import random
random.seed(42)
for y in range(190, 256):
    for x in range(0, 256, 2):
        r = random.random()
        if r < 0.3:
            c.set(x, y, GROUND_D1)
        elif r < 0.45:
            c.set(x + 1, y, GROUND_M if random.random() < 0.5 else GROUND_L)

# Ground clearing in the middle - lighter
c.rect(60, 200, 136, 56, GROUND_M)
c.rect(70, 205, 116, 51, GROUND_L)
# grass specks
random.seed(100)
for _ in range(200):
    x = random.randint(60, 195)
    y = random.randint(200, 254)
    r = random.random()
    if r < 0.3:
        c.set(x, y, MOSS_D if random.random() < 0.5 else (40, 70, 40))
    elif r < 0.5:
        c.set(x, y, (50, 90, 50))

# God rays - diagonal light beams from top
# Several light rays from top-left area
rays = [
    (50, 0, 15, 200, 60, 8),    # (start_x, start_y, ... define as triangles)
]
# Draw god rays as elongated triangles/polygons from top
def draw_ray(x_top, y_top, x_bottom_center, bottom_width, y_bottom, alpha_col, alpha_bright):
    # Draw a beam going from top spreading downward
    # Actually draw as a polygon: trapezoid from top narrow to bottom wide
    top_w = 6
    pts = [
        (x_top - top_w, y_top),
        (x_top + top_w, y_top),
        (x_bottom_center + bottom_width, y_bottom),
        (x_bottom_center - bottom_width, y_bottom),
    ]
    c.poly(pts, alpha_col)
    # brighter core
    pts2 = [
        (x_top - top_w//2, y_top),
        (x_top + top_w//2, y_top),
        (x_bottom_center + bottom_width//2, y_bottom),
        (x_bottom_center - bottom_width//2, y_bottom),
    ]
    c.poly(pts2, alpha_bright)

draw_ray(60, 0, 110, 28, 210, RAY, RAY_BRIGHT)
draw_ray(95, 0, 140, 35, 220, RAY, RAY_BRIGHT)
draw_ray(130, 0, 175, 30, 205, RAY, RAY_BRIGHT)
draw_ray(160, 0, 195, 22, 190, RAY, RAY_BRIGHT)

# ============================================================
# The TREANT - massive towering creature in the center
# ============================================================

# Roots rising from the ground - various root shapes at the base
# Left roots
def draw_root_shape(cx, cy, spread, thickness, col):
    # Draw a curving root using path
    d = f"M {cx-thickness//2} {cy} Q {cx-thickness} {cy-spread//2} {cx-spread} {cy-spread}"
    c.path(d, col)

# Big gnarled base roots
c.poly([(128-42, 250), (128-18, 200), (128-8, 195), (128-2, 210), (128+6, 230), (128+20, 245), (128+30, 250)], ROOT_D)
c.poly([(128-50, 248), (128-25, 215), (128-10, 210), (128-5, 220), (128+8, 235), (128+25, 248)], ROOT_M)
c.poly([(128+42, 250), (128+22, 205), (128+10, 200), (128+4, 215), (128-4, 235), (128-18, 248)], ROOT_D)
c.poly([(128+50, 248), (128+28, 218), (128+15, 212), (128+8, 225), (128-5, 240), (128-20, 248)], ROOT_M)

# Main trunk - massive vertical column
# Trunk from y=60 to y=210, centered around x=128
# Main body with varying width, gnarled texture
def draw_trunk():
    # Outline first (dark)
    # Define trunk silhouette
    # Trunk shape: bulging middle, wider at bottom
    profile_top = [
        (96, 60, 14),   # (y, half_width at that y)
        (84, 90, 20),
        (78, 120, 26),
        (74, 150, 34),
        (72, 180, 42),
        (74, 200, 50),
        (80, 215, 55),
    ]
    # Draw trunk as filled polygon using many points
    pts = []
    for y, _, hw in profile_top:
        pts.append((128 - hw, y))
    # right side going up
    for y, _, hw in reversed(profile_top):
        pts.append((128 + hw, y))
    # close
    c.poly(pts, BARK_D)  # dark fill for outline base
    
    # Inner lighter bark
    pts2 = []
    for y, _, hw in profile_top:
        pts2.append((128 - hw + 3, y + 3))
    for y, _, hw in reversed(profile_top):
        pts2.append((128 + hw - 3, y + 3))
    c.poly(pts2, BARK_M)
    
    # Midtone highlight side (right side lighter)
    pts3 = []
    for y, _, hw in profile_top:
        pts3.append((128 + hw - 3, y + 3))
    for y, _, hw in reversed(profile_top):
        pts3.append((128 + hw - 14, y + 4))
    c.poly(pts3, BARK_L)
    
    # Dark side (left)
    pts4 = []
    for y, _, hw in profile_top:
        pts4.append((128 - hw + 3, y + 3))
    for y, _, hw in reversed(profile_top):
        pts4.append((128 - hw + 16, y + 4))
    c.poly(pts4, BARK_D0)

draw_trunk()

# ============================================================
# HEAD - massive branching top of the treant
# ============================================================
# Head/upper structure from y~30 to y~90
# Wide branching top
head_pts = [
    (128-30, 55),
    (128-45, 45),
    (128-55, 35),
    (128-50, 30),
    (128-38, 38),
    (128-25, 30),
    (128-15, 40),
    (128-5, 28),
    (128+5, 35),
    (128+15, 26),
    (128+25, 38),
    (128+38, 30),
    (128+50, 35),
    (128+45, 42),
    (128+30, 55),
]
c.poly(head_pts, BARK_D)
# inner head
head_pts2 = [(x, y+2) for x, y in head_pts]
c.poly(head_pts2, BARK_M)
# highlight spots
for (x, y) in [(128-20, 42), (128+8, 40), (128+20, 45), (128-30, 48)]:
    c.circle(x, y, 4, BARK_L)

# Branch arms extending sideways
# LEFT ARM - massive branch arm
left_arm_pts = [
    (128-35, 95),
    (128-55, 85),
    (128-80, 70),
    (128-100, 60),
    (128-115, 50),
    (128-105, 42),
    (128-90, 52),
    (128-70, 62),
    (128-50, 70),
    (128-30, 80),
]
c.poly(left_arm_pts, BARK_D)
c.poly([(x+3, y+2) for x, y in left_arm_pts], BARK_M)
# claws at the end of left arm
claw_color = BARK_L
# left arm claw-like twigs pointing down
for (cx, cy), angle in [((128-105, 50), 0), ((128-112, 55), 15), ((128-108, 44), -10), ((128-95, 55), 25), ((128-100, 65), 35)]:
    # Draw short claw lines
    c.line(cx, cy, cx-6, cy+10, claw_color)
    c.line(cx-2, cy, cx-8, cy+12, BARK_M)
    c.line(cx-3, cy-1, cx-10, cy+6, claw_color)

# RIGHT ARM - massive branch arm
right_arm_pts = [
    (128+35, 95),
    (128+55, 85),
    (128+80, 70),
    (128+100, 60),
    (128+115, 50),
    (128+105, 42),
    (128+90, 52),
    (128+70, 62),
    (128+50, 70),
    (128+30, 80),
]
c.poly(right_arm_pts, BARK_D)
c.poly([(x-3, y+2) for x, y in right_arm_pts], BARK_M)
# claws at the right arm
for (cx, cy), angle in [((128+105, 50), 0), ((128+112, 55), -15), ((128+108, 44), 10), ((128+95, 55), -25), ((128+100, 65), -35)]:
    c.line(cx, cy, cx+6, cy+10, claw_color)
    c.line(cx+2, cy, cx+8, cy+12, BARK_M)
    c.line(cx+3, cy-1, cx+10, cy+6, claw_color)

# ============================================================
# GIANT CLAWED HANDS - large branch claw shapes at arm ends
# ============================================================
# Left hand - big claw at end of left arm
# Left arm extends up-left, so hand claws reach up
left_hand_base = (128-100, 50)
c.poly([(left_hand_base[0]-12, left_hand_base[1]+15), (left_hand_base[0]-5, left_hand_base[1]), (left_hand_base[0]+5, left_hand_base[1]), (left_hand_base[0]+8, left_hand_base[1]+15)], BARK_D)
# three big claws pointing up-left
c.line(left_hand_base[0]-8, left_hand_base[1]-2, left_hand_base[0]-25, left_hand_base[1]-20, BARK_M)
c.line(left_hand_base[0]-3, left_hand_base[1]-2, left_hand_base[0]-18, left_hand_base[1]-25, BARK_M)
c.line(left_hand_base[0]+3, left_hand_base[1]-2, left_hand_base[0]-10, left_hand_base[1]-28, BARK_M)
# thicken the claws
for i in range(3):
    c.line(left_hand_base[0]-8+i*5, left_hand_base[1]-2, left_hand_base[0]-22+i*4, left_hand_base[1]-20-i*4, BARK_M)
# brighter claw tips
c.line(left_hand_base[0]-22, left_hand_base[1]-20, left_hand_base[0]-25, left_hand_base[1]-20, BARK_HL)
c.line(left_hand_base[0]-18, left_hand_base[1]-25, left_hand_base[0]-18, left_hand_base[1]-28, BARK_HL)

# Right hand
right_hand_base = (128+100, 50)
c.poly([(right_hand_base[0]-8, right_hand_base[1]+15), (right_hand_base[0]-5, right_hand_base[1]), (right_hand_base[0]+5, right_hand_base[1]), (right_hand_base[0]+12, right_hand_base[1]+15)], BARK_D)
c.line(right_hand_base[0]+8, right_hand_base[1]-2, right_hand_base[0]+25, right_hand_base[1]-20, BARK_M)
c.line(right_hand_base[0]+3, right_hand_base[1]-2, right_hand_base[0]+18, right_hand_base[1]-25, BARK_M)
c.line(right_hand_base[0]-3, right_hand_base[1]-2, right_hand_base[0]+10, right_hand_base[1]-28, BARK_M)
for i in range(3):
    c.line(right_hand_base[0]+8-i*5, right_hand_base[1]-2, right_hand_base[0]+22-i*4, right_hand_base[1]-20-i*4, BARK_M)
c.line(right_hand_base[0]+22, right_hand_base[1]-20, right_hand_base[0]+25, right_hand_base[1]-20, BARK_HL)
c.line(right_hand_base[0]+18, right_hand_base[1]-25, right_hand_base[0]+18, right_hand_base[1]-28, BARK_HL)

# ============================================================
# GLOWING GREEN EYES in the trunk
# ============================================================
# Eyes at around y=110-125 in the trunk
eye_y = 112
eye_spacing = 14
# Left eye
c.circle(128-14, eye_y, 7, GREEN_GLOW)
c.circle(128-14, eye_y, 4, GREEN_BRIGHT)
c.circle(128-14, eye_y, 2, GREEN_CORE)
# Right eye
c.circle(128+14, eye_y, 7, GREEN_GLOW)
c.circle(128+14, eye_y, 4, GREEN_BRIGHT)
c.circle(128+14, eye_y, 2, GREEN_CORE)

# Glow spreading around eyes on the bark
c.circle(128-14, eye_y, 10, (40, 180, 70, 60))
c.circle(128+14, eye_y, 10, (40, 180, 70, 60))

# Wrinkle lines around eyes (bark texture)
for i in range(-2, 3):
    if i != 0:
        c.line(128-20-i, eye_y-8, 128-8 - i*2, eye_y-12, BARK_D0)
        c.line(128+8+i*2, eye_y-12, 128+20+i, eye_y-8, BARK_D0)

# ============================================================
# MOSS on trunk
# ============================================================
def add_moss_patch(cx, cy, size, density):
    for dx in range(-size, size+1):
        for dy in range(-size, size+1):
            if abs(dx) + abs(dy) <= size and random.random() < density:
                col = random.randint(0, 2)
                cc = [MOSS_D, MOSS_M, MOSS_L][col]
                c.set(cx+dx, cy+dy, cc)

random.seed(200)
add_moss_patch(128-15, 155, 8, 0.6)
add_moss_patch(128+20, 175, 6, 0.55)
add_moss_patch(128-25, 190, 5, 0.5)
add_moss_patch(128-5, 140, 4, 0.5)
add_moss_patch(85, 60, 5, 0.4)
add_moss_patch(160, 75, 4, 0.45)
add_moss_patch(112, 85, 6, 0.5)

# ============================================================
# HANGING VINES from branches
# ============================================================
def draw_vine(x, top_y, length, sway=0):
    # draw a curving hanging vine
    d = f"M {x} {top_y} Q {x + sway} {top_y + length//2} {x + sway} {top_y + length}"
    c.path(d, VINE_M, fill=False)
    # leaf at end
    lx = x + sway
    ly = top_y + length
    c.line(lx, ly, lx-3, ly+4, VINE_M)
    c.line(lx, ly, lx+3, ly+4, VINE_M)
    # small leaf
    c.line(lx, ly+1, lx-2, ly+4, VINE_D)

random.seed(55)
vine_positions = [
    (108, 55, 45, 8),
    (95, 62, 55, -5),
    (120, 50, 35, -3),
    (140, 58, 48, 5),
    (150, 65, 40, -8),
    (160, 52, 35, 3),
    (100, 75, 30, 6),
    (155, 80, 25, -4),
    (130, 95, 30, 2),
    (75, 50, 40, 5),
    (88, 75, 35, -6),
]
for (vx, vy, vl, vs) in vine_positions:
    draw_vine(vx, vy, vl, vs)

# ============================================================
# Gnarled bark texture - cracks and ridges
# ============================================================
random.seed(300)
for _ in range(40):
    x = random.randint(128-38, 128+38)
    y = random.randint(70, 210)
    length = random.randint(8, 25)
    # draw a crack line
    pts = [(x, y)]
    for i in range(1, length):
        pts.append((x + random.randint(-3, 3), y + i))
    c.path(f"M {pts[0][0]} {pts[0][1]}", BARK_D0, fill=False)
    for i in range(1, len(pts)):
        c.line(pts[i-1][0], pts[i-1][1], pts[i][0], pts[i][1], BARK_D0)

# vertical bark ridges (lighter lines)
for _ in range(25):
    x = random.randint(128-35, 128+35)
    y = random.randint(75, 200)
    length = random.randint(6, 18)
    c.line(x, y, x + random.randint(-2, 2), y + length, BARK_L)

# ============================================================
# Roots rising from the ground (extending from trunk base outward)
# ============================================================
# Large root tentacle on left
root_pts = [
    (128-20, 210),
    (128-35, 205),
    (128-60, 215),
    (128-85, 230),
    (128-100, 245),
    (128-110, 250),
    (128-95, 242),
    (128-70, 228),
    (128-45, 220),
    (128-30, 218),
]
c.poly(root_pts, ROOT_M)
# highlight on root
c.line(128-40, 215, 128-80, 228, ROOT_M)
c.line(128-35, 210, 128-60, 218, (35, 45, 30))

# Root tentacle on right
root_pts2 = [
    (128+20, 210),
    (128+35, 205),
    (128+60, 215),
    (128+85, 230),
    (128+100, 245),
    (128+110, 250),
    (128+95, 242),
    (128+70, 228),
    (128+45, 220),
    (128+30, 218),
]
c.poly(root_pts2, ROOT_M)
c.line(128+40, 215, 128+80, 228, ROOT_M)
c.line(128+35, 210, 128+60, 218, (35, 45, 30))

# Small extra roots
c.line(128-30, 215, 128-50, 250, ROOT_D)
c.line(128+30, 215, 128+50, 250, ROOT_D)
c.line(128-55, 220, 128-70, 248, ROOT_D)
c.line(128+55, 220, 128+70, 248, ROOT_D)

# ============================================================
# Moss on the head / top of treant
# ============================================================
random.seed(77)
add_moss_patch(128-10, 35, 10, 0.35)
add_moss_patch(128+15, 40, 7, 0.3)
add_moss_patch(128-35, 48, 5, 0.35)

# ============================================================
# Additional foliage tufts at the top (branches/leaves)
# ============================================================
def foliage_cluster(cx, cy, r, col):
    pts = []
    n = 10
    random.seed(hash((cx, cy)) % 10000)
    for i in range(n):
        ang = (i / n) * 3.14159 * 2
        rr = r * (0.6 + random.random() * 0.4)
        pts.append((int(cx + rr * 0.5), int(cy + rr * 0.7)))
    # draw as several overlapping circles instead
    random.seed(hash((cx, cy)) % 10000)
    for i in range(8):
        ang = (i / 8) * 3.14159 * 2
        rr = r * random.random() * 0.8
        px = int(cx + rr * 0.5)
        py = int(cy + rr * 0.7)
        c.circle(px, py, int(r * 0.6), col)

foliage_cluster(105, 28, 10, MOSS_D)
foliage_cluster(125, 22, 12, MOSS_D)
foliage_cluster(142, 26, 9, MOSS_D)
foliage_cluster(80, 40, 8, MOSS_D)
foliage_cluster(165, 35, 8, MOSS_D)

# ============================================================
# Dark outline around the whole treant silhouette
# ============================================================
# The trunk outline was drawn as BARK_D (dark). Let's strengthen with darker
# outline specifically on the edges by re-drawing trunk outer edge

# Strong dark outline around the treant body
def outline_region(pts_list, width=2):
    c.poly(pts_list, (5, 6, 5))

# Redo trunk with strong dark outline
# Trunk outline (outer)
profile_outer = [
    (96, 62, 16),
    (84, 92, 22),
    (78, 122, 28),
    (74, 152, 36),
    (72, 182, 44),
    (74, 202, 52),
    (80, 218, 57),
]
pts_o = []
for y, _, hw in profile_outer:
    pts_o.append((128 - hw, y))
for y, _, hw in reversed(profile_outer):
    pts_o.append((128 + hw, y))
c.poly(pts_o, BARK_D0)

# Redo the highlight bark on top
pts_h = []
for y, _, hw in profile_outer:
    pts_h.append((128 - hw + 3, y + 3))
for y, _, hw in reversed(profile_outer):
    pts_h.append((128 + hw - 3, y + 3))
c.poly(pts_h, BARK_M)

# Light side
pts_h2 = []
for y, _, hw in profile_outer:
    pts_h2.append((128 + hw - 3, y + 3))
for y, _, hw in reversed(profile_outer):
    pts_h2.append((128 + hw - 15, y + 4))
c.poly(pts_h2, BARK_L)

# Dark side
pts_h3 = []
for y, _, hw in profile_outer:
    pts_h3.append((128 - hw + 3, y + 3))
for y, _, hw in reversed(profile_outer):
    pts_h3.append((128 - hw + 17, y + 4))
c.poly(pts_h3, BARK_D0)

# Redo eyes (they were before but trunk redraw might not have covered them since
# the trunk inner area is around x=128-18 to 128+18 at y=112, so eyes at 128±14 are safe)

# ============================================================
# Mouth - glowing crack in trunk between/under eyes
# ============================================================
# A menacing mouth - jagged glowing crack
for i, (dx, dy) in enumerate([
    (-16, 138), (-10, 143), (-4, 140), (0, 146), (5, 141), (11, 144), (16, 138)
]):
    c.circle(128+dx, dy, 3, GREEN_DARK)
    c.circle(128+dx, dy, 1, GREEN_BRIGHT)

# ============================================================
# Atmospheric details
# ============================================================
# Fireflies / floating particles
random.seed(900)
for _ in range(25):
    x = random.randint(20, 235)
    y = random.randint(30, 200)
    c.set(x, y, (200, 255, 150, 100))

# Additional trees in the background (silhouettes)
# Background trees on left
bg_tree_col = (15, 22, 18)
c.poly([(20, 90), (26, 90), (30, 185), (28, 185), (35, 215), (5, 215), (12, 185), (10, 185)], bg_tree_col)
c.poly([(35, 70), (40, 70), (45, 160), (38, 160), (50, 210), (12, 210), (25, 160), (20, 160), (35, 160)], bg_tree_col)
c.poly([(220, 50), (230, 50), (235, 180), (228, 180), (245, 215), (205, 215), (220, 180), (213, 180)], bg_tree_col)
c.poly([(238, 80), (244, 80), (248, 190), (240, 190), (250, 215), (225, 215), (236, 190), (232, 190)], bg_tree_col)

# Foreground ground details - grass tufts
for _ in range(30):
    x = random.randint(10, 245)
    y = random.randint(210, 250)
    h = random.randint(4, 10)
    c.line(x, y, x, y-h, (18, 32, 20))
    c.line(x+1, y, x+2, y-h+2, (25, 42, 28))

# ============================================================
# Enhance lighting on the treant (god ray highlights on trunk)
# ============================================================
# Light hitting the treant from above
# Bright highlights on the top of head area
c.circle(120, 42, 8, (80, 90, 65, 90))
c.circle(128, 38, 6, (90, 100, 75, 70))

# Roots rising near the base more dramatic
# Extra root spikes
for (rx, ry, rlx, rly, rlx2, rly2) in [
    (128-30, 200, 128-70, 180, 128-75, 190),
    (128+30, 200, 128+70, 180, 128+75, 190),
    (128-5, 205, 128-5, 175, 128-10, 180),
]:
    c.line(rx, ry, rlx, rly, ROOT_D)
    c.line(rx, ry, rlx2, rly2, ROOT_M)

# ============================================================
# Final check and save
# ============================================================

# Re-draw vines on top after all trunk work
for (vx, vy, vl, vs) in vine_positions:
    draw_vine(vx, vy, vl, vs)

# Final eyes re-drawn on top
c.circle(128-14, 112, 7, GREEN_GLOW)
c.circle(128-14, 112, 4, GREEN_BRIGHT)
c.circle(128-14, 112, 2, GREEN_CORE)
c.circle(128+14, 112, 7, GREEN_GLOW)
c.circle(128+14, 112, 4, GREEN_BRIGHT)
c.circle(128+14, 112, 2, GREEN_CORE)

# Let me verify composition with a view
# ============================================================
# FINAL ENHANCEMENTS - make the treant more menacing and detailed
# ============================================================

# More dramatic gnarled knots on the trunk
for (kx, ky, kr) in [(128-20, 145, 3), (128+15, 130, 4), (128-10, 170, 5), (128+8, 195, 3), (128-25, 160, 2), (128+20, 160, 3)]:
    c.circle(kx, ky, kr, BARK_D0)
    c.circle(kx, ky, max(1, kr-1), BARK_HL)

# Thick vine strands wrapped around the trunk
for vx in [105, 115, 135, 145]:
    c.line(vx, 95, vx+10, 180, VINE_D)
    c.line(vx+1, 95, vx+8, 178, VINE_M)

# Additional small branches poking from the trunk sides
for (bx, by, bx2, by2) in [(128-25, 150, 128-45, 155), (128-30, 175, 128-55, 180), (128+25, 140, 128+45, 145), (128+28, 165, 128+50, 170)]:
    c.line(bx, by, bx2, by2, BARK_L)
    c.line(bx-1, by, bx2-1, by2, BARK_D0)

# More visible roots spreading wide
# Extra left roots reaching far
c.poly([(128-15, 210), (128-60, 220), (128-90, 240), (128-105, 250), (128-95, 245), (128-70, 230), (128-40, 218)], ROOT_D)
c.poly([(128+15, 210), (128+60, 220), (128+90, 240), (128+105, 250), (128+95, 245), (128+70, 230), (128+40, 218)], ROOT_D)

# Sun/moon glow in the sky background
c.circle(200, 35, 15, (255, 255, 220, 60))
c.circle(200, 35, 8, (255, 255, 230, 90))

# Deeper ground shadows under the treant
c.ellipse(128, 235, 50, 15, (5, 10, 7, 180))

# Less flat sky - add some cloud wisps
c.path("M 30 60 Q 80 50 140 55 Q 190 45 230 60", (30, 45, 60, 50), fill=False)
c.path("M 20 80 Q 60 72 100 78 Q 140 70 180 80", (25, 38, 50, 40))

# Ground glow from the treant (green aura at the base)
c.circle(128, 220, 30, (30, 100, 40, 40))

# ============================================================
# REDRAW EYES - bigger and more menacing
# ============================================================
# Left eye - more menacing shape
eye_y = 112
# Widen the eye sockets with dark outline
c.ellipse(128-14, 112, 9, 10, (5, 8, 5))
c.ellipse(128+14, 112, 9, 10, (5, 8, 5))
# Inner glow
c.ellipse(128-14, 112, 7, 8, GREEN_DARK)
c.ellipse(128+14, 112, 7, 8, GREEN_DARK)
# Bright centers
c.ellipse(128-14, 112, 4, 5, GREEN_BRIGHT)
c.ellipse(128+14, 112, 4, 5, GREEN_BRIGHT)
# Core glow (pinpoint)
c.circle(128-14, 112, 1, GREEN_CORE)
c.circle(128+14, 112, 1, GREEN_CORE)

# Eye glow bleed
for g in range(3, 14, 2):
    a = int(60 - g * 3)
    if a > 0:
        c.circle(128-14, 112, g, (50, 200, 90, a))
        c.circle(128+14, 112, g, (50, 200, 90, a))

# ============================================================
# Foreground detail - dead leaves/debris
# ============================================================
random.seed(42)
for _ in range(40):
    x = random.randint(20, 235)
    y = random.randint(220, 250)
    c.set(x, y, (60, 50, 30))
    c.set(x+1, y, (80, 65, 40))

# Moss dripping down larger areas
for mx, my in [(115, 160), (140, 145), (100, 185)]:
    for i in range(6):
        for j in range(3):
            if random.random() < 0.5:
                c.set(mx+i, my+j*3, MOSS_D if j > 0 else MOSS_M)

# ============================================================
# Final refinements to make the piece more dramatic
# ============================================================

# Bigger, more menacing overall presence
# Dark vignette at edges of the image
for v in range(20):
    alpha = int(v * 8)
    if alpha > 0:
        col = (0, 0, 5, min(120, alpha))
        c.rect(v, v, 256-v*2, 1, col)
        c.rect(v, 255-v, 256-v*2, 1, col)
        c.rect(v, v, 1, 256-v*2, col)
        c.rect(255-v, v, 1, 256-v*2, col)

# More dramatic eye beams/shooting glow
for i in range(-3, 4):
    c.line(128-14, 112, 128-14-i*6, 112-i*8, (30, 120, 50, 40))
    c.line(128+14, 112, 128+14+i*6, 112-i*8, (30, 120, 50, 40))

# Larger branch crown at top for a more massive silhouette
c.poly([(128-60, 30), (128-70, 20), (128-55, 15), (128-48, 25), (128-35, 12), (128-28, 22)], BARK_D0)
c.poly([(128+60, 30), (128+70, 20), (128+55, 15), (128+48, 25), (128+35, 12), (128+28, 22)], BARK_D0)
# foliage at the top crown
for fx in [60, 72, 35]:
    foliage_cluster(128-fx, 15, 7, MOSS_D)
    foliage_cluster(128+fx, 15, 7, MOSS_D)

# Strong dark outline around the treant's main body - draw the entire spanning silhouette
# This ensures the massive towering creature reads clearly
dark_outline = (4, 5, 4)
# Outline the full body as a composite silhouette
body_outline_pts = []
# Left side from top head down
for y, _, hw in profile_outer:
    body_outline_pts.append((128 - hw - 2, y - 1))
# Right side from bottom up
for y, _, hw in reversed(profile_outer):
    body_outline_pts.append((128 + hw + 2, y - 1))
# Add outline for the head on top
# Close at top
body_outline_pts.insert(0, (128 + 52, 58))
body_outline_pts.insert(0, (128 + 48, 32))
body_outline_pts.insert(0, (128 - 48, 32))
c.poly(body_outline_pts, dark_outline)

# Re-draw the inner trunk content on top of outline
for y, _, hw in profile_outer:
    c.line(128 - hw + 2, y, 128 + hw - 2, y, BARK_M)
# Re-draw eyes on TOP of everything
c.ellipse(128-14, 112, 9, 10, (5, 8, 5))
c.ellipse(128+14, 112, 9, 10, (5, 8, 5))
c.ellipse(128-14, 112, 7, 8, GREEN_DARK)
c.ellipse(128+14, 112, 7, 8, GREEN_DARK)
c.ellipse(128-14, 112, 4, 5, GREEN_BRIGHT)
c.ellipse(128+14, 112, 4, 5, GREEN_BRIGHT)
c.circle(128-14, 112, 1, GREEN_CORE)
c.circle(128+14, 112, 1, GREEN_CORE)

# ============================================================
# Final quality: re-draw the ground in front of the creature
# ============================================================

# Foreground grass/undergrowth in front of treant base
random.seed(500)
for _ in range(60):
    x = random.randint(70, 186)
    y = random.randint(220, 250)
    h = random.randint(3, 8)
    ang = random.randint(-3, 3)
    col = (20, 38, 25) if random.random() < 0.5 else (28, 48, 32)
    c.line(x, y, x+ang, y-h, col)

save("ancient_treant_boss", c)

finish(c)
