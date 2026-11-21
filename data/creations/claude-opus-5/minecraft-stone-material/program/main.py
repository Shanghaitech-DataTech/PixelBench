W = H = 16
c = new_canvas(W, H, name="stone")

P = {
    "m1": "#8b8b8b",  # base
    "m0": "#7e7e7e",  # base shade grain
    "m2": "#979797",  # base light grain
    "cr": "#5f5f5f",  # crack
    "cd": "#4b4b4b",  # deep crack / junction
    "li": "#a5a5a5",  # lit lip below a crack
    "sp": "#b6b6b6",  # bright fleck
}
for n, h in P.items():
    c.color(h, name=n)

# ---- base: per-pixel hash grain, so opposite edges stay compatible ----
for y in range(H):
    for x in range(W):
        h = (x * 7919 + y * 104729 + 31) % 97
        c.set(x, y, "m0" if h < 12 else ("m2" if h < 22 else "m1"))

# ---- crack network as explicit pixel runs; wraps: y=5 at x=0/15, x=10 at y=0/15 ----
main_h = [(0, 5), (1, 5), (2, 4), (3, 4), (4, 5), (5, 6), (6, 6), (7, 5),
          (8, 5), (9, 6), (10, 6), (11, 7), (12, 6), (13, 6), (14, 5), (15, 5)]

main_v = [(10, 0), (10, 1), (11, 2), (11, 3), (10, 4), (10, 5),
          (10, 7), (11, 8), (11, 9), (12, 10), (11, 11), (11, 12),
          (10, 13), (10, 14), (10, 15)]

branches = [
    [(4, 7), (3, 8), (2, 8), (1, 9), (0, 10)],   # exits left at y=10
    [(15, 10), (14, 11), (13, 11)],              # re-enters right at y=10
    [(2, 3), (3, 2), (3, 1)],                    # tapering upward spur
    [(4, 12), (5, 13), (6, 13), (7, 14)],        # loose lower crack
    [(14, 2), (14, 3), (13, 3)],                 # short upper-right nick
    [(6, 9), (7, 10)],                           # tiny fleck crack
]

crack = set(main_h) | set(main_v)
for b in branches:
    crack |= set(b)

for (x, y) in crack:
    c.set(x, y, "cr")

# widen/deepen a few spots: junctions and the middle of long runs
for (x, y) in [(10, 5), (10, 6), (11, 7), (5, 6), (2, 4), (11, 2), (12, 10),
               (0, 5), (15, 5), (10, 0), (10, 15), (0, 10), (1, 9)]:
    c.set(x, y, "cd")

# ---- lit lip: only under horizontally running crack segments ----
for (x, y) in sorted(crack):
    horiz = ((x - 1) % W, y) in crack or ((x + 1) % W, y) in crack
    if not horiz:
        continue
    b = (x, (y + 1) % H)
    if b not in crack and ((x, (y + 2) % H) not in crack):
        c.set(b[0], b[1], "li")

# ---- flecks on open stone ----
for (x, y) in [(1, 1), (7, 2), (13, 8), (3, 10), (8, 12), (14, 14), (5, 15)]:
    if (x, y) not in crack:
        c.set(x, y, "sp")

print(c.stats_text())
view(c)

t = new_canvas(48, 48, name="tiled")
for j in range(3):
    for i in range(3):
        t.blit(c, i * 16, j * 16)
view(t)

finish(c)
