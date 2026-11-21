result = new_canvas(128, 64, '#fff8e8', name='fruit_chart')
c = result
# Quiet plotting guides, with an even six pixels per fruit.
grid = '#e5ddc9'
ink = '#514b47'
for x in (53, 83, 113):
    for y in range(3, 54, 3):
        c.line(x, y, x, y+1, grid)
c.line(23, 3, 23, 54, '#b8af9d')
c.line(23, 54, 116, 54, '#b8af9d')
for x, label in ((23,'0'),(53,'5'),(83,'10'),(113,'15')):
    c.set(x,55,'#b8af9d')
    c.text(x-(2 if len(label)==1 else 5),57,label,'#888071')
# Exact, common-scale bar lengths. Light upper edges and dark lower edges.
rows = [(10,'#dd4f53','#f47d70','#b93749'),
        (5,'#edc342','#ffe17b','#c89b2d'),
        (7,'#ef8c32','#ffb65b','#cd642b'),
        (14,'#e4d84e','#fff18b','#b6ad39'),
        (2,'#9363b4','#ba8dd0','#70448e')]
for i,(value,base,light,shade) in enumerate(rows):
    y = 5 + i*10
    w = value*6
    c.rect(24,y,w,7,base)
    c.line(24,y,23+w,y,light)
    c.line(24,y+6,23+w,y+6,shade)
    c.text(28+w,y,str(value),ink)
# Apple: cleft shoulders, woody stalk and a leaf.
c.line(11,2,12,4,'#6d513c')
c.poly([(12,2),(15,1),(15,3),(12,3)],'#54844e')
c.poly([(6,5),(8,4),(11,5),(14,4),(16,6),(16,9),(14,12),(12,13),(10,12),(8,13),(6,10)],'#9d3545')
c.poly([(7,6),(9,5),(11,6),(14,5),(15,7),(14,10),(12,12),(10,11),(8,12),(7,9)],'#e45458')
c.line(8,6,8,8,'#ff9a82')
c.set(9,5,'#ff9a82')
# Banana: a curved crescent with squared tips.
c.poly([(6,16),(8,15),(9,19),(12,21),(15,20),(17,17),(17,21),(14,24),(10,24),(7,22),(5,19)],'#a8802e')
c.poly([(6,16),(7,16),(8,20),(11,22),(14,22),(16,20),(15,22),(13,23),(10,23),(7,21),(6,19)],'#f3ce4f')
c.line(8,20,11,22,'#ffe99a')
c.line(11,22,14,22,'#ffe99a')
c.set(6,15,'#64513c')
c.set(17,17,'#64513c')
# Orange and its leaf.
c.circle(11,29,5,'#bd602c')
c.circle(11,28,4,'#f89b36')
c.line(8,27,9,26,'#ffcf73')
c.set(13,30,'#d77a2d')
c.line(11,24,11,22,'#74583c')
c.poly([(12,23),(14,21),(17,22),(15,24)],'#54844e')
# Lemon, with pointed ends and a tiny reflected glint.
c.poly([(5,39),(7,36),(10,35),(14,35),(16,37),(18,38),(16,41),(13,42),(9,42),(7,40)],'#a99a35')
c.poly([(6,38),(9,36),(13,36),(16,38),(16,40),(13,41),(10,41),(8,39)],'#eee05b')
c.line(9,37,12,37,'#fff7a8')
c.set(17,38,'#f2e66f')
# Grapes: individual outlined berries tapering to a single grape.
c.line(11,44,12,42,'#74583c')
c.poly([(12,44),(14,42),(17,43),(15,45)],'#54844e')
for x,y in ((8,46),(12,46),(16,47),(10,49),(14,50),(12,53)):
    c.circle(x,y,2,'#67447c')
    c.circle(x,y,1,'#9c6bbb')
    c.set(x-1,y-1,'#c99bda')
view(result, scale=6, margin=0)
save('fruit_chart', result)
finish(result)
