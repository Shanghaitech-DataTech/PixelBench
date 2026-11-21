from pixelbench_api import *

c = new_canvas(48, 48, name="result")

METAL_D = "#7a7f8a"   # dark metal
METAL   = "#b8bec9"   # mid metal
METAL_L = "#e2e6ec"   # light metal
BLACK   = "#2b2f36"
RED     = "#c23b2e"
RED_D   = "#8f2419"
WOOD    = "#6b4a2f"
GOLD    = "#d9a441"

# ---- base (wood table) ----
c.rect(4, 42, 40, 4, WOOD)
c.rect(4, 42, 40, 1, "#8a6440")

# ---- machine base plate ----
c.rect(8, 38, 34, 4, METAL_D)
c.rect(8, 38, 34, 1, METAL)

# ---- body pillar (angled side view: body rises to the right) ----
# main arm
c.rect(14, 12, 26, 6, METAL)          # horizontal arm top area
c.rect(14, 18, 26, 4, METAL_D)        # underside of arm
# vertical column at right
c.rect(34, 12, 8, 26, METAL)
c.rect(40, 12, 2, 26, METAL_D)
c.rect(34, 12, 8, 2, METAL_L)
# column base
c.rect(32, 36, 12, 3, METAL_D)

# ---- head / left end of arm ----
c.rect(10, 10, 6, 12, METAL)
c.rect(10, 10, 6, 2, METAL_L)
c.rect(10, 20, 6, 2, METAL_D)

# ---- handwheel (slightly angled -> ellipse) on left of head ----
c.ellipse(9, 16, 5, 6, METAL_D)
c.ellipse(9, 16, 3, 4, BLACK)
c.ellipse(9, 16, 1, 2, METAL_L)
# wheel spokes hint
c.set(9, 11, METAL); c.set(9, 21, METAL)

# ---- stitch length dial on arm ----
c.circle(24, 15, 2, GOLD)

# ---- needle bar + needle ----
c.rect(19, 22, 2, 5, METAL_L)   # needle bar
c.set(19, 27, METAL_L); c.set(19, 28, METAL_L); c.set(19, 29, METAL_L)  # needle
# presser foot bar
c.rect(23, 22, 2, 4, METAL)
# presser foot
c.rect(21, 26, 5, 2, METAL_D)

# ---- needle plate / throat area ----
c.rect(16, 32, 12, 2, BLACK)

# ---- red fabric under the needle ----
c.rect(12, 34, 20, 4, RED)
c.rect(12, 34, 20, 1, "#e0604f")
c.rect(12, 37, 20, 1, RED_D)
# stitch line
for x in range(14, 32, 2):
    c.set(x, 35, RED_D)

# ---- feed dog / bobbin hint ----
c.rect(18, 30, 4, 2, METAL_D)

# ---- highlights / outline for readability ----
c.rect(14, 12, 26, 1, METAL_L)

print(c.stats_text())
save("sewing_machine", c)
finish(c)
