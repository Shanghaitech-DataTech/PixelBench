result = new_canvas(32,32, name='bamboo_steamer')
c=result
outline='#67412f'
dark='#956039'
mid='#bd8548'
gold='#dda65b'
light='#f3cd82'
cream='#fff0c5'
# tilted lid, raised toward the upper left
c.poly([(3,9),(5,6),(13,3),(18,3),(23,6),(24,8),(21,10),(9,14),(5,13)],outline)
c.poly([(4,9),(6,7),(14,4),(18,4),(22,6),(22,8),(9,12),(6,12)],gold)
c.line(6,12,22,7,light)
c.line(6,13,21,9,dark)
# woven slats along the angled lid
c.line(7,8,10,10,mid)
c.line(10,6,14,9,mid)
c.line(14,5,18,8,mid)
c.line(18,5,20,6,mid)
c.line(6,10,19,5,light)
# raised bamboo handle
c.poly([(10,5),(10,3),(12,2),(15,2),(17,4),(15,5),(14,4),(12,4),(12,5)],outline)
c.line(11,3,14,3,light)
c.set(15,4,gold)
# steam curls on the clear right side
c.line(26,4,26,5,'#d6e5df')
c.line(25,6,25,7,'#eef3e5')
c.set(26,8,'#d6e5df')
c.line(29,9,29,10,'#d6e5df')
c.set(28,11,'#eef3e5')
# basket body and dark inner well
c.ellipse(16,24,13,5,outline)
c.rect(3,18,27,7,outline)
c.ellipse(16,18,13,5,outline)
c.rect(4,19,25,6,mid)
c.ellipse(16,24,12,4,mid)
c.ellipse(16,18,12,4,gold)
c.ellipse(16,18,10,3,dark)
c.ellipse(16,18,9,2,'#704a32')
# dumplings: individually outlined cream parcels
# rear dumpling
c.poly([(12,17),(12,15),(14,13),(15,11),(17,11),(18,13),(20,15),(20,17),(18,19),(14,19)],outline)
c.poly([(13,16),(14,14),(16,12),(17,13),(19,15),(19,17),(17,18),(14,18)],'#e4ca94')
c.poly([(13,15),(16,12),(17,13),(18,15),(17,17),(14,17)],cream)
c.line(16,13,15,15,'#c6a778')
c.line(17,14,18,16,'#c6a778')
# front left dumpling
c.poly([(5,20),(6,17),(8,16),(9,14),(11,15),(13,17),(14,20),(12,22),(8,22)],outline)
c.poly([(6,20),(7,18),(9,15),(11,17),(12,18),(13,20),(11,21),(8,21)],'#e4ca94')
c.poly([(7,19),(8,17),(9,16),(10,17),(12,19),(11,20),(8,20)],cream)
c.line(9,17,8,19,'#bd9a6d')
c.line(10,17,11,19,'#bd9a6d')
# front right dumpling
c.poly([(18,20),(19,17),(21,16),(23,14),(25,16),(27,18),(27,20),(25,22),(21,22)],outline)
c.poly([(19,20),(20,18),(22,16),(23,15),(25,17),(26,19),(26,20),(24,21),(21,21)],'#e4ca94')
c.poly([(20,19),(21,17),(23,16),(25,18),(25,19),(23,20),(21,20)],cream)
c.line(23,17,22,19,'#bd9a6d')
c.line(24,17,25,19,'#bd9a6d')
# front lip hides the parcel bases
c.path('M 3 20 Q 16 27 29 20 L 29 23 Q 16 30 3 23 Z',gold)
c.path('M 3 20 Q 16 27 29 20',outline,fill=False)
c.path('M 4 22 Q 16 28 28 22',light,fill=False)
# vertical bamboo segments
for x,y in [(6,24),(10,26),(15,27),(20,26),(25,24)]:
    c.line(x,y,x,y+1,dark)
c.path('M 5 26 Q 16 32 27 26',outline,fill=False)
c.path('M 7 27 Q 16 30 25 27',gold,fill=False)
view(c,scale=10)
finish(result)
