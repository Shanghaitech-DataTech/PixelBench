from pixelbench_api import *

out = input_canvas.copy(name="output")

# ---- chocolate tones (reuse the drawing's warm browns, add one gloss) ----
BODY = out.color((99, 51, 37))    # melted chocolate body
SH = out.color((85, 38, 18))      # deep shadow brown
HI = out.color((166, 102, 60))    # caramel gloss highlight
CHOC = {BODY, SH, HI}


def hline(x0, x1, y, col):
    for x in range(x0, x1 + 1):
        out.set(x, y, col)


def vline(x, y0, y1, col):
    for y in range(y0, y1 + 1):
        out.set(x, y, col)


# ------------------------------------------------------------------
# 1) Melt band: coats the ice cream's bottom face (rows 31-32) and
#    hangs over the cone rim (33-36) with a scalloped lower edge.
#    Three hanging lobes; the centre one is the deepest.
# ------------------------------------------------------------------
band = {19: 33, 20: 34, 21: 34, 22: 35, 23: 36, 24: 38, 25: 38, 26: 37,
        27: 36, 28: 36, 29: 39, 30: 41, 31: 42, 32: 41, 33: 39,
        34: 37, 35: 36, 36: 37, 37: 38, 38: 37, 39: 35, 40: 34,
        41: 34, 42: 33}
for x, yb in band.items():
    vline(x, 31, yb, BODY)

hline(20, 41, 31, HI)   # gloss catching the top edge of the melt
hline(20, 22, 32, SH)   # shadow on the left (cone is lit from the right)
hline(39, 42, 32, HI)

# ------------------------------------------------------------------
# 2) Left drip: 2px stream, 4px bulb, rounded tip.  y37-45.
# ------------------------------------------------------------------
out.set(24, 37, SH); out.set(25, 37, HI)
out.set(24, 38, SH); out.set(25, 38, HI)
for y in (39, 40, 41):
    out.set(24, y, SH); out.set(25, y, HI)
hline(23, 26, 42, BODY); hline(23, 26, 43, BODY)
out.set(23, 42, SH); out.set(26, 42, HI)
out.set(23, 43, SH); out.set(26, 43, HI)
out.set(24, 44, SH); out.set(25, 44, HI)
out.set(24, 45, SH)

# ------------------------------------------------------------------
# 3) Centre drip: the long one.  Lobe -> 3px stream -> bulb -> tip.
#    y37-52.
# ------------------------------------------------------------------
vline(29, 37, 39, SH)
vline(33, 37, 39, HI)
for y in (43, 44, 45, 46, 47):
    out.set(30, y, SH); out.set(31, y, BODY); out.set(32, y, HI)
for y in (48, 49, 50):
    hline(29, 33, y, BODY)
    out.set(29, y, SH); out.set(33, y, HI)
out.set(30, 51, SH); out.set(31, 51, BODY); out.set(32, 51, HI)
out.set(31, 52, SH)

# ------------------------------------------------------------------
# 4) Right drip, mirror of the left.  y37-45.
# ------------------------------------------------------------------
out.set(36, 37, SH); out.set(37, 37, HI)
out.set(36, 38, SH); out.set(37, 38, HI)
for y in (39, 40, 41):
    out.set(36, y, SH); out.set(37, y, HI)
hline(35, 38, 42, BODY); hline(35, 38, 43, BODY)
out.set(35, 42, SH); out.set(38, 42, HI)
out.set(35, 43, SH); out.set(38, 43, HI)
out.set(35, 44, SH); out.set(36, 44, BODY)
out.set(36, 45, SH)

# ------------------------------------------------------------------
# 5) A droplet that has just let go of the long drip.
# ------------------------------------------------------------------
out.set(30, 54, BODY); out.set(31, 54, HI)
hline(29, 32, 55, BODY)
out.set(29, 55, SH); out.set(32, 55, HI)
out.set(30, 56, SH); out.set(31, 56, BODY)

# ------------------------------------------------------------------
# verification: every chocolate pixel below the rim must sit on the cone
# ------------------------------------------------------------------
cone = {37: (21, 40), 38: (21, 40), 39: (21, 40), 40: (21, 40),
        41: (23, 38), 42: (23, 38), 43: (23, 38),
        44: (24, 36), 45: (24, 36), 46: (24, 36),
        47: (25, 36), 48: (25, 36), 49: (25, 36), 50: (25, 36),
        51: (25, 34), 52: (27, 34), 53: (27, 34), 54: (27, 34),
        55: (27, 34), 56: (29, 32), 57: (29, 32), 58: (29, 32),
        59: (29, 32)}
bad = []
for y, (x0, x1) in cone.items():
    for x in range(64):
        if out.get(x, y) in CHOC and not (x0 <= x <= x1):
            bad.append((x, y))
print("chocolate outside cone silhouette:", bad)

for y in range(29, 60):
    runs, start = [], None
    for x in range(64):
        if out.get(x, y) in CHOC:
            if start is None:
                start = x
        elif start is not None:
            runs.append((start, x - 1)); start = None
    if start is not None:
        runs.append((start, 63))
    if runs:
        print(y, runs)

print(out.stats_text())
print(out.matrix_text(region=(16, 24, 45, 40), indices=True))
print(out.matrix_text(region=(26, 44, 37, 58), indices=True))

finish(out)
