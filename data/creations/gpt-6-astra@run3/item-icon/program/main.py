result = new_canvas(32, 32, name='ancient_compass')
c = result
ink='#201d2a'
shade='#67402c'
darkgold='#946034'
gold='#c48b3f'
light='#edbc60'
shine='#ffe5a0'
face='#765332'
# Top suspension loop and dark silhouette
c.rect(13,1,6,2,ink)
c.rect(12,3,8,5,ink)
c.rect(14,3,4,3,gold)
c.rect(15,3,2,2,ink)
c.rect(13,4,1,2,light)
# Stepped round casing, two-pixel outer contour
c.poly([(11,5),(20,5),(20,6),(24,6),(24,8),(27,8),(27,11),(29,11),(29,21),(27,21),(27,25),(24,25),(24,28),(20,28),(20,30),(11,30),(11,29),(7,29),(7,27),(4,27),(4,24),(2,24),(2,12),(4,12),(4,9),(7,9),(7,7),(11,7)],ink)
c.poly([(11,7),(20,7),(20,8),(23,8),(23,10),(25,10),(25,12),(27,12),(27,22),(25,22),(25,25),(22,25),(22,27),(19,27),(19,28),(11,28),(11,27),(8,27),(8,25),(6,25),(6,22),(4,22),(4,13),(6,13),(6,11),(8,11),(8,9),(11,9)],gold)
# Raised bevel lighting
c.path('M 5 20 L 5 13 L 7 13 L 7 11 L 9 11 L 9 9 L 12 9 L 12 8 L 19 8',shine,fill=False)
c.path('M 7 23 L 7 25 L 10 25 L 10 27 L 20 27 L 20 26 L 23 26 L 23 24 L 25 24 L 25 21 L 26 21 L 26 13',shade,fill=False)
c.path('M 9 26 L 11 26 L 11 27 L 19 27',light,fill=False)
# Inset circular dial
c.poly([(12,10),(20,10),(20,11),(23,11),(23,14),(25,14),(25,21),(23,21),(23,24),(20,24),(20,26),(12,26),(12,25),(9,25),(9,23),(7,23),(7,14),(9,14),(9,12),(12,12)],ink)
c.poly([(12,11),(20,11),(20,12),(22,12),(22,14),(24,14),(24,21),(22,21),(22,23),(20,23),(20,25),(12,25),(12,24),(10,24),(10,22),(8,22),(8,14),(10,14),(10,13),(12,13)],face)
c.path('M 9 20 L 9 15 L 11 15 L 11 13 L 13 13 L 13 12 L 19 12',shade,fill=False)
# Cardinal and diagonal etched markers
c.rect(15,11,2,3,light)
c.rect(15,23,2,2,gold)
c.rect(8,17,3,2,light)
c.rect(22,17,2,2,gold)
for x,y in [(11,14),(20,14),(11,21),(20,21)]:
    c.set(x,y,gold)
# Eight-point compass rose beneath jewel
c.poly([(16,12),(18,16),(22,18),(18,20),(16,24),(14,20),(10,18),(14,16)],ink)
c.poly([(16,13),(17,17),(21,18),(17,19),(16,23),(15,19),(11,18),(15,17)],light)
c.poly([(16,18),(21,18),(17,19),(16,23)],darkgold)
# Gem setting and blue faceted crystal
c.poly([(15,14),(18,15),(20,18),(18,21),(15,22),(12,19),(12,17)],ink)
c.poly([(15,15),(17,15),(19,18),(17,21),(15,21),(13,19),(13,17)],'#167dad')
c.poly([(15,15),(17,15),(16,18),(13,19),(13,17)],'#60d9ee')
c.poly([(17,15),(19,18),(16,18)],'#2ca9d0')
c.poly([(16,18),(19,18),(17,21),(15,21)],'#204979')
c.poly([(16,17),(17,18),(16,20),(14,19)],'#249ecb')
c.line(15,15,14,17,'#d1fcf6')
c.set(16,16,'#a1f5f7')
# Bezel rivets, age nicks
for x,y in [(8,10),(24,11),(6,23),(23,25)]:
    c.set(x,y,shade)
    c.set(x,y-1,light)
c.line(12,7,15,7,light)
c.set(21,8,darkgold)
c.set(26,17,light)
c.set(10,27,darkgold)
c.set(18,28,darkgold)
view(result,scale=12)
finish(result)
