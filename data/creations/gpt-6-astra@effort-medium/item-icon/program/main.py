result = new_canvas(32,32,name='ancient_compass')
c=result
o='#211b28'; shadow='#69402e'; dark='#a16431'; gold='#d99c42'; light='#f5cf70'; hi='#fff0b0'; face='#795337'
# suspension loop
c.rect(12,1,8,7,o)
c.rect(14,2,4,4,gold)
c.rect(15,3,2,2,o)
# broad stepped silhouette
c.poly([(11,5),(20,5),(20,6),(24,6),(24,8),(27,8),(27,11),(29,11),(29,22),(27,22),(27,25),(24,25),(24,27),(21,27),(21,29),(10,29),(10,27),(7,27),(7,25),(4,25),(4,22),(2,22),(2,12),(4,12),(4,9),(7,9),(7,7),(11,7)],o)
c.ellipse(16,17,12,11,shadow)
c.ellipse(15,16,12,11,gold)
c.ellipse(15,16,10,9,light)
c.ellipse(16,17,9,9,dark)
c.ellipse(15,16,8,8,o)
c.ellipse(15,16,7,7,face)
c.ellipse(15,15,6,6,'#9a7244')
# bevel arcs
c.line(8,8,11,7,hi);c.line(5,11,7,9,light)
c.line(4,13,4,18,light)
c.line(7,23,10,25,dark);c.line(12,27,20,27,dark)
c.line(23,24,26,21,shadow)
c.line(24,11,26,14,hi)
# small rivets
for x,y in [(9,9),(23,9),(6,21),(24,21),(16,26)]:
 c.set(x,y,shadow);c.set(x,y-1,hi)
# compass rose, four cardinal points
c.poly([(15,7),(12,14),(15,16),(18,14)],o)
c.poly([(15,8),(13,13),(15,12)],hi)
c.poly([(15,9),(15,13),(17,14)],gold)
c.poly([(15,25),(12,19),(15,16),(18,19)],o)
c.poly([(15,23),(13,19),(15,18)],gold)
c.poly([(15,23),(15,18),(17,19)],dark)
c.poly([(6,16),(12,13),(15,16),(12,19)],o)
c.poly([(8,16),(12,14),(13,16)],light)
c.poly([(8,16),(13,16),(12,18)],dark)
c.poly([(24,16),(18,13),(15,16),(18,19)],o)
c.poly([(22,16),(18,14),(17,16)],light)
c.poly([(22,16),(17,16),(18,18)],gold)
# diagonal engraved marks
for x,y,dx,dy in [(10,11,1,1),(20,11,-1,1),(10,21,1,-1),(20,21,-1,-1)]:
 c.line(x,y,x+dx,y+dy,dark)
# crystal socket and gem
c.poly([(14,11),(17,11),(20,15),(20,18),(16,22),(12,20),(10,16)],o)
c.poly([(14,12),(17,12),(19,15),(19,18),(16,21),(12,19),(11,16)],gold)
c.poly([(14,13),(16,12),(18,15),(18,18),(15,20),(12,18),(12,16)],'#14659a')
c.poly([(14,13),(16,13),(16,16),(12,17)],'#70e6ee')
c.poly([(16,13),(18,15),(16,16)],'#37b6e0')
c.poly([(12,17),(16,16),(15,19)],'#228ec7')
c.poly([(16,16),(18,15),(18,18),(15,20)],'#233f81')
c.line(14,13,13,15,'#d3ffff');c.set(16,16,'#8af4f6')
view(result)
finish(result)
