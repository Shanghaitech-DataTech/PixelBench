# 32x32 laboratory microscope icon
result = new_canvas(32, 32, background=None, name="laboratory-microscope-icon")

# Compact cool-metal palette.
outline = "#17212b"
deep = "#263644"
shadow = "#3f5666"
steel = "#698292"
light = "#a9bdc5"
highlight = "#d9e5e5"
blue = "#4f8295"
blue_hi = "#79a9b5"
black = "#0c1219"
glass = "#9bd4da"

# Rear curved arm, the main three-quarter-view support.
result.poly([(15,7),(20,7),(24,10),(27,15),(27,20),(25,24),(22,27),(17,27),(15,23),(18,21),(20,21),(22,19),(22,16),(20,13),(17,12),(13,11)], outline)
result.poly([(17,9),(20,9),(23,12),(25,16),(25,20),(23,23),(21,25),(18,25),(17,23),(20,22),(22,20),(23,17),(22,14),(19,11),(16,11)], shadow)
result.poly([(21,10),(23,12),(25,16),(25,20),(23,23),(22,22),(23,19),(23,15),(21,12)], steel)
result.set(23,12,light).set(24,16,light).set(24,17,light)

# Eyepiece rim, viewed from above-left.
result.poly([(5,2),(11,2),(13,4),(11,7),(6,6),(4,4)], outline)
result.poly([(6,3),(10,3),(11,4),(10,5),(6,5),(5,4)], deep)
result.rect(6,3,4,1,steel)
result.set(6,3,light).set(10,4,black)

# Slanted optical body tube.
result.poly([(10,5),(14,5),(20,10),(18,14),(15,15),(9,9)], outline)
result.poly([(11,6),(14,6),(18,10),(17,12),(15,13),(10,8)], blue)
result.poly([(12,6),(14,7),(17,10),(16,11),(11,8)], blue_hi)
result.line(11,6,15,10,light)
result.set(12,8,highlight).set(15,12,deep).set(17,12,deep)

# Focus assembly on the outer face.
result.circle(20,11,3,outline)
result.circle(20,11,2,steel)
result.set(19,10,light).set(20,10,light).set(21,11,shadow).set(20,12,deep)
result.circle(23,12,1,outline)
result.set(23,11,steel).set(23,12,light)

# Revolving nosepiece and objective lenses.
result.poly([(14,13),(19,13),(20,15),(18,17),(13,16),(12,15)], outline)
result.poly([(14,14),(18,14),(19,15),(17,16),(13,15)], steel)
result.set(14,14,light).set(15,14,light)
# Two objectives at slightly different depths.
result.poly([(17,16),(20,16),(19,20),(17,20)], outline)
result.rect(18,17,1,2,light)
result.poly([(13,15),(16,16),(15,20),(12,20)], outline)
result.poly([(14,16),(15,17),(14,19),(13,19)], light)
result.rect(12,19,3,1,black)
result.set(13,19,glass)

# Mechanical stage with projecting left edge.
result.poly([(6,18),(20,18),(23,20),(21,22),(7,22),(4,20)], outline)
result.poly([(7,19),(19,19),(21,20),(20,20),(7,20),(5,20)], steel)
result.line(8,19,17,19,light)
result.rect(8,21,12,1,deep)
# Slide and stage clips.
result.rect(9,18,7,1,highlight)
result.rect(10,19,5,1,"#b9dfe0")
result.set(9,19,glass).set(15,19,glass)
result.line(7,18,10,18,outline)
result.line(17,18,20,19,outline)

# Lower pillar and hinge into the base.
result.poly([(18,21),(23,21),(23,25),(20,28),(15,28),(15,25)], outline)
result.poly([(19,22),(22,22),(21,25),(19,26),(17,26),(17,25)], shadow)
result.set(21,22,steel).set(20,23,light)

# Heavy perspective base.
result.poly([(8,24),(19,24),(28,28),(27,30),(7,30),(3,28)], outline)
result.poly([(9,25),(18,25),(25,28),(24,29),(8,29),(5,28)], shadow)
result.poly([(10,25),(18,25),(23,27),(8,27),(6,28),(5,28)], steel)
result.line(10,25,18,25,light)
result.line(8,27,23,27,deep)
result.set(7,28,blue).set(8,28,blue).set(24,28,deep)
# Feet and final corner accents.
result.rect(7,30,4,1,black)
result.rect(23,30,3,1,black)
result.set(4,28,deep).set(27,28,deep)

view(result, scale=16, margin=0)
finish(result)
