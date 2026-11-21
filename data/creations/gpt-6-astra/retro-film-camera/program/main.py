result = new_canvas(32, 32, name='retro_film_camera')
c=result
ink='#171b29'
shadow='#303343'
leather='#4a3635'
mid='#664740'
light='#866052'
metal='#a6b4b7'
bright='#e4e5cb'
# Stepped silhouette and top controls
c.rect(5,7,5,3,ink)
c.rect(6,7,3,1,bright)
c.rect(6,8,3,2,'#788b93')
c.rect(23,6,4,4,ink)
c.rect(24,6,2,1,'#f0cc8e')
c.rect(24,7,2,2,'#b87b55')
c.poly([(11,9),(13,5),(19,5),(22,9)],ink)
c.poly([(13,9),(14,6),(18,6),(20,9)],metal)
c.line(14,6,18,6,bright)
c.rect(2,9,28,16,ink)
c.rect(3,8,25,18,ink)
c.rect(4,26,23,1,ink)
# metal top plate
c.rect(4,10,23,5,metal)
c.line(4,9,26,9,bright)
c.line(3,11,3,15,'#788b93')
c.rect(27,10,2,5,'#667985')
c.line(5,11,11,11,'#d1d8c9')
c.line(4,15,27,15,shadow)
# finder and tiny badge
c.rect(14,8,5,4,ink)
c.rect(15,9,3,2,'#396775')
c.set(15,9,'#9cd2cd')
c.rect(5,12,4,2,ink)
c.rect(6,12,2,1,'#f2deaa')
c.rect(24,11,2,2,'#f2deaa')
c.set(25,12,'#d1955d')
# leather covering, shaded side and base
c.rect(4,16,23,9,leather)
c.rect(4,16,5,7,mid)
c.rect(27,16,2,8,'#292a35')
c.line(5,25,26,25,'#78868c')
c.line(5,24,26,24,'#382d32')
c.line(4,17,4,23,'#94715b')
# discrete pebbled leather texture
for x,y in [(6,17),(8,18),(5,20),(7,21),(6,23),(9,23),(24,17),(26,18),(25,20),(24,22),(26,23)]:
    c.set(x,y,light)
for x,y in [(5,18),(7,19),(8,22),(5,22),(24,19),(26,21),(25,23)]:
    c.set(x,y,'#352d32')
# shoulder strap eyes
c.rect(1,13,3,5,ink)
c.rect(2,14,1,2,'#8e9da5')
c.rect(29,13,2,5,ink)
c.set(29,14,'#8e9da5')
# lens barrel offset shadow and concentric rings
c.ellipse(17,20,9,7,ink)
c.ellipse(16,18,9,9,ink)
c.ellipse(16,18,8,8,'#667985')
c.ellipse(16,17,7,7,'#c8cdbd')
c.ellipse(16,18,7,7,'#788b93')
c.ellipse(16,18,6,6,ink)
c.ellipse(16,18,5,5,'#355568')
c.ellipse(16,18,4,4,'#182d46')
# angular glass facets
c.poly([(12,17),(14,14),(18,14),(15,17),(14,21),(12,19)],'#396e80')
c.poly([(16,21),(19,17),(20,18),(19,21),(16,22)],'#24485e')
c.line(14,15,17,15,'#80b5b6')
c.line(13,16,13,17,'#bce2d4')
c.set(14,16,'#e7f1d6')
c.line(17,21,18,20,'#5b92a1')
# lens rim highlights and knurling
c.line(13,11,18,11,bright)
c.line(10,14,9,16,'#d0d8ca')
c.line(10,21,11,22,'#a6b4b7')
c.line(15,25,18,25,'#485663')
for x,y in [(21,13),(23,16),(23,19),(22,22),(20,24)]:
    c.set(x,y,shadow)
c.set(8,18,'#d0d8ca')
c.set(26,14,shadow)
view(result)
finish(result)
