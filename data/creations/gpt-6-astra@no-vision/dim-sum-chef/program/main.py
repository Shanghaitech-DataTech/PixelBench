from pixelbench_api import *

# A compact, front-facing kitchen sprite. All clusters are placed on the native grid.
c = new_canvas(32, 32, name='Dim sum chef')
P = {
 'O':'#302d39', 'H':'#573d37',
 'W':'#fff6df', 'w':'#e1e8da', 's':'#9aafb0', 'j':'#bccfc9',
 'S':'#f1b17c', 'L':'#ffcf95', 't':'#bf7957', 'r':'#e28c72',
 'a':'#577d85', 'b':'#385965', 'l':'#7e9d9d', 'f':'#dce5d8',
 'R':'#b64f47', 'q':'#e07859',
 'D':'#66432f', 'B':'#a56a35', 'M':'#d59b4c', 'Y':'#f2c779',
 'u':'#c4aa7a', 'v':'#ead8ac', 'U':'#fff1ce',
 'p':'#515564', 'k':'#818c95',
}
for key, val in P.items():
    c.color(val, name=key)
def px(x,y,k): c.set(x,y,P[k])
def span(y,x0,x1,k): c.line(x0,y,x1,y,P[k])
def pattern(x,y,rows):
    for dy,row in enumerate(rows):
        for dx,ch in enumerate(row):
            if ch != '.': px(x+dx,y+dy,ch)

# Tailored jacket: broad shoulders, bent elbows and light sleeves.
for y,x0,x1 in [(14,10,21),(15,8,23),(16,7,24),(17,6,25),(18,6,25),(19,6,25),(20,6,25),(21,6,25),(22,7,24),(23,8,23),(24,9,22),(25,9,22),(26,9,22)]:
    span(y,x0,x1,'O')
for y,x0,x1 in [(15,10,21),(16,8,23),(17,7,24),(18,7,24),(19,7,24),(20,7,24),(21,7,24),(22,8,23),(23,9,22),(24,10,21),(25,10,21)]:
    span(y,x0,x1,'w')
# The shadow side of each sleeve remains separate from both skin and apron.
span(17,7,8,'j'); span(18,7,8,'j'); span(19,7,8,'s')
span(17,23,24,'j'); span(18,23,24,'j'); span(19,23,24,'s')
px(9,16,'W'); px(22,16,'W')
span(18,9,10,'W'); span(18,21,22,'W')

# Work trousers and shoes, behind the apron hem.
pattern(10,26,[
 'OOOOO..OOOOO',
 'OpppO..OpppO',
 'OpkpO..OpkpO',
 'OkkpO..OpkkO',
 'OOOOO..OOOOO',
])
# Slightly wider toe caps.
span(29,9,10,'O'); span(29,21,22,'O')
span(30,9,14,'O'); span(30,17,22,'O')

# Blue-green apron has an unmistakable bib and a squared, dusted lower hem.
c.poly([(12,15),(19,15),(20,18),(21,21),(22,26),(21,28),(10,28),(9,26),(10,21),(11,18)],P['O'])
c.poly([(12,16),(19,16),(19,19),(20,21),(21,26),(20,27),(11,27),(10,26),(11,21),(12,19)],P['a'])
span(26,11,20,'a'); span(27,11,20,'b')
# Apron folds / seam.
c.line(11,20,11,25,P['l']); c.line(20,20,20,25,P['b'])
# Small groups of flour rather than a uniform decorative pattern.
for x,y,k in [(12,17,'f'),(13,17,'l'),(12,18,'l'),(18,16,'l'),(18,17,'f'),
              (12,24,'l'),(12,25,'f'),(13,25,'f'),(11,26,'f'),(13,26,'l'),
              (17,25,'l'),(18,25,'f'),(19,26,'f'),(18,26,'l'),(15,26,'f')]: px(x,y,k)

# White lapels, a red neckerchief, and the two teal apron straps.
span(14,12,19,'O'); span(14,14,17,'S')
for x,y in [(11,15),(12,15),(13,16),(18,16),(19,15),(20,15)]: px(x,y,'W')
px(13,15,'w'); px(18,15,'w')
px(11,16,'b'); px(12,16,'l'); px(19,16,'l'); px(20,16,'b')
px(14,15,'R'); px(15,15,'q'); px(16,15,'R'); px(17,15,'R')
px(14,16,'O'); px(15,16,'R'); px(16,16,'q'); px(17,16,'O')

# Warm face and ears, precisely framed: two eyes and an open, friendly smile.
pattern(9,8,[
 '.OHLLLLLLLLHO.',
 'OStLLLLLLLLtSO',
 'OSSLOLLLLOLSSO',
 '.OSrSSLtSSrSO.',
 '..OSSHWWHSSO..',
 '...OtSLLStO...',
])

# A puffy, double-lobed toque with a shaded folded band.
span(1,11,14,'O'); span(1,17,20,'O')
span(2,9,22,'O'); span(2,11,14,'W'); span(2,17,20,'W')
span(3,8,23,'O'); span(3,9,22,'W')
span(4,8,23,'O'); span(4,9,22,'W')
span(5,9,22,'O'); span(5,10,21,'w')
span(6,10,21,'O'); span(6,11,20,'w')
span(7,10,21,'O')
# Folds are compact pixel clusters, not smooth shading.
px(9,4,'w'); px(10,4,'w'); px(11,3,'w'); px(11,4,'s')
px(20,3,'w'); px(20,4,'s'); px(21,4,'w'); px(22,4,'w')
span(5,12,19,'W'); span(6,12,19,'W'); px(20,6,'s')

# The open bamboo steamer: dark interior sits BEHIND the pale buns.
c.ellipse(15,20,7,2,P['D'])
span(18,9,22,'D'); span(19,8,23,'D')
span(20,9,22,'D')
# Three cream-coloured buns. Each has its own contour and pinched pleats;
# no skin colours are used in the food. The central bun sits at the back.
pattern(13,16,[
 '..uu..',
 '.uUUu.',
 'uUvUUu',
 '.uvvu.',
])
pattern(9,17,[
 '..uu..',
 '.uUUu.',
 'uUvUUu',
 '.uvvu.',
])
pattern(17,17,[
 '..uu..',
 '.uUUu.',
 'uUUvUu',
 '.uvvu.',
])

# Hands grasp the sides, outside the basket. Dark cuffs prevent merging.
pattern(6,20,[
 'OOO.',
 'OtSO',
 'OSLO',
 '.OSO',
 '..O.',
])
pattern(22,20,[
 '.OOO',
 'OStO',
 'OLSO',
 'OSO.',
 '.O..',
])
# Golden elliptical lip and basket wall, with a distinctly different outline.
span(20,10,21,'D')
span(21,9,22,'D'); span(21,10,21,'Y')
span(22,9,22,'D'); span(22,10,21,'M')
span(23,10,21,'D'); span(23,11,20,'B')
span(24,11,20,'D')
# Bamboo slats, a horizontal binding, and the warm lit upper edge.
for x in [11,14,17,20]: px(x,22,'Y'); px(x,23,'M')
for x in [12,15,18]: px(x,23,'D')
span(20,11,20,'Y')
px(10,20,'M'); px(21,20,'M')

print(c.stats_text())
print(c.matrix_text())
save('dim-sum-chef',c)
result = c
finish(result)
