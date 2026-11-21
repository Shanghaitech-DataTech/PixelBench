result = new_canvas(32, 32, name="retro_film_camera")
c = result
ink = '#181c29'
shadow = '#30313d'
leather = '#494047'
leatherlit = '#64565a'
metalsh = '#696c7b'
metal = '#a1a6b0'
light = '#d4d7d2'
white = '#f1e9d5'
# Compact silhouette, top controls and raised viewfinder housing.
c.rect(5,7,6,3,ink)
c.rect(6,7,4,2,metal)
c.set(6,7,light)
c.rect(23,6,4,4,ink)
c.rect(24,6,2,1,white)
c.rect(24,7,2,2,'#a76858')
c.poly([(12,9),(14,5),(20,5),(23,9)],ink)
c.poly([(14,8),(15,6),(19,6),(21,8)],metal)
c.line(15,6,19,6,light)
c.rect(3,9,26,17,ink)
c.rect(2,11,1,13,ink)
c.rect(29,11,1,13,ink)
c.rect(4,26,24,1,ink)
# Metal top plate, bright upper edge and shaded right bevel.
c.rect(4,10,24,6,metal)
c.line(5,10,26,10,light)
c.rect(27,11,1,14,metalsh)
c.rect(3,12,1,11,metalsh)
c.rect(4,16,23,9,shadow)
c.rect(5,16,21,8,leather)
c.line(4,25,26,25,metalsh)
c.line(5,25,23,25,metal)
# Stippled leather grain, deliberately confined to small clusters.
for x,y in [(5,17),(8,17),(6,19),(9,20),(5,22),(8,23),(23,17),(25,18),(24,20),(22,22),(25,23)]:
    c.set(x,y,leatherlit)
for x,y in [(7,18),(5,20),(8,22),(25,19),(23,21),(24,23)]:
    c.set(x,y,'#342e39')
# Viewfinder and small warm badge.
c.rect(6,11,6,4,ink)
c.rect(7,12,4,2,'#446574')
c.line(7,12,9,12,'#a4c2c4')
c.set(10,13,'#213b50')
c.rect(23,12,3,2,'#a76858')
c.set(23,12,'#e2b47b')
# Circular lens mount with dark outline and chrome stepped edges.
c.circle(17,18,8,ink)
c.circle(17,18,7,metalsh)
c.path('M 10 18 L 10 15 L 12 12 L 15 11 L 19 11 L 22 13 L 22 14 L 19 13 L 15 13 L 12 16 L 12 20 L 10 20 Z',light)
c.path('M 12 23 L 15 25 L 19 25 L 22 23 L 24 20 L 24 17 L 23 17 L 22 21 L 19 23 Z',shadow)
c.circle(17,18,6,ink)
c.circle(17,18,5,'#3f5265')
c.path('M 13 19 L 13 16 L 15 14 L 19 14 L 21 16 L 19 16 L 16 15 L 14 17 L 14 20 Z','#718c99')
c.circle(17,18,3,'#1d3049')
c.poly([(15,18),(17,16),(19,17),(20,20),(17,21),(15,20)],'#28485e')
c.line(15,16,17,15,'#b4e2dc')
c.set(14,17,'#78b8c4')
c.line(18,21,20,19,'#4c899f')
c.set(19,20,'#80bcb9')
# A few mechanical details along the rim and edges.
c.set(17,11,white)
c.set(11,20,metal)
c.set(22,21,metal)
c.set(4,11,white)
c.set(26,24,shadow)
view(result)
finish(result)
