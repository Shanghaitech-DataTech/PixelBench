result = new_canvas(32, 32, name='e-scooter-rider')
c = result
ink = '#202b40'
steel = '#617e91'
light = '#b8d6df'
skin = '#edb38a'
shade = '#bd7865'
# Small wheels and distinct low standing deck.
c.circle(7,27,3,ink)
c.circle(25,27,3,ink)
c.circle(7,27,1,steel)
c.circle(25,27,1,steel)
c.set(7,26,light)
c.set(25,26,light)
c.line(7,24,10,24,ink)
c.rect(9,24,14,3,ink)
c.line(10,24,21,24,'#8bd8cb')
c.line(10,25,22,25,'#349b99')
c.line(22,24,25,27,steel)
# Upright, slightly raked steering column.
c.line(25,25,23,13,ink)
c.line(24,24,22,13,ink)
c.line(24,23,22,14,steel)
c.set(23,18,light)
c.line(21,12,26,12,ink)
c.set(26,13,ink)
# Far leg bent forward to the front foot.
c.poly([(14,16),(18,17),(20,20),(18,23),(15,23),(16,20),(13,19)],ink)
c.line(16,18,18,20,'#4b607e')
c.line(18,20,16,23,'#4b607e')
c.rect(16,23,5,2,ink)
c.line(18,23,20,23,light)
# Weight-bearing leg and rear shoe.
c.poly([(11,16),(15,17),(14,21),(13,24),(10,24),(11,20)],ink)
c.line(12,18,12,22,'#657b98')
c.rect(10,23,6,2,ink)
c.line(11,24,15,24,'#e1e6dd')
# Jacket, leaned toward the handlebars.
c.poly([(13,9),(17,10),(18,13),(16,18),(10,18),(10,14)],ink)
c.poly([(13,10),(16,11),(16,14),(14,17),(11,17),(11,14)],'#e7774f')
c.line(12,13,11,16,'#ffc16b')
c.line(11,17,14,17,'#b94f44')
# Neck and side-profile face, facing right.
c.rect(15,8,3,3,ink)
c.rect(15,8,2,2,shade)
c.poly([(13,4),(18,4),(19,6),(20,7),(19,8),(18,9),(15,9),(13,7)],ink)
c.poly([(15,4),(18,5),(18,6),(19,7),(18,8),(16,8),(15,7)],skin)
c.set(18,6,ink)
c.set(16,6,'#ffd6a4')
# Helmet silhouette, brim, and strap.
c.poly([(11,3),(13,1),(17,1),(19,3),(19,5),(12,5),(11,4)],ink)
c.poly([(12,3),(14,2),(17,2),(18,3),(18,4),(12,4)],'#55c9c0')
c.line(14,2,16,2,'#bbf4dc')
c.line(12,5,15,5,'#319b9f')
c.line(14,6,15,8,ink)
c.set(14,6,skin)
# Reaching arm with a bent elbow and hand wrapped around grip.
c.poly([(16,10),(18,11),(19,13),(22,12),(23,13),(22,15),(18,15),(16,13)],ink)
c.line(17,11,18,13,'#f99a5c')
c.line(18,14,21,14,skin)
c.rect(22,12,2,2,skin)
c.set(23,13,shade)
view(result)
finish(result)
