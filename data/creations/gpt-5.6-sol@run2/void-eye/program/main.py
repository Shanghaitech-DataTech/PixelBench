from pixelbench_api import *

# 64px RPG boss sprite with a transparent background.
result = new_canvas(64, 64, background=None, name="void-eye")

# Compact palette: ominous violets, cold eye whites, and a small spectral glow.
outline = "#120b20"
outline2 = "#1d102d"
void = "#27133d"
body_dark = "#351752"
body = "#4a216b"
body_mid = "#63318a"
body_light = "#844db0"
rim = "#a06bc4"
white_dark = "#9d91b5"
white_mid = "#c8c0d5"
white = "#eee9f2"
iris_dark = "#32104f"
iris = "#552078"
iris_mid = "#7b35a0"
iris_light = "#ad64cf"
glow = "#d7b9f0"
glow_core = "#fff4ff"
shadow = "#160d2466"

# Soft hovering shadow, deliberately dithered at the edges.
result.ellipse(32, 55, 17, 4, shadow)
result.ellipse(32, 55, 12, 2, "#11091f88")
for x, y in [(17,53),(20,57),(23,52),(27,59),(36,59),(41,52),(45,57),(48,54)]:
    result.set(x, y, "#160d2433")

# Short tentacles behind the main eye, each with a blocky hooked tip.
result.poly([(13,31),(7,33),(4,37),(5,41),(9,40),(9,37),(15,36)], outline)
result.poly([(14,34),(8,37),(7,41),(10,43),(13,40),(18,38)], body_dark)
result.set(8,39, body_mid)

result.poly([(50,30),(57,31),(60,34),(59,38),(56,39),(55,36),(49,35)], outline)
result.poly([(49,33),(55,34),(57,36),(56,38),(52,37),(47,36)], body_dark)
result.set(56,35, body_mid)

result.poly([(18,42),(14,48),(14,53),(17,56),(20,54),(19,50),(23,44)], outline)
result.poly([(19,43),(17,49),(18,52),(20,51),(23,44)], body)
result.set(18,48, body_light)

result.poly([(27,44),(25,51),(27,57),(31,58),(33,55),(30,52),(32,44)], outline)
result.poly([(28,44),(28,51),(30,54),(31,53),(31,45)], body_dark)
result.set(29,49, body_mid)

result.poly([(39,43),(41,49),(40,55),(43,57),(46,54),(44,50),(45,43)], outline)
result.poly([(40,43),(43,49),(42,53),(44,54),(45,52),(43,44)], body)
result.set(42,47, body_light)

result.poly([(48,39),(51,43),(51,48),(54,50),(57,48),(55,45),(55,40)], outline)
result.poly([(48,39),(52,42),(53,46),(55,47),(54,43),(53,39)], body_dark)

# Heavy outer body: asymmetrical, horned upper contour and tapered lower edge.
result.poly([(9,25),(11,19),(16,15),(19,11),(25,12),(29,8),(34,11),(39,9),
             (43,13),(49,15),(53,20),(55,27),(53,34),(49,40),(43,44),(36,47),
             (29,46),(23,47),(17,43),(12,39),(9,33)], outline)
# Outer purple mantle inset from the near-black silhouette.
result.poly([(12,25),(14,20),(19,17),(21,13),(26,15),(30,11),(34,14),(39,12),
             (42,16),(48,18),(51,22),(53,28),(50,35),(46,39),(40,42),(34,44),
             (27,43),(21,44),(17,40),(13,36),(11,31)], body_dark)

# Faceted mantle lighting and small organic notches.
result.poly([(14,20),(20,16),(25,15),(22,20),(16,24)], body)
result.poly([(40,14),(47,18),(50,22),(45,21)], body)
result.poly([(12,31),(16,35),(18,41),(14,36)], void)
result.poly([(48,35),(45,40),(39,43),(44,36)], void)
result.poly([(19,17),(25,15),(22,19)], body_light)
result.poly([(39,14),(44,17),(41,19)], body_light)
result.rect(16, 24, 2, 3, body_mid)
result.rect(46, 25, 3, 2, body_mid)
result.set(18, 21, rim)
result.set(47, 22, body_light)
result.set(15, 29, body_light)
result.set(48, 32, body)

# Eye socket and sclera. The dark socket remains visible as a strong frame.
result.poly([(13,28),(17,22),(23,18),(31,16),(40,18),(47,22),(51,28),
             (47,34),(41,39),(33,41),(25,39),(18,35)], outline2)
result.poly([(16,28),(20,23),(26,20),(33,19),(40,20),(46,24),(48,28),
             (44,33),(39,36),(32,38),(25,36),(20,33)], white_dark)
result.poly([(18,27),(22,23),(28,21),(36,21),(42,23),(46,27),
             (43,31),(38,34),(31,36),(25,34),(20,31)], white)
# Cool low-plane shading and sharp sclera glints.
result.poly([(20,31),(25,34),(31,36),(38,34),(43,31),(40,35),(32,38),(25,36)], white_mid)
result.line(22, 24, 27, 22, "#ffffff")
result.set(19, 27, "#ffffff")
result.set(43, 26, white_mid)
result.set(22, 32, white_dark)

# Deep purple iris with concentric pixel-stepped rings.
result.ellipse(32, 28, 10, 10, iris_dark)
result.ellipse(32, 28, 8, 9, iris)
result.ellipse(32, 28, 6, 8, iris_mid)
# Iris striations give the boss eye scale and texture.
result.line(32, 20, 32, 23, iris_light)
result.line(27, 21, 29, 24, iris_light)
result.line(37, 22, 35, 25, iris_light)
result.line(24, 27, 28, 27, body_light)
result.line(36, 29, 40, 28, body_light)
result.line(27, 34, 29, 31, iris_light)
result.line(36, 34, 34, 31, iris_light)
result.set(25, 24, rim)
result.set(39, 25, rim)
result.set(25, 31, iris_dark)
result.set(39, 32, iris_dark)

# Vertical void pupil and a faint, contained inner glow.
result.ellipse(32, 28, 4, 7, "#1a0928")
result.rect(30, 23, 5, 11, "#13071e")
result.rect(31, 24, 3, 9, "#251034")
result.rect(32, 25, 2, 7, glow)
result.rect(32, 27, 2, 4, glow_core)
result.set(31, 25, "#8e5daa")
result.set(34, 31, "#5e3672")

# Sparse mantle specks and lower-edge highlights sharpen the silhouette.
for x, y, c in [(21,14,body_mid),(31,12,body_light),(42,17,rim),(50,28,body_light),
                (16,37,body_mid),(21,41,body_light),(38,42,body_mid),(46,37,body_light),
                (12,27,body_mid),(52,29,body)]:
    result.set(x, y, c)

view(result, scale=8, margin=0)
finish(result)
