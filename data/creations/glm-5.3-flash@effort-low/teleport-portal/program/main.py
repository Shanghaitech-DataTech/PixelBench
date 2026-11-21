import math
from pixelbench_api import new_canvas, finish, save, view

c = new_canvas(48, 48, background=None, name="portal")

PURPLE_D = "#4a1a7a"
PURPLE   = "#7a2fd0"
PURPLE_L = "#a855f7"
VIOLET   = "#c084fc"
MAGENTA  = "#d946ef"
PINK     = "#f0abfc"
WHITE    = "#f5e9ff"
HALO     = "#b06bff"
HALO_L   = "#d9b3ff"

cx, cy = 23.5, 23.5

# --- glowing halo (outer ring) ---
for ang in range(0, 360, 2):
    a = math.radians(ang)
    for r, col in ((21.5, HALO_L), (20.5, HALO), (19.5, PURPLE_L)):
        x = int(round(cx + r * math.cos(a)))
        y = int(round(cy + r * math.sin(a)))
        c.set(x, y, col)
# halo sparkle gaps for a glow feel
for ang in range(0, 360, 30):
    a = math.radians(ang + 8)
    x = int(round(cx + 21.5 * math.cos(a)))
    y = int(round(cy + 21.5 * math.sin(a)))
    c.set(x, y, None)

# --- vortex body: filled disc with spiral arms ---
for y in range(48):
    for x in range(48):
        dx, dy = x - cx, y - cy
        d = math.hypot(dx, dy)
        if d > 19.0:
            continue
        ang = math.atan2(dy, dx)
        # spiral arms
        s = math.sin(3 * ang + d * 1.1)
        if d < 3.0:
            col = WHITE
        elif d < 5.5:
            col = PINK if s > 0 else MAGENTA
        elif d < 9.0:
            col = MAGENTA if s > 0 else VIOLET
        elif d < 13.5:
            col = VIOLET if s > 0 else PURPLE_L
        elif d < 16.5:
            col = PURPLE_L if s > 0 else PURPLE
        else:
            col = PURPLE if s > -0.4 else PURPLE_D
        c.set(x, y, col)

# darker swirl gaps between arms
for ang in range(0, 360, 3):
    a = math.radians(ang)
    for t in range(6, 19):
        d = t + (ang / 360.0) * 6.0
        if d > 19:
            continue
        x = int(round(cx + d * math.cos(a + 1.0)))
        y = int(round(cy + d * math.sin(a + 1.0)))
        if c.get(x, y) is not None and t > 8:
            c.set(x, y, PURPLE_D)

# bright core
c.circle(24, 24, 2, WHITE)
c.set(24, 24, WHITE)

print(c.stats_text())
save("teleport_portal", c)
finish(c)
