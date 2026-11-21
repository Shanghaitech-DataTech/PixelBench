"""Explosion effect - 64x64, two animation frames packed side by side.

Frame 1 (left half) : bright yellow fireball, white-hot core, at centre.
Frame 2 (right half): expanded orange-red starburst blast with flying sparks.
Transparent background throughout.
"""
import math

from pixelbench_api import new_canvas, view, save, finish

W = H = 64
c = new_canvas(W, H, name="explosion")

# ---------------------------------------------------------------- palette ---
WHITE_HOT = "#FFFCE8"
PALE_YEL = "#FFF07A"
BRIGHT_YEL = "#FFD91C"
AMBER = "#FFA913"
ORANGE = "#FF7A12"
RED_ORG = "#E24A0B"
DEEP_RED = "#9E1F06"
MAROON = "#6E1403"

for col in (WHITE_HOT, PALE_YEL, BRIGHT_YEL, AMBER, ORANGE, RED_ORG,
            DEEP_RED, MAROON):
    c.color(col)


# ----------------------------------------------------------------- helpers --
def wobble(a, seed):
    """Smooth angular noise in [-1, 1] so blobs are lumpy, not circular."""
    return (0.50 * math.sin(3 * a + seed)
            + 0.30 * math.sin(5 * a + seed * 1.7 + 1.1)
            + 0.20 * math.sin(7 * a + seed * 2.3 + 2.4))


def blast(cv, cx, cy, rmax, amp, seed, bands, dither=0.05):
    """Radial banded fireball.  bands = [(t_max, colour), ...] ascending."""
    r_lim = int(math.ceil(rmax)) + 1
    for y in range(max(0, int(cy) - r_lim), min(H, int(cy) + r_lim + 1)):
        for x in range(max(0, int(cx) - r_lim), min(W, int(cx) + r_lim + 1)):
            dx, dy = x - cx, y - cy
            r = math.hypot(dx, dy)
            if r > rmax + 0.6:
                continue
            a = math.atan2(dy, dx)
            R = rmax * (1.0 + amp * wobble(a, seed)) / (1.0 + amp)
            if R <= 0:
                continue
            t = r / R
            # checker dither softens every band boundary
            t += dither if ((x + y) & 1) else -dither
            col = None
            for t_max, cand in bands:
                if t <= t_max:
                    col = cand
                    break
            if col is None:
                continue
            cv.set(x, y, col)


def rays(cv, cx, cy, items):
    """items = [(angle_deg, r_start, colour, length)] -> radial streaks."""
    for ang, rad, col, length in items:
        th = math.radians(ang)
        ux, uy = math.cos(th), math.sin(th)
        for i in range(length):
            x = int(round(cx + ux * (rad + i)))
            y = int(round(cy + uy * (rad + i)))
            if 0 <= x < W and 0 <= y < H:
                cv.set(x, y, col)


# ------------------------------------------------------------- frame 1 ------
# bright yellow fireball, compact and white-hot in the middle
F1_CX, F1_CY = 16, 32
blast(c, F1_CX, F1_CY, rmax=12.2, amp=0.18, seed=0.7, bands=[
    (0.22, WHITE_HOT),
    (0.44, PALE_YEL),
    (0.68, BRIGHT_YEL),
    (0.86, AMBER),
    (0.96, ORANGE),
    (1.02, RED_ORG),
])

# a few short licks of flame breaking off the rim
rays(c, F1_CX, F1_CY, [
    (28, 13, AMBER, 2),
    (152, 13, ORANGE, 2),
    (205, 13, AMBER, 2),
    (320, 13, ORANGE, 2),
    (95, 14, BRIGHT_YEL, 1),
    (262, 14, BRIGHT_YEL, 1),
])

# ------------------------------------------------------------- frame 2 ------
# expanded orange-red blast with a star of hot rays and debris flying clear
F2_CX, F2_CY = 47, 32
blast(c, F2_CX, F2_CY, rmax=15.0, amp=0.16, seed=5.2, bands=[
    (0.16, BRIGHT_YEL),
    (0.34, AMBER),
    (0.55, ORANGE),
    (0.76, RED_ORG),
    (0.90, DEEP_RED),
    (1.02, MAROON),
])

# eight hot rays bursting out of the core, over the body
ray_angles = [0, 45, 90, 135, 180, 225, 270, 315]
pale_len = [5, 3, 4, 3, 5, 3, 4, 3]
amber_len = [4, 3, 4, 4, 3, 4, 3, 4]
rays(c, F2_CX, F2_CY, [(a, 3, PALE_YEL, L) for a, L in zip(ray_angles, pale_len)])
rays(c, F2_CX, F2_CY, [(a, 3 + L, AMBER, M)
                       for a, L, M in zip(ray_angles, pale_len, amber_len)])
rays(c, F2_CX, F2_CY, [(a, 11, ORANGE, 2) for a in (22, 68, 112, 158,
                                                    202, 248, 292, 338)])

# sparks and embers thrown clear of the fireball
rays(c, F2_CX, F2_CY, [
    (8, 15, PALE_YEL, 2),
    (40, 16, AMBER, 2),
    (72, 17, BRIGHT_YEL, 2),
    (108, 17, ORANGE, 2),
    (140, 16, PALE_YEL, 1),
    (172, 14, AMBER, 1),
    (196, 14, BRIGHT_YEL, 1),
    (222, 16, ORANGE, 2),
    (252, 17, PALE_YEL, 2),
    (284, 16, AMBER, 2),
    (316, 16, BRIGHT_YEL, 2),
    (344, 15, ORANGE, 2),
])
# lone ember dots drifting further out
for ex, ey, ecol in [(58, 15, AMBER), (36, 14, BRIGHT_YEL), (60, 46, ORANGE),
                     (34, 49, PALE_YEL), (47, 12, ORANGE), (47, 52, AMBER)]:
    c.set(ex, ey, ecol)

# ---------------------------------------------------------------- output ----
print(c.stats_text())
view(c, scale=8, margin=0)
save("explosion_effect", c, indexed=True)
finish(c)
