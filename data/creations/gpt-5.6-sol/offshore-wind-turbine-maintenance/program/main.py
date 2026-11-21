from pixelbench_api import *

# Offshore wind maintenance scene, designed directly on a 64 px grid.
c = new_canvas(64, 64, background="#8fc8d8", name="offshore_maintenance")

# Palette
sky_hi = "#b8dce2"
sky = "#8fc8d8"
sky_low = "#71b1c3"
haze = "#d5e7e6"
sea_far = "#347f9d"
sea = "#17627f"
sea_deep = "#0c435f"
foam = "#b8e2df"
foam_hi = "#e7f2e9"
steel_dark = "#293b46"
steel = "#4f6670"
steel_mid = "#71858b"
steel_hi = "#aebbb8"
white = "#e8eee8"
shadow = "#17313d"
yellow = "#f4ca3a"
yellow_hi = "#ffe46a"
orange = "#ee7b32"
skin = "#b86f4f"
navy = "#19394f"
red = "#c84d3f"

# Sky bands and small pixel clouds.
c.rect(0, 0, 64, 13, sky_hi)
c.rect(0, 13, 64, 18, sky)
c.rect(0, 27, 64, 6, sky_low)
c.rect(3, 8, 10, 2, haze)
c.rect(6, 6, 4, 2, haze)
c.rect(11, 9, 7, 1, haze)
c.rect(29, 15, 10, 2, "#a9d3dc")
c.rect(32, 14, 4, 1, "#a9d3dc")

# Two distant turbines, thin and low contrast to preserve depth.
def distant_turbine(cx, hub_y, base_y):
    c.line(cx, hub_y + 1, cx - 1, base_y, "#d2dddd")
    c.set(cx, hub_y, steel_mid)
    c.line(cx, hub_y, cx, hub_y - 8, "#dce5e2")
    c.line(cx, hub_y, cx - 7, hub_y + 3, "#dce5e2")
    c.line(cx, hub_y, cx + 6, hub_y + 4, "#dce5e2")
    c.rect(cx - 1, base_y - 1, 3, 1, "#b6c8c8")

distant_turbine(14, 18, 31)
distant_turbine(35, 21, 31)

# Horizon and layered ocean.
c.rect(0, 31, 64, 33, sea_far)
c.rect(0, 37, 64, 27, sea)
c.rect(0, 49, 64, 15, sea_deep)
# Long horizontal wave bands.
for x, y, w in [(1,33,8),(18,34,11),(39,33,8),(53,35,9),(5,40,13),(24,39,8),(43,42,13),(0,47,9),(14,45,11),(30,48,8),(49,46,10),(7,54,10),(21,52,13),(40,56,9),(54,53,10),(1,61,12),(28,61,15)]:
    c.rect(x, y, w, 1, foam)
for x, y, w in [(3,34,3),(21,35,4),(54,36,4),(8,41,5),(25,40,3),(46,43,5),(16,46,4),(31,49,3),(3,55,6),(24,53,4),(55,54,5),(34,59,6)]:
    c.rect(x, y, w, 1, foam_hi)
# Broken dark trough pixels.
for x, y, w in [(0,43,6),(18,42,5),(34,44,7),(56,40,8),(8,50,7),(25,56,6),(45,51,8),(2,58,5),(14,63,8),(50,61,9)]:
    c.rect(x, y, w, 1, shadow)

# Main turbine tower: massive tapered steel column on the right.
c.poly([(47,0),(58,0),(56,39),(44,39)], steel_dark)
c.poly([(48,0),(56,0),(54,38),(46,38)], white)
c.poly([(48,0),(51,0),(49,38),(46,38)], steel_hi)
c.rect(51, 1, 4, 37, "#d9e1dd")
# Bolted base collar.
c.rect(43, 36, 15, 3, steel_dark)
c.rect(44, 36, 13, 1, steel_hi)
c.set(46, 37, shadow); c.set(50, 37, shadow); c.set(55, 37, shadow)

# Heavy maintenance deck and its yellow safety edge.
c.rect(22, 38, 41, 2, steel_dark)
c.rect(20, 40, 44, 3, steel)
c.rect(20, 40, 44, 1, steel_hi)
c.rect(20, 43, 44, 2, steel_dark)
c.rect(20, 38, 23, 1, yellow)
c.rect(58, 38, 5, 1, yellow)
# Deck braces and offshore support legs.
c.poly([(23,45),(28,45),(23,64),(18,64)], steel_dark)
c.poly([(55,45),(60,45),(63,64),(58,64)], steel_dark)
c.poly([(25,45),(28,45),(24,62),(22,62)], steel_mid)
c.line(25,46,57,62, steel)
c.line(58,46,22,61, steel)
c.line(21,54,61,54, steel_dark)
c.rect(18,61,8,3, shadow)
c.rect(57,61,7,3, shadow)

# Guard rails around working deck.
c.line(22,37,22,31, steel_dark)
c.line(42,37,42,31, steel_dark)
c.line(59,37,59,31, steel_dark)
c.line(22,32,42,32, steel_dark)
c.line(22,35,42,35, steel_mid)
c.line(58,32,63,32, steel_dark)
c.line(58,35,63,35, steel_mid)
for x in (28,35):
    c.line(x,32,x,37,steel_mid)

# Ladder hanging from deck into the wave zone.
c.rect(31, 36, 1, 19, steel_hi)
c.rect(36, 36, 1, 19, steel_dark)
for y in range(38, 55, 3):
    c.rect(31, y, 6, 1, steel_mid)
# Ladder lower shadow and splash.
c.rect(30,54,8,1, foam_hi)
c.rect(28,55,4,1, foam)
c.rect(37,56,5,1, foam)

# Technician climbing: helmet, face, hi-vis suit, harness, boots and hands.
# Head and helmet at y37-39, body centered between ladder rails.
c.rect(32, 36, 4, 2, orange)
c.set(31,37,orange)
c.rect(32, 38, 3, 2, skin)
c.set(35,39,skin)
# Torso leans into ladder.
c.rect(32, 40, 4, 5, yellow)
c.set(31,41,yellow_hi)
c.set(31,42,yellow)
c.set(36,42,yellow)
c.rect(33, 40, 1, 5, yellow_hi)
# Harness bands.
c.set(32,41,navy); c.set(35,41,navy)
c.rect(32,43,4,1,navy)
c.set(34,42,navy)
# Arms gripping rails.
c.set(31,40,yellow); c.set(30,40,skin)
c.set(36,40,yellow); c.set(37,39,skin)
# Legs in navy work trousers, offset on rungs.
c.rect(32,45,2,3,navy)
c.rect(35,45,2,3,navy)
c.set(31,48,navy); c.set(34,48,navy)
c.set(30,48,steel_dark); c.set(34,49,steel_dark)
# Small fall-arrest line to the rail.
c.line(35,43,39,37,red)
c.set(39,36,red)

# Platform details: control box, warning light and a few specular pixels.
c.rect(23,34,4,4,steel_dark)
c.rect(24,34,3,3,steel_hi)
c.set(25,35,red)
c.rect(60,29,2,3,steel_dark)
c.set(60,28,orange)
c.set(45,35,white)
c.set(57,41,steel_hi)

# Foreground spray overlaps legs to seat the structure in the sea.
c.rect(17,62,10,1,foam)
c.rect(55,60,9,1,foam)
c.rect(59,59,5,1,foam_hi)
c.set(27,61,foam_hi); c.set(56,62,foam)

view(c, scale=8, margin=0)
finish(c)
