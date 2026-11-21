from pixelbench_api import *

out = input_canvas.copy(name='output')

F = out.color('#1d8baa')          # dry-pattern teal (existing)
G = out.color('#2ec7dc')          # dry-pattern cyan (existing)
W = out.color('#4db2e8', name='water')
L = out.color('#a9e8fb', name='light')
FO = out.color('#eaf8ff', name='foam')

def dry_water(x0, y0, x1, y1):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            i = out.get(x, y)
            if i == F or i == G:
                out.set(x, y, W)

# --- fill the three basins with water ---
dry_water(18, 6, 45, 12)   # upper bowl
dry_water(8, 12, 55, 32)   # main bowl
dry_water(4, 42, 59, 57)   # pond

# --- shimmering dashed ripples on the water surfaces ---
for r, off in [(8,1),(9,2),(10,0),(11,2),
               (14,1),(16,0),(18,2),(20,1),(22,0),(24,2),(26,1),(28,0),(30,2),
               (45,0),(47,2),(49,0),(51,2),(53,0),(55,1)]:
    for x in range(64):
        if out.get(x, r) == W and x % 4 == off:
            out.set(x, r, L)

# --- top plume: a solid jet spurting from the spout ---
for x in range(30, 34):
    out.set(x, 0, FO)                       # foam cap
for x in range(30, 34):
    out.set(x, 1, W)
out.set(29, 1, L); out.set(34, 1, L)
for x in range(29, 35):
    out.set(x, 2, W)
out.set(28, 2, L); out.set(35, 2, L)
for x in range(29, 35):
    out.set(x, 3, W)
out.set(28, 3, FO); out.set(35, 3, FO)
for x in range(30, 34):
    out.set(x, 4, W)
out.set(29, 4, L); out.set(34, 4, L)
out.set(31, 2, L); out.set(32, 3, L)         # glints down the jet
out.set(30, 5, W); out.set(31, 5, W); out.set(32, 5, W); out.set(33, 5, W)
out.set(28, 5, FO); out.set(35, 5, FO)

# --- overflow cascades: upper bowl spilling into the main bowl ---
for y in range(10, 13):
    out.set(21, y, W); out.set(42, y, W)
out.set(21, 12, FO); out.set(42, 12, FO)

# --- falls: main bowl running down the column sides into the pond ---
for y in range(31, 42):
    out.set(11, y, W); out.set(52, y, W)
for y in range(36, 42):
    out.set(12, y, L); out.set(51, y, L)
out.set(11, 39, L); out.set(52, 39, L)
out.set(12, 40, FO); out.set(51, 40, FO)
out.set(13, 41, L); out.set(50, 41, L)
out.set(14, 42, FO); out.set(49, 42, FO)

# --- white sparkles on the main bowl water ---
for x, y in [(18,15),(45,17),(23,21),(40,23),(17,25),(25,31),(30,14)]:
    out.set(x, y, '#ffffff')
# --- extra glints on the pond ---
for x, y in [(14,46),(49,48),(22,53),(43,54),(29,47),(33,50)]:
    out.set(x, y, L)

print(out.stats_text())
print(out.matrix_text())
finish(out)
