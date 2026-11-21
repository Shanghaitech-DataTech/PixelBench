c = new_canvas(48, 48, name="output")

BLACK  = "#14151c"
BODY_D = "#272b38"
BODY   = "#394153"
BODY_L = "#4e5872"
BODY_H = "#6b779a"
GOLD   = "#e0ad3e"
GOLD_D = "#9c7322"
GOLD_L = "#f5d98a"
WOOD   = "#8b5a31"
WOOD_L = "#ab7542"
WOOD_D = "#5a3a1e"
WOOD_T = "#6d4524"
METAL  = "#b4bcc9"
METAL_D= "#79828f"
METAL_L= "#e6ebf2"
RED    = "#c43b3b"
RED_D  = "#8d2424"
RED_L  = "#e06b6b"

# ---------------- wooden base (slightly angled: top face recedes right) ---
c.poly([(2, 41), (6, 39), (47, 39), (47, 41)], WOOD_L)      # top face
c.poly([(2, 41), (47, 41), (47, 45), (2, 45)], WOOD)        # front face
c.rect(2, 44, 46, 2, WOOD_D)                                 # shadow edge
c.line(2, 41, 47, 41, WOOD_T)

# ---------------- machine bed ----------------
c.poly([(4, 36), (8, 33), (45, 33), (45, 36)], BODY_L)       # top of bed
c.poly([(4, 36), (45, 36), (45, 40), (4, 40)], BODY)         # front of bed
c.line(4, 39, 45, 39, BODY_D)
c.line(4, 36, 45, 36, BODY_H)

# ---------------- body: arm + column (C shape) ----------------
c.poly([
    (13, 7), (40, 7), (43, 10), (43, 34),
    (32, 34), (32, 18), (18, 18), (18, 25),
    (8, 25), (8, 12),
], BODY)

# shading: light along top/left, dark along bottom/right
c.line(13, 7, 40, 7, BODY_H)
c.line(9, 12, 13, 8, BODY_H)
c.rect(8, 13, 2, 12, BODY_L)
c.line(41, 11, 41, 34, BODY_D)
c.rect(42, 11, 2, 24, BODY_D)
c.line(18, 17, 31, 17, BODY_D)
c.line(9, 24, 17, 24, BODY_D)
c.rect(33, 8, 2, 26, BODY_L)

# ---------------- spool pin + thread spool on top ----------------
c.line(24, 3, 24, 7, METAL_D)
c.rect(22, 4, 5, 3, RED)
c.line(22, 4, 26, 4, RED_L)
c.line(22, 6, 26, 6, RED_D)
c.set(24, 3, METAL_L)

# thread tension disc on the head
c.circle(13, 15, 2, METAL_D, fill=False)
c.set(13, 15, GOLD)

# ---------------- needle bar, needle, presser foot ----------------
c.rect(11, 25, 2, 4, METAL_D)       # needle bar descending from the head
c.set(11, 25, METAL)
c.set(11, 26, METAL)
c.set(12, 29, METAL_L)              # needle
c.set(12, 30, METAL_L)
# presser bar + foot, set just behind the needle
c.rect(14, 25, 2, 6, METAL_D)
c.set(14, 25, METAL)
c.set(14, 26, METAL)
c.rect(11, 31, 6, 1, METAL)         # sole resting on the cloth
c.set(10, 31, METAL_D)
c.set(16, 31, METAL_D)
c.set(13, 31, METAL_L)

# thread from spool to needle
c.line(22, 6, 18, 9, RED_L)
c.line(17, 10, 14, 13, RED_L)
c.line(12, 18, 12, 24, RED_L)

# ---------------- handwheel on the right ----------------
# hand-authored bitmap so the rim reads as a ring, not a star
WHEEL = [
    "...KKKKK...",
    ".KKFFFFFKK.",
    ".KFFFFFFFK.",
    "KFFFFFFFFFK",
    "KFFFFFFFFFK",
    "KFFFFGFFFFK",
    "KFFFFFFFFFK",
    "KFFFFFFFFFK",
    ".KFFFFFFFK.",
    ".KKFFFFFKK.",
    "...KKKKK...",
]
wcx, wcy = 42, 21
for ry, row in enumerate(WHEEL):
    dy = ry - 5
    for rx, ch in enumerate(row):
        dx = rx - 5
        if ch == ".":
            continue
        if ch == "K":
            col = BLACK                    # rubber rim
        elif ch == "G":
            col = GOLD                     # hub screw
        else:
            s = dx + dy
            col = METAL_L if s <= -4 else METAL if s < 2 else METAL_D
        c.set(wcx + dx, wcy + dy, col)
# hub ring and crank knob on the wheel face
c.set(wcx - 1, wcy, METAL_D)
c.set(wcx + 1, wcy, METAL_D)
c.set(wcx, wcy - 1, METAL_D)
c.set(wcx, wcy + 1, METAL_D)
c.set(wcx + 2, wcy - 3, GOLD_D)

# ---------------- red fabric being sewn ----------------
# cloth lies on the bed, passing under the presser foot, hanging off the front-left
c.poly([(6, 34), (30, 34), (32, 33), (8, 33)], RED_L)        # far/top edge
c.poly([(5, 35), (31, 35), (30, 36), (4, 36)], RED)
c.line(8, 33, 31, 33, RED_L)
c.rect(5, 34, 25, 1, RED)
c.line(4, 36, 29, 36, RED_D)
# drape hanging off the front-left corner, folded over the bed edge
c.poly([(4, 36), (10, 36), (9, 40), (4, 40)], RED)
c.line(4, 36, 10, 36, RED_L)
c.line(4, 37, 9, 37, RED_L)
c.set(9, 38, RED_D)
c.set(9, 39, RED_D)
c.line(4, 40, 9, 40, RED_D)
c.set(6, 38, RED_L)
# stitch line running back from the needle
c.set(17, 34, GOLD_L)
c.set(20, 34, GOLD_L)
c.set(23, 34, GOLD_L)
c.set(26, 34, GOLD_L)

# ---------------- gold decals ----------------
c.path("M 21 11 Q 25 9 29 11 Q 25 13 21 11", GOLD)
c.set(25, 11, GOLD_L)
c.line(19, 13, 31, 13, GOLD_D)
c.line(35, 15, 38, 15, GOLD_D)
c.line(35, 29, 39, 29, GOLD_D)

view(c)
finish(c)
