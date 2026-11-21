import math
import random

# One 64x64 canvas, two frames side by side:
#   frame 1: x 0..31  - bright yellow fireball at center
#   frame 2: x 32..63 - expanding orange-red blast with sparks
cv = new_canvas(64, 64, background=None, name="explosion")

WHITE = '#FFFFFF'
PALE  = '#FFF3B0'
YEL   = '#FFD93B'
GOLD  = '#FFB31A'
ORG   = '#FF7A00'
DORG  = '#E8550A'
RED   = '#D62828'
DRED  = '#8F1D22'
EMBER = '#5E2B25'


def blob(c, cx, cy, bands, seed, amp=1.0):
    """Organic wobbly filled disc. bands: [(radius, colour), ...] outermost first."""
    R = int(bands[0][0]) + 4
    for y in range(cy - R, cy + R + 1):
        for x in range(cx - R, cx + R + 1):
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy)
            a = math.atan2(dy, dx)
            wob = (1.7 * math.sin(3 * a + seed)
                   + 1.1 * math.sin(5 * a + 2.3 * seed)
                   + 0.7 * math.sin(9 * a + 1.3 * seed)) * amp
            dd = d - wob
            for r, col in reversed(bands):  # innermost band first
                if dd <= r:
                    c.set(x, y, col)
                    break


def sparks(c, cx, cy, r_min, r_max, n, colors, seed, dash=False,
           xmin=0, xmax=63, ymin=0, ymax=63):
    rnd = random.Random(seed)
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi)
        r = rnd.uniform(r_min, r_max)
        x = int(round(cx + r * math.cos(a)))
        y = int(round(cy + r * math.sin(a)))
        if not (xmin <= x <= xmax and ymin <= y <= ymax):
            continue
        col = rnd.choice(colors)
        c.set(x, y, col)
        if dash and rnd.random() < 0.6:
            # a second pixel further out along the same ray -> tiny streak
            x2 = int(round(cx + (r + 1.3) * math.cos(a)))
            y2 = int(round(cy + (r + 1.3) * math.sin(a)))
            if xmin <= x2 <= xmax and ymin <= y2 <= ymax:
                c.set(x2, y2, col)


# ---------------- frame 1: bright yellow fireball ----------------
blob(cv, 16, 32, [
    (10.5, DORG),
    (9.5, ORG),
    (7.0, GOLD),
    (5.5, YEL),
    (3.2, PALE),
    (1.8, WHITE),
], seed=1.7, amp=0.5)
sparks(cv, 16, 32, 11.5, 14.0, 10, [YEL, GOLD, ORG], seed=11, xmax=30)

# ---------------- frame 2: expanding orange-red blast ----------------
blob(cv, 48, 32, [
    (13.0, DRED),
    (12.0, RED),
    (10.0, DORG),
    (8.5, ORG),
    (6.0, GOLD),
    (3.5, YEL),
], seed=4.2, amp=0.8)
# charred flecks drifting in the red outer region
sparks(cv, 48, 32, 9.0, 12.0, 7, [EMBER, DRED], seed=37, xmin=34)
# flying sparks, some as 2px dashes
sparks(cv, 48, 32, 14.0, 16.0, 26, [YEL, GOLD, ORG, RED, DRED],
       seed=23, dash=True, xmin=33)

print(cv.stats_text())
view(cv)
finish(cv)
