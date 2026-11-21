c = input_canvas.copy(name="output")

# palette indices (from the input legend)
F, G, W = 6, 7, 4           # dark water, light water, white foam
LIGHT = {2, 5, 12}          # b, e, l  -> light water
DARK = {1, 3}               # a, c     -> dark water

def conv(x, y):
    """turn a dry-basin stone pixel into water, keeping its shading"""
    i = c.get(x, y)
    if i in LIGHT:
        c.set(x, y, G)
    elif i in DARK:
        c.set(x, y, F)

def fill_span(y, x0, x1, protect=()):
    for x in range(x0, x1 + 1):
        if protect and isinstance(protect[0], int):
            protect = (protect,)
        if any(a <= x <= b for a, b in protect):
            continue
        conv(x, y)

def fill_auto(y, x0, x1, protect=()):
    """fill the basin floor between the outermost existing water pixels"""
    xs = [x for x in range(x0, x1 + 1) if c.get(x, y) in (F, G)]
    if xs:
        fill_span(y, min(xs) - 1, max(xs) + 1, protect)

def stream(x0, x1, y0, y1):
    """paint a falling sheet of water with foam flecks"""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            m = (x * 5 + y * 3) % 7
            c.set(x, y, W if m == 3 else (G if m < 2 else F))

# ---------- 1. fill every dry basin with water ----------
prot = {44: (19, 44), 45: (18, 42), 46: (18, 44), 47: (18, 42),
        48: (20, 43), 49: (22, 41), 50: (25, 38)}   # keep the stone base dome
for y, p in [(8, (29, 34)), (9, (29, 34)), (10, ()), (11, ()), (12, ())]:
    fill_auto(y, 20, 43, p)                     # tier 1 (keep the spout base)
for y in range(15, 22):
    fill_auto(y, 15, 48)                        # tier 2
for y in range(27, 32):
    fill_auto(y, 13, 50)                        # tier 3
for y in range(44, 57):
    fill_auto(y, 9, 54, (prot[y],) if y in prot else ())     # lower pool

# ---------- 2. running water: jets and cascades ----------
c.set(31, 0, W); c.set(32, 0, W)                # eruption at the very top
stream(30, 30, 2, 4); stream(33, 33, 2, 4)      # down the finial's sides
stream(29, 30, 5, 7); stream(33, 34, 5, 7)      # spreading over tier 1's rim
stream(24, 26, 12, 14); stream(37, 39, 12, 14)  # tier 1 -> tier 2
stream(22, 23, 22, 26); stream(40, 41, 22, 26)  # tier 2 -> tier 3
stream(29, 34, 32, 35); stream(30, 33, 36, 50)  # tier 3 -> lower pool

# ---------- 3. splash and ripples where the cascade lands ----------
for x, y in [(29, 49), (34, 49), (29, 50), (34, 50), (28, 51), (36, 51)]:
    c.set(x, y, W)
for x, y in [(25, 51), (26, 51), (37, 51), (38, 51), (24, 52), (39, 52)]:
    c.set(x, y, G)

# ---------- 4. sparkles on the pools ----------
for x, y in [(25, 10), (38, 11), (22, 16), (41, 17), (26, 28), (38, 29),
             (20, 50), (44, 50), (16, 52), (47, 52), (24, 53), (40, 54),
             (18, 55), (45, 55)]:
    c.set(x, y, W)

# ---------- 5. drips running down the pedestal below the spillway ----------
for x, y in [(32, 62), (32, 64), (33, 64), (33, 66), (32, 68)]:
    c.set(x, y, G if y % 2 else F)

print(c.stats_text())
finish(c)
