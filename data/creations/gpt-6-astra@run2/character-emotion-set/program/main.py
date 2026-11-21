result = new_canvas(64,64, name='emotion_set')
# Unified palette, warm skin and blue-black hair, teal jacket.
ink='#202032'
hair='#343349'
hmid='#50516b'
hlight='#70738a'
skin='#f1bb91'
shade='#d98d78'
light='#ffdbaf'
blush='#e99487'
teal='#368c96'
tlight='#69bec0'
tdark='#286174'
white='#fff2d8'

def portrait(ox,oy,mood):
    c=new_canvas(32,32)
    # shoulders, high collar, and identical shirt
    c.poly([(4,31),(4,29),(7,26),(11,25),(12,23),(20,23),(21,25),(25,26),(28,29),(28,31)],ink)
    c.poly([(6,31),(6,29),(9,27),(12,26),(20,26),(24,27),(26,29),(26,31)],teal)
    c.rect(12,24,8,5,ink)
    c.rect(13,23,6,4,shade)
    c.rect(14,24,4,2,skin)
    c.poly([(10,26),(12,25),(15,29),(13,31),(9,28)],tlight)
    c.poly([(21,25),(23,27),(20,31),(17,29)],tlight)
    c.rect(15,29,3,2,white)
    c.line(7,29,7,30,tdark)
    c.line(25,29,25,30,tdark)
    # big round silhouette and ears
    c.poly([(9,2),(21,2),(25,5),(27,10),(27,18),(25,22),(22,24),(10,24),(6,21),(5,17),(5,9),(7,5)],ink)
    c.poly([(9,4),(21,3),(24,6),(26,10),(25,20),(22,23),(9,23),(7,20),(6,11),(7,7)],hair)
    c.rect(5,14,4,6,ink)
    c.rect(6,15,3,4,shade)
    c.rect(24,14,4,6,ink)
    c.rect(24,15,3,4,shade)
    # face
    c.poly([(10,9),(21,9),(24,12),(24,20),(22,23),(19,25),(13,25),(9,22),(8,19),(8,12)],ink)
    c.poly([(10,10),(21,10),(23,12),(23,20),(21,22),(18,24),(13,24),(10,22),(9,19),(9,12)],skin)
    c.line(10,20,12,22,shade)
    c.line(13,23,18,23,shade)
    c.rect(11,12,3,2,light)
    c.rect(20,12,2,2,light)
    c.set(16,19,shade)
    c.set(17,19,light)
    # sweeping fringe, identical across all portraits
    c.poly([(7,11),(8,7),(11,4),(20,4),(24,7),(25,11),(24,15),(22,13),(21,10),(19,9),(16,12),(12,13),(13,10),(10,12),(8,15)],ink)
    c.poly([(7,10),(9,6),(12,4),(20,4),(23,7),(24,10),(24,12),(22,10),(21,8),(18,8),(15,11),(14,11),(15,8),(12,10),(9,12),(8,13)],hair)
    c.poly([(9,7),(12,5),(20,5),(22,7),(17,6),(14,8),(11,9),(12,7)],hmid)
    c.line(12,5,18,5,hlight)
    c.line(8,9,9,7,hmid)
    c.line(24,8,24,10,hmid)
    # expressions
    if mood=='calm':
        c.line(10,14,13,14,hair)
        c.line(19,14,22,14,hair)
        c.line(10,16,13,16,ink)
        c.line(19,16,22,16,ink)
        c.set(12,17,ink); c.set(20,17,ink)
        c.line(14,21,18,21,ink)
        c.set(18,20,shade)
    elif mood=='smile':
        c.line(10,14,13,13,hair)
        c.line(19,13,22,14,hair)
        c.poly([(10,17),(11,16),(12,16),(13,17)],ink,fill=False)
        c.poly([(19,17),(20,16),(21,16),(22,17)],ink,fill=False)
        c.rect(10,19,3,1,blush); c.rect(21,19,2,1,blush)
        c.poly([(13,20),(20,20),(19,23),(15,23)],ink)
        c.line(14,20,19,20,white)
        c.line(16,22,18,22,blush)
    elif mood=='angry':
        c.line(10,13,14,15,ink)
        c.line(18,15,22,13,ink)
        c.line(10,16,13,16,white); c.line(19,16,22,16,white)
        c.rect(12,16,2,2,ink); c.rect(19,16,2,2,ink)
        c.line(14,22,15,21,ink); c.line(15,21,18,21,ink); c.set(19,22,ink)
        c.set(10,19,blush); c.set(22,19,blush)
    elif mood=='surprise':
        c.line(10,13,13,12,hair)
        c.line(19,12,22,13,hair)
        c.rect(10,15,4,4,ink); c.rect(19,15,4,4,ink)
        c.rect(10,15,3,3,white); c.rect(20,15,3,3,white)
        c.rect(12,16,2,3,ink); c.rect(19,16,2,3,ink)
        c.rect(15,20,4,4,ink)
        c.rect(16,21,2,2,shade)
        c.set(16,21,'#903f51')
    result.blit(c,ox,oy)

portrait(0,0,'calm')
portrait(32,0,'smile')
portrait(0,32,'angry')
portrait(32,32,'surprise')
view(result)
finish(result)
