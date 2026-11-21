result = new_canvas(32,32)
c=result
out='#65422f'; dark='#916039'; mid='#bd8749'; gold='#dbac65'; light='#f2ce88'; inner='#704632'
# tilted lid behind basket
c.poly([(3,12),(4,9),(8,7),(20,4),(25,5),(27,7),(26,10),(20,13),(8,16),(4,15)],out)
c.poly([(4,11),(8,8),(20,5),(24,6),(26,7),(24,9),(9,13),(5,13)],gold)
c.poly([(5,14),(10,14),(24,10),(26,8),(26,10),(20,12),(9,15),(5,15)],mid)
c.line(7,11,21,7,light)
c.line(9,12,24,8,mid)
c.line(8,9,17,6,light)
c.line(13,8,17,10,mid)
c.line(19,6,23,8,mid)
# lid handle
c.poly([(13,6),(13,4),(16,3),(18,4),(18,5),(16,5),(16,4),(15,5),(15,6)],out)
c.set(14,4,gold)
# basket body
c.ellipse(16,24,13,6,out)
c.rect(3,18,27,7,out)
c.ellipse(16,23,12,5,mid)
c.rect(4,19,25,5,gold)
c.ellipse(16,18,13,6,out)
c.ellipse(16,18,12,5,light)
c.ellipse(16,18,10,4,inner)
# interior mat
c.line(8,20,23,20,dark)
# rear dumpling
c.poly([(12,17),(12,15),(14,13),(15,12),(17,12),(18,13),(20,15),(20,17),(18,19),(14,19)],'#ba9670')
c.poly([(13,16),(14,14),(16,12),(18,14),(19,16),(18,18),(14,18)],'#fff0c6')
c.line(16,13,15,16,'#d8bd91')
c.line(17,14,18,16,'#d8bd91')
# left dumpling
c.poly([(6,20),(7,18),(9,17),(10,16),(11,17),(13,19),(14,21),(12,23),(8,23)],'#ae835d')
c.poly([(7,20),(8,18),(10,17),(12,19),(13,21),(11,22),(8,22)],'#fff1cc')
c.line(10,18,9,20,'#d9be94')
c.line(11,19,11,21,'#d9be94')
c.set(8,20,'#ffffff')
# right dumpling
c.poly([(18,21),(19,18),(22,16),(24,17),(26,20),(25,22),(23,23),(20,23)],'#ae835d')
c.poly([(19,20),(20,18),(22,17),(24,18),(25,20),(24,22),(20,22)],'#fff1cc')
c.line(22,18,21,20,'#d9be94')
c.line(23,18,24,20,'#d9be94')
c.set(20,20,'#ffffff')
# front rim arc, bamboo staves
c.path('M 3 20 Q 5 25 16 25 Q 27 25 29 20 L 29 23 Q 26 28 16 28 Q 6 28 3 23 Z',mid)
c.path('M 4 21 Q 7 25 16 25 Q 25 25 28 21',light,fill=False)
for x,y in [(6,25),(10,26),(15,26),(20,26),(25,25)]:
 c.line(x,y,x,y+2,dark)
 c.set(x+1,y,gold)
c.path('M 5 27 Q 16 32 27 27',out,fill=False)
c.path('M 7 27 Q 16 30 25 27',gold,fill=False)
# small steam wisps above opening
c.line(7,6,7,4,'#cadbd8')
c.set(8,3,'#eef6eb')
c.line(23,13,23,11,'#cadbd8')
c.set(22,10,'#eef6eb')
c.line(28,14,28,12,'#eef6eb')
c.set(27,11,'#cadbd8')
view(result)
finish(result)
