c = new_canvas(32, 32, background=None, name="result")

INK      = c.color("#1a1c22", "ink")
BRICK    = c.color("#ab4a3b", "brick")
BRICK_LT = c.color("#cb6550", "brick_lt")
BRICK_DK = c.color("#6f2b24", "brick_dk")
MORTAR   = c.color("#7d322a", "mortar")
ROOF_LT  = c.color("#5d6470", "roof_lt")
ROOF     = c.color("#464d58", "roof")
ROOF_DK  = c.color("#2b3038", "roof_dk")
CONC_LT  = c.color("#a3a9b1", "conc_lt")
CONC     = c.color("#868c95", "conc")
CONC_DK  = c.color("#5c626b", "conc_dk")
WIN_LT   = c.color("#ffe39a", "win_lt")
WIN      = c.color("#f5c463", "win")
WIN_DK   = c.color("#c07f2e", "win_dk")
DOOR_LT  = c.color("#6b7788", "door_lt")
DOOR     = c.color("#4f5a69", "door")
DOOR_DK  = c.color("#343c48", "door_dk")


def vent(x, ytop, w=6):
    c.rect(x, ytop, w, 4, INK)                          # outlined box
    c.rect(x + 1, ytop + 1, w - 2, 2, CONC)             # body
    c.rect(x + 1, ytop + 1, w - 2, 1, CONC_LT)          # lit top
    c.rect(x + w - 2, ytop + 1, 1, 2, CONC_DK)          # shaded side


# ---------------- roof vents ----------------
vent(5, 7)
vent(12, 7)

# ---------------- chimney ----------------
c.rect(20, 2, 8, 3, INK)
c.rect(21, 3, 6, 1, CONC_LT)
c.rect(21, 4, 6, 1, CONC)
c.rect(21, 5, 6, 7, INK)
for y in range(6, 11):
    c.set(22, y, BRICK_LT)
    c.set(23, y, BRICK)
    c.set(24, y, BRICK)
    c.set(25, y, BRICK_DK)
c.rect(22, 7, 4, 1, MORTAR)
c.rect(22, 10, 4, 1, MORTAR)

# ---------------- roof ----------------
c.rect(2, 11, 28, 4, INK)
c.rect(3, 12, 26, 1, ROOF_LT)
c.rect(3, 13, 26, 1, ROOF)
c.rect(3, 14, 26, 1, ROOF_DK)

# ---------------- wall brickwork ----------------
c.rect(3, 15, 26, 13, INK)
c.rect(4, 15, 24, 12, BRICK)
for y in (17, 20, 23, 26):
    c.rect(4, y, 24, 1, MORTAR)
for y0, xs in ((15, (7, 11, 15, 19, 23)),
               (18, (5, 9, 13, 17, 21, 25)),
               (21, (7, 11, 15, 19, 23)),
               (24, (5, 9, 13, 17, 21, 25))):
    for jx in xs:
        c.rect(jx, y0, 1, 2, MORTAR)
c.rect(4, 15, 1, 12, BRICK_LT)          # lit left corner
c.rect(27, 15, 1, 12, BRICK_DK)         # shaded right corner

# ---------------- window ----------------
c.rect(5, 18, 6, 6, INK)
c.rect(6, 19, 4, 4, WIN)
c.rect(6, 19, 2, 2, WIN_LT)
c.rect(8, 21, 2, 2, WIN_DK)
c.rect(5, 24, 6, 1, CONC_DK)

# ---------------- wall pipe ----------------
c.rect(25, 15, 2, 12, CONC)
c.rect(25, 15, 1, 12, CONC_LT)
c.rect(24, 15, 4, 1, CONC_DK)
c.rect(24, 20, 4, 1, CONC_DK)
c.rect(24, 24, 4, 1, CONC_DK)

# ---------------- roller door ----------------
c.rect(12, 17, 8, 10, INK)
c.rect(13, 18, 6, 8, DOOR)
c.rect(13, 18, 6, 1, DOOR_LT)
for sy in (20, 22, 24):
    c.rect(13, sy, 6, 1, DOOR_DK)

# ---------------- plinth ----------------
c.rect(2, 28, 28, 3, INK)
c.rect(3, 28, 26, 1, CONC_LT)
c.rect(3, 29, 26, 1, CONC)

print(c.stats_text())
print(c.matrix_text())
save("factory_icon", c)
finish(c)
