out = input_canvas.copy(name='output')

# ---- palette ----
VINE_DARK  = '#1c3a24'
VINE_MID   = '#2e5c33'
VINE_LIGHT = '#4c8142'
CLOAK_MID  = '#262b36'
CLOAK_DARK = '#171b24'
CLOAK_LIGHT= '#3d4557'
BOOT       = '#12141a'
STAFF      = '#5c4326'

# ================= VINES on the tower walls =================
def leaf(x, y, side):
    out.set(x, y, VINE_LIGHT)
    if side == 'L':
        out.set(x - 1, y + 1, VINE_MID); out.set(x, y + 1, VINE_MID)
    else:
        out.set(x + 1, y + 1, VINE_MID); out.set(x, y + 1, VINE_MID)

# left climbing vine
lp = [(46,216),(45,208),(46,200),(44,192),(45,184),(43,176),(44,168),(42,160),(43,152),(44,146)]
for i in range(len(lp) - 1):
    (x0, y0), (x1, y1) = lp[i], lp[i + 1]
    out.line(x0, y0, x1, y1, VINE_DARK)
for i, (x, y) in enumerate(lp[:-1]):
    if i % 2 == 0:
        out.set(x - 1, y, VINE_LIGHT)
for (x, y, s) in [(44,212,'L'),(47,204,'R'),(42,196,'L'),(46,188,'R'),(41,180,'L'),
                  (45,172,'R'),(42,164,'L'),(44,156,'R'),(41,148,'L')]:
    leaf(x, y, s)

# right climbing vine
rp = [(88,216),(89,208),(88,200),(90,192),(89,184),(91,176),(90,168),(92,160),(91,152),(90,146)]
for i in range(len(rp) - 1):
    (x0, y0), (x1, y1) = rp[i], rp[i + 1]
    out.line(x0, y0, x1, y1, VINE_DARK)
for i, (x, y) in enumerate(rp[:-1]):
    if i % 2 == 0:
        out.set(x + 1, y, VINE_LIGHT)
for (x, y, s) in [(86,212,'L'),(90,204,'R'),(85,196,'L'),(92,188,'R'),(86,180,'L'),
                  (93,172,'R'),(87,164,'L'),(92,156,'R'),(94,148,'R')]:
    leaf(x, y, s)

# ivy patch on the wall left of the entrance
ivy = [(40,132),(42,130),(44,133),(41,136),(43,138),(45,135),(47,139),(40,127),(43,126),
       (46,129),(48,133),(45,142),(42,141),(47,145),(49,141),(44,147),(48,149),(41,146),
       (50,137),(46,124)]
for i, (x, y) in enumerate(ivy):
    out.set(x, y, VINE_MID if i % 2 else VINE_LIGHT)
    if i % 3 == 0:
        out.set(x, y + 1, VINE_DARK)

# small hanging tufts under the arch ledge
for (x, y0, y1) in [(57,150,158),(69,151,157),(63,149,154)]:
    for y in range(y0, y1 + 1):
        dx = 1 if (y - y0) % 3 == 2 else 0
        out.set(x + dx, y, VINE_DARK if (y - y0) % 2 else VINE_MID)
    out.set(x, y0, VINE_LIGHT)

# ================= MAGE (back view, walking into the tower) =================
mx = 68  # centre of body

# soft glow pool on the ground from the staff (drawn under the figure)
out.ellipse(76, 219, 6, 2, '#8fd45e3d')
# faint glow spill on the archway wall behind him
for (x, y) in [(59,206),(58,212),(61,202),(80,203),(81,209)]:
    out.set(x, y, '#7fc85a30')

# cloak body: flared trapezoid, hem at y=216
for y in range(200, 217):
    t = (y - 200) / 16.0
    half = 4 + int(round(t * 3))
    out.rect(mx - half, y, half * 2 + 1, 1, CLOAK_MID)
    out.set(mx - half, y, CLOAK_DARK)                       # shadow side
    if y <= 210:
        out.set(mx + half, y, CLOAK_LIGHT)                  # staff-glow side
    else:
        out.set(mx + half, y, CLOAK_MID)

# hood (head seen from behind)
out.ellipse(mx, 196, 4, 5, CLOAK_MID)                       # rows 191-201
out.set(mx, 190, CLOAK_MID)                                 # hood peak
out.set(71, 194, CLOAK_LIGHT); out.set(72, 196, CLOAK_LIGHT); out.set(71, 198, CLOAK_LIGHT)
out.set(65, 194, CLOAK_DARK);  out.set(64, 196, CLOAK_DARK);  out.set(65, 198, CLOAK_DARK)

# cloak back seam + hem shadow
out.line(mx, 203, mx, 214, CLOAK_DARK)
for x in range(mx - 7, mx + 8):
    out.set(x, 216, CLOAK_DARK)

# boots (right foot forward, mid-stride)
out.rect(64, 217, 3, 2, BOOT)
out.rect(70, 216, 3, 2, BOOT)

# staff held in his right hand, planted as he walks
out.rect(76, 192, 1, 27, STAFF)
out.rect(74, 205, 2, 2, CLOAK_MID)                          # sleeve reaching the staff

# glowing orb at the staff head + halo
for (x, y) in [(73,190),(79,190),(76,187),(76,193),(74,188),(78,188),(74,192),(78,192)]:
    out.set(x, y, '#8fd45e55')
for (x, y) in [(75,189),(77,189),(75,191),(77,191),(74,190),(78,190),(76,188),(76,192)]:
    out.set(x, y, '#b7e56f88')
for (x, y) in [(76,190),(75,190),(77,190),(76,189),(76,191)]:
    out.set(x, y, '#f4ffd6')
out.set(76, 190, '#ffffff')

print(out.stats_text())
view(out, size=256, margin=0)
finish(out)
