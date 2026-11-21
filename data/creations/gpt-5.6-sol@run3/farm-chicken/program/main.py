# 32x32 cozy farm chicken sprite
result = new_canvas(32, 32, background=None, name="farm-chicken")

# Warm muted palette
outline = "#51372f"
deep = "#765044"
shadow = "#b87857"
mid = "#d99a6c"
cream = "#f1c98b"
light = "#ffe1a8"
highlight = "#fff0c2"
comb_dark = "#a94f48"
comb = "#cf6257"
comb_light = "#e77b68"
beak_dark = "#a9683d"
beak = "#e2a451"
eye = "#342a28"
leg_dark = "#9b623b"
leg = "#c88144"

# Tail silhouette: layered, softly stepped feathers
result.poly([(5,15),(2,12),(3,18),(1,18),(5,22),(8,23),(10,18)], outline)
result.poly([(6,16),(3,14),(4,18),(3,19),(7,21),(9,20),(9,17)], shadow)
result.set(4,16,mid).set(5,17,mid).set(5,18,mid)

# Main plump body silhouette
result.poly([(8,13),(13,11),(19,12),(23,15),(25,20),(24,24),(21,27),(15,29),(9,28),(5,25),(4,20),(5,16)], outline)
# Body fill, leaving a one-pixel dark contour
result.poly([(8,14),(13,12),(18,13),(22,15),(24,19),(23,23),(20,26),(15,28),(10,27),(6,24),(5,20),(6,16)], cream)

# Warm lower-body shading
result.poly([(5,21),(8,24),(12,25),(17,25),(21,23),(23,20),(23,24),(20,26),(15,28),(10,27),(6,24)], mid)
result.poly([(8,25),(12,27),(17,27),(20,25),(20,27),(15,29),(9,28),(6,25)], shadow)
result.set(6,22,shadow).set(7,23,shadow).set(8,24,shadow)

# Neck rising into the head silhouette
result.poly([(18,15),(18,10),(20,7),(24,6),(27,8),(28,12),(27,16),(24,19),(20,19)], outline)
result.poly([(20,15),(19,11),(21,8),(24,7),(26,9),(27,12),(26,15),(24,17),(21,18)], light)
# Blend neck into body
result.poly([(18,14),(21,15),(23,18),(22,21),(18,23),(16,18)], cream)
result.set(19,12,highlight).set(20,10,highlight).set(21,9,highlight)

# Comb with rounded pixel lobes
result.rect(20,5,2,3,outline)
result.rect(22,3,3,5,outline)
result.rect(25,4,2,5,outline)
result.set(21,4,outline).set(24,3,outline).set(27,6,outline).set(27,7,outline)
result.rect(21,5,2,2,comb)
result.rect(23,4,2,3,comb_light)
result.rect(25,5,2,3,comb)
result.set(22,4,comb).set(24,4,comb_light).set(26,6,comb_light)

# Face, eye and brow pixel
result.set(25,10,deep)
result.set(25,11,eye)
result.set(24,10,highlight)

# Beak, clear side profile
result.poly([(27,11),(31,13),(27,14)], outline)
result.poly([(27,12),(30,13),(27,13)], beak)
result.set(28,14,beak_dark)

# Small wattle beneath beak
result.set(26,15,outline).set(27,15,outline).set(26,16,outline)
result.set(26,15,comb).set(26,16,comb_dark)

# Rounded wing with dark lower rim
result.poly([(9,17),(12,15),(17,16),(20,19),(19,23),(16,25),(11,24),(8,21)], deep)
result.poly([(10,17),(13,16),(17,17),(19,19),(18,22),(16,23),(12,23),(9,21)], shadow)
result.poly([(11,17),(15,17),(18,19),(17,21),(14,22),(10,20)], mid)
# Wing feather scallops / highlights
result.set(11,18,light).set(12,18,light).set(13,17,light)
result.set(11,21,cream).set(14,22,deep).set(17,21,cream)
result.line(12,23,16,23,deep)

# Body highlights and sparse farm-game texture pixels
result.set(8,16,light).set(9,15,light).set(10,14,highlight)
result.set(7,18,light).set(6,19,mid)
result.set(20,16,highlight).set(21,17,highlight)
result.set(8,22,cream).set(20,23,shadow)

# Legs, separated and sturdy
result.rect(11,28,2,2,leg_dark)
result.set(12,28,leg)
result.rect(19,27,2,3,leg_dark)
result.set(19,28,leg)
# Feet with dark anchor pixels
result.line(9,30,13,30,outline)
result.set(11,29,leg).set(10,30,leg).set(12,30,leg)
result.line(17,30,22,30,outline)
result.set(19,29,leg).set(18,30,leg).set(19,30,leg).set(21,30,leg)

view(result, scale=16, margin=0)
finish(result)
