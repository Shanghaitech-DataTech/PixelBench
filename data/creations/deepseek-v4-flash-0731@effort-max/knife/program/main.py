from pixelbench_api import *

c = input_canvas
w, h = c.stats()["size"]

# Re-pose the knife: rotate so it thrusts horizontally to the right,
# cutting edge facing downward (tip at right, handle at left).
rot = c.select(0, 0, w, h).rotate(124.5, algorithm="rotsprite").preview()
rw, rh = rot.stats()["size"]

W, H = 326, 130
out = new_canvas(W, H)

def ghost_canvas(color):
    g = new_canvas(rw, rh)
    for y in range(rh):
        for x in range(rw):
            if rot.get(x, y) != 0:
                g.set(x, y, color)
    return g

# Semi-transparent afterimages trailing left; the older ones are fainter and
# sit slightly higher along the back-swing arc.
ghosts = [
    (8, -18, (44, 58, 100, 56)),
    (62, -10, (58, 74, 118, 92)),
    (114, -4, (78, 96, 154, 134)),
]
for gx, gy, col in ghosts:
    out.blit(ghost_canvas(col), gx, gy)

white = (255, 255, 255, 255)
softglow = (255, 255, 255, 95)
soft = (255, 255, 255, 150)

# White slash: wide soft glow, bright core band, and fine accent strokes.
out.path("M 26 114 Q 160 80 322 68 Q 160 102 40 122 Z", softglow)
out.path("M 48 105 Q 172 68 322 60 Q 172 84 52 110 Z", white)
out.path("M 34 108 Q 160 63 324 56", soft, fill=False)
out.path("M 150 122 Q 240 108 302 76", soft, fill=False)

# The actual knife (opaque) on top.
out.blit(rot, 158, -12)

# Small white sparks at the thrust tip.
sparks = [(316, 58), (311, 49), (308, 66), (300, 44), (306, 74), (318, 63), (303, 78)]
for sx, sy in sparks:
    out.set(sx, sy, white)

print(out.stats_text())
finish(out)
