# 64x64 fast-food combo, drawn with Astra Pixel Art API.
from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64, background="#17333a", name="fast-food-combo")

# Palette
ink = "#291b1b"
ink2 = "#452523"
table_hi = "#204650"
tray_dark = "#7d2024"
tray = "#be3030"
tray_hi = "#ed4a3f"
liner_shadow = "#d9b987"
liner = "#f6dcaa"
liner_hi = "#fff0c8"
bun_dark = "#9a4c24"
bun_mid = "#d77a32"
bun = "#eea94d"
bun_hi = "#ffd57a"
sesame = "#fff0ba"
lettuce_dark = "#387238"
lettuce = "#65a744"
cheese_dark = "#d99118"
cheese = "#ffc52f"
patty = "#6b3426"
patty_hi = "#914a2c"
fry_dark = "#c97b1f"
fry = "#f4b633"
fry_hi = "#ffd95a"
white = "#fff4dc"
cola_dark = "#53231c"
cola = "#8d3922"
ice = "#c9eff0"
ice_hi = "#f2ffff"
nugget_dark = "#9b4d23"
nugget = "#d97b2b"
nugget_hi = "#f4ad45"
sauce_dark = "#8c251c"
sauce = "#d34425"

# Sparse tabletop pixels / cast shadow.
c.rect(0, 0, 64, 64, table_hi)
c.dither(0, 0, 64, 64, ["#17333a", "#1a3a42"], pattern="checker")
c.poly([(5,31),(40,16),(63,37),(27,60),(2,43)], "#10272d")

# Isometric tray: dark bottom, red rim, inset liner.
c.poly([(3,25),(40,9),(63,29),(25,56),(3,43)], ink)
c.poly([(4,24),(40,10),(62,29),(25,54),(4,42)], tray_dark)
c.poly([(6,24),(40,12),(59,29),(25,51),(6,40)], tray_hi)
c.poly([(8,25),(39,14),(57,29),(25,49),(8,39)], tray)
c.poly([(10,26),(39,16),(54,29),(25,47),(10,38)], liner_shadow)
c.poly([(11,26),(39,17),(53,29),(25,46),(11,37)], liner)
c.line(13,28,38,19,liner_hi)
c.line(29,44,50,31,liner_hi)
c.set(12,36,liner_hi); c.set(47,29,liner_shadow)

# Rear fries: individual outlined sticks behind carton.
def fry_stick(points):
    c.poly(points, ink)
    # central golden stripe is added separately per stick

fry_stick([(35,10),(38,9),(41,24),(38,25)])
c.poly([(36,11),(37,11),(40,23),(39,23)], fry_hi)
fry_stick([(40,8),(43,8),(44,24),(41,24)])
c.poly([(41,9),(42,9),(43,23),(42,23)], fry)
fry_stick([(44,10),(47,11),(45,25),(42,24)])
c.poly([(45,11),(46,12),(44,23),(43,23)], fry_hi)
fry_stick([(48,12),(51,14),(46,27),(43,25)])
c.poly([(49,14),(50,14),(45,25),(44,25)], fry)
fry_stick([(33,14),(36,12),(41,25),(38,27)])
c.poly([(35,14),(36,14),(40,24),(39,25)], fry)
fry_stick([(51,16),(54,18),(47,28),(44,26)])
c.poly([(52,18),(53,18),(46,27),(45,26)], fry_hi)
# Red fry carton with folded top and yellow emblem.
c.poly([(34,20),(44,22),(51,18),(48,32),(40,36),(35,31)], ink)
c.poly([(36,21),(44,23),(49,20),(47,30),(40,34),(37,30)], tray)
c.poly([(36,21),(44,24),(49,20),(48,24),(44,27),(36,24)], tray_hi)
c.poly([(40,27),(43,28),(46,26),(45,30),(42,32),(40,31)], cheese)
c.set(38,27,"#f06b4f"); c.set(46,23,"#ff7160")

# Burger left: stacked irregular ovals read as an isometric sandwich.
# Back shadow / bottom bun.
c.poly([(8,31),(11,27),(21,24),(31,26),(35,30),(33,34),(23,38),(13,37),(8,34)], ink)
c.poly([(10,32),(13,29),(22,27),(31,28),(33,31),(30,34),(21,36),(13,35)], bun_dark)
c.line(14,34,27,34,bun_mid)
# Patty layer.
c.poly([(9,28),(13,25),(22,23),(31,25),(35,28),(33,32),(24,34),(14,33),(9,31)], ink)
c.poly([(11,28),(14,26),(22,25),(31,26),(33,28),(31,30),(23,32),(14,31),(11,30)], patty)
c.set(15,29,patty_hi); c.rect(19,31,7,1,patty_hi); c.set(29,28,patty_hi)
# Cheese sheet and drips.
c.poly([(10,25),(16,22),(26,22),(34,25),(32,29),(27,28),(24,32),(21,28),(14,29),(10,27)], ink)
c.poly([(12,25),(17,23),(26,23),(32,25),(30,27),(26,26),(24,30),(22,27),(15,28),(12,27)], cheese)
c.set(17,24,"#ffe15b"); c.line(26,24,30,25,"#ffe15b")
# Lettuce frill.
c.poly([(9,23),(13,20),(18,20),(21,18),(26,20),(30,19),(35,22),(33,26),(29,25),(26,27),(22,25),(18,27),(15,25),(11,26),(9,25)], ink)
c.poly([(11,23),(14,21),(18,22),(21,20),(25,22),(29,21),(33,23),(31,24),(28,23),(25,25),(22,23),(18,25),(15,23),(12,25)], lettuce)
c.set(15,22,"#91c957"); c.set(23,22,"#91c957"); c.set(29,22,lettuce_dark)
# Top bun, domed and sesame-speckled.
c.poly([(10,22),(11,18),(15,14),(21,12),(28,13),(33,16),(35,20),(33,23),(27,25),(18,25),(12,23)], ink)
c.poly([(12,21),(13,18),(17,15),(22,14),(28,15),(32,17),(33,20),(31,22),(26,23),(18,23),(14,22)], bun)
c.poly([(14,18),(18,15),(24,14),(29,16),(31,18),(27,18),(22,17),(17,19)], bun_hi)
c.line(14,21,31,21,bun_mid)
# sesame seeds
for x,y in [(17,18),(21,16),(25,17),(29,18),(20,20),(27,20)]:
    c.set(x,y,sesame)
c.set(18,17,bun_dark); c.set(26,16,bun_dark)

# Nugget cluster in front center, each with a chunky outline.
def draw_nugget(poly, inner, highlights):
    c.poly(poly, ink)
    c.poly(inner, nugget)
    for x,y in highlights: c.set(x,y,nugget_hi)

draw_nugget([(17,39),(20,36),(25,36),(28,39),(27,43),(24,45),(19,44),(16,42)],
       [(19,39),(21,37),(25,38),(26,40),(25,42),(21,43),(18,41)], [(21,38),(24,39),(20,41)])
draw_nugget([(26,37),(30,34),(35,35),(37,38),(35,42),(31,43),(27,41)],
       [(28,37),(31,36),(34,37),(35,39),(33,41),(30,41),(28,40)], [(31,37),(34,39)])
draw_nugget([(28,44),(31,41),(36,41),(39,44),(38,48),(34,50),(29,48)],
       [(30,44),(32,42),(36,43),(37,45),(35,48),(31,47)], [(33,43),(36,45),(32,47)])

# Dipping sauce cups near front edge.
c.poly([(11,42),(16,40),(22,42),(22,46),(18,49),(12,47)], ink)
c.poly([(13,42),(17,41),(20,42),(20,45),(17,47),(13,46)], white)
c.poly([(13,42),(17,41),(20,42),(17,45),(13,44)], sauce_dark)
c.poly([(14,42),(17,42),(19,42),(17,44),(14,44)], sauce)
c.set(15,42,"#ef6840")
# A second smaller cup with golden mustard, tucked along the front rim.
c.poly([(19,47),(23,45),(28,47),(28,51),(24,54),(19,52)], ink)
c.poly([(21,47),(24,46),(27,47),(26,50),(24,52),(21,51)], white)
c.poly([(21,47),(24,46),(27,47),(24,50),(21,49)], fry_dark)
c.poly([(22,47),(24,47),(26,47),(24,49),(22,49)], cheese)
# Crisp breading flecks on the exposed nugget faces.
c.set(19,40,nugget_dark); c.set(23,42,"#f7c064")
c.set(29,39,nugget_dark); c.set(33,38,"#f7c064")
c.set(31,45,nugget_dark); c.set(35,46,"#f7c064")

# Cola cup on right, in front of tray contents.
# Straw behind lid.
c.line(52,23,56,13,ink); c.line(53,23,57,13,white); c.set(57,13,tray_hi); c.set(56,16,tray_hi); c.set(55,19,tray_hi)
# cup body outline and body.
c.poly([(45,31),(58,31),(57,48),(54,53),(47,52),(44,47)], ink)
c.poly([(47,33),(56,33),(55,47),(53,51),(48,50),(46,46)], white)
c.poly([(47,36),(56,36),(55,47),(53,50),(48,49),(46,45)], cola_dark)
c.poly([(48,38),(55,38),(54,46),(52,48),(48,47),(47,44)], cola)
# Ice cubes and cola highlights.
c.poly([(48,35),(50,33),(53,34),(52,37)], ice)
c.poly([(52,34),(55,33),(56,36),(53,37)], ice_hi)
c.set(49,36,ice_hi); c.set(54,39,"#c16a35"); c.set(49,42,"#c16a35"); c.set(53,45,"#6c291d")
# lid rim.
c.poly([(44,29),(47,27),(56,27),(59,30),(58,34),(55,36),(48,35),(44,33)], ink)
c.poly([(46,30),(48,28),(55,28),(57,30),(56,33),(54,34),(48,33),(46,32)], white)
c.poly([(48,30),(55,29),(56,31),(54,32),(49,32),(47,31)], ice)
c.line(48,29,55,29,ice_hi)

# Final selective dark pixels strengthen silhouettes without blanket outlining.
c.set(5,39,ink2); c.set(24,53,ink); c.set(58,29,ink)
c.set(41,35,ink2); c.set(43,34,tray_dark)

view(c, scale=8, margin=0)
finish(c)
