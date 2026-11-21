# Two hand-pixelled contact poses for a right-facing RPG swordsman.
P = {
    'ink':'#141b2b', 'deep':'#192740',
    'cape0':'#1b2a4d', 'cape1':'#253e68', 'cape2':'#365787', 'cape3':'#537ba8',
    'hair0':'#733238', 'hair1':'#ae3f35', 'hair2':'#df5a35', 'hair3':'#ff9250',
    'skin0':'#ab6150', 'skin1':'#dd9568', 'skin2':'#ffd098',
    'steel0':'#42566b', 'steel1':'#708998', 'steel2':'#b0ccd0', 'steel3':'#e8f3df',
    'leather0':'#47343a', 'leather1':'#795047', 'leather2':'#ae7956',
    'gold0':'#8e673c', 'gold1':'#d0a15b', 'gold2':'#f8d48a',
    'pants0':'#273345', 'pants1':'#455569', 'pants2':'#647489'
}

def draw_frame(phase):
    c = new_canvas(32, 32, name='stride_'+str(phase+1))
    def poly(points, color): c.poly(points, P[color])
    def line(x0,y0,x1,y1,color): c.line(x0,y0,x1,y1,P[color])
    def rect(x,y,w,h,color): c.rect(x,y,w,h,P[color])
    def dot(x,y,color): c.set(x,y,P[color])
    # Alternating legs, rear leg first. Feet share a ground line.
    if phase == 0:
        poly([(13,19),(16,20),(14,23),(11,26),(11,27),(14,28),(14,29),(8,29),(7,27),(9,24),(11,22)],'ink')
        poly([(12,21),(14,21),(12,24),(10,26),(8,26),(10,23)],'pants0')
        line(12,22,10,25,'pants1')
        poly([(8,26),(10,26),(10,28),(13,28),(13,29),(8,29)],'leather0')
        line(8,27,10,27,'leather1')
    else:
        poly([(16,18),(18,19),(19,22),(21,25),(21,26),(24,27),(24,29),(19,29),(18,26),(16,24),(14,21)],'ink')
        poly([(16,20),(18,20),(18,23),(20,26),(18,26),(16,23)],'pants0')
        line(18,23,20,25,'pants1')
        poly([(19,26),(21,26),(21,27),(23,28),(23,29),(19,29)],'leather0')
        line(19,27,21,27,'leather1')
    # Cape is behind the body and near leg; its folds lag behind the step.
    if phase == 0:
        poly([(13,10),(16,12),(16,19),(14,23),(12,25),(10,24),(7,26),(6,25),(3,25),(5,22),(7,19),(8,15),(10,12)],'ink')
        poly([(12,11),(14,12),(14,20),(12,23),(10,22),(7,24),(5,24),(8,19),(9,15)],'cape1')
        poly([(13,12),(15,13),(15,19),(13,23),(12,24),(11,23),(12,19)],'cape0')
        poly([(11,13),(12,13),(11,17),(8,22),(6,23),(8,19),(9,16)],'cape2')
        line(10,14,9,17,'cape3')
        line(10,20,8,23,'cape0')
        line(6,24,7,24,'cape2')
    else:
        poly([(13,9),(16,11),(16,18),(14,22),(12,24),(10,23),(8,24),(5,23),(4,23),(6,20),(7,16),(10,11)],'ink')
        poly([(12,10),(14,11),(14,19),(12,22),(10,21),(8,23),(6,22),(8,18),(9,14)],'cape1')
        poly([(13,12),(15,12),(15,18),(13,22),(12,23),(11,22),(12,18)],'cape0')
        poly([(11,12),(12,12),(11,16),(8,21),(6,22),(8,17),(9,14)],'cape2')
        line(10,13,9,16,'cape3')
        line(10,19,9,21,'cape0')
    # Foreground leg switches from a forward reach to a trailing push.
    if phase == 0:
        poly([(14,19),(18,19),(18,22),(19,24),(21,26),(21,27),(24,28),(24,30),(18,30),(17,26),(15,24),(13,22)],'ink')
        poly([(14,20),(17,20),(17,23),(18,25),(16,25),(14,23)],'pants1')
        line(15,21,16,23,'pants2')
        poly([(17,24),(18,24),(20,27),(18,28),(17,27),(16,25)],'steel0')
        line(17,24,19,27,'steel2')
        poly([(18,27),(20,27),(20,28),(23,28),(23,29),(18,29)],'leather1')
        line(18,28,20,28,'leather2')
    else:
        poly([(13,18),(17,19),(16,22),(13,24),(12,26),(13,27),(15,28),(15,30),(9,30),(8,28),(9,25),(11,22)],'ink')
        poly([(13,20),(16,20),(14,22),(12,24),(10,26),(9,26),(11,23)],'pants1')
        line(14,20,12,23,'pants2')
        poly([(10,24),(12,24),(11,27),(9,28),(9,26)],'steel0')
        line(10,25,10,27,'steel2')
        poly([(9,28),(11,27),(12,28),(14,29),(14,30),(9,30)],'leather1')
        line(10,28,12,28,'leather2')
    # Upper body bobs by one pixel on the second contact.
    b = -phase
    def pp(points,color): poly([(x,y+b) for x,y in points],color)
    def rr(x,y,w,h,color): rect(x,y+b,w,h,color)
    def ll(x0,y0,x1,y1,color): line(x0,y0+b,x1,y1+b,color)
    def dd(x,y,color): dot(x,y+b,color)
    # Tunic, chest plate, hip panels and belt.
    pp([(13,11),(17,11),(19,13),(19,16),(18,18),(19,21),(17,23),(14,22),(12,23),(12,19),(11,15)],'ink')
    pp([(13,14),(17,13),(18,16),(17,19),(18,21),(15,21),(13,22),(13,18)],'leather1')
    pp([(14,12),(17,12),(18,14),(17,17),(14,17),(13,15)],'steel1')
    pp([(14,12),(17,12),(17,14),(14,15),(13,14)],'steel2')
    ll(14,12,16,12,'steel3')
    ll(14,17,16,17,'steel0')
    ll(13,19,17,19,'leather0')
    ll(13,20,17,20,'gold0')
    rr(16,19,2,2,'gold1')
    dd(16,19,'gold2')
    ll(14,21,14,22,'leather2')
    # Neck, blue collar and a small warm cape clasp.
    rr(15,9,4,3,'ink')
    rr(16,9,2,3,'skin0')
    dd(17,10,'skin1')
    ll(12,11,15,12,'cape2')
    dd(15,12,'gold2')
    # Head in profile. Nose, eye and cheek remain visibly right-facing.
    pp([(14,2),(18,2),(20,3),(20,5),(21,6),(20,7),(22,8),(21,9),(20,9),(20,11),(17,12),(14,10),(12,8),(12,4)],'ink')
    pp([(17,5),(20,6),(20,8),(21,8),(21,9),(19,9),(19,10),(17,10),(16,9),(16,7)],'skin1')
    ll(18,6,19,6,'skin2')
    rr(18,8,2,1,'skin2')
    dd(20,8,'skin2')
    dd(19,7,'ink')
    dd(19,10,'skin0')
    pp([(14,3),(18,3),(19,4),(20,4),(20,5),(18,6),(18,7),(16,7),(16,9),(14,10),(12,8),(13,7),(12,6),(13,4)],'hair1')
    pp([(14,3),(17,3),(19,4),(18,5),(16,5),(16,6),(14,7),(13,6),(13,5)],'hair2')
    ll(14,4,17,4,'hair3')
    dd(13,5,'hair3')
    dd(18,5,'hair2')
    ll(13,8,14,9,'hair0')
    dd(15,7,'hair0')
    dd(16,8,'skin2')
    dd(16,9,'skin0')
    # Sword: dark silhouette, cool cutting edge, gold crossguard, leather grip.
    pp([(22,14),(29,5),(30,4),(30,7),(24,15)],'ink')
    pp([(23,13),(29,6),(29,8),(24,14)],'steel1')
    ll(23,13,29,5,'steel3')
    ll(24,13,29,7,'steel2')
    ll(19,20,23,15,'ink')
    ll(20,19,23,15,'leather1')
    dd(20,19,'gold1')
    ll(21,13,26,17,'ink')
    ll(21,14,25,17,'gold0')
    ll(22,14,25,16,'gold1')
    dd(22,14,'gold2')
    # Front shoulder and bent arm overlap the grip naturally.
    pp([(16,12),(18,12),(19,14),(19,16),(21,16),(22,17),(22,19),(20,20),(18,18),(16,17),(15,14)],'ink')
    pp([(16,13),(18,13),(18,15),(17,16),(16,15)],'steel1')
    ll(16,13,17,13,'steel3')
    dd(18,14,'steel2')
    ll(17,16,19,18,'leather1')
    ll(18,16,20,18,'steel1')
    ll(19,16,20,17,'steel2')
    rr(20,17,2,2,'skin1')
    dd(21,17,'skin2')
    dd(20,19,'leather0')
    return c

frames = [draw_frame(0), draw_frame(1)]
result = new_canvas(64, 32, name='swordsman_walk')
result.blit(frames[0],0,0)
result.blit(frames[1],32,0)
stats = result.stats()
assert tuple(stats['size']) == (64, 32)
assert stats['colors_used'] <= 86
print(result.stats_text())
view(result, scale=8, margin=0)
save('swordsman_walk', result)
finish(result)
