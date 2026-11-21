from pixelbench_api import *

# Summer seaside scene, authored directly at 128x128.
c = new_canvas(128, 128, background="#69cdf2", name="summer-seaside")

# Palette.
sky = "#69cdf2"
sky_hi = "#83dcf6"
cloud = "#fffaf0"
cloud_sh = "#d9eff2"
sun = "#ffe45c"
sun_hi = "#fff3a1"
sun_orange = "#ffc83d"
horizon = "#176cae"
deep = "#187fbd"
midblue = "#159ac6"
teal = "#19b8c2"
lightsea = "#45d0c9"
sea_glint = "#9ce9dc"
foam = "#fffdf0"
foam_sh = "#cdece2"
sand = "#f3c766"
sand_hi = "#ffdc7e"
sand_sh = "#dda84e"
sand_dark = "#c98b3e"
red = "#e8423f"
red_hi = "#ff6258"
red_dark = "#b92f35"
white = "#fff8e8"
pole = "#694b43"
pole_hi = "#a57758"
navy = "#15507a"
towel_blue = "#197fac"
towel_light = "#58c5cf"
flip = "#ee524d"
flip_dark = "#ae3437"

# Sky: subtle horizontal open-air bands.
c.rect(0, 0, 128, 18, sky_hi)
c.rect(0, 18, 128, 30, sky)

# Bright pixel sun and short blocky rays.
c.rect(103, 6, 4, 5, sun)
c.rect(103, 29, 4, 5, sun)
c.rect(92, 18, 5, 4, sun)
c.rect(113, 18, 6, 4, sun)
c.rect(96, 10, 3, 3, sun)
c.rect(112, 10, 3, 3, sun)
c.rect(96, 27, 3, 3, sun)
c.rect(112, 27, 3, 3, sun)
c.circle(105, 20, 9, sun_orange)
c.circle(105, 19, 8, sun)
c.rect(101, 13, 6, 3, sun_hi)
c.rect(99, 16, 3, 5, sun_hi)

# Soft clouds assembled from stepped clusters.
c.rect(9, 25, 35, 7, cloud)
c.rect(14, 20, 24, 12, cloud)
c.rect(20, 16, 10, 16, cloud)
c.rect(7, 29, 41, 4, cloud_sh)
c.rect(12, 25, 30, 5, cloud)
c.rect(64, 30, 25, 6, cloud)
c.rect(69, 26, 15, 10, cloud)
c.rect(74, 23, 7, 13, cloud)
c.rect(62, 34, 31, 3, cloud_sh)
c.rect(66, 31, 23, 3, cloud)

# Two distant gull silhouettes with small sunlit wing edges.
c.poly([(48,39),(52,36),(56,39),(52,38)], navy)
c.set(49,38,white); c.set(55,38,white)
c.poly([(79,16),(83,13),(88,17),(83,15)], navy)
c.set(80,15,white); c.set(87,16,white)

# Sea layers from horizon to shore.
c.rect(0, 47, 128, 7, horizon)
c.rect(0, 54, 128, 10, deep)
c.rect(0, 64, 128, 10, midblue)
c.rect(0, 74, 128, 11, teal)
c.rect(0, 85, 128, 11, lightsea)
# Pixel glints and distant wavelets.
for x, y, w, col in [
    (4,51,12,deep),(22,50,7,sky_hi),(48,52,13,deep),(70,50,8,sky_hi),(112,52,10,deep),
    (9,59,8,sea_glint),(31,62,13,teal),(55,57,8,sky_hi),(76,61,15,midblue),(103,58,12,sea_glint),
    (2,69,16,lightsea),(25,71,7,sea_glint),(45,67,13,deep),(69,72,9,sea_glint),(92,68,15,deep),(117,73,9,sea_glint),
    (10,80,13,sea_glint),(37,77,17,lightsea),(65,82,12,sea_glint),(90,78,9,lightsea),(108,84,17,sea_glint)
]: c.rect(x,y,w,2,col)

# Tiny sailboat at the horizon.
c.line(99, 43, 99, 56, navy)
c.poly([(99,44),(99,52),(91,52)], white)
c.poly([(101,46),(101,52),(106,52)], sun_hi)
c.rect(91, 53, 17, 2, navy)
c.rect(94, 55, 11, 1, red)

# Golden sand base.
c.rect(0, 94, 128, 34, sand)
c.rect(0, 102, 128, 26, sand_hi)

# Main rolling wave, jagged white lip and translucent-looking shadow band.
c.poly([(0,84),(8,86),(17,84),(25,88),(34,86),(44,89),(54,85),(64,88),(75,87),(86,91),(96,88),(107,91),(118,87),(127,89),(127,99),(116,98),(105,100),(94,97),(82,100),(70,96),(58,99),(47,96),(35,99),(23,95),(12,97),(0,94)], foam)
c.poly([(0,94),(11,96),(21,94),(34,98),(45,95),(58,98),(70,95),(83,99),(94,96),(106,99),(118,96),(127,98),(127,102),(116,101),(104,103),(92,100),(80,103),(68,99),(56,102),(44,99),(32,102),(20,98),(9,100),(0,98)], foam_sh)
# Holes/sea accents inside the foam front.
for x,y,w in [(5,89,8),(28,92,6),(50,90,9),(75,93,7),(101,92,10),(119,90,6)]: c.rect(x,y,w,2,lightsea)

# Sand grain and damp marks.
for x,y,w,col in [
    (3,106,5,sand_sh),(17,116,3,sand_sh),(8,124,8,sand),(28,105,6,sand_dark),
    (42,118,5,sand_sh),(55,108,3,sand_sh),(70,123,7,sand),(85,107,5,sand_sh),
    (104,118,4,sand_sh),(116,108,7,sand_dark),(94,126,4,sand_sh),(33,125,3,sand_dark)
]: c.rect(x,y,w,2,col)

# Umbrella cast shadow, behind objects.
c.poly([(8,116),(41,108),(66,113),(35,121)], "#d6a04c")

# Umbrella pole with bright edge.
c.line(39,66,34,116,pole)
c.line(40,67,35,115,pole_hi)
c.rect(31,114,7,2,pole)

# Large red-and-white beach umbrella canopy with dark undersill.
c.poly([(8,66),(12,58),(19,52),(29,48),(42,48),(54,52),(63,59),(67,67),(57,65),(49,69),(40,65),(31,69),(22,65),(14,68)], red_dark)
# Canopy overall red surface.
c.poly([(8,64),(12,57),(20,51),(30,47),(42,47),(54,51),(62,57),(67,64),(57,62),(49,66),(40,62),(31,66),(22,62),(14,66)], red)
# White alternating panels.
c.poly([(14,62),(20,53),(30,48),(31,64),(22,60)], white)
c.poly([(32,63),(34,48),(42,48),(49,64),(40,60)], white)
c.poly([(50,64),(44,48),(53,52),(61,59),(57,61)], white)
# Red highlights and central cap.
c.line(12,59,20,53,red_hi)
c.line(35,49,40,49,red_hi)
c.line(53,53,60,59,red_hi)
c.rect(35,44,8,3,red_dark)
c.rect(37,43,4,3,red)

# Towel in perspective on right foreground; stripes follow its skew.
c.poly([(73,105),(107,102),(121,122),(82,127)], towel_blue)
c.poly([(77,105),(84,104),(93,126),(85,127)], white)
c.poly([(91,103),(98,103),(111,124),(103,125)], white)
c.poly([(106,103),(110,106),(121,122),(116,123)], towel_light)
c.line(75,108,109,105,navy)
# Short fringe pixels.
for x in [83,88,95,101,108,115]: c.line(x,125,x-1,127,white)

# Pair of red flip-flops on the towel/sand edge.
c.poly([(61,110),(66,106),(71,108),(72,118),(68,123),(63,121)], flip_dark)
c.poly([(62,109),(66,107),(70,109),(70,117),(67,121),(64,120)], flip)
c.line(64,110,67,114,white); c.line(69,110,67,114,white)
c.poly([(52,115),(56,111),(61,113),(62,122),(58,126),(53,123)], flip_dark)
c.poly([(53,114),(57,112),(60,114),(60,121),(57,124),(54,122)], red_hi)
c.line(55,115,57,118,white); c.line(59,115,57,118,white)

# Final foreground specks and shell.
c.rect(14,110,4,2,sand_dark); c.set(16,109,sand_dark)
c.rect(45,111,3,2,sand_sh)
c.poly([(18,121),(21,118),(24,121),(23,123),(19,123)], white)
c.set(21,121,red)
c.rect(124,114,3,2,sand_dark)

# A few crisp sparkle pixels on the nearest water.
c.rect(16,82,4,1,foam); c.rect(59,80,5,1,foam); c.rect(112,77,4,1,foam)

result = c
view(result, scale=4, margin=0)
finish(result)
