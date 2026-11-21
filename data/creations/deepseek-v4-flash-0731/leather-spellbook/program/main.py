from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="spellbook")

outline       = c.color("#1b110a")   # dark outline
leather_dark  = c.color("#43240f")   # deep leather / spine
leather       = c.color("#7c4523")   # main leather cover
leather_light = c.color("#aa6630")   # leather sheen
metal_dark    = c.color("#7c5c14")   # brass shadow
metal         = c.color("#c9a22a")   # brass
metal_light   = c.color("#f2d576")   # brass shine
page          = c.color("#e3d5b5")   # page edges

# ---- dark silhouette / outline ring ----
c.rect(4, 5, 25, 22, outline)
# rounded outer corners (2 px steps)
c.clear(4, 5, 2, 1)
c.clear(27, 5, 2, 1)
c.clear(4, 6, 1, 1)
c.clear(28, 6, 1, 1)
c.clear(4, 25, 1, 1)
c.clear(28, 25, 1, 1)
c.clear(4, 26, 2, 1)
c.clear(27, 26, 2, 1)

# ---- spine (left panel, ribbed) ----
c.rect(5, 6, 4, 20, leather_dark)
c.line(6, 7, 6, 24, leather)
c.line(7, 7, 7, 24, leather_light)
c.rect(5, 10, 4, 1, leather)     # raised rib band
c.rect(5, 21, 4, 1, leather)     # raised rib band

# ---- cover ----
c.rect(9, 6, 16, 20, leather)
c.rect(9, 6, 16, 3, leather_light)   # sheen along top
c.line(9, 9, 24, 9, leather)         # sheen bottom edge
c.line(9, 6, 9, 25, outline)         # seam: spine / cover
c.line(24, 6, 24, 25, outline)       # seam: cover / pages

# ---- page edges (right side) ----
c.rect(25, 6, 3, 20, page)
c.line(25, 12, 27, 12, leather_dark)
c.line(25, 18, 27, 18, leather_dark)

# ---- tooled frame on the cover ----
c.rect(12, 9, 9, 13, leather_dark)
c.set(11, 13, leather_dark)

# ---- brass corner brackets ----
# TL
c.rect(9, 6, 4, 4, metal)
c.clear(11, 8, 2, 2)
c.set(9, 6, metal_light)
c.set(12, 7, metal_dark)
# TR
c.rect(21, 6, 4, 4, metal)
c.clear(21, 8, 2, 2)
c.set(24, 6, metal_light)
c.set(21, 7, metal_dark)
# BL
c.rect(9, 22, 4, 4, metal)
c.clear(11, 22, 2, 2)
c.set(9, 25, metal_light)
c.set(10, 22, metal_dark)
# BR
c.rect(21, 22, 4, 4, metal)
c.clear(21, 22, 2, 2)
c.set(24, 25, metal_light)
c.set(23, 22, metal_dark)

# ---- brass emblem in the centre ----
c.poly([(16, 12), (19, 15), (16, 18), (13, 15)], metal)
c.poly([(16, 13), (18, 15), (16, 17), (14, 15)], metal_light)
c.set(16, 11, metal_light)

print(c.stats_text())
print(c.matrix_text())

finish(c)
