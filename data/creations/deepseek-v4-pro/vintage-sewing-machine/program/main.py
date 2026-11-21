from pixelbench_api import *

c = new_canvas(48, 48, name="vintage-sewing-machine")

# ---- palette ---------------------------------------------------------------
body        = c.color('#1b1b20', 'body')
body_hi     = c.color('#3d3d45', 'body_hi')
body_lo     = c.color('#0a0a0d', 'body_lo')
gold        = c.color('#d4a017', 'gold')
gold_hi     = c.color('#eac34a', 'gold_hi')
metal       = c.color('#9aa1ab', 'metal')
metal_dark  = c.color('#565c66', 'metal_dark')
metal_light = c.color('#e2e5e8', 'metal_light')
wood        = c.color('#7a4a22', 'wood')
wood_dark   = c.color('#4c2e14', 'wood_dark')
wood_light  = c.color('#a86a34', 'wood_light')
fabric      = c.color('#c0392b', 'fabric')
fabric_dark = c.color('#8b2318', 'fabric_dark')
fabric_light= c.color('#e8644f', 'fabric_light')
thread      = c.color('#f2ecdb', 'thread')

# ---- base (slightly angled: lighter top plane + darker front face) ---------
c.rect(2, 34, 44, 4, wood_light, fill=True)          # top surface y34..37
c.rect(2, 38, 44, 7, wood, fill=True)                # front face y38..44
c.line(2, 38, 45, 38, wood_light)                    # top edge highlight
c.line(2, 44, 45, 44, wood_dark)                     # bottom edge
# little feet
c.rect(4, 44, 6, 2, wood_dark, fill=True)
c.rect(38, 44, 6, 2, wood_dark, fill=True)
# wood grain
for gx in (9, 16, 24, 31, 40):
    c.line(gx, 39, gx, 43, wood_dark)

# metal bed / needle plate on top of base
c.rect(6, 31, 20, 4, metal, fill=True)               # y31..34
c.line(6, 31, 25, 31, metal_light)

# ---- red fabric under the presser foot -------------------------------------
c.poly([
    (5, 31), (8, 28), (12, 30), (15, 27), (19, 29),
    (23, 31), (25, 33), (22, 35), (15, 34), (7, 35)
], fabric, fill=True)
# red cloth draping over the base edge (right side)
c.poly([(19, 34), (24, 34), (26, 40), (22, 41), (17, 40), (16, 36)], fabric, fill=True)
# folds / shading
c.line(11, 29, 10, 34, fabric_dark)
c.line(15, 28, 15, 34, fabric_dark)
c.line(19, 30, 19, 34, fabric_dark)
c.line(8, 28, 8, 33, fabric_light)
c.line(23, 31, 23, 34, fabric_light)
c.line(21, 35, 21, 40, fabric_dark)
c.line(18, 35, 18, 39, fabric_light)

# ---- machine body (head + arm + pillar) ------------------------------------
c.rect(9, 10, 11, 15, body, fill=True)               # head  x9..19  y10..24
c.rect(17, 10, 20, 8, body, fill=True)               # arm   x17..36 y10..17
c.rect(32, 14, 5, 22, body, fill=True)               # pillar x32..36 y14..35

# body shading for a slightly angled, dimensional read
c.line(9, 10, 36, 10, body_hi)                       # top edge
c.line(9, 10, 9, 24, body_hi)                        # front edge of head
c.line(17, 17, 31, 17, body_lo)                      # under-arm shadow
c.line(32, 14, 32, 35, body_hi)                      # pillar front edge
c.line(36, 14, 36, 35, body_lo)                      # pillar back edge

# gold decoration
c.rect(18, 12, 18, 2, gold, fill=True)               # arm band
c.line(10, 15, 17, 15, gold)
c.line(10, 18, 17, 18, gold)
c.line(34, 18, 34, 22, gold)                         # pillar medallion
c.line(32, 20, 36, 20, gold)
c.set(34, 20, gold_hi)

# small tension dial on the head
c.circle(11, 13, 1, metal, fill=True)
c.set(11, 13, metal_dark)

# ---- needle bar + presser foot --------------------------------------------
c.rect(12, 24, 2, 10, metal_dark, fill=True)         # needle bar y24..33
c.line(12, 33, 12, 35, metal_light)                  # needle point
c.rect(11, 23, 3, 3, metal_dark, fill=True)          # needle clamp
c.rect(15, 25, 2, 5, metal, fill=True)               # presser foot shaft
c.rect(13, 29, 6, 2, metal, fill=True)               # presser foot
c.line(13, 29, 18, 29, metal_light)
c.line(13, 31, 18, 31, fabric_dark)                  # foot pressing into cloth

# ---- handwheel -------------------------------------------------------------
c.circle(38, 20, 7, body_lo, fill=True)       # dark outer rim
c.circle(38, 20, 6, metal_light, fill=True)   # bright rim
c.circle(38, 20, 4, metal_dark, fill=True)    # recessed face
c.line(38, 16, 38, 24, metal_light)           # spokes
c.line(34, 20, 42, 20, metal_light)
c.line(35, 17, 41, 23, metal_light)
c.line(35, 23, 41, 17, metal_light)
c.circle(38, 20, 1, metal, fill=True)         # hub
c.set(38, 20, metal_dark)

# ---- thread spool and thread ----------------------------------------------
c.line(26, 3, 26, 9, metal)                          # spool pin
c.rect(23, 4, 7, 1, wood_light, fill=True)
c.rect(23, 9, 7, 1, wood_light, fill=True)
c.rect(24, 5, 5, 4, thread, fill=True)
# thread path: spool -> tension area -> needle bar
c.line(26, 10, 26, 12, thread)
c.line(26, 12, 13, 20, thread)
c.line(13, 20, 13, 24, thread)

print(c.stats_text())
finish(c)
