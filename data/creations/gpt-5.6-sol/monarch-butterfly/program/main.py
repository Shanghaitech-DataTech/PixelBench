from pixelbench_api import *

# 32x32 monarch butterfly sprite on transparent background.
result = new_canvas(32, 32, background=None, name="monarch_butterfly")

black = result.color("#17131a", "black")
dark = result.color("#3a2020", "dark_brown")
orange = result.color("#e66b20", "monarch_orange")
light = result.color("#f89a32", "sunlit_orange")
shade = result.color("#a83c19", "wing_shadow")
cream = result.color("#fff4d2", "cream_spot")
gray = result.color("#978c83", "body_highlight")

# Dark outer wing silhouette: broad upper wings, scalloped lower wings.
left_outer = [
    (14,10),(12,7),(10,4),(7,2),(4,2),(2,4),(1,7),(1,11),
    (2,14),(4,16),(3,18),(3,22),(5,25),(8,27),(11,26),(13,23),
    (14,19)
]
right_outer = [(31-x, y) for x, y in left_outer]
result.poly(left_outer, black)
result.poly(right_outer, black)

# Orange upper wing cells, inset to leave a heavy black rim.
result.poly([(13,10),(11,7),(9,5),(7,4),(5,4),(3,6),(3,10),(4,13),(7,15),(10,14)], orange)
result.poly([(18,10),(20,7),(22,5),(24,4),(26,4),(28,6),(28,10),(27,13),(24,15),(21,14)], orange)
# Warm highlight panels.
result.poly([(11,8),(9,6),(7,5),(5,5),(4,7),(4,10),(5,12),(8,13)], light)
result.poly([(20,8),(22,6),(24,5),(26,5),(27,7),(27,10),(26,12),(23,13)], light)
# Lower orange wings.
result.poly([(13,17),(11,16),(8,17),(6,18),(5,21),(6,23),(8,25),(10,24),(12,22)], orange)
result.poly([(18,17),(20,16),(23,17),(25,18),(26,21),(25,23),(23,25),(21,24),(19,22)], orange)
result.poly([(11,18),(8,18),(6,20),(6,22),(8,24),(10,23)], shade)
result.poly([(20,18),(23,18),(25,20),(25,22),(23,24),(21,23)], shade)

# Characteristic monarch vein network.
for pts in [
    [(14,11),(10,9),(4,7)], [(13,13),(9,12),(3,11)], [(12,15),(8,14),(5,15)],
    [(12,16),(9,19),(8,24)], [(13,17),(12,22),(10,25)], [(18,11),(22,9),(28,7)],
    [(18,13),(22,12),(28,11)], [(19,15),(23,14),(26,15)],
    [(19,16),(22,19),(23,24)], [(18,17),(19,22),(21,25)]
]:
    for a, b in zip(pts, pts[1:]):
        result.line(a[0], a[1], b[0], b[1], black)

# Reopen orange cells after the strong one-pixel veins, including cells near the thorax.
result.poly([(13,11),(11,10),(10,12),(10,14),(12,15),(13,14)], orange)
result.poly([(18,11),(20,10),(21,12),(21,14),(19,15),(18,14)], orange)
result.poly([(13,18),(11,18),(10,20),(11,22),(13,21)], shade)
result.poly([(18,18),(20,18),(21,20),(20,22),(18,21)], shade)
result.set(9,8, light).set(8,11, light).set(6,9, light)
result.set(22,8, light).set(23,11, light).set(25,9, light)
result.set(9,20, orange).set(10,21, orange)
result.set(22,20, orange).set(21,21, orange)
# Crisp inner veins separate those cells from the body.
result.line(13,11,13,15,black).line(18,11,18,15,black)
result.line(13,18,13,22,black).line(18,18,18,22,black)

# Cream border spots on the black tips and lower scallops.
spots = [(3,5),(6,3),(9,5),(2,8),(3,12),(5,14),(4,19),(5,23),(8,25),
         (28,5),(25,3),(22,5),(29,8),(28,12),(26,14),(27,19),(26,23),(23,25)]
for x, y in spots:
    result.set(x, y, cream)
# Slightly larger signature spots near the upper tips.
result.rect(5,5,2,1,cream).rect(25,5,2,1,cream)
result.set(3,9, cream).set(28,9, cream)

# Body and head sit cleanly above both wings.
result.circle(16,8,2,black)
result.rect(14,10,4,10,black)
result.rect(15,19,2,7,black)
result.set(15,11,gray).set(15,14,gray).set(15,17,gray).set(15,20,gray)
# Tapered abdomen tip.
result.set(15,26,black).set(16,26,black).set(16,27,black)
# Fine antennae with hooked tips.
result.line(15,7,12,3,black)
result.line(16,7,19,3,black)
result.set(11,3,black).set(12,2,black)
result.set(20,3,black).set(19,2,black)
# Tiny eye glints keep the head readable at native scale.
result.set(15,7,cream).set(17,7,cream)

# Inspect against a neutral backing while keeping the submitted canvas transparent.
proof_bg = new_canvas(32, 32, background="#d9d3c7", name="proof_background")
proof = flatten([proof_bg, result], name="proof")
view(proof, scale=16, margin=0)
finish(result)
