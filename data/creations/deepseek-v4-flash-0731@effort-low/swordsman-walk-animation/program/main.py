from pixelbench_api import new_canvas, finish, flatten

# Palette
RED    = (204, 41, 54)     # red hair
RED_D  = (143, 29, 44)     # hair shade
SKIN   = (242, 196, 155)
SKIN_D = (217, 160, 110)
ARM    = (201, 209, 224)   # armor light
ARM_D  = (154, 166, 189)   # armor dark
CAPE   = (35, 43, 107)     # dark blue cape
CAPE_D = (20, 27, 69)
PANT   = (90, 95, 122)
BOOT   = (107, 63, 38)
SW     = (232, 232, 232)   # sword blade
SWD    = (150, 156, 176)
GOLD   = (201, 162, 39)
OUT    = (32, 34, 46)

def draw_common(c, cape_front):
    # ---- Head, facing right ----
    # top hair
    for y in range(3, 6):
        for x in range(14, 21):
            c.set(x, y, RED)
    # hair fringe across forehead
    for x in range(15, 22):
        c.set(x, 6, RED)
    c.set(21, 5, RED)      # front spike
    # back hair
    for x in range(11, 14):
        for y in range(4, 10):
            c.set(x, y, RED_D)
    c.set(12, 10, RED_D)
    c.set(13, 10, RED)
    c.set(12, 11, RED)
    # face
    for y in range(7, 11):
        for x in range(16, 21):
            c.set(x, y, SKIN)
    # chin
    c.set(16, 10, SKIN)
    c.set(20, 9, SKIN)
    # eye + brow
    c.set(18, 8, OUT)
    c.set(18, 7, RED)
    # neck
    for y in range(11, 13):
        for x in range(16, 19):
            c.set(x, y, SKIN_D)
    c.set(15, 11, SKIN_D)
    # ---- Cape (dark blue) behind torso ----
    cape_front(c)
    for x in range(11, 14):
        for y in range(12, 18):
            c.set(x, y+1, CAPE)
    for x in range(8, 12):
        for y in range(15, 19):
            c.set(x, y+1, CAPE_D)
    # ---- Torso armor ----
    for y in range(12, 19):
        for x in range(13, 22):
            c.set(x, y, ARM)
    # armor shading
    for x in range(13, 22):
        c.set(x, 17, ARM_D)
    c.set(13, 18, ARM_D)
    # belt
    for x in range(12, 21):
        c.set(x, 18, OUT)
    for x in range(14, 21):
        c.set(x, 19, PANT)
    # ---- Sword held in front (right) ----
    # front arm
    for y in range(13, 15):
        for x in range(20, 23):
            c.set(x, y, ARM)
    c.set(23, 13, ARM)
    # hand
    c.set(23, 14, SKIN)
    c.set(24, 14, SKIN)
    # guard
    for y in range(13, 16):
        c.set(24, y, GOLD)
    # handle
    c.set(24, 15, BOOT)
    # blade horizontal pointing right
    for x in range(25, 32):
        c.set(x, 14, SW)
    c.set(31, 13, SWD)
    c.set(31, 15, SWD)
    # waist/pants top
    for x in range(14, 21):
        c.set(x, 20, PANT)

def cape1(c):
    # less trailing
    c.set(10, 12, CAPE)
    c.set(10, 17, CAPE)
    c.set(9, 18, CAPE_D)

def cape2(c):
    # more flowing cape
    for x in range(9, 13):
        c.set(x, 18, CAPE_D)
    c.set(8, 17, CAPE_D)
    c.set(7, 16, CAPE_D)
    for x in range(5, 8):
        c.set(x, 19, CAPE_D)
    c.set(6, 20, CAPE_D)

def legs1(c):
    # front leg forward
    for y in range(21, 28):
        for x in range(18, 21):
            c.set(x, y, PANT)
    # front boot
    for y in range(28, 30):
        for x in range(18, 22):
            c.set(x, y, BOOT)
    c.set(17, 29, BOOT)
    # back leg trailing
    for y in range(21, 26):
        for x in range(13, 15):
            c.set(x, y, PANT)
    # back boot
    for y in range(26, 28):
        for x in range(12, 15):
            c.set(x, y, BOOT)

def legs2(c):
    # legs passing (mid stride)
    for y in range(21, 27):
        for x in range(16, 18):
            c.set(x, y, PANT)
    for y in range(28, 30):
        for x in range(16, 19):
            c.set(x, y, BOOT)
    # rear leg lifted, knee forward
    for y in range(21, 25):
        for x in range(14, 16):
            c.set(x, y, PANT)
    for y in range(24, 26):
        for x in range(14, 17):
            c.set(x, y, BOOT)

f1 = new_canvas(32, 32)
draw_common(f1, cape1)
legs1(f1)

f2 = new_canvas(32, 32)
draw_common(f2, cape2)
legs2(f2)

result = flatten([f1, f2], name="swordsman-walk")
result2 = new_canvas(64, 32)
result2.blit(f1, 0, 0)
result2.blit(f2, 32, 0)

print("F1 stats:")
print(f1.stats_text())
print("F2 stats:")
print(f2.stats_text())
print("Result stats:")
print(result2.stats_text())

finish(result2)
