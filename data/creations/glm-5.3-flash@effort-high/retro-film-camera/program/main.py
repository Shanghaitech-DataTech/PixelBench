from pixelbench_api import *

c = new_canvas(32, 32, name="retro-camera")

# palette
OUT   = c.color("#241a14", "outline")
BODY  = c.color("#5c3a26", "leather")
BODYD = c.color("#452a1a", "leather_dark")
BODYL = c.color("#7a5236", "leather_light")
METAL = c.color("#b8b2a6", "metal")
METD  = c.color("#8a8478", "metal_dark")
METL  = c.color("#ded8ca", "metal_light")
RING  = c.color("#3a3a3a", "lens_ring")
GLASS = c.color("#3f6a8c", "glass")
GLASD = c.color("#2a4a66", "glass_dark")
GLASL = c.color("#a8d0e8", "glass_light")
RED   = c.color("#c4453a", "shutter_red")
REDL  = c.color("#e07a6a", "shutter_red_light")

# ============ TOP PLATE (metal) ============
c.rect(2, 7, 28, 3, OUT)            # outline y7..9
c.rect(3, 8, 26, 2, METAL)          # metal y8..9
c.line(3, 8, 28, 8, METL)           # top highlight
c.rect(12, 8, 4, 1, METD)           # small vent slit detail
c.set(24, 9, METD)                  # screw dot

# ============ VIEWFINDER (top-left) ============
c.rect(4, 4, 7, 4, OUT)             # x4..10, y4..7
c.rect(5, 5, 5, 2, METAL)
c.rect(6, 5, 3, 2, RING)            # dark window
c.set(7, 5, GLASL)                  # glint

# ============ SHUTTER BUTTON (red) ============
c.rect(20, 4, 4, 3, OUT)            # x20..23, y4..6
c.rect(21, 5, 2, 2, RED)
c.set(21, 5, REDL)

# ============ FILM ADVANCE KNOB (top-right) ============
c.rect(25, 4, 5, 4, OUT)            # x25..29, y4..7
c.rect(26, 5, 3, 2, METD)
c.line(26, 5, 28, 5, METL)

# ============ BODY (leather) ============
c.rect(1, 10, 30, 15, OUT)          # x1..30, y10..24
c.rect(2, 11, 28, 13, BODY)         # leather y11..23
c.line(2, 11, 29, 11, BODYL)        # top light edge
c.line(2, 23, 29, 23, BODYD)        # bottom shade

# strap lugs
c.rect(0, 11, 1, 2, METD)
c.rect(31, 11, 1, 2, METD)
c.rect(0, 10, 1, 1, OUT)
c.rect(31, 10, 1, 1, OUT)
c.rect(0, 13, 1, 1, OUT)
c.rect(31, 13, 1, 1, OUT)

# ============ LENS ============
cx, cy = 16, 19
c.circle(cx, cy, 7, OUT)            # outer edge (protrudes below body)
c.circle(cx, cy, 6, METD)           # metal ring
c.circle(cx, cy, 5, RING)           # barrel
c.circle(cx, cy, 4, GLASS)          # glass
c.circle(cx + 1, cy + 1, 2, GLASD)  # depth shading
c.set(14, 17, GLASL); c.set(13, 18, GLASL); c.set(14, 18, GLASL)  # glint

# ============ LEATHER TEXTURE (speckles) ============
dark_spots = [(3,13),(5,12),(7,14),(4,16),(6,18),(3,19),(5,21),(7,22),(4,22),
              (8,12),(8,16),(8,20),(25,12),(27,13),(29,12),(26,15),(28,16),
              (24,13),(25,18),(27,19),(29,17),(26,21),(28,22),(24,22),(29,21),
              (11,12),(21,12),(13,11),(19,11),(10,22),(22,22),(12,23),(20,23)]
light_spots = [(4,14),(6,13),(5,15),(7,12),(3,17),(6,20),(8,18),(4,20),
               (26,13),(28,14),(25,16),(27,12),(29,19),(24,20),(26,23),(28,20),
               (10,12),(22,12),(12,11),(18,11),(11,23),(21,23)]
for (x, y) in dark_spots:
    if c.get(x, y) == BODY:
        c.set(x, y, BODYD)
for (x, y) in light_spots:
    if c.get(x, y) == BODY:
        c.set(x, y, BODYL)

print(c.stats_text())
print(c.matrix_text())

save("retro-film-camera", c)
finish(c)

