from pixelbench_api import new_canvas, view, finish

# Offshore wind turbine maintenance, 64x64 pixel art.
c = new_canvas(64, 64, background="#8bc9dc", name="offshore_maintenance")

# Palette
sky_hi = "#b9e2e7"
sky = "#8bc9dc"
sky_low = "#6eb4cc"
cloud = "#d8edf0"
cloud_sh = "#a8d5df"
haze = "#7aafbd"
sea_far = "#327e9c"
sea = "#17627f"
sea_deep = "#0a405d"
foam = "#d7eef0"
foam_sh = "#71b7c5"
steel_dark = "#263944"
steel = "#3e5660"
steel_mid = "#60747a"
steel_hi = "#aab8b7"
white = "#e7eeee"
blade_sh = "#c1ced0"
yellow = "#f3b72c"
yellow_sh = "#c47b1d"
orange = "#ed662f"
orange_hi = "#ff9a36"
red = "#a9332d"
skin = "#ad6546"
visor = "#182c35"
rope = "#f1d15a"

# Sky bands and squared cloud wisps.
c.rect(0, 0, 64, 15, sky_hi)
c.rect(0, 15, 64, 17, sky)
c.rect(0, 32, 64, 8, sky_low)
c.rect(3, 7, 12, 2, cloud)
c.rect(7, 5, 10, 2, cloud)
c.rect(16, 8, 8, 2, cloud)
c.rect(26, 17, 9, 2, cloud_sh)
c.rect(30, 15, 11, 2, cloud)
c.rect(1, 25, 13, 2, cloud_sh)
c.rect(5, 23, 6, 2, cloud)

# Two distant turbines, softened by atmospheric perspective.
def distant_turbine(cx, hub_y, base_y):
    c.line(cx, hub_y + 1, cx - 1, base_y, haze)
    c.line(cx + 1, hub_y + 1, cx + 1, base_y, cloud_sh)
    c.circle(cx, hub_y, 1, cloud_sh)
    c.line(cx, hub_y, cx, hub_y - 10, cloud_sh)
    c.line(cx, hub_y, cx - 8, hub_y + 4, cloud_sh)
    c.line(cx, hub_y, cx + 7, hub_y + 5, cloud_sh)

distant_turbine(11, 20, 39)
distant_turbine(28, 24, 40)
# Small distant platform marks.
c.rect(8, 37, 7, 2, haze)
c.rect(25, 38, 7, 2, haze)

# Horizon and layered sea.
c.rect(0, 40, 64, 24, sea)
c.rect(0, 40, 64, 3, sea_far)
c.line(0, 43, 15, 43, foam_sh)
c.line(20, 42, 34, 42, foam_sh)
c.line(3, 48, 11, 48, foam)
c.line(11, 48, 16, 50, foam)
c.line(18, 46, 30, 46, sea_deep)
c.line(0, 54, 9, 53, sea_deep)
c.line(9, 53, 18, 55, foam_sh)
c.line(22, 57, 33, 55, foam)
c.line(32, 55, 43, 57, foam_sh)
c.line(1, 61, 14, 59, foam)
c.line(44, 48, 63, 46, sea_deep)
c.line(49, 52, 63, 54, foam)
c.line(47, 59, 62, 57, sea_deep)
# Pixel wave caps.
for x,y,w in [(2,45,5),(14,51,4),(25,50,7),(35,44,5),(42,52,4),(6,57,6),(17,61,8),(53,61,7)]:
    c.rect(x,y,w,1,foam_sh)
    c.set(x+1,y-1,foam)

# Main turbine tower behind platform: tapered steel column.
c.poly([(48,14),(56,14),(59,64),(44,64)], steel_dark)
c.poly([(50,14),(55,14),(56,64),(48,64)], steel_mid)
c.poly([(51,14),(53,14),(53,63),(49,63)], steel_hi)
# Tower segment seams.
for y in (28, 42, 55):
    c.line(47 if y < 42 else 45, y, 57, y, steel_dark)
    c.line(49 if y < 42 else 47, y+1, 56, y+1, steel_hi)

# Foreground hub, nacelle, and rotor.
c.rect(47, 10, 12, 7, steel_dark)
c.rect(46, 9, 11, 6, white)
c.rect(48, 10, 9, 2, blade_sh)
c.rect(55, 11, 5, 4, steel_mid)
c.circle(48, 12, 2, steel_dark)
c.circle(48, 12, 1, yellow)
# Three blades with chunky tapered silhouettes.
c.poly([(47,11),(44,1),(46,0),(49,10)], blade_sh)
c.poly([(46,13),(32,18),(31,20),(47,15)], white)
c.poly([(50,13),(61,23),(63,23),(51,11)], blade_sh)
c.line(45,3,47,10,white)
c.line(34,18,45,14,blade_sh)

# Maintenance platform deck and railings.
c.rect(33, 35, 30, 3, steel_dark)
c.rect(31, 38, 33, 3, yellow)
c.rect(31, 41, 33, 2, steel_dark)
c.rect(34, 36, 28, 1, steel_hi)
# guard rail posts and bars
for x in (34, 41, 48, 56, 62):
    c.rect(x, 29, 1, 7, steel_dark)
    c.set(x+1,29,steel_hi)
c.rect(34, 29, 29, 1, steel_dark)
c.rect(34, 33, 29, 1, steel_mid)
c.rect(32, 37, 2, 4, yellow_sh)
# safety stripe edge
for x in range(32,64,6):
    c.line(x,38,min(x+3,63),40,steel_dark)

# Platform under-bracing, visibly separate over the water.
c.poly([(35,43),(39,43),(34,61),(30,61)], steel_dark)
c.poly([(59,43),(62,43),(64,61),(61,61)], steel_dark)
c.line(36,44,61,60,steel_mid)
c.line(61,44,33,60,steel_mid)
c.line(37,44,60,59,steel_hi)
c.rect(29,60,7,3,steel_dark)
c.rect(60,60,4,3,steel_dark)

# Ladder from sea-access level to platform.
c.rect(38, 39, 2, 24, steel_dark)
c.rect(45, 39, 2, 24, steel_dark)
c.rect(39, 39, 1, 23, steel_hi)
c.rect(45, 39, 1, 23, steel_hi)
for y in range(41,63,4):
    c.rect(40,y,5,1,steel_hi)
    c.set(40,y+1,steel_dark)

# Technician climbing ladder: helmet/head, torso, harness, limbs and boots.
# back arm reaching upper rung
c.line(41,47,39,43,orange)
c.rect(39,42,2,2,orange_hi)
c.set(39,41,skin)
# helmet and face
c.rect(40,44,5,2,yellow)
c.rect(41,43,3,1,yellow)
c.rect(40,46,4,3,skin)
c.rect(43,46,2,2,visor)
# body in high visibility suit
c.poly([(40,49),(44,48),(47,52),(45,57),(40,56),(39,52)], orange)
c.rect(41,49,3,2,orange_hi)
c.rect(40,52,6,2,yellow)
c.rect(42,49,1,8,steel_dark)  # harness spine
c.rect(40,53,6,1,steel_dark)
c.set(45,51,yellow)
# forward arm gripping right rail
c.line(44,49,46,46,orange_hi)
c.set(46,45,skin)
# legs in braced climbing pose
c.poly([(40,56),(43,56),(42,61),(40,61)], orange)
c.poly([(44,56),(46,56),(47,59),(45,60)], orange)
c.rect(39,60,4,2,steel_dark)
c.rect(45,59,4,2,steel_dark)
# clipped safety lanyard
c.line(40,52,37,50,rope)
c.line(37,50,38,45,rope)
c.set(38,45,red)

# Foreground water overlap at feet of structure.
c.line(0,63,20,61,sea_deep)
c.line(10,63,28,61,foam_sh)
c.line(46,63,63,62,foam)
c.set(37,62,foam)
c.set(58,63,sea_deep)

view(c, scale=8, margin=0)
finish(c)
