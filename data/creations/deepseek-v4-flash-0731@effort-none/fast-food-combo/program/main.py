from pixelbench_api import *

W = 64
H = 64

c = new_canvas(W, H, name="combo")

# Palette-ish colors (hex)
# Background - transparent outside tray, warm brown table? Let's make tray with dark outline on transparent
# Define colors
BLACK = "#1a1a1a"
DARK = "#222222"
BROWN = "#8B5A2B"
DARKBROWN = "#5C3A1E"

# Tray - large rounded rectangle occupying most of bottom area
# 45-degree top-down: things look mostly top-down but arranged in perspective
# Let's draw the tray as a large rounded tray
tray_color = "#D8C9A8"
tray_dark = "#BFAF8D"
tray_edge = "#8F8162"

# Fill tray - a rounded rectangle from roughly (2,6) to (61,60)
c.rect(2, 6, 60, 55, tray_color)
# Tray edge/outline dark
# Rounded corners approximated

# Dark outline around tray
c.rect(2, 6, 60, 1, BLACK)
c.rect(2, 60, 60, 1, BLACK)
c.rect(2, 6, 1, 54, BLACK)
c.rect(61, 6, 1, 54, BLACK)

# Inside tray shading - a lip
c.rect(3, 7, 58, 1, tray_dark)
c.rect(3, 59, 58, 1, tray_dark)
c.rect(3, 7, 1, 52, tray_dark)
c.rect(60, 7, 1, 52, tray_dark)

# ---- FRIES CARTON (red) - back center-left ----
# Carton roughly at x=4..18, y=10..28 (tilted slightly for 45deg)
fry_red = "#D8322D"
fry_red_dark = "#A8221E"
fry_yellow = "#F5C518"
fry_yellow_dark = "#D4A814"
carton_white = "#F0EAE0"

# Carton body (red trapezoid)
# Draw carton as a shape with angled top (diagonal)
# Top opening
# Back edge of carton
# Let's draw carton: red rectangle from (5,14) to (18,29)
c.rect(5, 15, 14, 15, fry_red)
# Top angled
c.rect(4, 14, 16, 1, fry_red)
c.rect(4, 14, 16, 1, fry_red)

# angled top back
# The carton viewed at 45deg shows top opening
# front vertical
c.line(4, 14, 5, 15, BLACK)
c.line(19, 14, 18, 15, BLACK)
# sloping top
c.line(4, 14, 6, 11, BLACK)
c.line(19, 14, 17, 11, BLACK)
# top edge
c.line(6, 11, 17, 11, BLACK)

# fill top opening area (inside)
# Draw fries sticking out the top
for fx in range(6, 18, 2):
    for fy in range(9, 12):
        c.set(fx, fy, fry_yellow)

# red front face
c.rect(5, 15, 14, 14, fry_red)
# dark outline bottom
c.rect(5, 28, 14, 1, BLACK)
c.rect(5, 15, 1, 13, BLACK)
c.rect(18, 15, 1, 13, BLACK)

# interior opening darker
c.rect(6, 12, 11, 2, fry_red_dark)

# fries poking above
c.set(7, 10, fry_yellow)
c.set(9, 10, fry_yellow)
c.set(11, 10, fry_yellow)
c.set(13, 10, fry_yellow)
c.set(15, 10, fry_yellow)
c.set(8, 9, fry_yellow_dark)
c.set(12, 9, fry_yellow)
c.set(10, 8, fry_yellow_dark)
c.set(14, 9, fry_yellow_dark)
c.set(16, 9, fry_yellow)
c.set(9, 8, fry_yellow)
c.set(13, 8, fry_yellow)
c.set(11, 7, fry_yellow_dark)

# fries scattered down the sides (spilling)
c.set(4, 20, fry_yellow)
c.set(3, 22, fry_yellow_dark)
c.set(6, 30, fry_yellow)

# ---- CHEESEBURGER - center ----
# Burger at ~x=22..42, y=16..42, with sesame bun top
bun_top = "#E8A33D"
bun_top2 = "#D98F2F"
bun_dark = "#B5711E"
meat = "#5A3A22"
cheese = "#FFC93C"
cheese_drip = "#F5B900"
lettuce = "#4CAF50"
lettuce2 = "#3E8A41"
patty_edge = "#3D2814"

# Bottom bun (roughly square-ish with rounding), y around 34..41
c.rect(24, 35, 16, 6, bun_top)
c.rect(24, 35, 16, 1, bun_top2)
c.rect(24, 40, 16, 1, bun_dark)

# Patty - dark meat between
c.rect(23, 32, 18, 3, meat)
# patty edge darker
c.rect(23, 32, 18, 1, BLACK)
c.rect(23, 34, 18, 1, BLACK)

# Cheese - melted, dripping over patty edges
c.rect(22, 30, 20, 3, cheese)
# drips
# cheese drips hanging over sides
for dx,dy in [(22,31),(22,32),(22,33),(41,31),(41,32),(24,33),(38,33)]:
    c.set(dx,dy,cheese_drip)
# cheese melting streaks
c.set(22, 34, cheese_drip)
c.set(41, 34, cheese_drip)

# Lettuce - wavy green on top
# ruffled top edge
c.rect(22, 28, 20, 2, lettuce)
c.rect(23, 27, 18, 1, lettuce2)
# lettuce ruffle bumps
c.set(22,27,lettuce), c.set(26,27,lettuce2), c.set(31,27,lettuce), c.set(36,27,lettuce2), c.set(41,27,lettuce)

# Top bun - round domed bun with sesame seeds
# bun body
c.rect(23, 22, 18, 6, bun_top)
# dome top
c.circle(32, 23, 10, bun_top)
# but we want flattened dome
# Let's build bun dome with paths/rows
# Top dome
c.rect(24, 21, 16, 1, bun_top)
c.rect(25, 20, 14, 1, bun_top)
c.rect(26, 19, 12, 1, bun_top2)
c.rect(27, 18, 10, 1, bun_top2)
c.rect(28, 17, 8, 1, bun_top2)
c.rect(29, 16, 6, 1, bun_top2)

# bun bottom edge
c.rect(23, 28, 18, 1, bun_dark)
c.rect(23, 27, 18, 1, bun_top2)

# sesame seeds - white speckles on top
seed = "#F5EFE0"
c.set(28, 18, seed)
c.set(32, 17, seed)
c.set(36, 18, seed)
c.set(30, 20, seed)
c.set(34, 20, seed)
c.set(27, 21, seed)
c.set(37, 21, seed)
c.set(31, 19, seed)
c.set(29, 22, seed)
c.set(35, 22, seed)
c.set(33, 21, seed)

# Burger outline dark around whole shape
# We can add outlines by drawing dark pixels around key edges
# top bun outline
c.rect(28, 16, 8, 1, BLACK)
c.line(29, 15, 35, 15, BLACK)
# sides
c.line(28, 16, 27, 19, BLACK)
c.line(36, 16, 37, 19, BLACK)
c.rect(27, 19, 1, 3, BLACK)
c.rect(36, 19, 1, 3, BLACK)
c.rect(26, 20, 1, 2, BLACK)
c.rect(37, 20, 1, 2, BLACK)
c.rect(25, 21, 1, 2, BLACK)
c.rect(38, 21, 1, 2, BLACK)
c.rect(24, 22, 1, 6, BLACK)
c.rect(39, 22, 1, 6, BLACK)

# ---- COLA CUP with ice and straw - right/back ----
# Cup at ~x=44..58, y=12..34, red cup with white/blue
cup_red = "#D02A26"
cup_white = "#F2EEE6"
cup_blue = "#1E50A0"
cola = "#3A1E0A"
cola_light = "#552C10"
ice = "#BFD9E8"
ice_light = "#E8F2F8"
straw_red = "#C2302C"
straw_white = "#F5F0E0"

# Cup body - wider at top (slight cup shape)
# Top rim
c.rect(43, 12, 17, 1, cup_red)
# taper sides
c.set(43, 13, cup_red)
c.set(59, 13, cup_red)
# body straight
c.rect(44, 13, 15, 20, cup_red)
# bottom
c.rect(45, 32, 13, 1, cup_red)
c.rect(46, 33, 11, 1, cup_red)

# cup white band
c.rect(44, 18, 15, 4, cup_white)
# blue accent band
c.rect(44, 19, 15, 1, cup_blue)
c.rect(44, 21, 15, 1, cup_blue)

# cola liquid surface through opening
c.rect(44, 13, 15, 1, cola)
c.rect(44, 14, 15, 1, cola_light)

# Ice cubes on top
c.set(46, 13, ice)
c.set(50, 13, ice_light)
c.set(54, 13, ice)
c.set(48, 14, ice)
c.set(52, 14, ice_light)
c.set(56, 13, ice)

# straw sticking out diagonally
c.line(50, 26, 47, 8, straw_red)
# straw white pinstripe
c.set(48, 11, straw_white)
c.set(49, 9, straw_white)

# straw outline (thicker)
c.line(49, 27, 46, 8, BLACK)
c.line(51, 26, 48, 8, BLACK)

# cup dark outline
c.line(43, 12, 43, 33, BLACK)
c.line(59, 12, 59, 33, BLACK)
c.rect(42, 10, 19, 1, BLACK)
c.rect(45, 33, 13, 1, BLACK)
c.rect(46, 34, 11, 1, BLACK)

# ---- CHICKEN NUGGETS - front area ----
nugget = "#E8A23B"
nugget_dark = "#C8862C"
nugget_light = "#F0B85A"

# Nugget1 - in front of burger, left
# nugget shaped irregular gold pieces
def draw_nugget(x0, y0):
    # small roundish nugget
    c.rect(x0, y0, 8, 6, nugget)
    c.rect(x0, y0, 1, 2, nugget_dark)
    # dark outline
    c.rect(x0-1, y0-1, 10, 8, BLACK)
    c.rect(x0, y0, 8, 6, nugget)
    c.fill_at(x0, y0, nugget)
    c.fill_at(x0+7, y0+5, nugget)
    # highlight
    c.rect(x0+1, y0+1, 3, 1, nugget_light)
    # texture dots
    c.set(x0+4, y0+3, nugget_dark)
    c.set(x0+2, y0+4, nugget_dark)

# Nugget bottom layer
# Let's draw 5-6 nuggets scattered in front at y=36..52
# Bottom bun overlaps area; let's place nuggets around front of tray
nuggets = [(6, 36), (17, 38), (27, 46), (36, 49), (46, 42), (54, 40)]
# gaps on tray. tray extends y=6..60. Burger occupies 22..42, 15..41.
# place nuggets in front area y=44..58 and left/right around

# Recompute placements to avoid overlaps where messy
# Left front nugget near fries
draw_nugget(6, 40)
draw_nugget(16, 42)
# front center
draw_nugget(27, 46)
draw_nugget(37, 49)
draw_nugget(45, 46)
# right front
draw_nugget(52, 44)

# Also a couple behind near cup
draw_nugget(43, 36)
draw_nugget(25, 42)

# ---- SAUCE CUPS - dipping sauce ----
# small white cups with dark outline, sauce inside
sauce_cup = "#F0EAE0"
sauce_red = "#C22E24"
sauce_mustard = "#F0B522"

def draw_sauce(x0, y0, color):
    # small cup ~7x6 with sauce surface
    c.rect(x0, y0, 7, 5, color)
    c.rect(x0-1, y0-1, 9, 2, sauce_cup)
    c.rect(x0-1, y0+4, 9, 1, sauce_cup)
    c.line(x0-1, y0, x0-1, y0+5, sauce_cup)
    c.line(x0+7, y0, x0+7, y0+5, sauce_cup)
    # sauce surface highlight
    c.rect(x0+1, y0, 2, 1, color)
    # dark outline
    c.rect(x0-2, y0-2, 11, 2, BLACK)
    c.line(x0-2, y0-1, x0-2, y0+6, BLACK)
    c.line(x0+8, y0-1, x0+8, y0+6, BLACK)
    c.rect(x0-2, y0+6, 11, 1, BLACK)

draw_sauce(48, 33, sauce_red)

# ---- Extra fries scattered on tray ----
for fx,fy in [(2,52),(4,54),(6,56),(8,53),(10,55),(55,36),(57,38),(59,40),(56,44),(58,46)]:
    c.set(fx, fy, fry_yellow)
    c.set(fx+1, fy, fry_yellow_dark)

# ---- Dipping sauce next to nuggets ----
draw_sauce(14, 50, sauce_mustard)
draw_sauce(2, 45, sauce_red)

# cleanup: ensure tray covers full bottom nicely
# Put a subtle shadow under items - dark transparent blend under burger
shadow = "#00000022"
# We'll just leave darker under shapes

# Ensure everything within 64x64

result = c
finish(result)
print(c.stats_text())
print(c.matrix_text(region=(20,16,44,40)))
