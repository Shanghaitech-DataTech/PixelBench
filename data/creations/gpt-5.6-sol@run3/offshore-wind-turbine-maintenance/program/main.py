from pixelbench_api import *

# Offshore wind maintenance scene, 64x64.
c = new_canvas(64, 64, background="#9bc9d2", name="offshore-maintenance")

# Restrained industrial/coastal palette.
sky_hi = "#c8e2df"
sky = "#9bc9d2"
sky_low = "#78adb9"
cloud = "#e2efea"
cloud_shade = "#b6d5d5"
horizon = "#527f8f"
sea_far = "#397487"
sea = "#245c73"
sea_deep = "#17465e"
foam = "#d5ece7"
foam_dim = "#82b8bd"
steel_dark = "#263c48"
steel = "#49636b"
steel_mid = "#657b7d"
steel_light = "#9aa9a3"
shadow = "#172b36"
yellow = "#f3c94b"
yellow_hi = "#ffe27a"
orange = "#e56b31"
orange_dark = "#9f3f26"
skin = "#b66b4b"
white = "#eef3e9"
red = "#c84c36"

# Sky bands and stepped cloud clusters.
c.rect(0, 0, 64, 13, sky_hi)
c.rect(0, 13, 64, 13, sky)
c.rect(0, 26, 64, 9, sky_low)
c.rect(3, 7, 14, 2, cloud)
c.rect(6, 5, 7, 2, cloud)
c.rect(1, 9, 20, 2, cloud)
c.rect(14, 10, 8, 1, cloud_shade)
c.rect(34, 13, 17, 2, cloud)
c.rect(38, 11, 8, 2, cloud)
c.rect(31, 15, 24, 2, cloud_shade)
c.rect(55, 5, 7, 1, cloud)
c.rect(58, 4, 4, 1, cloud)
# Fine distant haze streaks.
c.line(0, 22, 13, 22, cloud_shade)
c.line(18, 19, 27, 19, cloud_shade)
c.line(46, 24, 63, 24, "#8fbfc5")

# Distant turbines, kept slim and pale for atmospheric depth.
def distant_turbine(cx, hub_y, base_y, blade):
    c.poly([(cx-1, hub_y+2), (cx+1, hub_y+2), (cx+2, base_y), (cx-1, base_y)], steel_light)
    c.rect(cx-2, hub_y-1, 5, 3, steel_mid)
    c.set(cx+2, hub_y, steel_dark)
    c.circle(cx, hub_y, 1, steel_light)
    # Three stepped blades with distinct directions.
    c.line(cx, hub_y-1, cx, hub_y-blade, steel_light)
    c.line(cx-1, hub_y, cx-blade, hub_y+3, steel_light)
    c.line(cx+1, hub_y+1, cx+blade-1, hub_y+5, steel_light)

# Two complete background machines at different scales.
distant_turbine(12, 18, 35, 9)
distant_turbine(35, 15, 29, 7)
# Tiny offshore bases at horizon.
c.rect(9, 34, 7, 2, horizon)
c.rect(45, 34, 7, 2, horizon)

# Ocean base and horizontal wave rhythm.
c.rect(0, 35, 64, 29, sea)
c.rect(0, 35, 64, 3, sea_far)
c.line(0, 38, 15, 38, foam_dim)
c.line(20, 37, 34, 37, "#5d96a2")
c.line(42, 39, 63, 39, foam_dim)
c.rect(2, 42, 11, 1, foam)
c.rect(0, 43, 7, 1, foam_dim)
c.rect(17, 41, 9, 1, foam_dim)
c.rect(23, 45, 14, 1, foam)
c.rect(27, 46, 7, 1, foam_dim)
c.rect(46, 44, 14, 1, foam_dim)
c.rect(5, 49, 17, 1, "#4d8997")
c.rect(0, 53, 8, 2, sea_deep)
c.rect(9, 52, 12, 1, foam)
c.rect(14, 53, 11, 1, foam_dim)
c.rect(28, 50, 9, 1, sea_deep)
c.rect(40, 51, 15, 1, foam)
c.rect(50, 52, 12, 1, foam_dim)
c.rect(2, 58, 16, 2, sea_deep)
c.rect(18, 57, 8, 1, foam_dim)
c.rect(29, 60, 18, 2, sea_deep)
c.rect(38, 58, 10, 1, foam)
c.rect(51, 56, 13, 2, sea_deep)
c.rect(54, 60, 10, 1, foam_dim)
# Small crests.
c.line(0, 47, 4, 45, foam)
c.line(4, 45, 8, 47, foam)
c.line(14, 61, 19, 59, foam_dim)
c.line(19, 59, 24, 61, foam_dim)
c.line(42, 55, 46, 53, foam)
c.line(46, 53, 50, 55, foam)

# Foreground turbine monopile, cropped at right for imposing scale.
c.poly([(49, 0), (63, 0), (63, 64), (45, 64), (47, 48), (48, 25)], steel_dark)
c.poly([(53, 0), (63, 0), (63, 64), (54, 64), (55, 38)], steel)
c.poly([(58, 0), (63, 0), (63, 64), (59, 64)], steel_mid)
c.rect(48, 25, 3, 29, steel_mid)
c.line(49, 27, 49, 54, steel_light)
# Segmented tower seams and marine staining.
c.rect(48, 12, 16, 2, shadow)
c.rect(49, 13, 15, 1, steel_light)
c.rect(47, 31, 17, 2, shadow)
c.rect(48, 32, 16, 1, steel_light)
c.rect(46, 50, 18, 3, orange_dark)
c.rect(47, 50, 17, 1, orange)
c.rect(45, 57, 19, 7, shadow)
c.dither(46, 57, 18, 7, [orange_dark, shadow], pattern="checker")

# Maintenance platform deck, railings, and triangular under-bracing.
c.rect(22, 30, 31, 3, shadow)
c.rect(21, 29, 33, 2, yellow)
c.rect(22, 29, 30, 1, yellow_hi)
c.rect(23, 33, 29, 2, steel_mid)
c.line(23, 35, 30, 43, steel_dark)
c.line(30, 35, 38, 43, steel_dark)
c.line(38, 35, 46, 43, steel_dark)
c.line(46, 35, 51, 40, steel_dark)
c.line(23, 42, 51, 42, steel_dark)
c.line(24, 35, 24, 42, steel)
c.line(51, 34, 51, 42, steel)
# Guard rails, clearly separated from deck.
for x in (23, 31, 39, 47, 52):
    c.rect(x, 23, 2, 7, steel_dark)
c.rect(23, 22, 31, 2, steel_light)
c.rect(24, 25, 28, 1, steel_mid)
c.rect(21, 21, 4, 3, yellow)
c.rect(52, 21, 3, 4, yellow)
# Rail shadow pixels.
c.set(31, 24, shadow); c.set(39, 24, shadow); c.set(47, 24, shadow)

# Access ladder from platform down toward wave zone.
c.rect(32, 31, 2, 29, steel_light)
c.rect(39, 31, 2, 29, steel_light)
c.rect(33, 31, 6, 1, shadow)
for y in range(34, 59, 4):
    c.rect(33, y, 7, 2, steel_mid)
    c.rect(34, y, 5, 1, steel_light)
# Ladder foot and splash.
c.rect(31, 59, 3, 3, steel_dark)
c.rect(39, 59, 3, 3, steel_dark)
c.rect(27, 61, 7, 1, foam)
c.rect(40, 61, 8, 1, foam)
c.set(30, 60, foam); c.set(43, 59, foam)

# Technician climbing: helmet, head, hi-vis suit, harness, boots and gripping arms.
# Back silhouette first for clean separation.
c.rect(34, 39, 5, 10, shadow)
c.rect(35, 37, 4, 3, yellow)
c.rect(36, 38, 4, 2, yellow_hi)
c.set(36, 40, skin); c.set(37, 40, skin)
# Torso and reflective jacket.
c.rect(34, 41, 5, 6, orange)
c.rect(34, 43, 5, 1, yellow_hi)
c.set(34, 45, orange_dark); c.set(38, 45, orange_dark)
# Arms: one high grip, one lateral grip.
c.rect(33, 40, 2, 5, orange)
c.set(33, 39, skin)
c.set(33, 38, skin)
c.rect(39, 42, 2, 2, orange)
c.set(40, 41, skin)
# Harness and clipped safety line.
c.rect(36, 41, 1, 7, shadow)
c.line(35, 45, 39, 47, yellow)
c.set(39, 46, red)
c.line(39, 46, 42, 39, red)
c.set(42, 38, red)
# Split legs planted on separate rungs.
c.rect(34, 47, 2, 5, orange_dark)
c.rect(38, 47, 2, 4, orange_dark)
c.set(33, 52, shadow); c.set(34, 52, shadow)
c.set(39, 51, shadow); c.set(40, 51, shadow)
# Helmet highlight and face opening.
c.rect(36, 37, 3, 1, yellow_hi)
c.set(38, 40, shadow)

# Platform utility box and warning accents.
c.rect(25, 25, 6, 4, steel_dark)
c.rect(26, 25, 4, 3, steel_mid)
c.set(27, 26, red)
c.rect(44, 27, 5, 2, yellow)
c.set(46, 27, shadow)

# Final foreground wave overlaps anchor the steel in the sea.
c.rect(44, 62, 20, 2, sea_deep)
c.rect(46, 61, 8, 1, foam_dim)
c.rect(55, 60, 9, 1, foam)

view(c, scale=8, margin=0)
finish(c)
