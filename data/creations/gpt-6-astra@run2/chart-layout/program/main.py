result = new_canvas(128,64, background='#101a29', name='fruit_chart')
c=result
# Compact plotting panel, with a common zero and a five-pixel unit.
c.rect(15,3,110,54,'#152235')
for x in [18,43,68,93]:
    c.line(x,4,x,56,'#26364a')
c.line(18,55,117,55,'#516078')
for x,t in [(18,'0'),(43,'5'),(68,'10'),(93,'15')]:
    c.line(x,55,x,57,'#516078')
    c.text(x-(2 if len(t)==1 else 5),57,t,'#8b9bb1')
# Bar lengths are exactly proportional to the data: five pixels per unit.
rows=[(5,10,'#ed5261','#ff8790','#b8314c'),(15,5,'#eac34f','#ffe48a','#b78d33'),(25,7,'#f28e3d','#ffc06b','#be5b2e'),(35,14,'#e4dd55','#fffa9a','#aaa634'),(45,2,'#9b72d3','#c5a1ee','#6e479f')]
for y,value,base,hi,shadow in rows:
    c.rect(19,y,value*5,7,base)
    c.line(19,y,18+value*5,y,hi)
    c.line(19,y+6,18+value*5,y+6,shadow)
    c.text(22+value*5,y,str(value),'#f0f2df')
# Apple: leaf, split crown and a rounded red body.
c.line(7,5,7,3,'#a8784b')
c.line(8,3,10,2,'#78bc70')
c.poly([(3,6),(5,5),(7,6),(9,5),(11,6),(12,8),(11,11),(9,13),(7,12),(5,13),(3,11),(2,8)],'#af314d')
c.poly([(3,7),(5,6),(7,7),(10,6),(11,8),(10,11),(8,12),(5,11),(3,9)],'#ef5768')
c.line(4,7,4,9,'#ffadb0')
# Banana: a curved crescent with stepped edges.
c.poly([(3,16),(4,18),(6,21),(9,21),(12,18),(12,21),(10,24),(6,24),(3,22),(2,19),(2,16)],'#b88b31')
c.poly([(3,17),(4,20),(6,22),(9,22),(12,19),(11,22),(9,23),(6,23),(3,21)],'#f7d65f')
c.line(5,22,8,23,'#ffed9a')
c.set(2,16,'#77623c'); c.set(12,18,'#77623c')
# Orange: round citrus, small leaf and peel sparkle.
c.circle(7,29,5,'#bd5b2e')
c.circle(7,29,4,'#f39a43')
c.line(4,27,5,26,'#ffce80')
c.set(10,30,'#dd732f'); c.set(8,32,'#dd732f')
c.line(7,24,7,25,'#805c39'); c.line(8,24,10,23,'#6eac64')
# Lemon: pointed ends, bright rind, and a tiny green leaf.
c.poly([(1,39),(3,36),(6,35),(9,36),(12,39),(10,42),(7,43),(4,42)],'#a5a137')
c.poly([(2,39),(4,37),(6,36),(9,37),(11,39),(9,41),(6,42),(4,41)],'#eee666')
c.line(4,38,6,37,'#fff7b0'); c.set(7,37,'#fff7b0')
c.set(10,35,'#70ae64')
# Grapes: individual berries and a curling green stem.
c.line(7,45,8,43,'#8aae68'); c.line(8,43,10,43,'#8aae68')
for x,y in [(4,47),(8,47),(11,48),(5,50),(9,51),(7,54)]:
    c.circle(x,y,2,'#63468d')
    c.set(x,y,'#a783d5'); c.set(x-1,y-1,'#c7aaeb')
view(result, scale=5, margin=0)
save('fruit_chart',result)
finish(result)
