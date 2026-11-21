# Two-frame RPG walk cycle, each tile is 32 x 32.
result = new_canvas(64, 32, name='swordsman_walk')
ink='#171c30'
blue0='#202b4b'; blue1='#293f67'; blue2='#3a5782'; blue3='#537498'
red0='#733047'; red1='#b84336'; red2='#e96a3d'; red3='#ffad59'
skin0='#aa6053'; skin1='#e5a16f'; skin2='#ffd09a'
steel0='#516579'; steel1='#91b1be'; steel2='#d6e8df'; white='#f1f5dc'
cloth0='#30333f'; cloth1='#535260'; cloth2='#777480'
leather0='#372c39'; leather1='#664449'; leather2='#9d6550'
gold='#d7ad60'

def draw_frame(f):
    c=new_canvas(32,32,name='pose_'+str(f+1))
    # Cape: collar anchored, hem swings with the step.
    if f==0:
        c.poly([(13,10),(18,12),(17,21),(13,25),(8,24),(4,25),(6,21),(8,17),(10,12)],ink)
        c.poly([(11,12),(15,12),(15,21),(12,24),(8,23),(6,24),(8,19)],blue1)
        c.poly([(11,13),(13,13),(11,20),(8,22),(9,18)],blue2)
        c.poly([(15,14),(16,18),(14,23),(12,24)],blue0)
        c.line(6,24,10,24,blue0)
    else:
        c.poly([(12,11),(17,12),(17,21),(13,24),(9,23),(5,22),(7,19),(8,15),(10,12)],ink)
        c.poly([(11,12),(15,13),(14,20),(12,23),(9,22),(7,21),(9,17)],blue1)
        c.poly([(11,13),(13,13),(11,19),(8,21)],blue2)
        c.poly([(15,15),(16,20),(13,23),(11,22)],blue0)
    # Far leg, dark to establish depth.
    if f==0:
        c.poly([(16,19),(19,19),(19,23),(16,26),(14,29),(9,29),(9,27),(12,26),(14,23)],ink)
        c.poly([(16,21),(18,21),(16,24),(13,27),(11,27),(15,23)],cloth1)
        c.poly([(12,26),(15,27),(13,29),(9,29),(10,27)],leather0)
        c.line(10,27,12,27,leather1)
    else:
        c.poly([(16,19),(19,19),(20,23),(23,26),(25,27),(25,29),(20,29),(18,26),(16,24)],ink)
        c.poly([(17,21),(19,21),(19,24),(22,27),(20,27),(17,24)],cloth1)
        c.poly([(21,26),(23,26),(24,28),(20,28)],leather1)
        c.line(21,29,25,29,ink)
    # Near leg and tall leather boot.
    if f==0:
        c.poly([(13,19),(17,19),(18,22),(19,24),(22,26),(24,27),(24,29),(19,29),(17,26),(15,24),(13,22)],ink)
        c.poly([(14,21),(16,21),(17,23),(19,26),(17,26),(14,23)],cloth2)
        c.set(16,23,steel1)
        c.poly([(18,25),(20,25),(21,27),(23,27),(23,28),(19,28),(17,26)],leather1)
        c.line(18,25,20,26,leather2)
    else:
        c.poly([(14,19),(18,20),(17,24),(15,26),(15,28),(17,28),(17,30),(12,30),(11,28),(12,25),(14,23)],ink)
        c.poly([(15,21),(17,21),(16,24),(13,26),(13,24)],cloth2)
        c.line(14,24,15,23,steel1)
        c.poly([(12,26),(14,26),(14,28),(16,29),(12,29)],leather1)
        c.line(12,26,14,26,leather2)
    # Tunic, breastplate and belt.
    c.poly([(13,11),(18,11),(20,14),(19,18),(20,21),(15,22),(12,20),(13,17),(12,14)],ink)
    c.poly([(14,12),(17,12),(19,14),(18,18),(14,18),(13,15)],steel0)
    c.poly([(14,12),(17,12),(17,15),(15,17),(14,15)],steel1)
    c.line(14,12,16,12,steel2)
    c.rect(14,18,5,2,leather1)
    c.set(17,18,gold)
    c.poly([(14,20),(18,20),(19,21),(15,21)],blue1)
    # Neck, face in right-facing profile.
    c.rect(16,9,3,3,ink)
    c.rect(17,9,2,3,skin0)
    c.poly([(15,4),(20,4),(21,6),(21,8),(23,9),(22,10),(21,10),(21,12),(18,12),(16,10),(14,8)],ink)
    c.poly([(17,5),(20,5),(20,8),(22,9),(20,10),(20,11),(18,11),(16,9)],skin1)
    c.line(20,6,20,7,skin2)
    c.set(20,8,ink)
    c.set(18,10,skin0)
    # Angular red hair with swept-back tufts.
    c.poly([(12,3),(16,3),(17,2),(20,3),(22,5),(21,6),(18,6),(17,8),(16,9),(16,11),(14,10),(13,8),(11,7),(12,6),(10,5)],ink)
    c.poly([(13,4),(16,4),(17,3),(20,4),(21,5),(18,5),(16,7),(16,9),(14,8),(12,7),(14,6),(12,5)],red1)
    c.line(14,4,18,4,red2)
    c.line(14,5,17,5,red2)
    c.set(18,3,red3)
    c.set(19,4,red3)
    c.line(13,7,15,8,red0)
    c.set(15,6,red2)
    # Shoulder, elbow and sword hand.
    c.poly([(17,12),(20,12),(21,14),(21,16),(23,17),(23,19),(20,19),(18,17),(17,15)],ink)
    c.poly([(18,12),(20,13),(20,15),(18,15)],steel1)
    c.line(18,12,19,12,steel2)
    c.line(18,16,20,17,steel0)
    c.line(20,17,21,17,leather1)
    # Long sword held forward: dark perimeter, blue steel and bright cutting edge.
    # Keep the weapon stable while the legs and cape alternate.
    c.poly([(23,17),(25,12),(30,5),(30,9),(26,15),(25,18)],ink)
    c.poly([(24,16),(26,12),(29,7),(29,9),(25,16)],steel1)
    c.line(25,14,29,8,steel2)
    c.line(26,12,29,7,white)
    c.line(23,18,22,21,ink)
    c.line(23,18,22,20,leather2)
    c.line(22,16,26,19,ink)
    c.line(22,16,25,18,gold)
    c.set(26,18,leather1)
    c.rect(22,18,2,2,skin0)
    c.set(22,18,skin2)
    c.set(23,18,skin1)
    c.set(22,21,gold)
    return c

for f in range(2):
    result.blit(draw_frame(f),32*f,0)
view(result,scale=8,margin=0)
save('swordsman_walk', result)
finish(result)
