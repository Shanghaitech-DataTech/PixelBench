import math

# 32x32 inventory icon: ancient golden compass, top-down view
c = new_canvas(32, 32, name="compass")

# Register palette colours
OUTLINE     = c.color("#2a1a0e", "outline")       # near-black warm brown
GOLD        = c.color("#d4a017", "gold")          # base gold
GOLD_LIGHT  = c.color("#ecc860", "gold_light")    # bright rim gold
GOLD_DARK   = c.color("#9a6c1e", "gold_dark")     # darker gold
GOLD_DEEP   = c.color("#6e4a12", "gold_deep")     # deep bronze
BLUE        = c.color("#3f7fd8", "blue")          # crystal base
BLUE_LIGHT  = c.color("#7fc4ff", "blue_light")    # crystal highlight
BLUE_DARK   = c.color("#1f4a96", "blue_dark")     # crystal shadow
WHITE       = c.color("#f0f0e8", "white")         # glint

W = H = 32
CX = CY = 16.0


def d2(x, y):
    # squared distance from pixel centre to canvas centre
    dx = (x + 0.5) - CX
    dy = (y + 0.5) - CY
    return dx * dx + dy * dy


def disc(r, colour):
    r2 = r * r
    for y in range(H):
        for x in range(W):
            if d2(x, y) <= r2:
                c.set(x, y, colour)


def ring(r_in, r_out, colour):
    rin2 = r_in * r_in
    rout2 = r_out * r_out
    for y in range(H):
        for x in range(W):
            dd = d2(x, y)
            if rin2 < dd <= rout2:
                c.set(x, y, colour)


def in_poly(px, py, pts):
    x = px + 0.5
    y = py + 0.5
    inside = False
    n = len(pts)
    j = n - 1
    for i in range(n):
        xi, yi = pts[i]
        xj, yj = pts[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


def fill_poly(pts, colour):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x0 = max(0, int(min(xs)) - 1)
    x1 = min(W - 1, int(max(xs)) + 1)
    y0 = max(0, int(min(ys)) - 1)
    y1 = min(H - 1, int(max(ys)) + 1)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if in_poly(x, y, pts):
                c.set(x, y, colour)


def tri(ang, r_tip, r_base, hw, colour):
    """Isoceles triangle pointing outward from the centre.

    ang is in degrees, 0 = east, 90 = south (screen y is down).
    """
    rad = math.radians(ang)
    ux = math.cos(rad)
    uy = math.sin(rad)
    px = -math.sin(rad)
    py = math.cos(rad)

    tip = (CX + r_tip * ux, CY + r_tip * uy)
    b1 = (CX + r_base * ux + hw * px, CY + r_base * uy + hw * py)
    b2 = (CX + r_base * ux - hw * px, CY + r_base * uy - hw * py)
    fill_poly([tip, b1, b2], colour)


# ---- golden body with thick dark outline -------------------------------
disc(15.0, OUTLINE)          # full circular silhouette (1px margin all round)
disc(13.0, GOLD)             # gold face, leaving a 2px dark outline
ring(11.5, 13.0, GOLD_LIGHT) # bright outer rim
ring(10.8, 11.5, OUTLINE)    # thin dark groove inside the rim

# ---- compass rose (eight points) ---------------------------------------
for ang in (0, 90, 180, 270):          # long cardinal points
    tri(ang, 12.8, 6.8, 3.4, OUTLINE)
for ang in (45, 135, 225, 315):        # short diagonal points
    tri(ang, 11.2, 7.6, 2.2, GOLD_DEEP)

# ---- blue crystal centre ------------------------------------------------
ring(6.0, 6.6, GOLD_LIGHT)    # bright gold mount around the crystal
ring(5.0, 6.0, OUTLINE)       # dark bezel ring around the crystal
disc(5.0, BLUE)               # crystal body

# faceted look: light top half, dark bottom half of a rotated square
fill_poly([(16.0, 11.5), (20.5, 16.0), (16.0, 20.5), (11.5, 16.0)], BLUE_LIGHT)
fill_poly([(11.5, 16.0), (16.0, 20.5), (20.5, 16.0)], BLUE_DARK)

# small glint on the upper-left facet
for gx, gy in ((13, 12), (14, 12), (13, 13), (14, 13)):
    c.set(gx, gy, WHITE)

print(c.stats_text())
print(c.matrix_text())
finish(c)
