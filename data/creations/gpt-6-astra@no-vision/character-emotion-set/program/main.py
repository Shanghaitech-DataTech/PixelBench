# Four expressions of the same copper-haired adventurer.
result = new_canvas(64, 64, name='copper_emotions')
P = {
 'ink':'#242438', 'hairdark':'#713d4c', 'hair':'#b65a52',
 'hairlight':'#e88665', 'shine':'#ffc18b',
 'skinshadow':'#ce8272', 'skin':'#f2b891', 'skinlight':'#ffdab0',
 'blush':'#e98c80', 'white':'#fff1d3', 'iris':'#407e7d',
 'coatdark':'#285365', 'coat':'#3f8790', 'coatlight':'#71b9b3',
 'gold':'#e9b568', 'mouth':'#9b4c60', 'tongue':'#e8888e'
}
for name, col in P.items(): result.color(col, name)

def portrait(ox, oy, mood):
    def r(x,y,w,h,col): result.rect(ox+x,oy+y,w,h,col)
    def p(points,col): result.poly([(ox+x,oy+y) for x,y in points],col)
    def l(x,y,X,Y,col): result.line(ox+x,oy+y,ox+X,oy+Y,col)
    def s(x,y,col): result.set(ox+x,oy+y,col)
    # Compact shoulders and high teal collar.
    p([(11,23),(21,23),(21,24),(25,25),(28,28),(28,30),(4,30),(4,28),(7,25),(11,24)],'ink')
    p([(11,25),(21,25),(24,26),(26,28),(26,30),(6,30),(6,28),(8,26)],'coat')
    p([(21,26),(24,27),(26,29),(26,30),(19,30)],'coatdark')
    l(8,27,10,26,'coatlight'); l(7,28,7,29,'coatlight')
    r(12,22,8,4,'ink'); r(13,22,6,4,'skinshadow'); r(14,22,4,3,'skin')
    p([(10,24),(15,26),(15,29),(11,27)],'ink')
    p([(22,24),(17,26),(17,29),(21,27)],'ink')
    l(11,25,14,27,'coatlight'); l(21,25,18,27,'coatlight')
    r(15,27,3,3,'ink'); r(16,27,1,2,'gold')
    # Stepped, shared hair silhouette and copper volume.
    p([(12,1),(20,1),(20,2),(23,2),(23,3),(25,3),(25,5),(27,5),(27,8),(28,8),(28,18),(27,18),(27,21),(24,21),(24,23),(8,23),(8,21),(5,21),(5,18),(4,18),(4,9),(5,9),(5,6),(6,6),(6,4),(8,4),(8,3),(11,3),(11,2),(12,2)],'ink')
    p([(12,3),(20,3),(20,4),(23,4),(23,5),(25,5),(25,8),(26,8),(26,19),(24,19),(24,21),(8,21),(8,19),(6,19),(6,9),(7,9),(7,6),(9,6),(9,5),(12,5)],'hairdark')
    p([(11,4),(20,4),(20,5),(23,5),(23,7),(25,7),(25,13),(8,13),(7,10),(8,7),(10,7),(10,5)],'hair')
    # Face silhouette, ear tips, lit cheek and warm lower edge.
    p([(11,7),(22,7),(22,9),(24,9),(24,11),(26,11),(26,16),(24,17),(24,19),(22,21),(20,22),(13,22),(10,20),(8,17),(6,16),(6,12),(9,11)],'ink')
    r(7,12,2,4,'skinshadow'); r(24,12,2,4,'skinshadow')
    p([(12,8),(21,8),(21,9),(23,9),(23,17),(22,19),(20,21),(13,21),(10,19),(9,16),(9,11)],'skin')
    p([(12,9),(20,9),(20,11),(22,11),(22,17),(20,19),(13,19),(10,17),(10,11)],'skinlight')
    l(22,17,21,19,'skinshadow'); l(14,21,19,21,'skinshadow')
    # Swept fringe, asymmetrical highlights, and matching side locks.
    p([(10,5),(20,5),(23,7),(23,10),(21,9),(20,7),(18,8),(16,9),(14,10),(11,10),(11,12),(8,13),(8,18),(7,18),(7,10)],'ink')
    p([(11,5),(19,5),(20,6),(18,7),(16,8),(14,9),(10,9),(10,11),(8,12),(8,10),(9,7)],'hair')
    l(11,5,17,5,'hairlight'); l(9,6,14,6,'hairlight'); l(8,8,10,8,'hairlight')
    l(12,4,18,4,'shine')
    p([(21,5),(24,7),(25,10),(25,18),(24,19),(23,17),(23,11),(22,8)],'hair')
    l(23,7,24,9,'hairlight'); l(24,11,24,15,'hairlight')
    l(6,11,6,16,'hair'); s(7,19,'hairlight'); s(25,19,'hair')
    # Delicate cheek pixels and nose are common to every expression.
    r(10,16,2,1,'blush'); r(21,16,2,1,'blush')
    s(17,16,'skinshadow'); s(16,15,'skin')
    if mood == 'calm':
        l(10,11,13,11,'hairdark'); l(20,11,23,11,'hairdark')
        r(10,13,4,2,'ink'); r(20,13,4,2,'ink')
        r(10,14,2,1,'white'); r(20,14,2,1,'white')
        s(12,14,'iris'); s(22,14,'iris')
        l(15,19,18,19,'mouth'); s(14,18,'skinshadow')
    elif mood == 'smile':
        l(10,11,12,10,'hairdark'); l(21,10,23,11,'hairdark')
        l(10,14,11,13,'ink'); l(11,13,12,13,'ink'); l(12,13,14,15,'ink')
        l(19,15,21,13,'ink'); l(21,13,22,13,'ink'); s(23,14,'ink')
        p([(13,17),(20,17),(19,20),(15,20)],'ink')
        r(14,17,6,1,'white'); r(15,19,4,1,'tongue')
        r(10,16,3,1,'blush'); r(21,16,3,1,'blush')
    elif mood == 'angry':
        l(10,11,14,13,'hairdark'); s(13,13,'ink')
        l(19,13,23,11,'hairdark'); s(20,13,'ink')
        r(10,14,4,2,'ink'); r(20,14,4,2,'ink')
        s(10,14,'white'); s(20,14,'white'); s(11,15,'iris'); s(21,15,'iris')
        l(14,20,15,19,'mouth'); l(15,19,18,19,'mouth'); s(19,20,'mouth')
        s(17,12,'skinshadow')
    else:
        l(10,10,13,10,'hairdark'); l(20,10,23,10,'hairdark')
        r(10,12,4,4,'ink'); r(20,12,4,4,'ink')
        r(10,13,3,2,'white'); r(20,13,3,2,'white')
        r(12,13,1,2,'iris'); r(22,13,1,2,'iris')
        s(12,13,'ink'); s(22,13,'ink')
        p([(16,17),(18,17),(19,18),(19,20),(18,21),(16,21),(15,20),(15,18)],'ink')
        r(16,18,2,2,'mouth'); r(16,20,2,1,'tongue')

for x,y,m in [(0,0,'calm'),(32,0,'smile'),(0,32,'angry'),(32,32,'surprise')]:
    portrait(x,y,m)
print(result.stats_text())
print(result.matrix_text(region=(4,8,27,22)))
save('character-emotion-set',result)
finish(result)
