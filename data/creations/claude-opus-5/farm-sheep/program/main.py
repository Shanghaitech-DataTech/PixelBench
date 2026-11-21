c = new_canvas(32, 32, name="output")

WOOL   = c.color("#fdf8f0", "wool")
WOOL_S = c.color("#efe5d7", "wool_shade")
WOOL_D = c.color("#dbcebb", "wool_deep")
FACE   = c.color("#dfc8b4", "face")
FACE_S = c.color("#c6ab95", "face_shade")
FACE_D = c.color("#a98d79", "face_deep")
EAR    = c.color("#f2c6c9", "ear")
EAR_S  = c.color("#dba0a7", "ear_shade")
EYE    = c.color("#4b3b34", "eye")
HOOF   = c.color("#90776a", "hoof")
HOOF_D = c.color("#75604f", "hoof_dark")

# ---------------- legs ----------------
def leg(x, top, bottom, body, hoof):
    c.rect(x, top, 2, bottom - 1 - top, body)
    c.rect(x, bottom - 1, 2, 2, hoof)

leg(9, 22, 29, FACE_S, HOOF_D)   # far pair
leg(16, 22, 29, FACE_S, HOOF_D)
leg(12, 22, 30, FACE, HOOF)      # near pair
leg(19, 22, 30, FACE, HOOF)

# ---------------- fleece body on its own layer ----------------
w = new_canvas(32, 32, name="fleece")
w.ellipse(12, 16, 9, 7, WOOL)
for (bx, by, br) in [(3, 15, 2), (4, 12, 2), (7, 10, 3), (11, 9, 3), (15, 10, 3),
                     (18, 11, 2), (20, 14, 2), (20, 18, 2), (18, 21, 3),
                     (14, 22, 3), (10, 22, 3), (6, 21, 3), (3, 19, 2),
                     (2, 17, 2)]:
    w.circle(bx, by, br, WOOL)
w.circle(2, 13, 2, WOOL)                 # tail tuft
# forehead tuft: a solid curl that overlaps the brow
w.circle(23, 12, 2, WOOL)
w.circle(25, 12, 1, WOOL)
w.set(22, 10, WOOL)
w.set(23, 10, WOOL)

# shading that follows the underside of the fleece
for x in range(32):
    col = [y for y in range(32) if w.get(x, y) == WOOL]
    if not col:
        continue
    bottom = col[-1]
    for y in col:
        if y >= bottom - 1:
            w.set(x, y, WOOL_D)
        elif y >= bottom - 3:
            w.set(x, y, WOOL_S)
# shade where the head tucks behind the fleece
for (x, y) in [(21, 14), (21, 15), (22, 14), (20, 12), (19, 11)]:
    if w.get(x, y) == WOOL:
        w.set(x, y, WOOL_S)

c.blit(w, 0, 0)

# ---------------- head ----------------
head_rows = {
    13: (22, 26),
    14: (21, 28),
    15: (21, 29),
    16: (21, 29),
    17: (21, 29),
    18: (22, 29),
    19: (23, 28),
    20: (24, 27),
}
for y, (x0, x1) in head_rows.items():
    c.line(x0, y, x1, y, FACE)

# jaw / muzzle shading
c.line(23, 19, 28, 19, FACE_S)
c.line(24, 20, 27, 20, FACE_S)
c.set(29, 18, FACE_S)
c.set(28, 18, FACE_S)
# nose and mouth hint
c.set(29, 16, FACE_D)
c.set(29, 17, FACE_D)
c.set(27, 19, FACE_D)

# ---------------- ear, pale pink, swept back ----------------
c.set(20, 13, EAR)
c.set(21, 13, EAR)
c.set(19, 14, EAR_S)
c.set(20, 14, EAR)
c.set(21, 14, EAR_S)

# ---------------- eye ----------------
c.set(26, 16, EYE)
c.set(25, 16, FACE_S)

# fleece curl sits in front of the brow
for (x, y) in [(22, 11), (23, 11), (24, 11), (22, 12), (23, 12), (24, 12),
               (25, 12), (23, 13), (24, 13)]:
    c.set(x, y, WOOL)
c.set(24, 13, WOOL_S)
c.set(25, 13, WOOL_S)

view(c)
finish(c)
