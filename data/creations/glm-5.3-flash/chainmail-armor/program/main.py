try:
    from pixelbench_api import *  # noqa: F401,F403
except Exception:
    pass

# ---------------------------------------------------------------- 32x32 chainmail hauberk
c = new_canvas(32, 32, background=None, name="chainmail")

OUTLINE  = c.color("#171921", name="outline")
INTERIOR = c.color("#232833", name="neck_shadow")
BASE     = c.color("#39404b", name="mail_gap")
RING_D   = c.color("#59616e", name="ring_dim")
RING_M   = c.color("#8a92a1", name="ring")
RING_L   = c.color("#bdc5d3", name="ring_light")
SHINE    = c.color("#eef2f8", name="ring_shine")
LEATH    = c.color("#6d4527", name="leather")
LEATH_D  = c.color("#43291a", name="leather_dark")

# silhouette: (y, x0, x1) inclusive spans -- sloped shoulders, short sleeves, tapered skirt
SPANS = [
    (3, 12, 19), (4, 10, 21), (5, 8, 23), (6, 7, 24), (7, 6, 25),
    (8, 5, 26), (9, 3, 28), (10, 3, 28), (11, 3, 28), (12, 3, 28),
    (13, 4, 27), (14, 6, 25), (15, 7, 24), (16, 7, 24), (17, 7, 24),
    (18, 7, 24), (19, 7, 24), (20, 7, 24), (21, 7, 24), (22, 7, 24),
    (23, 8, 23), (24, 8, 23), (25, 8, 23), (26, 9, 22), (27, 9, 22),
    (28, 10, 21),
]
# neck opening (top centre)
NOTCH = {(14, 3), (15, 3), (16, 3), (17, 3), (14, 4), (15, 4), (16, 4), (17, 4)}

S = set()
for y, x0, x1 in SPANS:
    for x in range(x0, x1 + 1):
        if (x, y) not in NOTCH:
            S.add((x, y))

for x, y in S:
    c.set(x, y, BASE)

# ---- interlocking rings: 4x4 diamond rings, alternate rows offset by 2 px
RING_PTS = [(1, 0), (2, 0), (0, 1), (3, 1), (0, 2), (3, 2), (1, 3), (2, 3)]
HI_PTS = [(1, 0), (0, 1)]          # lit top-left arc
LO_PTS = [(2, 3), (3, 2)]          # shaded bottom-right arc


def zone(cx, cy):
    """Light falls from the upper left: lit / mid / shadow diagonal bands."""
    d = (cx - 12) + (cy - 8)
    if d > 19:
        return "shadow"
    if d > 8:
        return "mid"
    return "lit"


for ri, y0 in enumerate([5, 9, 13, 17, 21, 25]):
    xs = range(2, 27, 4) if ri % 2 == 0 else range(4, 25, 4)
    for x0 in xs:
        z = zone(x0 + 1.5, y0 + 1.5)
        if z == "lit":
            base, hi, lo = RING_M, RING_L, RING_D
            if (x0 // 4 + y0 // 4) % 2 == 0:
                hi = SHINE
        elif z == "mid":
            base, hi, lo = RING_M, RING_M, RING_D
        else:
            base, hi, lo = RING_D, RING_M, BASE
        for dx, dy in RING_PTS:
            if (x0 + dx, y0 + dy) in S:
                c.set(x0 + dx, y0 + dy, base)
        for dx, dy in HI_PTS:
            if (x0 + dx, y0 + dy) in S:
                c.set(x0 + dx, y0 + dy, hi)
        for dx, dy in LO_PTS:
            if (x0 + dx, y0 + dy) in S:
                c.set(x0 + dx, y0 + dy, lo)

# ---- dark outline around the whole silhouette
c.outline(OUTLINE)

# ---- neck: dark interior depth, then leather collar trim around the opening
for x in range(14, 18):
    c.set(x, 3, OUTLINE)      # far edge of the opening
    c.set(x, 4, INTERIOR)     # shadowed inside of the collar
TRIM = [(13, 3), (18, 3), (13, 4), (18, 4), (14, 5), (15, 5), (16, 5), (17, 5)]
for x, y in TRIM:
    c.set(x, y, LEATH)
for x, y in [(13, 3), (18, 3)]:
    c.set(x, y, LEATH_D)

# ---- leather hem closing the bottom of the skirt
for x in range(10, 22):
    c.set(x, 27, LEATH)

print(c.stats_text())
print(c.matrix_text())
# ruler + detail zooms for verification
print("    " + "".join(str(x % 10) for x in range(32)))
for y in (1, 2, 3, 4, 5, 6, 7, 8):
    print(f"y{y:2d} " + "".join("." if c.get(x, y) == 0 else "#" for x in range(32)))
print("neck zoom (x10-22, y2-7):")
print(c.matrix_text(region=(10, 2, 22, 7)))
finish(c)
