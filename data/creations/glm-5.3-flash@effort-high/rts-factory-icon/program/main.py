from pixelbench_api import *

c = new_canvas(32, 32, name="factory")

# ---- palette ----
BRICK    = c.color("#a8502e", "brick")
BRICK_D  = c.color("#7c3520", "brick_dark")
BRICK_L  = c.color("#c4744a", "brick_light")
ROOF     = c.color("#6e737b", "roof")
ROOF_D   = c.color("#4c5058", "roof_dark")
ROOF_L   = c.color("#8d939c", "roof_light")
VENT     = c.color("#9aa1aa", "vent")
CHIM     = c.color("#5a5e66", "chimney")
CHIM_D   = c.color("#3c3f46", "chimney_dark")
WIN      = c.color("#ffd977", "window_glow")
WIN_D    = c.color("#c79a3a", "window_frame")
DOOR     = c.color("#3a2a22", "door")
BASE     = c.color("#5c4a42", "base")
SMOKE    = c.color("#cfd4da", "smoke")

# ---- chimney (left, tall) ----
c.rect(6, 3, 5, 8, CHIM)          # shaft
c.rect(6, 3, 5, 1, CHIM_D)        # dark rim top
c.set(6, 3, CHIM_D); c.set(10, 3, CHIM_D)
c.rect(5, 10, 7, 2, CHIM_D)       # cap flange
c.rect(5, 10, 7, 1, CHIM)         # cap top
c.rect(7, 5, 1, 4, CHIM_D)        # shading stripe
c.rect(6, 4, 1, 4, BRICK_L)       # highlight

# ---- smoke puffs ----
c.set(11, 1, SMOKE); c.set(12, 0, SMOKE)
c.set(13, 2, SMOKE); c.set(14, 1, SMOKE)
c.set(10, 2, SMOKE); c.set(12, 3, SMOKE)

# ---- flat roof slab ----
c.rect(3, 12, 26, 3, ROOF)
c.rect(3, 12, 26, 1, ROOF_L)      # top edge highlight
c.rect(3, 14, 26, 1, ROOF_D)      # underside shadow

# ---- vents on roof ----
for vx in (8, 15, 22):
    c.rect(vx, 9, 3, 3, VENT)
    c.rect(vx, 9, 3, 1, ROOF_L)
    c.rect(vx, 11, 3, 1, ROOF_D)
    c.set(vx, 10, ROOF_D)

# ---- walls (brick) ----
c.rect(4, 15, 24, 13, BRICK)
c.rect(4, 15, 24, 1, BRICK_L)     # wall top highlight
c.rect(4, 26, 24, 2, BRICK_D)     # lower shading
c.rect(4, 27, 24, 1, BRICK_D)     # bottom row

# brick mortar lines (offset rows)
for yy in (17, 20, 23):
    c.line(4, yy, 27, yy, BRICK_D)
# vertical joints, staggered
for yy, xs in ((16, (8, 14, 20, 26)), (17, (6, 11, 17, 23)),
               (18, (8, 14, 20, 26)), (19, (6, 11, 17, 23)),
               (21, (8, 14, 20, 26)), (22, (6, 11, 17, 23)),
               (24, (8, 14, 20, 26)), (25, (6, 11, 17, 23))):
    for xx in xs:
        c.set(xx, yy, BRICK_D)

# ---- windows ----
for wx in (7, 22):
    c.rect(wx, 18, 4, 4, WIN_D)
    c.rect(wx+1, 19, 2, 2, WIN)
    c.set(wx+1, 19, WIN)

# ---- door ----
c.rect(14, 20, 4, 7, DOOR)
c.rect(14, 20, 4, 1, BRICK_D)
c.set(16, 23, WIN)                # door handle

# ---- foundation ----
c.rect(3, 28, 26, 2, BASE)
c.rect(3, 29, 26, 1, ROOF_D)

print(c.stats_text())
print(c.matrix_text())

view(c, scale=8)
finish(c)
