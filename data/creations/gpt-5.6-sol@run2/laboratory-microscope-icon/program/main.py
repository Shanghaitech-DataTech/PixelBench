# 32x32 laboratory microscope icon, transparent background
c = new_canvas(32, 32, background=None, name="laboratory-microscope-icon")

# Compact palette
outline = c.color("#17202b", "outline")
deep = c.color("#263746", "deep")
shadow = c.color("#385064", "shadow")
steel = c.color("#607b8d", "steel")
light = c.color("#9bb2bd", "light")
shine = c.color("#d9e5e7", "shine")
blue = c.color("#3b8fbd", "blue")
blue_hi = c.color("#76c6dd", "blue highlight")
gold = c.color("#d49a3a", "brass")
gold_hi = c.color("#ffd271", "brass highlight")

# Rear foot / base three-quarter silhouette
c.poly([(8,25),(21,25),(28,28),(27,30),(8,30),(4,28)], outline)
c.poly([(9,25),(21,25),(26,28),(8,28),(5,27)], steel)
c.poly([(8,28),(26,28),(25,29),(8,29),(5,28)], shadow)
c.line(10,26,20,26,light)
c.set(7,27,shine)

# Upright curved arm: dark outer silhouette then inset face
c.poly([(22,8),(26,9),(27,12),(26,18),(23,24),(20,26),(16,26),
        (16,23),(19,22),(21,18),(22,14),(21,11)], outline)
c.poly([(23,9),(25,10),(25,14),(24,18),(21,23),(19,24),(17,24),
        (20,21),(22,17),(23,13)], blue)
c.poly([(24,10),(25,11),(24,16),(21,21),(20,21),(22,16),(23,12)], blue_hi)
c.line(22,22,20,24,shadow)

# Focus knob behind tube
c.circle(23,14,3,outline)
c.circle(23,14,2,gold)
c.set(23,13,gold_hi)
c.set(24,14,"#a96c27")

# Angled body tube outer profile
c.poly([(8,3),(13,3),(21,11),(21,14),(18,16),(15,14),(15,12),(9,7),(7,7)], outline)
# tube side plane
c.poly([(11,5),(13,4),(20,11),(20,13),(18,14),(17,12)], shadow)
# tube main plane
c.poly([(9,4),(12,4),(18,10),(16,12),(9,6)], light)
c.poly([(9,4),(11,4),(17,10),(16,11),(9,5)], shine)
c.line(12,6,17,11,steel)

# Eyepiece, stepped and tilted
c.poly([(5,2),(11,2),(13,4),(10,7),(7,7),(5,5)], outline)
c.poly([(6,3),(10,3),(11,4),(9,6),(7,6),(6,5)], deep)
c.line(6,3,10,3,steel)
c.set(7,4,light)

# Nosepiece and objectives
c.poly([(16,12),(21,12),(22,15),(20,17),(16,16),(14,14)], outline)
c.poly([(16,13),(20,13),(21,15),(19,16),(16,15),(15,14)], steel)
c.set(17,13,shine)
# objective barrels
c.poly([(16,15),(19,16),(18,20),(16,20),(15,19)], outline)
c.poly([(17,16),(18,16),(17,19),(16,19)], gold)
c.set(17,16,gold_hi)
c.poly([(20,15),(22,16),(21,19),(19,19)], outline)
c.poly([(20,16),(21,16),(20,18)], light)

# Stage with projected right side
c.poly([(6,18),(20,18),(24,20),(22,22),(6,22),(4,20)], outline)
c.poly([(6,18),(20,18),(22,20),(6,20),(5,19)], steel)
c.line(7,19,18,19,shine)
c.poly([(6,20),(22,20),(21,21),(6,21),(5,20)], deep)
# slide and sample
c.rect(9,17,8,1,shine)
c.rect(11,16,5,1,"#bdebf0")
c.set(13,16,blue)
c.set(14,16,blue_hi)

# Stage controls / lower hinge
c.rect(7,22,2,3,outline)
c.rect(8,22,1,2,gold)
c.circle(15,24,2,outline)
c.circle(15,24,1,steel)
c.set(15,23,light)

# Ground-contact accents
c.rect(8,29,5,1,deep)
c.rect(22,29,3,1,deep)

result = c
view(result, scale=16, margin=0)
finish(result)
