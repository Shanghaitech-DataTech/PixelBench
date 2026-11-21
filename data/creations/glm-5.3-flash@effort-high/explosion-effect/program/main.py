import math

c = new_canvas(64, 64, None, 'explosion')

# Palette
WHITE      = c.color('#FFFFFF', 'white_hot')
PALE_YEL   = c.color('#FFF3A0', 'pale_yellow')
YELLOW     = c.color('#FFD23F', 'yellow')
ORANGE     = c.color('#FF9F1C', 'orange')
RED_ORANGE = c.color('#F2541B', 'red_orange')
DEEP_RED   = c.color('#C1272D', 'deep_red')

CX, CY = 32.0, 32.0


def jagged_star(cx, cy, r_inner, r_outer, n, phase=0.0, wobble=None):
    """Simple (non self-crossing) star polygon: n spikes."""
    pts = []
    for i in range(2 * n):
        ang = math.pi * i / n + phase
        r = r_outer if i % 2 == 0 else r_inner
        if wobble is not None:
            r = wobble(r, i)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def wob(r, i):
    # deterministic irregularity so the blast looks organic
    return r * (0.82 + 0.36 * ((i * 37) % 11) / 10.0)


# --- Frame-2 expanding blast: layered jagged flame shells (outermost first) ---
c.poly(jagged_star(CX, CY, 11, 19, 9, phase=0.13, wobble=wob), DEEP_RED)
c.poly(jagged_star(CX, CY, 9, 15.5, 8, phase=0.42, wobble=wob), RED_ORANGE)
c.poly(jagged_star(CX, CY, 7, 12.5, 8, phase=0.75, wobble=wob), ORANGE)

# --- Frame-1 fireball still burning at the heart ---
c.poly(jagged_star(CX, CY, 5, 9.5, 7, phase=0.30, wobble=wob), YELLOW)
c.circle(32, 32, 4, PALE_YEL)
c.circle(32, 32, 2, WHITE)

# --- Rising flame tongues off the top of the blast ---
c.poly([(27, 16), (25, 6), (30, 15)], ORANGE)
c.poly([(33, 15), (36, 4), (38, 16)], RED_ORANGE)
c.poly([(30, 16), (31, 2), (34, 16)], YELLOW)
c.set(31, 3, PALE_YEL)

# --- Sparks flying outward ---
def spark(angle_deg, dist, colour, length=0):
    a = math.radians(angle_deg)
    x = CX + dist * math.cos(a)
    y = CY + dist * math.sin(a)
    xi, yi = int(round(x)), int(round(y))
    if length:
        x2 = CX + (dist - length) * math.cos(a)
        y2 = CY + (dist - length) * math.sin(a)
        c.line(int(round(x2)), int(round(y2)), xi, yi, colour)
    else:
        c.set(xi, yi, colour)

# long streaks
for ang, d, col, ln in [
    (15, 26, ORANGE, 5), (60, 27, RED_ORANGE, 4), (105, 25, ORANGE, 5),
    (150, 26, RED_ORANGE, 4), (200, 27, ORANGE, 5), (245, 26, RED_ORANGE, 4),
    (290, 25, ORANGE, 4), (335, 27, RED_ORANGE, 5),
]:
    spark(ang, d, col, ln)

# short streaks
for ang, d, col, ln in [
    (35, 21, YELLOW, 3), (80, 22, YELLOW, 3), (130, 21, YELLOW, 3),
    (175, 22, YELLOW, 3), (220, 21, YELLOW, 3), (265, 22, YELLOW, 3),
    (310, 21, YELLOW, 3),
]:
    spark(ang, d, col, ln)

# dot sparks at the tips and beyond
dots = [
    (15, 30, ORANGE), (60, 31, YELLOW), (105, 29, YELLOW), (150, 30, ORANGE),
    (200, 31, YELLOW), (245, 30, ORANGE), (290, 29, YELLOW), (335, 31, ORANGE),
    (0, 24, RED_ORANGE), (45, 24, RED_ORANGE), (90, 24, RED_ORANGE),
    (135, 24, RED_ORANGE), (180, 24, RED_ORANGE), (225, 24, RED_ORANGE),
    (270, 24, RED_ORANGE), (315, 24, RED_ORANGE),
    (25, 33, PALE_YEL), (70, 33, PALE_YEL), (160, 33, PALE_YEL),
    (255, 33, PALE_YEL), (300, 34, PALE_YEL), (120, 34, PALE_YEL),
]
for ang, d, col in dots:
    spark(ang, d, col)

# a few stray embers drifting further out
for x, y, col in [(10, 12, ORANGE), (54, 9, YELLOW), (57, 50, ORANGE),
                  (7, 47, YELLOW), (46, 58, RED_ORANGE), (18, 57, ORANGE),
                  (60, 28, PALE_YEL), (4, 30, PALE_YEL)]:
    c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
