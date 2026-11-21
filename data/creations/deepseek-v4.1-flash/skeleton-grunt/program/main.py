from pixelbench_api import *

c = new_canvas(32, 32, name="skeleton_grunt")

# ---------------- palette ----------------
BONE    = "#ece3cc"
BONE_M  = "#c9bd9c"
BONE_D  = "#9d9074"
JOINT   = "#463c2d"
JOINT_D = "#2b241a"
SOCK    = "#191612"
TEETH   = "#f7f2df"
GLOW    = "#5fc4d2"

STEEL   = "#b3bdc8"
STEEL_L = "#e4ecf3"
STEEL_D = "#6d7a86"
GOLD    = "#c8a24c"
GOLD_D  = "#8a6c28"

WOOD    = "#9c6b3b"
WOOD_L  = "#bb8c56"
WOOD_D  = "#6a4525"
WOOD_DD = "#3d2513"
IRON    = "#8e959c"
IRON_L  = "#c3cad0"


def sp(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)


# ================= SKULL =================
sp(2, 14, 17, BONE)
sp(3, 13, 18, BONE)
sp(4, 12, 19, BONE)
sp(5, 11, 20, BONE)
sp(6, 11, 20, BONE)
sp(7, 11, 20, BONE)
sp(8, 12, 19, BONE)
sp(9, 12, 19, BONE_M)
sp(10, 13, 18, BONE_M)

# right side volume / under-jaw shadow
c.set(20, 5, BONE_M)
c.set(20, 6, BONE_M)
c.set(20, 7, BONE_D)
sp(8, 17, 19, BONE_D)
sp(9, 18, 19, BONE_D)
c.set(19, 10, BONE_D)
c.set(12, 4, BONE_M)

# eye sockets
for y in (5, 6, 7):
    sp(y, 12, 14, SOCK)
    sp(y, 17, 19, SOCK)
c.set(13, 6, GLOW)
c.set(18, 6, GLOW)

# nasal cavity
sp(8, 15, 16, SOCK)

# jaw / teeth
c.set(14, 9, JOINT)
c.set(16, 9, JOINT)
sp(10, 13, 18, TEETH)
c.set(14, 10, JOINT)
c.set(16, 10, JOINT)

# ================= NECK =================
sp(11, 14, 17, JOINT)
c.set(15, 11, JOINT_D)
c.set(16, 11, JOINT_D)

# ================= CLAVICLE / SHOULDERS =================
sp(12, 11, 20, BONE_M)
sp(12, 14, 17, JOINT)
sp(13, 8, 23, BONE)
sp(13, 8, 9, BONE_M)
sp(13, 22, 23, BONE_M)

# ================= RIB CAGE =================
sp(14, 10, 21, BONE)
sp(14, 10, 10, BONE_M)
sp(14, 20, 21, BONE_M)
sp(14, 15, 16, BONE_M)     # sternum

sp(15, 10, 21, JOINT)      # rib gap
sp(15, 15, 16, BONE_M)     # sternum

sp(16, 11, 20, BONE)
c.set(10, 16, JOINT)       # armpit shadow
c.set(21, 16, JOINT)
sp(16, 19, 20, BONE_M)

sp(17, 11, 20, BONE_M)
c.set(10, 17, JOINT)
c.set(21, 17, JOINT)
sp(17, 19, 20, BONE_D)

sp(18, 11, 20, JOINT)      # rib gap
sp(18, 15, 16, BONE_M)     # sternum
c.set(11, 18, JOINT_D)
c.set(20, 18, JOINT_D)

# ================= PELVIS =================
sp(19, 11, 20, BONE_M)
sp(19, 14, 17, BONE_D)
c.set(10, 18, JOINT)       # close armpit gap
c.set(10, 19, JOINT)
sp(20, 11, 20, BONE)
sp(20, 11, 11, BONE_M)
sp(20, 20, 20, BONE_M)
c.set(15, 20, JOINT)
c.set(16, 20, JOINT)

# ================= LEFT ARM (shield side) =================
sp(14, 8, 9, BONE)
sp(15, 8, 9, BONE)
c.set(8, 15, BONE_M)
sp(16, 8, 9, BONE_M)
sp(17, 8, 9, BONE_M)
sp(18, 8, 9, JOINT)        # elbow
c.set(9, 18, JOINT_D)
sp(19, 8, 9, BONE_M)
sp(20, 8, 9, BONE)
c.set(9, 20, JOINT)
sp(21, 8, 9, BONE)
c.set(9, 21, JOINT_D)

# ================= RIGHT ARM (sword side) =================
sp(14, 22, 23, BONE)
c.set(23, 14, BONE_M)
sp(15, 22, 23, BONE)
c.set(23, 15, BONE_M)
sp(16, 22, 23, BONE_M)
sp(17, 22, 23, JOINT)      # elbow
c.set(23, 17, JOINT_D)
sp(18, 22, 23, BONE_M)
sp(19, 22, 23, BONE)
c.set(22, 19, BONE_D)

# ================= SWORD =================
# cross guard
sp(20, 22, 27, GOLD)
c.set(22, 20, GOLD_D)
c.set(27, 20, GOLD_D)
# fist gripping the handle
sp(21, 23, 25, BONE)
c.set(24, 21, JOINT_D)
c.set(23, 21, BONE_M)
c.set(25, 21, BONE_M)
sp(22, 23, 25, BONE_M)
c.set(24, 22, JOINT)
c.set(23, 22, BONE_D)
# pommel
c.set(24, 23, GOLD)
c.set(24, 24, GOLD_D)

# blade
for y in (19, 18, 17):
    c.set(24, y, STEEL_L)
    c.set(25, y, STEEL)
for y in (16, 15, 14):
    c.set(25, y, STEEL_L)
    c.set(26, y, STEEL)
for y in (13, 12, 11, 10):
    c.set(26, y, STEEL_L)
    c.set(27, y, STEEL)
c.set(27, 9, STEEL)

# ================= SHIELD =================
SH_OUT = [(0, 15), (7, 15), (7, 20), (3, 25), (0, 20)]
SH_IN  = [(1, 16), (6, 16), (6, 20), (3, 24), (1, 20)]
c.poly(SH_OUT, WOOD_DD)
c.poly(SH_IN, WOOD)

iw = c.color(WOOD)
for y in range(16, 25):
    for x in range(1, 7):
        if c.get(x, y) == iw:
            if y <= 16:
                c.set(x, y, WOOD_L)
            elif y >= 21:
                c.set(x, y, WOOD_D)
            elif x >= 6:
                c.set(x, y, WOOD_D)
# grain
c.set(1, 19, WOOD_L)
c.set(2, 19, WOOD_L)
# corner nails
c.set(0, 16, IRON)
c.set(7, 16, IRON)
c.set(0, 15, IRON_L)
# boss
c.circle(3, 20, 1, IRON)
c.set(2, 19, IRON_L)
c.set(4, 21, STEEL_D)

# ================= LEGS =================
# hip joints
sp(21, 12, 13, JOINT)
sp(21, 18, 19, JOINT)
c.set(13, 21, JOINT_D)
c.set(19, 21, JOINT_D)
# femurs
for y in range(22, 26):
    c.set(12, y, BONE)
    c.set(13, y, BONE_M)
    c.set(18, y, BONE_M)
    c.set(19, y, BONE_D)
# knees
sp(26, 12, 13, JOINT)
sp(26, 18, 19, JOINT)
c.set(13, 26, JOINT_D)
c.set(19, 26, JOINT_D)
# shins
for y in range(27, 30):
    c.set(12, y, BONE)
    c.set(13, y, BONE_M)
    c.set(18, y, BONE_M)
    c.set(19, y, BONE_D)
c.set(13, 29, BONE_D)
c.set(19, 29, BONE_D)
# feet
sp(30, 10, 13, BONE)
sp(31, 10, 14, BONE_M)
c.set(10, 31, BONE_D)
c.set(14, 31, BONE_D)
sp(30, 18, 21, BONE_M)
sp(31, 17, 21, BONE_M)
c.set(21, 31, BONE_D)
c.set(17, 31, BONE_D)

# ================= FRAME =================
c.shift(2, -1)

print(c.stats_text())
print(c.matrix_text())
save("skeleton_grunt", c)
finish(c)
