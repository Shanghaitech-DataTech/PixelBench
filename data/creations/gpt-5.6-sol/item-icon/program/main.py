# Ancient golden compass inventory icon, 32x32.
result = new_canvas(32, 32, background=None, name="ancient_golden_compass")

# Compact, high-contrast palette.
outline = "#17131b"
outline_hi = "#2b1b20"
shadow = "#5a321b"
bronze = "#855020"
gold_dark = "#a96822"
gold = "#d69a2f"
gold_light = "#f2c653"
highlight = "#ffe58a"
patina = "#60734f"
blue_dark = "#12395f"
blue = "#176fa1"
blue_light = "#35b9d1"
blue_glint = "#9bf4e8"

# Four cardinal finials form the outer silhouette.
result.poly([(12,7),(14,1),(16,1),(18,7),(17,10),(13,10)], outline)
result.poly([(12,25),(14,31),(16,31),(18,25),(17,22),(13,22)], outline)
result.poly([(7,13),(1,15),(1,17),(7,19),(10,18),(10,14)], outline)
result.poly([(23,13),(29,15),(29,17),(23,19),(20,18),(20,14)], outline)

# Heavy outer casing and stepped antique-gold ring.
result.circle(15,16,12,outline)
result.circle(15,16,10,shadow)
result.circle(15,16,9,gold_dark)
result.circle(15,16,8,gold)
result.circle(15,16,6,outline_hi)
result.circle(15,16,5,bronze)

# Blocked highlights and shadows give the raised ring depth.
result.set(10,8,gold_light).set(11,7,gold_light).set(12,7,gold_light)
result.set(18,7,gold_light).set(19,8,gold_light).set(20,9,gold_light)
result.set(7,13,gold_light).set(7,14,gold_light).set(8,11,gold_light)
result.set(8,20,bronze).set(9,22,bronze).set(11,24,bronze)
result.set(19,24,shadow).set(21,22,shadow).set(23,19,shadow)
result.set(23,13,bronze).set(22,11,gold_dark)

# Gold insets on the cardinal points.
result.poly([(14,7),(15,3),(16,7),(15,9)], gold)
result.set(15,3,highlight).set(15,4,gold_light)
result.poly([(14,25),(15,29),(16,25),(15,23)], gold_dark)
result.poly([(7,15),(3,16),(7,17),(9,16)], gold)
result.set(4,16,gold_light)
result.poly([(23,15),(27,16),(23,17),(21,16)], gold_dark)
result.set(26,16,gold)

# Tiny engraved studs and aged patina marks.
for x,y,c in [
    (10,10,highlight),(20,10,gold_light),(9,12,bronze),(21,12,shadow),
    (8,16,highlight),(22,16,gold),(10,22,gold_dark),(20,22,shadow),
    (12,24,patina),(7,18,patina),(22,14,patina)
]:
    result.set(x,y,c)

# Four-point compass needle beneath the crystal, with dark edging.
result.poly([(14,15),(15,9),(17,15),(21,16),(17,17),(15,23),(13,17),(9,16)], outline)
result.poly([(14,15),(15,10),(16,15),(15,16)], gold_light)
result.poly([(16,16),(20,16),(16,17),(15,16)], gold)
result.poly([(14,16),(15,17),(15,22),(13,17)], gold_dark)
result.poly([(10,16),(14,15),(15,16),(14,17)], highlight)

# Faceted blue crystal centre, outlined as a clear focal jewel.
result.poly([(15,12),(19,15),(18,19),(15,21),(11,18),(11,15)], outline)
result.poly([(15,13),(18,15),(17,18),(15,20),(12,18),(12,15)], blue_dark)
result.poly([(15,13),(18,15),(15,16),(12,15)], blue_light)
result.poly([(12,15),(15,16),(15,20),(12,18)], blue)
result.poly([(15,16),(18,15),(17,18),(15,20)], "#15527f")
result.set(14,14,blue_glint).set(13,15,blue_light)

# A few deliberate outline pixels square off the silhouette at icon scale.
result.set(13,2,outline).set(17,2,outline)
result.set(2,14,outline).set(2,18,outline)
result.set(28,14,outline).set(28,18,outline)
result.set(13,30,outline).set(17,30,outline)

view(result, scale=16, margin=0)
finish(result)
