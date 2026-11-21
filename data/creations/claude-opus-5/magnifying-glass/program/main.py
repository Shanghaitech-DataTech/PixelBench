c = new_canvas(16, 16, name="output")

DARK    = "#15151f"   # outline
RIM     = "#8a93a8"   # steel mid
RIM_HI  = "#dde4f0"   # rim highlight
RIM_SH  = "#4a5367"   # rim shadow
GLASS   = "#59b2d8"   # lens
GLASS_L = "#a9e3f6"   # lens streak
GLASS_D = "#2d7aa6"   # lens shadow
SPEC    = "#ffffff"   # glint
WOOD    = "#a4642e"   # handle
WOOD_H  = "#d7975a"   # handle lit side
WOOD_D  = "#6b3a16"   # handle shadow side

CX, CY = 6, 6


def disc(r):
    """Midpoint disc centred on a pixel: symmetric, no single-pixel nubs."""
    lim = (r + 0.5) ** 2
    return {(x, y)
            for y in range(16) for x in range(16)
            if (x - CX) ** 2 + (y - CY) ** 2 <= lim}


outer, metal_disc, glass_disc = disc(6), disc(5), disc(4)

# --- handle first, so the lens body can overlap its root ---
for y in range(16):
    for x in range(16):
        d, s = x - y, x + y
        if s < 20 or not 0 <= d <= 4:
            continue
        c.set(x, y, {0: DARK, 1: WOOD_D, 2: WOOD, 3: WOOD_H, 4: DARK}[d])

# ferrule: a short metal collar between rim and wood
for (x, y) in [(10, 10), (11, 10), (10, 11), (11, 11), (12, 9), (9, 12)]:
    c.set(x, y, RIM_SH)
c.set(11, 10, RIM)
c.set(10, 11, RIM)

# --- lens body: dark outline, metal ring, glass ---
for (x, y) in outer - metal_disc:
    c.set(x, y, DARK)

for (x, y) in metal_disc - glass_disc:
    s = (x - CX) + (y - CY)
    c.set(x, y, RIM_HI if s <= -4 else RIM_SH if s >= 3 else RIM)

for (x, y) in glass_disc:
    s = (x - CX) + (y - CY)
    c.set(x, y, GLASS_D if s >= 3 else GLASS)

# lens streaks: one broad diagonal sweep plus a short parallel one
for (x, y) in [(5, 3), (4, 4), (3, 5), (4, 3), (3, 4), (2, 5), (3, 6)]:
    c.set(x, y, GLASS_L)
c.set(4, 3, SPEC)
c.set(3, 4, SPEC)

view(c)
save("magnifier", c)
finish(c)
