try:
    from pixelbench_api import *
except Exception:
    pass

c = new_canvas(32, 32, background=None, name="retro-film-camera")

# ------------------------------------------------------------------ palette
OUT       = c.color("#1b1310", "outline")
LEATHER   = c.color("#3d2b1f", "leather")
LEATHER_D = c.color("#2a1c13", "leather_dark")
LEATHER_L = c.color("#54422d", "leather_light")
CHROME    = c.color("#b9bec7", "chrome")
CHROME_L  = c.color("#e6eaf0", "chrome_light")
CHROME_M  = c.color("#8f96a3", "chrome_mid")
CHROME_D  = c.color("#5c6373", "chrome_dark")
BARREL_D  = c.color("#1f1f28", "barrel_dark")
BARREL_M  = c.color("#3a3a46", "barrel_mid")
BARREL_L  = c.color("#606070", "barrel_light")
GLASS_D   = c.color("#122436", "glass_dark")
GLASS_M   = c.color("#2b5884", "glass_mid")
GLASS_L   = c.color("#6fb0d8", "glass_light")
GLASS_HL  = c.color("#e6f6ff", "glass_spark")
RED       = c.color("#b23327", "red_dot")
RED_L     = c.color("#dd6350", "red_dot_light")
RED_D     = c.color("#731f19", "red_dot_dark")

CX, CY = 16, 18          # lens centre

# ------------------------------------------------------------------ top plate (x4..27, y6..9)
c.rect(4, 6, 24, 4, CHROME)                    # classic chrome top plate
for x in range(4, 28):
    c.set(x, 6, CHROME_L)      # top bevel
    c.set(x, 9, CHROME_D)      # bottom bevel

# ------------------------------------------------------------------ viewfinder bump (x4..9, y2..5)
c.rect(4, 2, 6, 4, BARREL_D)
c.rect(5, 3, 4, 2, GLASS_M)
c.set(5, 3, GLASS_L); c.set(6, 3, GLASS_L)
c.set(7, 4, GLASS_D); c.set(8, 4, GLASS_D)

# ------------------------------------------------------------------ film advance knob (x12..17, y2..5)
c.rect(12, 2, 6, 4, CHROME_M)
for x in range(12, 18):
    c.set(x, 2, CHROME_L)
    c.set(x, 5, CHROME_D)
c.set(13, 3, CHROME_L); c.set(14, 3, CHROME_L)
c.set(15, 4, CHROME_D); c.set(16, 4, CHROME_D)

# ------------------------------------------------------------------ shutter release (button x21..25 y2..4, collar x20..26 y5)
c.rect(20, 5, 7, 1, CHROME_D)
c.rect(21, 2, 5, 3, CHROME_M)
for x in (22, 23, 24):
    c.set(x, 3, CHROME_L)
    c.set(x, 4, CHROME_M)

# ------------------------------------------------------------------ leather body (x3..28, y10..26)
c.rect(3, 10, 26, 17, LEATHER)
c.rect(3, 27, 26, 2, CHROME_M)                 # chrome base plate
for x in range(3, 29):
    c.set(x, 28, CHROME_D)

# rounded shoulders / feet -> transparent notches
for (x, y) in [(3, 10), (4, 10), (3, 11), (28, 10), (27, 10), (28, 11),
               (3, 26), (3, 27), (3, 28), (4, 28),
               (28, 26), (28, 27), (28, 28), (27, 28)]:
    c.set(x, y, "transparent")

# shadow cast by the top plate onto the body
for x in range(5, 27):
    c.set(x, 10, LEATHER_D)

# ------------------------------------------------------------------ rangefinder window (x4..7, y12..15)
c.rect(4, 12, 4, 4, BARREL_D)
c.rect(5, 13, 2, 2, GLASS_M)
c.set(5, 13, GLASS_L)
c.set(6, 14, GLASS_D)

# ------------------------------------------------------------------ red dot badge (3x3, x25..27 y13..15)
c.rect(25, 13, 3, 3, RED)
c.set(26, 13, RED_L)                           # top highlight
c.set(25, 14, RED_L)                           # left sheen
c.set(26, 15, RED_D)                           # bottom shade
c.set(27, 15, RED_D)

# ------------------------------------------------------------------ lens
c.circle(CX, CY, 7, OUT)                       # dark rim  x9..23, y11..25
c.circle(CX, CY, 6, BARREL_D)                  # outer barrel
for dy in range(-5, 6):                        # knurled focus ring, lit from upper-left
    for dx in range(-5, 6):
        d2 = dx * dx + dy * dy
        if 16 < d2 <= 25:
            s = dx + dy
            col = BARREL_L if s <= -4 else (BARREL_D if s >= 4 else BARREL_M)
            c.set(CX + dx, CY + dy, col)
c.circle(CX, CY, 4, GLASS_D)                   # glass bezel
c.circle(CX, CY, 3, GLASS_M)                   # glass
c.circle(CX, CY, 1, GLASS_D)                   # aperture core
c.set(14, 16, GLASS_HL)                        # specular
c.set(13, 17, GLASS_L); c.set(14, 17, GLASS_L); c.set(15, 16, GLASS_L)
c.set(18, 20, GLASS_L)                         # faint counter reflection

# ------------------------------------------------------------------ leather grain
# only retouch pixels that are still plain leather, so windows / badge / lens stay clean
LEATHER_IDX = LEATHER
def hsh(x, y):
    n = (x * 73856093) ^ (y * 19349663) ^ 0x9e3779b9
    n = ((n ^ (n >> 13)) * 1274126177) & 0x7fffffff
    return (n ^ (n >> 16)) % 100

for y in range(11, 27):
    for x in range(3, 29):
        if c.get(x, y) != LEATHER_IDX:
            continue
        v = hsh(x, y)
        if v < 9:
            c.set(x, y, LEATHER_D)
        elif v < 17:
            c.set(x, y, LEATHER_L)

# ------------------------------------------------------------------ dark outline
c.outline(OUT)

# ------------------------------------------------------------------ diagnostics
print(c.stats_text())
print(c.matrix_text())
finish(c)
