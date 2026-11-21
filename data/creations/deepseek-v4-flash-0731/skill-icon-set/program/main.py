from pixelbench_api import new_canvas, finish
import math

OUTLINE = "#1c2430"

def quad_line(c, x0, y0, x1, y1, colour, w):
    """Draw a thick segment as a filled quad; w is half width."""
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy)
    if L == 0:
        c.circle(x0, y0, w, colour)
        return
    ux = round(-dy / L * w)
    uy = round(dx / L * w)
    c.poly([(x0 + ux, y0 + uy), (x1 + ux, y1 + uy),
            (x1 - ux, y1 - uy), (x0 - ux, y0 - uy)], colour)

c = new_canvas(64, 64)

# ---------------- Fireball (0,0) ----------------
ox, oy = 0, 0
cx, cy = 16, 15
# flame cap
c.poly([(cx - 7, oy + 6), (cx + 7, oy + 6), (cx, oy)], OUTLINE)
c.poly([(cx - 5, oy + 6), (cx + 5, oy + 6), (cx, oy + 2)], "#e64545")
c.poly([(cx - 3, oy + 6), (cx + 3, oy + 6), (cx, oy + 3)], "#f28c28")
# fireball body
c.circle(cx, cy, 12, OUTLINE)
c.circle(cx, cy - 1, 10, "#e64545")
c.circle(cx, cy - 1, 7, "#f28c28")
c.circle(cx, cy - 1, 4, "#ffd23f")
c.circle(cx, cy - 1, 2, "#fff3b0")

# ---------------- Ice Shield (32,0) ----------------
ox, oy = 32, 0
outer = [(ox + 5, oy + 3), (ox + 26, oy + 3), (ox + 26, oy + 10),
         (ox + 21, oy + 20), (ox + 16, oy + 27), (ox + 11, oy + 20), (ox + 5, oy + 10)]
inner = [(ox + 8, oy + 6), (ox + 23, oy + 6), (ox + 23, oy + 11),
         (ox + 20, oy + 18), (ox + 16, oy + 23), (ox + 12, oy + 18), (ox + 8, oy + 11)]
shade = [(ox + 12, oy + 19), (ox + 20, oy + 19), (ox + 16, oy + 23)]
c.poly(outer, OUTLINE)
c.poly(inner, "#4aa8ff")
c.poly(shade, "#2b6cb0")
c.poly([(ox + 16, oy + 11), (ox + 20, oy + 15), (ox + 16, oy + 19), (ox + 12, oy + 15)], "#9adcff")
c.poly([(ox + 16, oy + 13), (ox + 18, oy + 15), (ox + 16, oy + 17), (ox + 14, oy + 15)], "#eaffff")

# ---------------- Healing (0,32) ----------------
ox, oy = 0, 32
c.rect(ox + 11, oy + 3, 10, 26, OUTLINE)
c.rect(ox + 3, oy + 11, 26, 10, OUTLINE)
c.circle(ox + 16, oy + 8, 5, OUTLINE)
c.circle(ox + 16, oy + 24, 5, OUTLINE)
c.circle(ox + 8, oy + 16, 5, OUTLINE)
c.circle(ox + 24, oy + 16, 5, OUTLINE)
c.rect(ox + 13, oy + 5, 6, 22, "#39c15b")
c.rect(ox + 5, oy + 13, 22, 6, "#39c15b")
c.circle(ox + 16, oy + 8, 3, "#39c15b")
c.circle(ox + 16, oy + 24, 3, "#39c15b")
c.circle(ox + 8, oy + 16, 3, "#39c15b")
c.circle(ox + 24, oy + 16, 3, "#39c15b")
# shading
c.circle(ox + 23, oy + 16, 2, "#1e7a3a")
c.circle(ox + 16, oy + 23, 2, "#1e7a3a")
# highlights
c.circle(ox + 10, oy + 16, 1, "#7ce38b")
c.circle(ox + 16, oy + 10, 1, "#7ce38b")
c.circle(ox + 16, oy + 16, 2, "#eaffea")

# ---------------- Lightning (32,32) ----------------
ox, oy = 32, 32
# ---------------- Lightning (32,32) ----------------
ox, oy = 32, 32
bolt_pts = [(12, 3), (8, 14), (19, 14), (13, 27)]
bolt_segs = [(bolt_pts[0], bolt_pts[1]), (bolt_pts[1], bolt_pts[2]), (bolt_pts[2], bolt_pts[3])]
# outline pass
for (a, b) in bolt_segs:
    quad_line(c, ox + a[0], oy + a[1], ox + b[0], oy + b[1], OUTLINE, 1.6)
# fill pass
for (a, b) in bolt_segs:
    quad_line(c, ox + a[0], oy + a[1], ox + b[0], oy + b[1], "#f5b700", 0.8)
# highlights
c.line(ox + bolt_pts[0][0], oy + bolt_pts[0][1], ox + bolt_pts[1][0], oy + bolt_pts[1][1], "#ffd83d")
c.line(ox + bolt_pts[2][0], oy + bolt_pts[2][1], ox + bolt_pts[3][0], oy + bolt_pts[3][1], "#ffd83d")
c.circle(ox + 10, oy + 8, 1, "#fff8c4")

print(c.stats_text())
finish(c)
