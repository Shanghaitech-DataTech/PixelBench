from pixelbench_api import *
import random

# Minecraft-style dirt block texture
# 16x16 seamless tile with granular dirt
# Seamless: all randomization is position-based (wraps naturally at edges)

c = new_canvas(16, 16, name="dirt")

# Colors - Minecraft dirt palette (10 max)
DARK_BROWN = c.color((101, 67, 33))    # darkest dirt
BROWN = c.color((110, 76, 38))         # main dirt
MID_BROWN = c.color((120, 84, 42))     # lighter dirt
LIGHT_BROWN = c.color((131, 93, 49))   # light dirt
DARK_SPECK = c.color((89, 59, 29))     # dark specks
LIGHT_SPECK = c.color((141, 102, 56))  # light specks
GRAVEL = c.color((99, 76, 44))         # gravel bits
DARK_GRAVEL = c.color((85, 62, 36))    # dark gravel
VERY_LIGHT = c.color((150, 110, 62))   # sand bits
REDDISH = c.color((106, 70, 35))       # iron-red tint

def rnd(x, y, seed):
    """Deterministic pseudo-random in [0,1) based on position, wraps seamlessly."""
    h = (x * 374761393 + y * 668265263 + seed * 1274126177) & 0x7FFFFFFF
    h = (h ^ (h >> 13)) * 1274126177
    h = h & 0x7FFFFFFF
    return (h ^ (h >> 16)) / 2147483648.0

# Fill base - main dirt color
c.rect(0, 0, 16, 16, BROWN)

# Per-pixel base variation: mix of mid/dark/light depending on smooth noise
# Use a periodic smooth function: rnd(x,y,seed) directly is fine for fine noise.
# For large-scale variation use a smoothed multi-tap approach that wraps.
for y in range(16):
    for x in range(16):
        # Smooth large-scale: average of nearby rnd values to create blobs
        # Using wrapping indices for seamless behavior
        n = (
            rnd((x - 1) % 16, (y - 1) % 16, 42) +
            rnd(x, (y - 1) % 16, 42) +
            rnd((x + 1) % 16, (y - 1) % 16, 42) +
            rnd((x - 1) % 16, y, 42) +
            rnd(x, y, 42) +
            rnd((x + 1) % 16, y, 42) +
            rnd((x - 1) % 16, (y + 1) % 16, 42) +
            rnd(x, (y + 1) % 16, 42) +
            rnd((x + 1) % 16, (y + 1) % 16, 42)
        ) / 9.0
        
        if n < 0.30:
            c.set(x, y, DARK_BROWN)
        elif n < 0.55:
            c.set(x, y, BROWN)
        elif n < 0.80:
            c.set(x, y, MID_BROWN)
        else:
            c.set(x, y, LIGHT_BROWN)

# Fine speckles - dark grain
for y in range(16):
    for x in range(16):
        r = rnd(x, y, 123)
        if r < 0.10:
            c.set(x, y, DARK_SPECK)

# Fine speckles - dark gravel
for y in range(16):
    for x in range(16):
        r = rnd(x, y, 321)
        if r < 0.06:
            c.set(x, y, DARK_GRAVEL)

# Fine speckles - gravel
for y in range(16):
    for x in range(16):
        r = rnd(x, y, 456)
        if r < 0.05:
            c.set(x, y, GRAVEL)

# Light specks - light stones
for y in range(16):
    for x in range(16):
        r = rnd(x, y, 77)
        if r < 0.05:
            c.set(x, y, LIGHT_SPECK)

# Very light specks
for y in range(16):
    for x in range(16):
        r = rnd(x, y, 555)
        if r < 0.03:
            c.set(x, y, VERY_LIGHT)

# Reddish tint
for y in range(16):
    for x in range(16):
        r = rnd(x, y, 999)
        if r < 0.02:
            c.set(x, y, REDDISH)

# Occasional 2x2 small stone clusters
for x in range(16):
    for y in range(16):
        r = rnd(x, y, 1357)
        if r < 0.02:
            c.set(x, y, GRAVEL)
            c.set((x + 1) % 16, y, DARK_GRAVEL)
            c.set(x, (y + 1) % 16, DARK_GRAVEL)
            c.set((x + 1) % 16, (y + 1) % 16, GRAVEL)

# Occasional 2x2 dark moist patch
for x in range(16):
    for y in range(16):
        r = rnd(x, y, 24680)
        if r < 0.015:
            c.set(x, y, DARK_SPECK)
            c.set((x + 1) % 16, y, DARK_BROWN)
            c.set(x, (y + 1) % 16, DARK_BROWN)
            c.set((x + 1) % 16, (y + 1) % 16, DARK_SPECK)

print(c.stats_text())
print()
print(c.matrix_text(region=(0,0,15,15)))

finish(c)
