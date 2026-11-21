# Sky pirate girl portrait, 64x64 pixel art
from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64, background=None, name="sky-pirate-girl")

# Palette
ink = "#17213b"
ink2 = "#273150"
navy = "#263656"
navy_hi = "#3d5275"
navy_light = "#597094"
sky = "#79c8df"
sky_hi = "#b9edf1"
cloud = "#e6fbf2"
cloud_sh = "#a8dfe2"
hair_dark = "#7b3f35"
hair = "#b85b3f"
hair_hi = "#e58a55"
hair_glint = "#f4b56d"
skin_dark = "#b85e4e"
skin_sh = "#d77962"
skin = "#f1a079"
skin_hi = "#ffd0a0"
red_dark = "#7d2537"
red = "#c73742"
red_hi = "#ed5a4d"
brass_dark = "#7a512e"
brass = "#d49a43"
brass_hi = "#ffe183"
lens = "#79d6db"
lens_hi = "#d9ffff"
white = "#fff3d6"

# Round sky window and clouds, leaving transparent corners.
c.circle(31, 30, 27, ink)
c.circle(31, 29, 25, sky)
c.dither(8, 15, 47, 22, [sky, sky_hi], pattern="bayer4")
# distant cloud banks
c.poly([(7,38),(7,34),(12,34),(14,31),(20,31),(23,34),(30,34),(31,39)], cloud_sh)
c.poly([(8,36),(12,36),(14,33),(19,33),(22,36),(30,36),(30,40),(8,40)], cloud)
c.poly([(42,16),(46,16),(48,13),(53,14),(55,17),(57,17),(57,20),(42,20)], sky_hi)
# tiny flight streaks
c.line(8,23,16,23,sky_hi); c.line(11,25,18,25,sky_hi)
c.line(48,28,57,28,sky_hi); c.line(51,30,58,30,sky_hi)

# Scarf tails behind the body, flying left.
c.poly([(29,43),(23,43),(18,40),(8,41),(15,45),(6,48),(19,49),(27,53),(34,49)], ink)
c.poly([(27,44),(19,43),(12,42),(18,46),(10,48),(21,48),(30,52),(34,48)], red_dark)
c.poly([(26,45),(18,44),(21,46),(14,47),(23,47),(31,50)], red)
c.line(16,47,24,48,red_hi)

# Hair mass and wind-swept locks behind head.
c.poly([(18,34),(13,32),(8,33),(13,29),(6,28),(14,25),(9,21),(19,21),(21,15),(31,11),(43,15),(48,24),(46,37),(40,43),(26,44)], ink)
c.poly([(20,34),(15,31),(10,32),(16,28),(10,27),(18,24),(13,22),(21,22),(23,17),(31,13),(41,16),(46,23),(44,35),(39,41),(27,42)], hair_dark)
# swept outer orange locks
c.poly([(25,18),(18,18),(12,21),(21,21),(14,25),(25,23)], hair)
c.poly([(22,24),(13,27),(21,27),(14,31),(27,28)], hair)
c.poly([(22,31),(12,34),(21,35),(16,38),(29,35)], hair_dark)
c.poly([(25,18),(19,20),(27,20),(21,23),(31,20)], hair_hi)

# Neck and ear behind jaw.
c.poly([(29,38),(29,47),(38,50),(43,43),(41,35)], ink)
c.poly([(31,37),(31,45),(38,48),(41,42),(40,35)], skin_dark)
c.poly([(33,38),(33,44),(38,46),(40,41),(39,36)], skin)
c.poly([(43,29),(49,28),(51,32),(49,37),(44,38)], ink)
c.poly([(44,30),(48,30),(49,32),(48,35),(44,36)], skin_sh)
c.set(47,33,skin_hi); c.line(45,35,47,34,skin_dark)

# Face in three-quarter view, with pointed chin and strong readable outline.
c.poly([(27,17),(37,14),(44,18),(47,24),(46,31),(43,38),(37,43),(30,40),(25,34),(23,26)], ink)
c.poly([(28,18),(36,16),(42,18),(45,23),(45,30),(42,36),(37,41),(31,39),(27,34),(25,27)], skin_sh)
# lit face plane
c.poly([(31,18),(38,17),(42,20),(44,24),(43,30),(41,35),(36,39),(31,37),(29,32),(29,24)], skin)
c.poly([(34,18),(39,18),(42,21),(43,25),(41,27),(34,26),(31,23)], skin_hi)
c.poly([(30,28),(35,27),(35,35),(31,36),(28,33)], skin_hi)
# cheek warmth and nose shadow
c.rect(38,29,4,3,"#e88772")
c.poly([(37,24),(39,29),(42,30),(39,31),(37,30)], skin_dark)
c.set(41,29,skin_hi)

# Hair fringe over forehead and temple.
c.poly([(24,19),(28,14),(36,13),(42,16),(38,17),(34,22),(33,17),(29,23),(27,30),(23,27)], ink)
c.poly([(26,19),(29,16),(35,15),(40,16),(36,18),(33,23),(32,18),(29,25),(27,29),(25,26)], hair)
c.poly([(29,17),(34,15),(38,16),(34,18),(32,21),(32,17)], hair_hi)
c.poly([(26,21),(29,18),(28,25),(25,27)], hair_hi)
c.line(29,16,34,15,hair_glint)
# right side lock
c.poly([(42,17),(46,21),(47,28),(44,27),(44,34),(41,38),(42,29),(40,24)], ink)
c.poly([(42,19),(44,22),(45,27),(43,26),(43,32),(41,35),(42,27),(40,23)], hair_dark)
c.line(43,21,44,26,hair_hi)

# Goggles perched on forehead: strap, twin lenses, bridge.
c.line(24,18,42,16,ink); c.line(24,19,43,17,brass_dark)
c.poly([(24,15),(31,14),(34,17),(32,22),(25,22),(22,19)], ink)
c.poly([(25,16),(30,15),(32,17),(31,20),(26,21),(24,19)], brass)
c.poly([(26,16),(30,16),(31,18),(30,19),(26,20),(25,18)], lens)
c.line(26,16,30,16,lens_hi); c.set(26,17,lens_hi)
c.poly([(34,13),(41,14),(44,17),(42,21),(36,20),(33,17)], ink)
c.poly([(35,15),(40,15),(42,17),(41,19),(36,19),(35,17)], brass)
c.poly([(36,15),(40,16),(41,17),(40,18),(36,18),(35,17)], lens)
c.line(36,15,39,16,lens_hi)
c.line(32,17,35,16,brass_hi)
c.set(24,17,brass_hi); c.set(42,16,brass_hi)

# Eye and eyebrow, angled for confidence.
c.line(31,26,36,24,ink)
c.line(36,24,40,25,hair_dark)
c.poly([(32,27),(36,26),(39,27),(36,29),(33,29)], white)
c.line(33,27,38,27,ink)
c.rect(35,27,2,2,"#356477")
c.set(36,27,ink); c.set(34,27,lens_hi)
# far eye hint
c.line(41,25,43,26,ink); c.set(42,27,ink)
# eyebrow accent
c.line(31,24,36,22,hair_dark)

# Nose and confident half-smile.
c.line(38,29,39,32,skin_dark); c.line(39,32,41,32,skin_dark)
c.line(34,35,38,36,red_dark); c.line(38,36,41,34,red_dark)
c.line(35,35,38,35,white); c.set(39,34,skin_hi)
c.set(33,33,"#d97967")

# Torso silhouette / short navy coat.
c.poly([(28,43),(20,46),(16,54),(15,63),(54,63),(52,52),(44,45),(40,43),(35,48)], ink)
c.poly([(28,45),(22,48),(19,55),(19,63),(50,63),(49,53),(43,47),(40,45),(35,51)], navy)
# far shoulder and raised collar
c.poly([(22,47),(25,42),(30,41),(34,48),(29,52)], ink)
c.poly([(24,47),(27,43),(30,43),(32,48),(29,50)], navy_hi)
c.poly([(40,44),(45,45),(49,50),(44,52),(38,48)], ink)
c.poly([(41,46),(44,47),(47,50),(44,50),(39,48)], navy_hi)

# Red scarf wrap at neck.
c.poly([(27,41),(32,43),(40,42),(45,45),(42,51),(34,52),(28,48)], ink)
c.poly([(29,42),(33,45),(39,44),(43,46),(41,49),(34,50),(30,47)], red_dark)
c.poly([(31,43),(34,46),(40,45),(42,46),(40,48),(34,49),(31,47)], red)
c.line(34,46,40,45,red_hi)

# Coat lapels and shirt opening.
c.poly([(30,49),(35,52),(33,63),(24,54)], navy_hi)
c.poly([(40,50),(36,52),(38,63),(47,54)], navy_light)
c.poly([(35,51),(40,50),(38,63),(33,63)], ink2)
c.poly([(35,53),(38,52),(37,61),(34,61)], white)
c.poly([(35,53),(38,52),(37,56)], skin_sh)
# seams, brass fasteners and shoulder highlight
c.line(22,54,21,62,navy_light); c.line(46,53,48,61,ink2)
c.set(26,55,brass); c.set(27,56,brass_hi)
c.set(44,55,brass); c.set(43,56,brass_dark)
c.line(20,52,24,49,navy_light)
# tiny coat edge pixels sharpen silhouette
c.set(17,58,navy_hi); c.set(50,58,navy_hi)

view(c, scale=8, margin=0)
finish(c)
