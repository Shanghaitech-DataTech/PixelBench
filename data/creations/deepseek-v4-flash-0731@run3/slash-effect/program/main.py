import math
from pixelbench_api import new_canvas, finish

W = H = 48
c = new_canvas(W, H, name="slash_fx")

WHITE = "#ffffff"
SOFT = "#ffffffcc"
FAINT = "#ffffff88"


def arc(cv, cx, cy, r, a0, a1, color, step=1.5):
    """Arc using y-down canvas coords; theta=270 points up."""
    a0r, a1r = math.radians(a0), math.radians(a1)
    n = max(2, int(abs(a1r - a0r) / math.radians(step)))
    pts = [
        (round(cx + r * math.cos(a0r + (a1r - a0r) * i / n)),
         round(cy + r * math.sin(a0r + (a1r - a0r) * i / n)))
        for i in range(n + 1)
    ]
    for p, q in zip(pts, pts[1:]):
        cv.line(p[0], p[1], q[0], q[1], color)


# ---- Frame 1 (left half, x 0..23): small white arc slash ----
arc(c, 12, 26, 8, 205, 335, WHITE)
arc(c, 12, 26, 9, 205, 335, WHITE)

# ---- Frame 2 (right half, x 24..47): larger arc slash with trailing streak ----
arc(c, 34, 27, 15, 208, 332, FAINT)   # soft outer glow ring
arc(c, 34, 27, 12, 200, 345, WHITE)
arc(c, 34, 27, 13, 200, 345, WHITE)
# trailing streak tapering toward the upper-right
c.line(41, 25, 47, 20, WHITE)
c.line(44, 25, 47, 23, SOFT)
c.line(46, 25, 47, 24, FAINT)

print(c.stats_text())
print(c.matrix_text())
finish(c)
