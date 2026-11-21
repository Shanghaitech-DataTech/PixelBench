c = new_canvas(32, 32, name="skeleton")

BONE = c.color("#eae6d4", "bone")
BONE_M = c.color("#c2bba1", "bone_mid")
BONE_D = c.color("#948d76", "bone_dark")
JOINT = c.color("#4d4942", "joint")
SOCK = c.color("#26241f", "socket")
EYEG = c.color("#86e6c4", "eyeglow")
CAV = c.color("#3a372f", "cavity")

WOOD = c.color("#8a5a32", "wood")
WOOD_D = c.color("#54341b", "wood_dark")
WOOD_L = c.color("#a97a44", "wood_light")
IRON = c.color("#737b87", "iron")
IRON_D = c.color("#474e56", "iron_dark")

BLADE = c.color("#d4dae2", "blade")
BLADE_D = c.color("#8b929c", "blade_dark")
HILT = c.color("#3f2c1b", "hilt")
GOLD = c.color("#b4903c", "gold")

# ============ SKULL: thrust forward (left) and sunk into the shoulders ===
c.rect(10, 3, 5, 1, BONE)
c.rect(9, 4, 7, 5, BONE)        # cranium rows 4-8
c.rect(10, 9, 5, 1, BONE)       # cheekbones
c.rect(10, 10, 4, 1, BONE)      # jaw
# form shading: lit from upper-left
c.set(9, 4, BONE_M)
c.line(15, 4, 15, 8, BONE_M)
c.set(14, 9, BONE_M)
c.set(13, 10, BONE_M)
c.set(10, 10, BONE_M)
# eye sockets under a heavy brow
c.rect(10, 6, 2, 2, SOCK)
c.rect(13, 6, 2, 2, SOCK)
c.set(10, 6, EYEG)
c.set(13, 6, EYEG)
c.set(10, 5, BONE_M)
c.set(13, 5, BONE_M)
c.set(12, 6, BONE_M)
# nose + teeth
c.set(12, 8, SOCK)
c.set(10, 9, BONE_D)
c.set(12, 9, BONE_D)
c.set(14, 9, BONE_D)
c.set(11, 10, BONE_D)

# ============ NECK + SHOULDER GIRDLE: shoulders ride above the neck ======
c.set(14, 10, JOINT)            # vertebra behind the jaw
c.set(15, 10, BONE_M)
c.rect(11, 11, 7, 1, BONE)      # clavicle span
c.set(11, 11, BONE_M)
c.set(17, 11, BONE_M)
c.set(10, 11, JOINT)            # left shoulder socket
c.set(18, 11, JOINT)            # right shoulder socket
c.set(10, 10, BONE)             # shoulder balls hiked up
c.set(18, 10, BONE)
c.set(9, 11, BONE_D)
c.set(19, 11, BONE_D)
c.set(15, 11, BONE_D)           # shadow under the skull

# ============ RIBCAGE ===================================================
# gaps between the ribs: dark cavity, with the spine visible down the middle
c.rect(12, 13, 5, 1, CAV)
c.rect(12, 15, 5, 1, CAV)
c.rect(13, 17, 3, 1, CAV)
c.set(14, 13, BONE_D)           # spine column seen through the gaps
c.set(14, 15, BONE_D)
c.set(14, 17, BONE_D)
# rib bands, tapering toward the waist
c.rect(11, 12, 7, 1, BONE)
c.rect(12, 14, 5, 1, BONE)
c.rect(12, 16, 5, 1, BONE)
c.rect(13, 18, 3, 1, BONE)
for x, y in ((11, 12), (17, 12), (12, 14), (16, 14), (12, 16), (16, 16), (13, 18), (15, 18)):
    c.set(x, y, BONE_D)
c.set(14, 19, JOINT)            # lumbar joint

# ============ PELVIS ====================================================
c.rect(12, 20, 5, 2, BONE)
c.set(12, 20, BONE_M)
c.set(12, 21, BONE_D)
c.set(16, 21, BONE_D)
c.set(14, 21, JOINT)

# ============ LEGS ======================================================
c.set(12, 22, JOINT)            # left hip
c.line(12, 23, 11, 25, BONE)
c.set(11, 24, BONE_M)
c.set(11, 26, JOINT)            # knee
c.rect(11, 27, 1, 2, BONE)
c.set(11, 29, JOINT)            # ankle
c.rect(9, 30, 3, 1, BONE)
c.set(9, 30, BONE_D)

c.set(16, 22, JOINT)            # right hip
c.line(16, 23, 17, 25, BONE)
c.set(17, 24, BONE_M)
c.set(17, 26, JOINT)            # knee
c.rect(17, 27, 1, 2, BONE)
c.set(17, 29, JOINT)            # ankle
c.rect(17, 30, 3, 1, BONE)
c.set(19, 30, BONE_D)

# ============ SWORD ARM (viewer right, cocked back) =====================
c.line(19, 12, 20, 14, BONE)    # humerus
c.set(20, 13, BONE_M)
c.set(20, 15, JOINT)            # elbow
c.line(21, 14, 22, 12, BONE)    # forearm up
c.set(21, 13, BONE_M)
c.set(22, 11, JOINT)            # hand

# short sword
c.set(22, 10, HILT)             # grip
c.set(22, 12, HILT)             # pommel
c.rect(21, 9, 3, 1, IRON)       # crossguard
c.set(22, 9, GOLD)
c.set(22, 3, BLADE)             # tip
c.rect(22, 4, 1, 5, BLADE)      # lit edge
c.rect(23, 5, 1, 4, BLADE_D)    # shaded edge
c.set(21, 9, IRON_D)

# ============ SHIELD ARM (viewer left, braced) ==========================
c.line(9, 12, 8, 14, BONE)      # humerus
c.set(8, 13, BONE_M)
c.set(8, 15, JOINT)             # elbow
c.set(9, 16, BONE)              # forearm behind the shield

# small round wooden shield
c.circle(7, 17, 3, WOOD)
c.circle(7, 17, 3, WOOD_D, fill=False)
c.line(7, 15, 7, 19, WOOD_L)    # plank seam
c.set(6, 15, WOOD_L)
c.set(5, 16, WOOD_L)
c.set(8, 19, WOOD_D)
c.set(6, 19, WOOD_D)
c.rect(6, 17, 2, 1, IRON)       # iron boss
c.set(7, 16, IRON)
c.set(7, 17, IRON_D)

# bone grain: a few darker speckles so the bone is not a flat field
c.set(13, 4, BONE_M)
c.set(11, 23, BONE_M)
c.set(17, 23, BONE_M)
c.set(11, 28, BONE_M)
c.set(17, 28, BONE_M)
c.set(19, 13, BONE_M)
c.set(9, 13, BONE_M)
c.set(10, 30, BONE_M)
c.set(18, 30, BONE_M)

view(c)
finish(c)
