from pixelbench_api import new_canvas, finish

c = new_canvas(48, 48, name="magic-staff")

# ---- palette ----
WOOD_DARK = "#3c2210"
WOOD = "#7a4a22"
WOOD_LIGHT = "#9c6830"
WOOD_HL = "#c28a4e"
PURPLE_DARK = "#3d1168"
PURPLE = "#6f24ad"
PURPLE_BRIGHT = "#9d4de8"
PURPLE_LIGHT = "#c58cff"
PURPLE_PALE = "#e8d4ff"
GLOW_A = "#6f24ad40"
GLOW_B = "#9d4de820"
GLOW_C = "#c58cff0c"

# ---- soft auras behind everything ----
c.circle(30, 18, 7, GLOW_C)
c.circle(30, 18, 5, GLOW_B)
c.circle(30, 18, 4, GLOW_A)
c.circle(26, 9, 6, GLOW_C)
c.circle(26, 9, 4, GLOW_B)

# ---- wooden shaft ----
for y in range(14, 47):
    c.set(20, y, WOOD_DARK)
    c.set(21, y, WOOD)
    c.set(22, y, WOOD_LIGHT)
    c.set(23, y, WOOD_LIGHT)
    c.set(24, y, WOOD)
    c.set(25, y, WOOD_DARK)
for y in range(15, 46, 4):
    c.set(22, y, WOOD_HL)
# leather grip wraps
for y in (28, 29, 30):
    c.set(21, y, WOOD_DARK)
    c.set(22, y, WOOD_DARK)
    c.set(23, y, WOOD_DARK)
    c.set(24, y, WOOD_DARK)
    c.set(22, y, WOOD)
# base cap
for x in range(20, 26):
    c.set(x, 47, WOOD_DARK)

# ---- curved crook head (thick band along an arc) ----
centers = [(22, 13), (23, 11), (24, 9), (26, 8), (28, 8), (30, 9), (31, 11), (31, 13), (30, 15)]
for (cx, cy) in centers:
    c.circle(cx, cy, 2, WOOD_DARK)
for (cx, cy) in centers:
    c.circle(cx - 1, cy - 1, 2, WOOD)
for (cx, cy) in centers:
    c.circle(cx - 1, cy - 1, 1, WOOD_LIGHT)
for (cx, cy) in [(24, 8), (28, 7), (30, 9)]:
    c.circle(cx - 1, cy - 1, 1, WOOD_HL)

# ---- purple orb hanging from the hook tip ----
c.circle(30, 18, 3, PURPLE_DARK)
c.circle(30, 18, 2, PURPLE)
c.circle(30, 18, 1, PURPLE_BRIGHT)
c.set(30, 17, PURPLE_LIGHT)
c.set(29, 17, PURPLE_PALE)
# small wooden mount connecting tip to orb
c.set(30, 16, WOOD)
c.set(29, 16, WOOD_DARK)
c.set(31, 17, WOOD_DARK)

# ---- purple particles ----
dots = [(10, 7), (13, 4), (8, 13), (15, 9), (19, 5), (24, 3), (28, 2),
        (33, 4), (36, 7), (39, 11), (42, 15), (38, 19), (33, 21), (28, 20),
        (18, 2), (7, 17), (12, 16), (41, 8), (36, 3), (14, 20), (32, 20), (28, 22)]
for (x, y) in dots:
    c.set(x, y, PURPLE_BRIGHT)
pale = [(9, 9), (17, 6), (35, 5), (40, 13), (11, 12), (6, 19), (37, 21),
        (15, 17), (31, 2), (41, 17), (19, 24), (16, 28), (36, 26), (31, 23)]
for (x, y) in pale:
    c.set(x, y, PURPLE_LIGHT)
mid = [(33, 23), (18, 26), (29, 25), (40, 22), (12, 25)]
for (x, y) in mid:
    c.set(x, y, PURPLE_BRIGHT)


def sparkle(x, y):
    c.set(x, y, PURPLE_BRIGHT)
    c.set(x - 1, y, PURPLE_LIGHT)
    c.set(x + 1, y, PURPLE_LIGHT)
    c.set(x, y - 1, PURPLE_LIGHT)
    c.set(x, y + 1, PURPLE_LIGHT)


sparkle(16, 8)
sparkle(38, 10)
sparkle(11, 11)

print(c.stats_text())
finish(c)
