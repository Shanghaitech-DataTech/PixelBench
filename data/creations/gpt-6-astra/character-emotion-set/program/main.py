result = new_canvas(64, 64, name="emotion_set")
ink='#222238'
hair_dark='#173e50'
hair='#246578'
hair_light='#398d9a'
hair_glint='#68b4b5'
skin_shadow='#c97c69'
skin='#efa987'
skin_light='#ffd0a4'
blush='#df847c'
shirt_dark='#943e5a'
shirt='#d25b70'
shirt_light='#ee8590'
collar='#36445c'
cream='#fff1ce'
gold='#f5c46c'

def portrait(ox,oy,emotion):
    def p(points,c): result.poly([(x+ox,y+oy) for x,y in points],c)
    def r(x,y,w,h,c): result.rect(x+ox,y+oy,w,h,c)
    def l(x,y,xx,yy,c): result.line(x+ox,y+oy,xx+ox,yy+oy,c)
    # Shoulders and uniform silhouette.
    p([(4,30),(5,27),(10,25),(12,24),(20,24),(22,25),(27,27),(28,30)],ink)
    p([(6,29),(7,27),(12,26),(20,26),(25,27),(26,30),(6,30)],shirt)
    r(7,28,2,2,shirt_light); r(24,28,2,2,shirt_dark)
    # Hair silhouette, matching in all four cells.
    p([(5,22),(3,18),(3,10),(5,6),(8,3),(13,1),(21,1),(25,3),(28,7),(29,12),(28,21),(25,25),(21,26),(9,25)],ink)
    p([(5,12),(6,7),(10,4),(15,2),(21,3),(25,5),(27,9),(27,20),(24,24),(10,24),(6,21)],hair_dark)
    # Neck with shaped high collar.
    r(12,22,8,5,ink); r(13,22,6,4,skin_shadow); r(14,23,4,2,skin)
    p([(10,25),(12,24),(16,27),(20,24),(23,26),(19,29),(13,29)],ink)
    p([(11,26),(12,25),(15,27),(14,28)],collar)
    p([(17,27),(20,25),(21,26),(18,28)],collar)
    r(16,28,1,2,gold)
    # Ears and rounded face.
    r(5,14,4,6,ink); r(6,15,3,4,skin_shadow); r(7,15,2,2,skin)
    r(24,14,4,6,ink); r(24,15,3,4,skin_shadow); r(24,15,2,2,skin)
    p([(9,8),(21,7),(25,11),(25,20),(23,23),(19,25),(14,25),(10,23),(8,20),(8,12)],ink)
    p([(10,9),(21,8),(24,11),(24,20),(22,22),(19,24),(14,24),(11,22),(9,19),(9,12)],skin_shadow)
    p([(10,10),(20,9),(23,11),(23,20),(21,22),(18,23),(14,22),(11,20),(10,17)],skin)
    p([(11,11),(19,10),(22,12),(22,16),(19,18),(12,17)],skin_light)
    # Side locks, swept fringe and a golden hair slide.
    p([(5,11),(7,6),(12,3),(20,3),(25,6),(27,10),(26,16),(24,17),(23,11),(20,9),(17,10),(14,12),(9,13),(8,19),(6,17)],hair)
    p([(7,9),(10,5),(15,3),(20,4),(23,6),(18,5),(14,6),(11,9)],hair_light)
    l(10,6,14,4,hair_glint); l(15,4,19,4,hair_glint)
    p([(8,10),(13,9),(17,6),(21,6),(18,10),(14,12),(9,13),(8,18),(7,15)],hair_dark)
    l(9,10,12,10,hair_light); l(13,9,16,7,hair_light)
    l(23,7,25,10,hair_light)
    l(24,10,26,12,ink); l(24,9,26,11,gold); l(24,9,25,10,cream)
    # Expression pixels. Eye whites are limited to the open expressions.
    if emotion == 'calm':
        l(11,14,14,14,hair_dark); l(19,14,22,14,hair_dark)
        l(11,16,14,16,ink); l(19,16,22,16,ink)
        r(13,17,1,1,ink); r(20,17,1,1,ink)
        l(15,21,18,21,ink)
        r(16,19,1,1,skin_shadow)
    elif emotion == 'smile':
        l(11,14,13,13,hair_dark); l(20,13,22,14,hair_dark)
        l(11,17,12,16,ink); l(12,16,13,16,ink); r(14,17,1,1,ink)
        l(19,17,20,16,ink); l(20,16,21,16,ink); r(22,17,1,1,ink)
        r(10,19,3,1,blush); r(21,19,3,1,blush)
        p([(14,19),(20,19),(19,22),(15,22)],ink)
        r(15,20,4,1,cream); r(16,22,2,1,blush)
    elif emotion == 'angry':
        l(10,13,14,15,ink); l(19,15,23,13,ink)
        r(11,16,4,2,cream); r(19,16,4,2,cream)
        r(13,16,2,2,ink); r(19,16,2,2,ink)
        r(11,15,2,1,ink); r(21,15,2,1,ink)
        l(15,21,19,21,ink); r(14,22,1,1,ink); r(20,22,1,1,ink)
        r(16,19,1,1,skin_shadow); r(10,19,2,1,blush); r(22,19,2,1,blush)
    elif emotion == 'surprise':
        l(11,12,14,12,hair_dark); l(19,12,22,12,hair_dark)
        r(11,14,4,5,ink); r(19,14,4,5,ink)
        r(11,15,3,3,cream); r(20,15,3,3,cream)
        r(13,15,1,3,ink); r(20,15,1,3,ink)
        r(15,20,4,3,ink); r(16,19,2,1,ink); r(16,23,2,1,ink)
        r(16,21,2,2,skin_shadow)
        r(10,20,2,1,blush); r(22,20,2,1,blush)

portrait(0,0,'calm')
portrait(32,0,'smile')
portrait(0,32,'angry')
portrait(32,32,'surprise')
view(result, scale=8, margin=0)
save('character-emotion-set', result)
finish(result)
