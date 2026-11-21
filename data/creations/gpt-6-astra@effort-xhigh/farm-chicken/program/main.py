# A warm, rounded farm hen, drawn directly on the 32-pixel grid.
result = new_canvas(32, 32, name="farm_chicken")
c = result
P = {
    'edge': '#715443',
    'shadow': '#b79a70',
    'ochre': '#d3b887',
    'cream': '#ead7a9',
    'light': '#f7ebcb',
    'white': '#fff4d9',
    'rededge': '#945548',
    'red': '#bd6a58',
    'pink': '#df9279',
    'beakedge': '#a16e42',
    'gold': '#dca258',
    'goldlight': '#edbd70',
    'eye': '#473a32',
}
def row(y,x0,x1,color):
    c.rect(x0,y,x1-x0+1,1,P[color])
# Two short legs and little splayed toes sit behind the soft belly.
c.rect(12,24,2,5,P['beakedge'])
c.rect(13,25,1,3,P['gold'])
row(28,10,14,'beakedge')
row(28,11,13,'gold')
c.set(12,27,P['goldlight'])
c.rect(20,24,2,5,P['beakedge'])
c.rect(21,25,1,3,P['gold'])
row(28,19,23,'beakedge')
row(28,20,22,'gold')
c.set(20,27,P['goldlight'])
# The comb has three rounded, slightly uneven lobes.
for y,a,b in [(3,22,23),(4,19,20),(4,22,24),(5,19,26),(6,19,26),(7,19,26),(8,20,25)]:
    row(y,a,b,'rededge')
for y,a,b in [(4,23,23),(5,20,20),(5,22,24),(6,20,25),(7,20,25)]:
    row(y,a,b,'red')
c.set(23,4,P['pink'])
c.set(20,5,P['pink'])
row(6,20,23,'pink')
# Continuous stepped silhouette: upright head, broad belly, lifted tail.
outline = {
  7:(20,24), 8:(18,25), 9:(17,26), 10:(4,27),
  11:(4,27),12:(3,27),13:(2,27),14:(3,27),
  15:(3,26),16:(4,26),17:(4,26),18:(4,26),19:(4,26),
  20:(4,25),21:(5,25),22:(6,24),23:(7,23),24:(9,22),25:(11,20)
}
# Head and torso are kept separate at the raised tail's tip.
for y,(a,b) in outline.items():
    if y in (10,11):
        row(y,17 if y==10 else 15,b,'edge')
    else:
        row(y,a,b,'edge')
row(10,4,5,'edge')
row(11,4,7,'edge')
# Cream plumage fill, manually stepped to preserve one-pixel contours.
for y,a,b in [
    (8,20,24),(9,18,25),(10,18,26),(11,17,26),
    (12,5,26),(13,4,26),(14,4,26),(15,5,25),
    (16,5,25),(17,5,25),(18,5,25),(19,5,25),
    (20,5,24),(21,6,24),(22,7,23),(23,9,22),(24,11,20)]:
    row(y,a,b,'cream')
# Tail feathers are three soft, upward-pointing tufts.
row(11,5,6,'light')
row(12,5,8,'light')
row(13,3,5,'light')
row(13,7,10,'light')
row(14,5,7,'ochre')
row(15,6,8,'ochre')
# Lower contour is shaded in honey and warm oat tones.
for y,a,b in [(18,5,6),(19,5,7),(20,5,8),(21,6,9),(22,7,11),(23,9,22),(24,11,20)]:
    row(y,a,b,'ochre')
row(23,12,21,'ochre')
row(24,12,19,'shadow')
row(22,21,23,'ochre')
row(21,23,24,'ochre')
row(20,24,24,'ochre')
# Broad top-left light: a softly rounded neck and back.
for y,a,b in [(9,20,24),(10,19,25),(11,18,25),(12,16,25),
              (13,10,25),(14,8,24),(15,8,23),(16,8,22),
              (17,9,21),(18,11,21),(19,18,22),(20,19,21)]:
    row(y,a,b,'light')
row(10,20,23,'white')
row(11,19,22,'white')
row(12,18,21,'white')
row(13,12,18,'white')
row(14,10,15,'white')
# The folded wing is a small pear-shaped patch, low on the round flank.
for y,a,b in [(16,10,14),(17,9,16),(18,9,17),(19,10,17),(20,11,17),(21,12,16)]:
    row(y,a,b,'ochre')
for y,a,b in [(16,11,14),(17,10,15),(18,10,16),(19,11,16),(20,12,15)]:
    row(y,a,b,'cream')
row(16,11,13,'light')
row(17,10,13,'light')
c.set(15,19,P['ochre'])
c.set(13,20,P['ochre'])
# A small cheek and red wattle hang below the beak.
row(15,25,26,'rededge')
row(16,24,26,'rededge')
row(17,24,25,'rededge')
c.set(25,15,P['pink'])
row(16,24,25,'red')
# Short golden beak points gently to the right.
row(12,27,28,'beakedge')
row(13,27,29,'beakedge')
row(14,27,28,'beakedge')
row(13,27,28,'goldlight')
c.set(27,14,P['gold'])
# A clear, kind eye with a single cream catchlight.
c.rect(24,10,2,3,P['eye'])
c.set(24,10,P['white'])
c.set(23,13,P['cream'])
view(result, scale=12, margin=2)
save('farm_chicken', result)
finish(result)
