# Vintage hand-crank sewing machine; native 48 x 48 pixel art.
result = new_canvas(48, 48, name='vintage-sewing-machine')
c = result
ink = '#151c25'
black = '#212b32'
shade = '#2e3d43'
mid = '#485e64'
light = '#738b8a'
steel = '#acbdb3'
glint = '#e0e4ca'
gold_dark = '#785a35'
gold = '#b68c4c'
gold_light = '#e5c77d'
wood_dark = '#4a2d2c'
wood = '#7d4936'
wood_light = '#ae7047'
red_dark = '#692738'
red = '#ac3041'
red_light = '#df4c51'
red_glint = '#f57c68'

# Walnut plinth in shallow perspective.
c.poly([(3,32),(12,28),(40,29),(45,32),(45,36),(35,42),(3,38)], ink)
c.poly([(4,34),(35,38),(35,41),(4,37)], wood)
c.poly([(35,38),(44,33),(44,36),(35,41)], wood_dark)
c.line(5,37,33,40,wood_light)
c.line(36,39,43,35,wood)
c.poly([(4,32),(12,29),(40,30),(43,32),(35,37),(4,34)], wood_light)
# Enameled bed, brass border and inset steel needle plate.
c.poly([(5,32),(13,29),(39,30),(41,32),(34,36),(5,34)], black)
c.line(6,34,33,36,gold_dark)
c.line(34,35,39,32,gold)
c.line(7,32,13,30,mid)
c.poly([(8,31),(14,29),(21,30),(16,33),(8,33)], mid)
c.line(9,32,15,30,steel)
c.set(17,31,ink)

# Handwheel: offset rim thickness, then the visible spoked face.
c.ellipse(37,17,7,8,ink)
c.ellipse(38,17,6,8,shade)
c.ellipse(39,17,5,7,light)
c.ellipse(39,17,4,6,None)
c.line(38,12,39,17,mid)
c.line(42,14,39,17,steel)
c.line(42,21,39,17,mid)
c.line(37,22,39,17,steel)
c.line(35,16,39,17,mid)
c.ellipse(39,17,2,2,black)
c.set(39,16,glint)
c.set(40,17,steel)
c.line(38,10,40,10,steel)
c.line(43,13,43,16,steel)
c.line(42,22,40,24,mid)

# Spool pin and ivory-gold thread spool.
c.line(25,4,25,10,ink)
c.rect(22,5,7,2,ink)
c.rect(23,7,5,4,gold)
c.line(23,7,27,7,gold_light)
c.line(23,9,27,9,gold_dark)
c.rect(22,10,7,2,ink)
c.line(23,10,27,10,gold_light)

# Main cast-iron silhouette, with a curved arm and flared pillar.
c.poly([(8,14),(9,12),(12,10),(17,10),(19,11),(28,10),(32,11),(35,14),(36,19),(35,27),(37,29),(38,31),(35,33),(27,32),(25,30),(28,28),(28,23),(27,21),(24,19),(17,19),(16,23),(10,24),(8,22)],ink)
# Right-facing bevel and upright.
c.poly([(30,12),(33,13),(35,16),(35,25),(34,28),(36,30),(33,31),(30,29),(31,20)],shade)
c.line(34,17,34,25,mid)
c.line(33,28,35,30,mid)
# Front enamel surface.
c.poly([(10,14),(12,12),(17,12),(19,13),(28,12),(30,14),(31,17),(30,22),(30,28),(28,30),(32,31),(27,30),(29,27),(29,22),(27,19),(23,17),(16,17),(14,21),(10,22)],black)
c.line(12,11,17,11,mid)
c.line(19,12,27,11,mid)
c.line(28,12,31,14,light)
c.line(10,14,10,19,mid)
# Fine gold filigree along the arm and pillar.
c.line(17,14,25,14,gold_dark)
c.line(18,14,23,14,gold)
c.set(20,15,gold_dark)
c.set(21,16,gold_light)
c.set(22,15,gold_dark)
c.set(24,13,gold)
c.set(26,14,gold_light)
c.line(27,15,29,17,gold)
c.line(30,19,30,25,gold_dark)
c.set(30,21,gold)
c.line(28,29,31,30,gold)
c.line(29,31,35,31,gold_dark)
c.set(32,30,gold_light)
# Head face plate, screw and tension assembly.
c.poly([(9,14),(12,12),(14,13),(14,21),(12,23),(9,22)],shade)
c.line(10,14,10,20,light)
c.line(12,14,12,20,mid)
c.set(11,13,steel)
c.set(11,21,steel)
c.rect(14,17,3,3,ink)
c.set(15,17,gold_light)
c.set(16,18,gold)
c.set(15,19,gold_dark)
# Upper thread path and take-up lever.
c.line(24,11,18,12,steel)
c.line(18,12,16,15,steel)
c.line(16,15,15,17,gold_light)
c.line(8,14,7,16,ink)
c.set(7,15,steel)

# Red cloth under the foot, spreading over the bed and folding over the edge.
c.poly([(12,30),(18,29),(23,31),(28,32),(26,35),(27,40),(24,43),(20,41),(18,39),(17,35),(11,33)],red_dark)
c.poly([(13,30),(18,30),(21,31),(26,32),(23,34),(19,35),(13,33)],red_light)
c.line(14,31,20,32,red_glint)
c.poly([(18,34),(23,34),(24,36),(25,41),(23,42),(20,40),(19,38)],red)
c.poly([(20,35),(22,35),(22,38),(24,41),(22,40),(21,38)],red_light)
c.line(25,35,25,38,red_dark)
c.line(18,33,22,32,red)
c.set(23,32,red_glint)
# Needle bar, fine needle, and separate presser mechanism in front of the cloth.
c.rect(10,23,3,3,ink)
c.line(11,23,11,27,steel)
c.set(12,25,glint)
c.line(11,28,11,30,steel)
c.set(11,31,glint)
c.line(14,23,14,28,ink)
c.line(15,23,15,28,mid)
c.line(14,28,13,30,steel)
c.line(12,31,16,31,ink)
c.line(13,30,16,30,glint)
c.set(16,29,light)

view(result, scale=8, margin=0)
save('vintage-sewing-machine', result)
finish(result)
