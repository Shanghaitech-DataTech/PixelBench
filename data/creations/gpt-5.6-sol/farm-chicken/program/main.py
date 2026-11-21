from pixelbench_api import new_canvas, view, finish

# Cozy 32px farm chicken, side view facing right.
c = new_canvas(32, 32, background=None, name="farm-chicken")

outline = "#5b3b32"
deep = "#7a4b37"
shadow = "#b97850"
mid = "#d99b69"
cream = "#f2cf94"
light = "#ffe3aa"
highlight = "#fff0c2"
red_dark = "#9f3f3c"
red = "#c95b4f"
beak_dark = "#b96737"
beak = "#e39a4a"
feet = "#c8793d"
eye = "#302a29"

# Tail feathers, layered behind the body.
c.poly([(5,12),(2,9),(3,15),(1,14),(4,19),(7,19),(9,16)], outline)
c.poly([(5,13),(3,11),(4,16),(3,16),(5,18),(8,17)], deep)
c.set(4,13,mid)
c.set(5,15,mid)

# Main plump body silhouette.
c.poly([(7,11),(10,8),(17,7),(22,9),(25,13),(26,18),(24,22),(20,25),(13,26),(8,24),(5,20),(5,15)], outline)
# Body base, inset to preserve a one-pixel handmade outline.
c.poly([(8,12),(11,9),(17,8),(21,10),(24,13),(25,18),(23,21),(19,24),(13,25),(9,23),(6,20),(6,15)], cream)
# Warm lower-body shadow.
c.poly([(6,18),(9,21),(13,23),(19,23),(23,20),(24,18),(24,21),(20,24),(13,25),(9,23),(6,20)], mid)
c.set(8,21, shadow)
c.set(10,23, shadow)
c.set(21,22, shadow)
# Back and breast highlights.
c.poly([(10,10),(15,8),(19,9),(21,11),(17,10),(13,11),(10,14),(7,15),(8,12)], light)
c.poly([(20,11),(23,14),(24,17),(23,19),(22,15),(20,13)], light)
c.set(13,9, highlight)
c.set(14,9, highlight)
c.set(8,14, highlight)
c.set(23,16, highlight)

# Rounded wing with scalloped lower edge.
c.poly([(9,15),(11,12),(16,11),(20,13),(21,16),(19,20),(16,22),(12,21),(9,19)], outline)
c.poly([(10,15),(12,13),(16,12),(19,14),(20,16),(18,19),(16,21),(12,20),(10,18)], mid)
c.poly([(11,15),(13,13),(16,13),(18,14),(18,16),(15,16),(13,18),(11,18)], light)
c.set(12,19, shadow)
c.set(15,20, shadow)
c.set(18,18, shadow)
c.set(16,17, cream)
c.set(17,17, cream)

# Head bump and face, integrated into body.
c.poly([(18,8),(19,5),(22,4),(25,6),(26,9),(25,13),(23,15),(20,13)], outline)
c.poly([(19,8),(20,6),(22,5),(24,6),(25,9),(24,12),(22,14),(20,12)], light)
c.set(20,7, highlight)
c.set(21,6, highlight)

# Comb: three soft lobes.
c.poly([(19,5),(18,3),(19,2),(21,4),(21,2),(22,1),(23,2),(23,4),(25,3),(26,4),(25,6),(22,6)], outline)
c.poly([(20,5),(19,3),(20,4),(21,5),(22,2),(22,5),(24,4),(24,5)], red)
c.set(22,3,"#df7463")

# Face details.
c.set(23,7, eye)
c.set(23,8, "#f9d98e")
# Beak points right.
c.poly([(25,8),(29,10),(25,11)], outline)
c.poly([(26,9),(28,10),(26,10)], beak)
c.set(26,10, beak_dark)
# Wattle under the beak.
c.poly([(24,11),(26,12),(25,15),(23,14),(23,12)], red_dark)
c.set(24,12, red)
c.set(24,13, red)

# Slim legs and separated three-toed feet.
c.set(12,25, outline)
c.set(13,25, outline)
c.set(13,26, feet)
c.set(13,27, feet)
c.set(12,28, outline)
c.set(13,28, feet)
c.set(14,28, feet)
c.set(10,29, feet)
c.set(11,29, feet)
c.set(12,29, feet)
c.set(14,29, feet)
c.set(15,29, feet)
c.set(16,29, feet)

c.set(20,24, outline)
c.set(21,24, outline)
c.set(20,25, feet)
c.set(20,26, feet)
c.set(20,27, feet)
c.set(19,28, feet)
c.set(20,28, feet)
c.set(21,28, feet)
c.set(17,29, feet)
c.set(18,29, feet)
c.set(19,29, feet)
c.set(21,29, feet)
c.set(22,29, feet)
c.set(23,29, feet)

# A few deliberate single-pixel texture accents.
c.set(7,18, light)
c.set(8,19, cream)
c.set(19,10, cream)
c.set(22,20, cream)

result = c
view(result, scale=16, margin=0)
finish(result)
