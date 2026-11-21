import random
random.seed(14)
result = new_canvas(64,64,background='#778c6a',name='harvest_terraces')
c=result
# Distant hillside, softened values
c.poly([(0,7),(12,4),(22,6),(35,1),(49,0),(63,4),(63,26),(0,26)],'#657c59')
c.path('M0 14 Q15 6 29 12 T64 9 L64 28 L0 28 Z','#8e9960')
c.path('M0 20 Q13 12 27 17 Q42 23 64 13 L64 27 L0 29 Z','#a6a364')
# high terraces and narrow contour lines
c.path('M0 11 Q12 8 24 11 M30 9 Q44 4 63 7','#a8aa74',False)
c.path('M0 18 Q15 11 29 17 Q44 21 63 12','#596f4b',False)
c.path('M0 21 Q16 15 30 20 Q46 24 63 16','#d0b568',False)
# village clearing
c.poly([(34,7),(51,5),(63,9),(63,15),(48,14),(34,12)],'#a8a578')
c.path('M42 10 Q49 14 61 16','#c6b684',False)
def house(x,y,w,h):
    c.rect(x,y,w,h,'#d1c39a')
    c.rect(x+w-2,y,2,h,'#a69874')
    c.poly([(x-1,y),(x+2,y-3),(x+w-2,y-3),(x+w+1,y+1),(x-1,y+1)],'#5b6257')
    c.line(x+2,y-3,x+w-2,y-3,'#89907b')
    c.rect(x+2,y+h-2,2,2,'#65664e')
house(36,9,6,4)
house(47,7,7,4)
house(56,11,6,4)
# village trees
for x,y in [(31,9),(44,7),(61,5)]:
    c.line(x,y,x,y+4,'#596847')
    c.circle(x,y,2,'#4e6b4c')
    c.set(x-1,y-1,'#7f9261')
# Broad contour terrace fields, rolling down the mountain
c.path('M0 25 Q13 17 27 25 Q41 34 64 20 L64 64 L0 64 Z','#59653b')
c.path('M0 24 Q13 16 27 24 Q42 33 64 19 L64 24 Q42 39 26 30 Q12 21 0 29 Z','#c9a849')
c.path('M0 24 Q13 16 27 24 Q42 33 64 19','#e2c56a',False)
c.path('M0 30 Q13 22 26 31 Q43 40 64 25 L64 31 Q43 48 24 37 Q12 28 0 36 Z','#9c7831')
c.path('M0 30 Q13 22 26 31 Q43 40 64 25 L64 29 Q43 45 25 35 Q12 26 0 34 Z','#dfb643')
c.path('M0 30 Q13 22 26 31 Q43 40 64 25','#f1d276',False)
c.path('M0 38 Q12 29 25 39 Q44 50 64 33 L64 40 Q44 58 23 46 Q12 36 0 45 Z','#775d2e')
c.path('M0 37 Q12 28 25 38 Q44 49 64 32 L64 38 Q44 54 24 44 Q12 34 0 42 Z','#e8be4c')
c.path('M0 37 Q12 28 25 38 Q44 49 64 32','#ffe095',False)
c.path('M0 47 Q12 37 25 47 Q44 60 64 42 L64 51 Q44 68 23 55 Q12 45 0 54 Z','#69532b')
c.path('M0 46 Q12 36 25 46 Q44 59 64 41 L64 48 Q44 65 24 52 Q12 42 0 51 Z','#d7a43a')
c.path('M0 46 Q12 36 25 46 Q44 59 64 41','#f8d875',False)
c.path('M0 57 Q12 45 25 57 Q44 71 64 52 L64 64 L0 64 Z','#edc353')
c.path('M0 57 Q12 45 25 57 Q44 71 64 52','#ffe59a',False)
# rice rows: short stalk clusters, deliberately follow the golden planting areas
fieldcols={c.color('#c9a849'),c.color('#dfb643'),c.color('#e8be4c'),c.color('#d7a43a'),c.color('#edc353')}
for y in range(21,64):
    for x in range(1,63):
        if c.get(x,y) in fieldcols and c.get(x,y-1) in fieldcols:
            if (x+2*y)%5==0 and random.random()<.62:
                col='#b88b31' if y<39 else '#b6842d'
                c.set(x,y,col)
                if random.random()<.65: c.set(x,y-1,'#f6d879')
# irregular grasses on the terrace retaining edges
for x,y in [(2,35),(8,26),(23,36),(30,46),(47,43),(56,32),(6,53),(20,52),(48,58),(59,49)]:
    c.line(x,y,x,y-1,'#586234')
    c.set(x+1,y,'#9a9845')
# two farmers on the ridges, with broad straw hats and small cast shadows
def farmer(x,y,shirt):
    c.ellipse(x+2,y+5,3,1,'#706331')
    c.set(x-1,y+4,'#4c4933'); c.set(x+1,y+4,'#4c4933')
    c.rect(x-1,y+1,3,3,shirt)
    c.set(x-2,y+2,'#be8551'); c.set(x+2,y+2,'#be8551')
    c.set(x,y,'#d8a36b')
    c.line(x-2,y-1,x+2,y-1,'#92692f')
    c.line(x-2,y-2,x+2,y-2,'#f6d887')
    c.rect(x-1,y-3,3,1,'#ffe8a5')
farmer(18,29,'#496d70')
c.line(21,31,23,28,'#655333')
c.set(24,28,'#d8d6a6')
farmer(48,47,'#a7543b')
# tied harvest sheaves beside the nearer worker
for x,y in [(42,47),(56,40),(8,41)]:
    c.line(x,y-2,x-1,y+1,'#f6dc83')
    c.line(x+1,y-2,x+2,y+1,'#f6dc83')
    c.line(x,y-1,x+1,y-1,'#97713a')
view(result)
finish(result)
