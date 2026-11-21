from pixelbench_api import *

c = new_canvas(64, 64, name="void-eye")

# soft shadow (semi-transparent dark)
c.ellipse(32, 60, 14, 3, "#1a0a2e55", fill=True)

# tentacles (short, below body)
tent = "#5b2a86"
dark_t = "#3d1c5c"
def tentacle(x0, y0, pts, col):
    for i in range(len(pts)-1):
        c.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], col)

# body sphere: fleshy purple-magenta
body = "#7a3b9e"
body_hi = "#a86bc4"
body_dk = "#4a2266"
edge = "#2b1240"

c.circle(32, 30, 22, edge, fill=True)
c.circle(32, 30, 21, body, fill=True)
# shading: darker lower-right crescent
c.ellipse(36, 36, 17, 14, body_dk, fill=True)
c.circle(32, 30, 21, body, fill=True)
c.ellipse(36, 36, 15, 12, body_dk, fill=True)
# re-lighten upper-left
c.ellipse(28, 26, 17, 15, body, fill=True)
c.ellipse(25, 23, 11, 9, body_hi, fill=True)

# eye socket / sclera
c.circle(32, 30, 15, "#1c0b2e", fill=True)
c.circle(32, 30, 14, "#e8e2f2", fill=True)
c.ellipse(28, 26, 8, 6, "#ffffff", fill=True)

# iris: deep purple
c.circle(32, 31, 9, "#2a0a4a", fill=True)
c.circle(32, 31, 8, "#4b1a7a", fill=True)
c.circle(32, 31, 6, "#6d2aa8", fill=True)
# radial iris streaks
import math
for a in range(0, 360, 30):
    x0 = 32 + int(3*math.cos(math.radians(a)))
    y0 = 31 + int(3*math.sin(math.radians(a)))
    x1 = 32 + int(7*math.cos(math.radians(a)))
    y1 = 31 + int(7*math.sin(math.radians(a)))
    c.line(x0, y0, x1, y1, "#8a3ec4")

# pupil: dark with glow
c.circle(32, 31, 3, "#0d0217", fill=True)
c.set(32, 31, "#b26bff")   # faint glow core
c.set(31, 30, "#7a3ec4")
c.set(33, 32, "#7a3ec4")

# highlight on iris
c.set(28, 27, "#ffffff")
c.set(29, 27, "#ffffff")

# tentacles
tentacle(0,0, [(18,48),(15,52),(14,56),(15,59)], tent)
tentacle(0,0, [(19,49),(17,53),(16,56)], dark_t)
tentacle(0,0, [(26,51),(25,55),(24,58),(26,60)], tent)
tentacle(0,0, [(38,51),(39,55),(40,58),(38,60)], tent)
tentacle(0,0, [(46,48),(49,52),(50,56),(49,59)], tent)
tentacle(0,0, [(45,49),(47,53),(48,56)], dark_t)
tentacle(0,0, [(32,52),(32,56),(31,60)], dark_t)

# small spikes/bumps on top of body for menace
c.set(20, 12, edge); c.set(21, 11, edge)
c.set(32, 8, edge); c.set(31, 8, edge)
c.set(44, 12, edge); c.set(43, 11, edge)

print(c.stats_text())
save("void-eye", c)
finish(c)
