from pixelbench_api import *

W = H = 32

armor = new_canvas(W, H, name="chainmail")

OUT = armor.color("#14161a", "outline")
FACE = armor.color("#13161d", "face")
BELT = armor.color("#4c3320", "belt")
BELT_D = armor.color("#2f1f10", "belt_dark")
BUCK = armor.color("#d8b23a", "buckle")
SL = armor.color("#b7bec8", "steel_light")
SM = armor.color("#7c848f", "steel_mid")
SD = armor.color("#454b54", "steel_dark")
SH = armor.color("#262a31", "shadow")

# ---- silhouette (per-row left/right inclusive) ----
rows = {
    2: (11, 20),
    3: (10, 21),
    4: (10, 21),
    5: (10, 21),
    6: (10, 21),
    7: (10, 21),
    8: (10, 21),
    9: (10, 21),
    10: (9, 22),
    11: (7, 24),
    12: (5, 26),
    13: (4, 27),
    14: (4, 27),
    15: (5, 26),
    16: (6, 25),
    17: (7, 24),
    18: (7, 24),
    19: (7, 24),
    20: (7, 24),
    21: (7, 24),
    22: (7, 24),
    23: (8, 23),
    24: (8, 23),
    25: (9, 22),
    26: (10, 21),
}

mask = new_canvas(W, H, name="mask")
for y, (l, r) in rows.items():
    mask.rect(l, y, r - l + 1, 1, OUT)
    armor.rect(l, y, r - l + 1, 1, SM)


def inside(x, y):
    return mask.get(x, y) is not None


def ringpal(ry):
    if ry <= 6:
        return (SL, SM, SD, SD)
    if ry >= 20:
        return (SM, SD, SH, SH)
    return (SL, SM, SD, SH)


# ---- interlocking ring pattern ----
for ry in range(4, 27, 3):
    off = 0 if (ry // 3) % 2 == 0 else 1
    A, B, C, D = ringpal(ry)
    rx = 2 + off
    while rx < 30:
        if inside(rx, ry):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    x, y = rx + dx, ry + dy
                    if not inside(x, y):
                        continue
                    if dx == 0 and dy == 0:
                        armor.set(x, y, D)
                    elif dx <= 0 and dy < 0:
                        armor.set(x, y, A)
                    elif dx < 0 and dy == 0:
                        armor.set(x, y, B)
                    elif dx == 0 and dy > 0:
                        armor.set(x, y, C)
                    else:
                        armor.set(x, y, C)
        rx += 3

# ---- face opening (dark hood shadow) with dark rim ----
for y, (l, r) in {4: (12, 19), 5: (12, 19), 9: (12, 19), 10: (12, 19)}.items():
    armor.rect(l, y, r - l + 1, 1, OUT)
for y, (l, r) in {5: (13, 18), 6: (12, 19), 7: (12, 19), 8: (12, 19), 9: (13, 18)}.items():
    armor.rect(l, y, r - l + 1, 1, FACE)

# ---- belt ----
armor.rect(7, 20, 17, 3, BELT_D)
armor.rect(7, 21, 17, 1, BELT)
armor.rect(14, 20, 4, 3, OUT)
armor.rect(14, 21, 4, 1, BUCK)
armor.rect(15, 21, 2, 1, BELT_D)

# ---- under-shoulder shadows ----
armor.rect(4, 13, 3, 3, SD)
armor.rect(25, 13, 3, 3, SD)

# ---- dark outline around the whole suit ----
armor.outline(OUT)
armor.outline(OUT)

print(armor.stats_text())
print(armor.matrix_text())
finish(armor)
