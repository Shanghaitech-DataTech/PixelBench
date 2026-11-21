try:
    new_canvas
except NameError:
    from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="forest-slime")

BODY   = '#66bb6a'
DARK   = '#3f9142'
DEEP   = '#2f7a38'
LIGHT  = '#a5e896'
MOSS   = '#35773a'
MOSSL  = '#9ccf5a'
ANT    = '#8a6742'
ANTD   = '#6b4e33'
SOCKET = '#1f4426'
GTINT  = '#d8e88a'
GMID   = '#ffd94d'
GCORE  = '#fff3b0'
WHITE  = '#ffffff'
SHEEN  = (178, 238, 158, 115)
RED    = '#e14b3f'
REDD   = '#a8342f'
STEM   = '#f2e3c6'
OUT    = '#1c3a22'

# ---------- body silhouette ----------
rows = {
    8: (13, 19), 9: (11, 22), 10: (9, 23), 11: (8, 24), 12: (7, 25),
    13: (6, 25), 14: (6, 26), 15: (5, 26), 16: (5, 26), 17: (5, 26),
    18: (5, 26), 19: (5, 26), 20: (5, 26), 21: (6, 25), 22: (6, 25),
    23: (6, 25), 24: (7, 24), 25: (7, 24), 26: (8, 23),
}
for y, (x0, x1) in rows.items():
    c.rect(x0, y, x1 - x0 + 1, 1, BODY)
# drippy base
c.rect(8, 27, 5, 1, BODY)
c.rect(15, 27, 3, 1, BODY)
c.rect(20, 27, 3, 1, BODY)
c.rect(9, 28, 2, 1, BODY)
c.set(16, 28, BODY)
c.set(21, 28, BODY)

# ---------- shading ----------
for y, (x0, x1) in rows.items():
    if y >= 11:
        c.set(x1, y, DARK)
    if y >= 21:
        c.set(x1 - 1, y, DARK)
c.rect(8, 26, 16, 1, DARK)
c.set(21, 27, DARK); c.set(22, 27, DARK)
c.set(24, 20, DEEP); c.set(25, 19, DEEP); c.set(25, 20, DEEP)
c.set(24, 22, DEEP); c.set(23, 24, DEEP)

# highlight (upper left)
c.set(12, 10, LIGHT); c.set(13, 10, LIGHT)
c.set(10, 12, LIGHT)
c.set(14, 9, LIGHT)

# ---------- antlers (L-shape tines, mirrored, outlined for contrast) ----------
ANT_PX = [(13, 7), (13, 6), (13, 5), (12, 4), (11, 3),
          (18, 7), (18, 6), (18, 5), (19, 4), (20, 3)]
for (x, y) in ANT_PX:
    c.set(x, y, ANT)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if c.get(x + dx, y + dy) == 0:
            c.set(x + dx, y + dy, ANTD)
for (x, y) in [(11, 2), (20, 2)]:
    c.set(x, y, ANTD)  # darker tips
# regrow the moss tufts at the antler bases
for (x, y) in [(14, 8), (15, 8)]:
    c.set(x, y, MOSS)
for (x, y) in [(14, 7), (15, 7), (16, 7), (17, 7)]:
    c.set(x, y, None)

# ---------- mushroom on back (right shoulder) ----------
c.set(22, 9, BODY)   # clear old stem leftovers back to body/air
c.set(23, 9, None)
c.set(22, 10, BODY)
c.set(23, 10, BODY)
c.rect(22, 4, 4, 1, RED)
c.rect(21, 5, 6, 1, RED)
c.rect(21, 6, 6, 1, RED)
c.set(21, 7, REDD); c.set(22, 7, REDD)
c.rect(23, 7, 2, 1, STEM)
c.set(25, 7, REDD); c.set(26, 7, REDD)
c.set(21, 5, REDD); c.set(26, 5, REDD)
c.set(23, 4, WHITE); c.set(25, 4, WHITE)
c.set(22, 6, WHITE); c.set(25, 6, WHITE)

# ---------- moss ----------
for (x, y) in [(11, 9), (12, 9), (11, 10), (14, 8), (15, 8),
               (20, 9), (20, 10), (26, 15), (26, 16), (5, 18), (5, 19),
               (6, 19)]:
    c.set(x, y, MOSS)
c.set(11, 11, MOSSL); c.set(26, 17, MOSSL); c.set(5, 20, MOSSL)
# mossy middle drip
c.rect(15, 27, 3, 1, MOSS)
c.set(16, 28, MOSS)
c.set(17, 27, MOSSL)

# ---------- face ----------
def eye(x0, y0):
    # glow tint halo ring
    for (dx, dy) in [(0, -1), (1, -1), (2, -1), (3, -1),
                     (-1, 1), (-1, 2), (4, 1), (4, 2),
                     (0, 4), (1, 4), (2, 4), (3, 4)]:
        c.set(x0 + dx, y0 + dy, GTINT)
    c.rect(x0, y0, 4, 4, SOCKET)
    for (dx, dy) in [(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1),
                     (0, 2), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3)]:
        c.set(x0 + dx, y0 + dy, GMID)
    c.rect(x0 + 1, y0 + 1, 2, 2, GCORE)
    c.set(x0 + 1, y0 + 1, WHITE)

eye(10, 14)
eye(18, 14)

# cat-like w mouth + tiny fangs
for (x, y) in [(13, 20), (14, 21), (15, 20), (16, 20), (17, 21), (18, 20)]:
    c.set(x, y, SOCKET)
for (x, y) in [(13, 21), (18, 21)]:
    c.set(x, y, DEEP)
c.set(14, 22, WHITE); c.set(17, 22, WHITE)

# ---------- outline ----------
c.outline(OUT)

# inner glassy sheen around the eyes
for p in [(12, 17), (20, 17)]:
    c.set(*p, SHEEN)

view(c)
print(c.stats_text())
save("forest-slime", c)
finish(c)
