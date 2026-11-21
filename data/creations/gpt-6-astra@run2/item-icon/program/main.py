result = new_canvas(32, 32, name='ancient_compass')
c = result
ink='#231d2a'
shade='#65402d'
bronze='#a36832'
gold='#d49a43'
light='#f3ca6b'
glint='#fff0ab'
face='#5a4737'
# Suspension ring, seen from above.
c.rect(12,1,8,6,ink)
c.rect(14,0,4,1,ink)
c.rect(14,1,4,4,gold)
c.rect(15,2,2,2,ink)
c.line(14,1,17,1,light)
c.rect(12,4,8,3,ink)
c.rect(14,5,4,2,light)
# Stepped thick exterior silhouette.
c.poly([(10,5),(21,5),(21,6),(25,7),(28,10),(30,14),(30,22),(27,27),(22,30),(10,30),(5,27),(2,22),(2,14),(4,10),(7,7),(10,6)],ink)
# Low right bronze bevel and illuminated upper left rim.
c.poly([(10,7),(21,7),(25,9),(28,14),(28,22),(25,26),(21,28),(11,28),(6,25),(4,21),(4,14),(7,10)],bronze)
c.poly([(10,7),(21,7),(25,9),(27,13),(27,21),(24,25),(20,27),(11,27),(7,24),(5,20),(5,14),(8,10)],gold)
c.path('M 6 17 L 6 14 L 9 10 L 12 8 L 21 8 L 24 10 L 20 9 L 12 9 L 9 12 L 7 16 L 7 21 L 6 20 Z',light)
c.line(11,7,20,7,light)
c.line(11,8,17,8,glint)
c.line(26,16,26,21,light)
c.line(12,27,20,27,shade)
c.line(24,25,26,22,shade)
# Dark inset dial with gold inner lip.
c.poly([(12,10),(20,10),(24,13),(25,16),(25,21),(22,24),(19,25),(12,25),(8,22),(7,18),(8,14)],ink)
c.poly([(12,11),(20,11),(23,14),(24,17),(24,20),(21,23),(18,24),(12,24),(9,21),(8,18),(9,14)],face)
c.poly([(12,12),(19,12),(22,14),(23,17),(23,20),(20,22),(12,22),(10,20),(9,17),(10,14)],'#3d3936')
# Index marks and small etched details.
c.rect(15,11,2,3,light)
c.rect(15,23,2,2,gold)
c.rect(8,17,3,2,gold)
c.rect(22,17,2,2,light)
c.line(11,13,12,14,bronze)
c.line(20,13,19,14,bronze)
c.line(11,22,12,21,bronze)
c.line(21,22,20,21,bronze)
# Compass rose: four gold spear points behind the crystal.
c.poly([(15,12),(17,12),(18,16),(22,17),(22,19),(18,20),(17,24),(15,24),(14,20),(10,19),(10,17),(14,16)],ink)
c.poly([(16,12),(18,17),(22,18),(17,20),(16,24),(14,19),(10,18),(14,16)],gold)
c.poly([(16,12),(16,18),(14,17)],glint)
c.poly([(10,18),(16,18),(14,19)],light)
c.poly([(16,18),(22,18),(18,20),(16,24)],bronze)
# Jewel bezel and cut sapphire.
c.poly([(14,14),(17,14),(20,17),(20,19),(17,22),(14,22),(12,19),(12,17)],ink)
c.poly([(14,15),(17,15),(19,17),(19,19),(17,21),(14,21),(13,19),(13,17)],light)
c.poly([(15,15),(17,16),(18,17),(18,19),(16,21),(14,19),(14,17)],'#1d608d')
c.poly([(15,15),(17,16),(16,18),(14,18),(14,17)],'#86edee')
c.poly([(17,16),(18,17),(18,19),(16,18)],'#399fd5')
c.poly([(14,18),(16,18),(16,21),(14,19)],'#247cbd')
c.poly([(16,18),(18,19),(16,21)],'#183b70')
c.set(15,16,'#e0ffff')
c.set(15,17,'#b0ffff')
# Age and rivets on the broad casing.
c.set(8,11,glint)
c.set(24,11,shade)
c.set(24,12,light)
c.set(7,23,shade)
c.set(8,24,light)
c.set(23,25,light)
c.line(10,26,12,26,light)
c.set(5,17,shade)
c.set(21,8,shade)
c.set(27,20,shade)
view(result, scale=12, margin=0)
finish(result)
