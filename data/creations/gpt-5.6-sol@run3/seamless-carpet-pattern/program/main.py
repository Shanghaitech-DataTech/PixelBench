from pixelbench_api import *

W = H = 32
c = new_canvas(W, H, background="#7b2f24", name="seamless_carpet")

# Compact warm wool palette.
COL = {
    "rust": "#7b2f24",
    "rust_dark": "#54251f",
    "rust_light": "#a84a2f",
    "brick": "#923a28",
    "gold": "#d79a3a",
    "gold_hi": "#efc064",
    "ochre": "#b66c2d",
    "cream": "#f1d89a",
    "brown": "#3b211c",
    "teal": "#315f57",
    "teal_hi": "#4e8170",
    "rose": "#c95b48",
}

# Woven ground: periodic over-under flecks, including both tile boundaries.
for y in range(H):
    for x in range(W):
        if (x + 2*y) % 8 == 0:
            c.set(x, y, COL["rust_light"])
        elif (2*x + y) % 8 == 3:
            c.set(x, y, COL["rust_dark"])
        elif x % 4 == 1 and y % 4 == 2:
            c.set(x, y, COL["brick"])

# Toroidal helpers make every cut motif continue exactly on the opposite side.
def td(a, b, n=32):
    d = abs(a-b)
    return min(d, n-d)

def torus_diamond(cx, cy, radius, outer, inner=None):
    for y in range(H):
        for x in range(W):
            d = td(x, cx) + td(y, cy)
            if d <= radius:
                c.set(x, y, outer if inner is None or d >= radius-1 else inner)

# Interlocking guard stripe on all four cuts, naturally continuing when tiled.
for y in range(H):
    for x in range(W):
        ex = td(x, 0)
        ey = td(y, 0)
        if ex == 0 or ey == 0:
            c.set(x, y, COL["brown"])
        elif ex == 1 or ey == 1:
            c.set(x, y, COL["gold"] if ((x//2 + y//2) % 2 == 0) else COL["ochre"])

# Half flowers centered on each edge and quarter flowers at corners.
def wrapped_flower(cx, cy, petal, core):
    for y in range(H):
        for x in range(W):
            dx, dy = td(x, cx), td(y, cy)
            # Four blocky petals with tiny diagonal shoulders.
            is_petal = ((dx <= 1 and 2 <= dy <= 3) or
                        (dy <= 1 and 2 <= dx <= 3) or
                        (dx == 2 and dy == 2))
            if is_petal:
                c.set(x, y, petal)
            if dx <= 1 and dy <= 1:
                c.set(x, y, core)

wrapped_flower(0, 0, COL["teal"], COL["gold_hi"])
wrapped_flower(16, 0, COL["cream"], COL["teal"])
wrapped_flower(0, 16, COL["cream"], COL["teal"])

# Small leafy vine buds between the edge flowers.
for cx, cy in [(8,2),(24,2),(2,8),(2,24),(30,8),(30,24),(8,30),(24,30)]:
    c.set(cx, cy, COL["gold_hi"])
    c.set((cx-1)%32, cy, COL["teal_hi"])
    c.set((cx+1)%32, cy, COL["teal"])

# Central stepped medallion, woven as nested diamonds.
cx = cy = 16
for y in range(H):
    for x in range(W):
        d = abs(x-cx) + abs(y-cy)
        if d <= 11:
            if d >= 10: col = COL["brown"]
            elif d >= 8: col = COL["gold"] if (x+y)%2 else COL["gold_hi"]
            elif d == 7: col = COL["brown"]
            elif d >= 5: col = COL["teal"]
            elif d == 4: col = COL["cream"]
            else: col = COL["rust_dark"]
            c.set(x, y, col)

# Cardinal floral border around the diamond: flowers sit just inside the gold band.
for fx, fy in [(16,8),(24,16),(16,24),(8,16)]:
    c.set(fx, fy, COL["cream"])
    c.set(fx-1, fy, COL["rose"]); c.set(fx+1, fy, COL["rose"])
    c.set(fx, fy-1, COL["rose"]); c.set(fx, fy+1, COL["rose"])
    c.set(fx-1, fy-1, COL["gold_hi"]); c.set(fx+1, fy+1, COL["gold_hi"])

# Central eight-point woven flower.
for x,y,col in [
    (16,16,"gold_hi"),(15,16,"cream"),(17,16,"cream"),(16,15,"cream"),(16,17,"cream"),
    (14,16,"rose"),(18,16,"rose"),(16,14,"rose"),(16,18,"rose"),
    (15,15,"gold"),(17,15,"gold"),(15,17,"gold"),(17,17,"gold"),
    (16,13,"teal_hi"),(19,16,"teal_hi"),(16,19,"teal_hi"),(13,16,"teal_hi")]:
    c.set(x,y,COL[col])

# Deliberate single-pixel highlights suggest raised wool knots.
for x,y in [(11,11),(21,11),(11,21),(21,21),(6,6),(26,6),(6,26),(26,26)]:
    c.set(x,y,COL["ochre"])

view(c, scale=16, margin=0)
finish(c)
