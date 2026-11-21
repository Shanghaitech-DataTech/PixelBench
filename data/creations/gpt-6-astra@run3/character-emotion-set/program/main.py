result = new_canvas(64,64,name='emotion-set')
# Cohesive warm skin, midnight hair, and teal jacket palette.
ink='#202035'
hair='#36354f'
hshadow='#29283f'
hlight='#55516b'
hshine='#71637c'
skin='#efb38b'
shade='#cf886f'
light='#ffd1a0'
blush='#df8d80'
teal='#398c91'
tealLight='#60b8b2'
tealDark='#28616c'
cream='#f9e3bb'

def portrait(ox,oy,emotion):
    def rect(x,y,w,h,col): result.rect(ox+x,oy+y,w,h,col)
    def line(x,y,x2,y2,col): result.line(ox+x,oy+y,ox+x2,oy+y2,col)
    def poly(points,col): result.poly([(ox+x,oy+y) for x,y in points],col)
    def dot(x,y,col): result.set(ox+x,oy+y,col)
    # Large rounded silhouette with characteristic side-swept fringe.
    poly([(5,13),(4,9),(6,5),(10,3),(13,3),(15,1),(18,2),(20,3),(24,4),(27,7),(28,12),(27,20),(24,24),(8,24),(5,20)],ink)
    poly([(6,10),(7,6),(11,4),(15,4),(16,3),(21,4),(25,6),(26,10),(26,19),(24,22),(7,22)],hair)
    # Shoulder silhouette, neck and identical jacket.
    poly([(11,24),(20,24),(20,25),(25,26),(28,29),(28,31),(4,31),(4,29),(7,26)],ink)
    poly([(6,29),(9,27),(13,26),(19,26),(24,27),(26,29),(26,31),(6,31)],teal)
    rect(7,29,3,2,tealLight)
    rect(24,29,3,2,tealDark)
    rect(12,23,8,4,ink)
    rect(13,23,6,4,shade)
    rect(14,24,4,3,skin)
    poly([(12,26),(16,29),(20,26),(19,31),(13,31)],ink)
    poly([(14,27),(16,28),(18,27),(17,31),(15,31)],cream)
    poly([(10,26),(13,26),(15,29),(12,29)],tealLight)
    poly([(19,26),(22,26),(20,29),(17,29)],tealDark)
    # Ears and face, outlined in a single dark pixel.
    rect(5,13,4,7,ink); rect(24,13,4,7,ink)
    rect(6,14,3,5,shade); rect(24,14,3,5,shade)
    dot(6,15,skin); dot(26,15,skin)
    poly([(9,8),(22,8),(25,11),(25,20),(23,23),(20,25),(13,25),(9,23),(7,20),(7,12)],ink)
    poly([(10,9),(21,9),(24,12),(24,20),(22,22),(19,24),(13,24),(10,22),(8,19),(8,12)],skin)
    poly([(8,13),(10,12),(10,20),(13,23),(20,23),(19,24),(13,24),(10,22),(8,19)],shade)
    rect(12,12,10,5,light)
    rect(13,17,9,3,light)
    dot(17,19,shade); dot(18,19,shade)
    # Face-specific eyebrows, eyes and mouth.
    if emotion=='calm':
        line(11,13,14,13,hair); line(20,13,23,13,hair)
        line(11,16,14,16,ink); line(20,16,23,16,ink)
        rect(12,16,2,2,ink); rect(21,16,2,2,ink)
        line(15,21,19,21,shade); line(16,21,18,21,ink)
    elif emotion=='smile':
        line(11,12,14,12,hair); line(20,12,23,12,hair)
        line(10,16,12,14,ink); line(12,14,14,16,ink)
        line(19,16,21,14,ink); line(21,14,23,16,ink)
        rect(10,18,3,1,blush); rect(21,18,3,1,blush)
        poly([(13,19),(21,19),(20,22),(18,23),(16,23),(14,22)],ink)
        rect(14,19,6,1,cream)
        rect(16,22,3,1,blush)
    elif emotion=='angry':
        line(10,12,14,14,ink); line(19,14,23,12,ink)
        line(11,16,14,16,ink); line(19,16,22,16,ink)
        rect(13,16,2,2,ink); rect(19,16,2,2,ink)
        line(14,22,16,21,ink); line(16,21,19,21,ink); dot(20,22,ink)
        rect(10,19,2,1,blush); rect(22,19,2,1,blush)
    else:
        line(11,11,14,11,hair); line(20,11,23,11,hair)
        rect(10,13,5,5,ink); rect(19,13,5,5,ink)
        rect(11,14,3,3,cream); rect(20,14,3,3,cream)
        rect(12,15,1,2,ink); rect(21,15,1,2,ink)
        poly([(16,20),(18,20),(19,21),(19,23),(18,24),(16,24),(15,23),(15,21)],ink)
        rect(16,22,2,1,shade)
    # The same sculpted fringe on each portrait, kept clear of brows.
    poly([(6,10),(8,6),(12,4),(18,4),(23,5),(26,9),(26,14),(24,15),(23,10),(20,8),(17,10),(13,11),(10,11),(9,15),(7,16)],ink)
    poly([(6,10),(9,6),(13,5),(18,5),(22,6),(24,8),(25,12),(24,12),(22,9),(20,7),(16,9),(12,10),(9,10),(8,13),(7,14)],hair)
    poly([(8,8),(11,6),(16,5),(20,6),(17,7),(12,8)],hlight)
    line(10,6,14,5,hshine)
    line(21,6,23,7,hlight)
    dot(24,9,hlight)
    # A small consistent gold ear stud.
    dot(6,18,cream)

portrait(0,0,'calm')
portrait(32,0,'smile')
portrait(0,32,'angry')
portrait(32,32,'surprised')
view(result,scale=8,margin=0)
finish(result)
