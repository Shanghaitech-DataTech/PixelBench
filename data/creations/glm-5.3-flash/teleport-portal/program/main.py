# Teleport portal - 48x48 pixel art, transparent background.
# A purple energy vortex (swirling arms + hot core) wrapped in a glowing halo.
# The two described animation frames (vortex / rotated vortex with halo) are
# merged into this single required 48x48 canvas.

import math

c = new_canvas(48, 48, background=None, name="teleport_portal")

CX = CY = 23.5
R_DISC = 16.2          # vortex disc radius
TWIST = 5.6            # radians of swirl from centre to rim
SECTOR = 2.0 * math.pi / 3.0
ARM_W = 0.60           # fraction of each sector filled by an arm

# ---- palette ----
CORE_W = "#ffffff"     # white hot core
CORE_P = "#fbe8ff"     # pale core glow
GAP = "#3b0764"        # dark space between arms
GAP_GLOW = "#6b21a8"   # glow bleeding off the arm edge
ARM = ["#f5d0fe", "#f0abfc", "#e879f9", "#d946ef",
       "#c026d3", "#a21caf", "#86198f"]   # inner -> outer arm shades
H1 = "#c084fc"         # halo inner ring (bright)
H2 = "#a855f7"         # halo mid ring
H3 = "#7c3aed"         # halo outer ring
BEAD = "#4c1d95"       # beaded fade
DUST = "#3b1a6e"       # outermost glow dust
SPARK = "#e9d5ff"      # highlight / energy fleck


def classify(x, y):
    """Colour for a pixel inside the vortex disc, else None."""
    dx = x + 0.5 - CX
    dy = y + 0.5 - CY
    d = math.hypot(dx, dy)
    if d >= R_DISC:
        return None
    if d <= 1.7:
        return CORE_W
    if d <= 3.1:
        return CORE_P
    th = math.atan2(dy, dx)
    t = d / R_DISC
    u = ((th + TWIST * t) % SECTOR) / SECTOR
    if u < ARM_W:
        band = min(6, int(t * 7))
        if u < 0.12:                      # lit trailing edge
            band = max(0, band - 1)
        elif u > ARM_W - 0.13:            # shaded leading edge
            band = min(6, band + 1)
        return ARM[band]
    if u < ARM_W + 0.20 or d < 5.2:       # gaps glow near the core
        return GAP_GLOW
    return GAP


# ---- 1. vortex disc ----
for y in range(48):
    for x in range(48):
        col = classify(x, y)
        if col is not None:
            c.set(x, y, col)

# ---- 2. glowing halo rings ----
for y in range(48):
    for x in range(48):
        d = math.hypot(x + 0.5 - CX, y + 0.5 - CY)
        if 16.2 <= d < 17.4:
            c.set(x, y, H1)
        elif 17.4 <= d < 18.6:
            c.set(x, y, H2)
        elif 18.6 <= d < 19.7:
            c.set(x, y, H3)

# beaded fade just outside the halo, then sparse glow dust
for a in range(0, 360, 15):
    th = math.radians(a + 7)
    fx = CX + 20.9 * math.cos(th)
    fy = CY + 20.9 * math.sin(th)
    c.set(int(math.floor(fx)), int(math.floor(fy)), BEAD)
for a in range(0, 360, 30):
    th = math.radians(a + 22)
    fx = CX + 22.4 * math.cos(th)
    fy = CY + 22.4 * math.sin(th)
    c.set(int(math.floor(fx)), int(math.floor(fy)), DUST)

# ---- 3. bright highlight arcs on the inner halo ring ----
for y in range(48):
    for x in range(48):
        dx = x + 0.5 - CX
        dy = y + 0.5 - CY
        d = math.hypot(dx, dy)
        if 16.2 <= d < 17.4:
            ang = math.degrees(math.atan2(dy, dx)) % 360.0
            if (20.0 <= ang <= 65.0) or (195.0 <= ang <= 255.0):
                c.set(x, y, SPARK)

# ---- 4. energy flecks riding the arms ----
for fx, fy, col in [(13, 11, SPARK), (32, 13, H1), (34, 30, SPARK),
                    (16, 33, H1), (22, 8, SPARK), (25, 38, H1),
                    (9, 22, H1), (38, 25, SPARK), (19, 17, SPARK),
                    (28, 29, H1)]:
    c.set(fx, fy, col)

# ---- 5. ambient sparks in the surrounding void ----
for sx, sy, col in [(4, 4, H2), (43, 5, H2), (5, 43, H2), (42, 42, H2),
                    (36, 2, H3), (2, 36, H3), (45, 14, H3), (14, 45, H3)]:
    c.set(sx, sy, col)

print(c.stats_text())
print(c.matrix_text())
finish(c)
