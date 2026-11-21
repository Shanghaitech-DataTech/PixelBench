from pixelbench_api import *

result = new_canvas(64, 64, background=None, name="void-eye")

# Compact ominous palette.
shadow = (20, 7, 32, 78)
shadow_core = (14, 4, 24, 112)
outline = "#100919"
void = "#180d24"
body_dark = "#28133a"
body_mid = "#43205c"
body_lit = "#63327b"
rim = "#9256a5"
sclera_shade = "#897e9d"
sclera = "#c5b9cf"
sclera_light = "#e3d9e7"
iris_outer = "#2b0a43"
iris_deep = "#421064"
iris_mid = "#692492"
iris_lit = "#9c45c2"
pupil = "#160720"
glow = "#d994ff"
glow_hot = "#f4d8ff"

# Soft hovering shadow, deliberately dithered and translucent.
result.ellipse(32, 56, 17, 3, shadow, fill=True)
result.ellipse(32, 56, 11, 2, shadow_core, fill=True)
result.set(14, 55, shadow).set(49, 55, shadow).set(19, 59, shadow).set(44, 59, shadow)

# Short curling tentacles behind the eye body.
result.poly([(11,34),(7,39),(7,46),(10,51),(14,52),(16,49),(12,47),(11,43),(15,38)], outline)
result.poly([(12,36),(9,40),(10,46),(13,49),(14,47),(13,42),(17,37)], body_mid)
result.set(10,42,body_lit).set(11,43,body_lit)

result.poly([(22,40),(20,45),(21,51),(24,55),(28,54),(29,51),(25,51),(25,46),(27,41)], outline)
result.poly([(23,41),(22,46),(23,51),(25,53),(27,52),(24,50),(25,44),(28,40)], body_mid)
result.set(23,46,body_lit).set(24,47,body_lit)

result.poly([(37,41),(39,47),(38,52),(41,55),(45,54),(46,51),(42,52),(43,47),(41,40)], outline)
result.poly([(39,41),(41,46),(40,51),(42,53),(44,52),(42,50),(44,45),(42,39)], body_mid)
result.set(41,45,body_lit).set(42,44,body_lit)

result.poly([(50,35),(54,39),(56,45),(54,49),(50,51),(47,48),(51,47),(52,44),(49,39)], outline)
result.poly([(50,37),(53,40),(54,44),(52,47),(50,48),(52,44),(49,39)], body_mid)
result.set(52,41,body_lit).set(53,42,body_lit)

# Crown nubs add a non-human, boss-like silhouette.
result.poly([(17,16),(16,9),(20,12),(23,8),(24,16)], outline)
result.poly([(19,16),(19,12),(21,14),(23,11),(23,17)], body_mid)
result.poly([(40,15),(42,8),(45,12),(49,10),(47,18)], outline)
result.poly([(42,16),(43,11),(45,15),(47,13),(46,18)], body_mid)

# Main floating eyelid/body mass.
result.path("M6 28 Q9 17 20 13 Q31 8 43 12 Q55 15 59 27 Q57 38 47 43 Q34 48 20 44 Q9 41 6 28 Z", outline)
result.path("M9 28 Q12 19 22 15 Q32 11 43 15 Q53 18 56 27 Q53 35 45 40 Q33 44 21 41 Q12 38 9 28 Z", body_dark)

# Upper lid planes and side volume.
result.path("M10 26 Q17 15 31 14 Q45 13 54 24 Q42 19 32 20 Q21 18 10 26 Z", body_mid)
result.poly([(10,29),(14,35),(21,40),(18,35),(13,31)], body_mid)
result.poly([(54,27),(51,34),(45,39),(48,33),(53,29)], body_mid)
result.path("M15 20 Q23 14 32 14 Q43 14 49 19 Q39 16 31 17 Q22 16 15 20 Z", body_lit)
result.line(18,17,27,13,rim)
result.set(28,13,rim).set(46,18,rim).set(50,21,body_lit)

# Pale exposed eye, slightly pointed at both corners.
result.path("M10 28 Q18 20 31 19 Q45 19 55 27 Q47 36 33 39 Q19 38 10 28 Z", sclera_shade)
result.path("M13 28 Q20 22 31 21 Q44 21 52 27 Q45 33 33 36 Q21 35 13 28 Z", sclera)
result.path("M16 26 Q23 22 32 22 Q41 22 47 25 Q36 23 27 27 Q20 29 16 26 Z", sclera_light)
# Corner occlusion sells the lid overlap.
result.poly([(10,28),(15,25),(14,30),(18,34),(13,32)], body_dark)
result.poly([(55,27),(50,24),(51,29),(47,34),(52,31)], body_dark)

# Giant deep-purple iris with stepped pixel shading.
result.circle(33,28,10,iris_outer,fill=True)
result.circle(33,28,8,iris_deep,fill=True)
result.poly([(28,21),(34,19),(39,22),(42,27),(39,27),(37,23),(31,22)], iris_mid)
result.poly([(25,27),(28,23),(30,23),(28,28),(29,34),(26,32)], iris_mid)
result.poly([(37,31),(41,28),(39,34),(35,37),(32,36)], iris_mid)
result.set(29,22,iris_lit).set(30,21,iris_lit).set(27,25,iris_lit)
result.set(39,24,iris_lit).set(40,25,iris_lit).set(38,33,iris_lit)
# Radial iris flecks.
for x,y in [(33,20),(36,21),(41,27),(40,30),(36,35),(31,36),(26,31),(25,28)]:
    result.set(x,y,iris_lit)
for x,y in [(31,23),(37,24),(39,28),(36,32),(30,33),(28,29),(29,25)]:
    result.set(x,y,"#7f32aa")

# Dark pupil with a contained supernatural glow.
result.circle(33,28,4,pupil,fill=True)
result.rect(31,25,5,7,"#24072f",fill=True)
result.rect(32,26,3,5,glow,fill=True)
result.rect(33,27,2,3,glow_hot,fill=True)
result.set(32,25,"#b85be0").set(31,27,"#b85be0").set(35,30,"#b85be0")
result.set(33,26,"#ffffff").set(34,27,"#ffffff")

# Jagged lower lid, pores, and contrast pixels.
result.line(17,39,24,42,body_lit)
result.line(42,41,48,37,body_lit)
result.set(15,34,rim).set(18,39,rim).set(46,38,rim)
result.set(12,23,void).set(15,19,void).set(50,22,void).set(53,31,void)
result.set(20,15,"#b66ac0").set(22,14,"#b66ac0")
result.set(8,30,"#06030a").set(57,27,"#06030a")

view(result, scale=8, margin=0)
finish(result)
