from pixelbench_api import *

c = new_canvas(64, 32, name="bus")

# Palette
body      = "#3AA0E0"
body_dark = "#1E6CB0"
body_light= "#7EC8F0"
roof      = "#D8E2EA"
glass     = "#BFE3F8"
glass_dark= "#7FAFCB"
door      = "#5B93C0"
white     = "#FFFFFF"
headlight = "#FFF3B0"
taillight = "#E03A3A"
black     = "#0E1418"
led       = "#FFE24A"
tire      = "#2A2E34"
wheelcap  = "#C8CCD2"
bumper   = "#E8ECEF"
chassis   = "#1A2026"
glow      = "#4E6072"
hood      = "#2C8BC8"   # darker accent shade

# ===== BODY =====
# Main body box, x=2..61
c.rect(2, 8, 60, 15, body)     # y=8..22
c.rect(2, 8, 60, 1, body_light)# roof highlight top
# Underglow
c.rect(2, 21, 60, 2, glow)     # y=21..22
# Chassis dark
c.rect(2, 23, 60, 2, chassis)  # y=23..24
c.rect(2, 25, 60, 1, black)    # bottom line

# ===== ROUTE DISPLAY (electronic LED sign, roof front) =====
c.rect(43, 5, 19, 3, black)    # bezel y=5..7
# LED digit "1" (lit)
c.rect(46, 5, 2, 3, led)
# LED digit "0" (lit ring, hollow center)
c.rect(53, 5, 6, 3, led)
c.rect(55, 6, 2, 1, black)     # dark hollow center of 0

# ===== WINDSHIELD (front, right side) =====
c.rect(50, 11, 9, 6, glass)    # x=50..58, y=11..16
c.rect(50, 11, 9, 1, glass_dark)
# windshield pillar
c.rect(53, 11, 2, 6, body)
# windshield frame bottom
c.rect(50, 17, 9, 1, body_dark)

# ===== SIDE WINDOW BAND =====
# continuous glass band
c.rect(5, 11, 44, 6, glass)    # x=5..48, y=11..16
c.rect(5, 11, 44, 1, glass_dark)
# pillars
for px in (11, 19, 27, 35, 43):
    c.rect(px, 11, 2, 6, body)
# rear window separate right before left bumper
c.rect(5, 11, 5, 6, glass)
c.rect(5, 11, 5, 1, glass_dark)

# ===== DOORS =====
# Rear door x=15..22, Front door x=39..46
c.rect(15, 11, 8, 10, door)    # y=11..20 both doors region handled
c.rect(39, 11, 8, 10, door)
# door panel lower part darker indicated by black seam line
# re-draw door with window on top area and panel below
c.rect(15, 11, 8, 4, glass)
c.rect(15, 11, 8, 1, glass_dark)
c.rect(39, 11, 8, 4, glass)
c.rect(39, 11, 8, 1, glass_dark)
# door seams (black stiles splitting each door)
c.rect(19, 11, 1, 10, black)
c.rect(43, 11, 1, 10, black)

# ===== ACCENT STRIPE =====
c.rect(2, 19, 60, 1, white)

# ===== BUMPERS =====
c.rect(58, 15, 4, 8, bumper)
c.rect(57, 15, 1, 8, body_dark)
c.rect(2, 15, 3, 8, bumper)
c.rect(5, 15, 1, 6, body_dark)

# ===== HEADLIGHTS (front right) =====
c.rect(59, 17, 4, 2, bumper)     # housing
c.rect(60, 17, 2, 2, headlight)
c.rect(60, 17, 2, 1, white)

# ===== TAIL LIGHTS (rear left) =====
c.rect(2, 17, 3, 2, taillight)

# ===== WINDOW VISOR shade under roof above each door/window? skip =====

# ===== WHEELS with arches =====
# wheel arches (dark cut)
c.circle(14, 25, 6, black)
c.circle(51, 25, 6, black)
# rear wheel
c.circle(14, 25, 5, tire)
c.circle(14, 25, 3, chassis)
c.circle(14, 25, 2, wheelcap)
c.circle(14, 25, 1, chassis)
# front wheel
c.circle(51, 25, 5, tire)
c.circle(51, 25, 3, chassis)
c.circle(51, 25, 2, wheelcap)
c.circle(51, 25, 1, chassis)

print(c.stats_text())

finish(c)
