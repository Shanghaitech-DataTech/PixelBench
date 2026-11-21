from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

A = c.color("#1d1208")  # outline near-black
B = c.color("#381f0e")  # dark leather shadow / spine
C = c.color("#5a3518")  # leather base
D = c.color("#7d4f23")  # leather highlight
E = c.color("#b8872c")  # gold metal
F = c.color("#e6bd52")  # gold bright
G = c.color("#dcc896")  # page cream
H = c.color("#8a6623")  # gold shadow / gem dark

# ---- book silhouette (dark outline) ----
c.rect(4, 3, 24, 26, A)      # x4..27, y3..28

# ---- leather cover face ----
c.rect(5, 4, 21, 24, C)      # x5..25, y4..27
c.rect(26, 5, 1, 23, G)      # fore-edge pages, column x26
c.rect(5, 4, 3, 24, B)       # spine x5..7
c.rect(6, 5, 1, 22, C)       # inner spine line
c.rect(8, 4, 5, 24, D)       # lit band x8..12
c.rect(23, 4, 3, 24, B)      # shadow band x23..25
c.rect(5, 8, 3, 2, D)        # raised bands on spine
c.rect(5, 22, 3, 2, D)

# ---- decorative gold panel ----
c.rect(10, 7, 11, 15, E, fill=False)   # x10..20, y7..21
for p in [(10, 7), (20, 7), (10, 21), (20, 21)]:
    c.set(*p, F)

# ---- gem on the cover ----
gem = [(15, 12),
       (14, 13), (15, 13), (16, 13),
       (13, 14), (14, 14), (15, 14), (16, 14), (17, 14),
       (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15),
       (13, 16), (14, 16), (15, 16), (16, 16), (17, 16),
       (14, 17), (15, 17), (16, 17),
       (15, 18)]
for p in gem:
    c.set(*p, H)
for p in [(15, 13), (14, 14), (15, 14), (16, 14), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15)]:
    c.set(*p, E)
for p in [(15, 13), (14, 14), (15, 14)]:
    c.set(*p, F)

# ---- metal corner brackets ----
def bracket(cx, cy, dx, dy):
    for p in [(cx, cy), (cx + dx, cy), (cx, cy + dy), (cx + 2 * dx, cy), (cx, cy + 2 * dy)]:
        c.set(*p, E)
    c.set(cx, cy, F)

bracket(5, 4, 1, 1)
bracket(25, 4, -1, 1)
bracket(5, 27, 1, -1)
bracket(25, 27, -1, -1)

# ---- clasp over the fore-edge ----
c.rect(21, 12, 7, 6, A, fill=False)   # x21..27, y12..17 dark frame
c.rect(22, 13, 5, 4, E)               # metal strap
c.rect(22, 13, 5, 1, F)               # top shine
c.rect(22, 16, 5, 1, H)               # bottom shade

print(c.stats_text())
finish(c)
