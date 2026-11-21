import sys
from pixelbench_api import new_canvas, finish, view, save

c = new_canvas(48, 48)

WOOD_TOP = c.color("#d2a679")
WOOD_FRONT = c.color("#a67c52")
WOOD_RIGHT = c.color("#734d26")

BED_TOP = c.color("#333333")
BED_FRONT = c.color("#1a1a1a")
BED_RIGHT = c.color("#0d0d0d")

BODY_TOP = c.color("#2a2a2a")
BODY_FRONT = c.color("#111111")
BODY_RIGHT = c.color("#000000")

GOLD = c.color("#d4af37")

RED_TOP = c.color("#ff4d4d")
RED_FRONT = c.color("#cc0000")
RED_RIGHT = c.color("#800000")

SILVER = c.color("#e6e6e6")
SILVER_DARK = c.color("#999999")

def box(x, y, w, h, d, c_front, c_top, c_right):
    # front
    c.rect(x, y, w, h, c_front)
    # top
    c.poly([(x, y), (x+d, y-d), (x+w+d, y-d), (x+w, y)], c_top)
    # right
    c.poly([(x+w, y), (x+w+d, y-d), (x+w+d, y+h-d), (x+w, y+h)], c_right)

# 1. Wood Base
box(6, 38, 30, 4, 6, WOOD_FRONT, WOOD_TOP, WOOD_RIGHT)
# Wood texture lines
c.line(6, 39, 35, 39, c.color("#8a5a33"))
c.line(6, 40, 35, 40, c.color("#6b4222"))

# 2. Metal Bed
box(8, 36, 26, 2, 6, BED_FRONT, BED_TOP, BED_RIGHT)
# Bed gold decal
c.poly([(9, 35), (13, 31), (39, 31), (35, 35)], GOLD, fill=False)

# 3. Fabric
c.poly([(4, 35), (10, 29), (22, 29), (16, 35)], RED_TOP)
c.poly([(4, 35), (16, 35), (16, 44), (4, 44)], RED_FRONT)
c.poly([(16, 35), (22, 29), (22, 38), (16, 44)], RED_RIGHT)
# Fabric folds and highlight
c.line(8, 35, 8, 44, RED_RIGHT)
c.line(7, 35, 7, 44, RED_TOP)
c.line(12, 35, 12, 44, RED_RIGHT)
c.line(11, 35, 11, 44, RED_TOP)
c.line(4, 35, 15, 35, c.color("#ff9999"))

# 4. Needle and Presser Foot
c.line(14, 15, 14, 34, SILVER) # Needle
c.rect(14, 32, 3, 1, SILVER) # Presser foot
c.line(16, 15, 16, 32, SILVER_DARK) # Presser bar

# 5. Machine Head
box(8, 12, 8, 12, 6, BODY_FRONT, BODY_TOP, BODY_RIGHT)

# 6. Machine Arm
box(16, 14, 12, 6, 6, BODY_FRONT, BODY_TOP, BODY_RIGHT)

# 7. Machine Pillar
box(28, 14, 6, 22, 6, BODY_FRONT, BODY_TOP, BODY_RIGHT)

# 8. Gold Decals on Body
# Head decal
c.rect(10, 14, 4, 8, GOLD, fill=False)
# Arm decal
c.line(18, 17, 25, 17, GOLD)
# Pillar decal
c.rect(30, 16, 2, 16, GOLD, fill=False)

# 9. Details
# Tension disc
c.circle(11, 19, 1, SILVER_DARK)
c.set(11, 19, SILVER)

# Bobbin winder
c.circle(30, 26, 1, SILVER_DARK)

# Stitch length lever
c.rect(30, 31, 2, 3, SILVER_DARK)
c.set(31, 31, SILVER)

# Handwheel
HW_BASE = c.color("#1a1a1a")
HW_RIM = c.color("#b3b3b3")
c.ellipse(37, 22, 2, 5, HW_BASE)
c.ellipse(38, 22, 2, 5, HW_RIM, fill=False)
c.set(37, 22, SILVER) # Center axis
c.set(39, 20, SILVER) # Knob

# Spool pin and Thread
c.line(25, 11, 25, 7, SILVER)
c.rect(24, 8, 3, 3, RED_FRONT)
THREAD = c.color("#ffcccc")
c.set(18, 12, SILVER) # Thread guide
c.line(24, 9, 18, 12, THREAD)
c.line(18, 12, 11, 18, THREAD) # to tension disc
c.line(11, 20, 14, 24, THREAD) # to needle

finish(c)
