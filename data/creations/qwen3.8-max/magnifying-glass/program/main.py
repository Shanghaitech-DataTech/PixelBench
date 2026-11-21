# 16x16 pixel art: detective-game magnifying glass icon
try:
    new_canvas
except NameError:  # pragma: no cover - fallback for helper modules
    from pixelbench_api import *

# ---------------------------------------------------------------- palette
OUT      = "#1b1f2b"   # unified dark outline
STEEL_L  = "#d7e3ec"   # rim highlight (upper-left)
STEEL_M  = "#93a9bc"   # rim mid tone
STEEL_D  = "#4e6a82"   # rim shadow (lower-right)
GLASS_L  = "#a9e9ff"
GLASS_M  = "#57bfe8"
GLASS_D  = "#2b7fb8"
WHITE    = "#ffffff"
WOOD_L   = "#e0a45c"
WOOD_M   = "#b06a2c"
WOOD_D   = "#7a4419"
FERR_L   = "#e2ecf3"   # metal ferrule
FERR_M   = "#9db2c4"
FERR_D   = "#5b7488"

CX, CY = 6, 6          # lens centre

c = new_canvas(16, 16, name="magnifier")

# ---------------------------------------------------------------- handle
# dark silhouette of the handle (drawn first, the rim overlaps it)
for y in range(10, 16):
    for x in range(10, 16):
        if abs(x - y) <= 2:
            c.set(x, y, OUT)

# wooden grip, 3 px wide, lit from the upper-left
for y in range(11, 15):
    for x in range(11, 15):
        if abs(x - y) <= 1:
            d = x - y
            c.set(x, y, WOOD_L if d == 1 else (WOOD_M if d == 0 else WOOD_D))

# metal ferrule where grip meets the rim
c.set(12, 11, FERR_L)
c.set(11, 11, FERR_M)
c.set(11, 12, FERR_D)

# ---------------------------------------------------------------- lens
H = {1: 3, 2: 7, 3: 9, 4: 11, 5: 11, 6: 11, 7: 11, 8: 11, 9: 9, 10: 7, 11: 3}
F = {2: 5, 3: 7, 4: 9, 5: 9, 6: 9, 7: 9, 8: 9, 9: 7, 10: 5}
G = {3: 3, 4: 5, 5: 7, 6: 7, 7: 7, 8: 5, 9: 3}


def span(cy, w):
    h = w // 2
    return range(CX - h, CX - h + w)


# outer dark ring
for y, w in H.items():
    for x in span(y, w):
        c.set(x, y, OUT)

# steel rim, shaded by angle to the light
for y, w in F.items():
    for x in span(y, w):
        s = (x - CX) + (y - CY)
        c.set(x, y, STEEL_L if s <= -4 else (STEEL_D if s >= 3 else STEEL_M))

# glass
for y, w in G.items():
    for x in span(y, w):
        s = (x - CX) + (y - CY)
        c.set(x, y, GLASS_L if s <= -3 else (GLASS_D if s >= 3 else GLASS_M))

# specular glint
c.set(5, 3, WHITE)
c.set(4, 4, WHITE)

view(c)
print(c.stats_text())
save("magnifier", c)
finish(c)
