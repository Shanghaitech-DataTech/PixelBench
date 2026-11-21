import math, random
random.seed(21)
result = new_canvas(64,64, '#52654b', name='harvest_terraces')
c=result
# Cool wooded uplands: the whole view looks down on the mountain.
c.poly([(0,0),(64,0),(64,12),(52,16),(36,10),(21,12),(0,8)], '#69765a')
c.poly([(0,0),(38,0),(31,6),(17,8),(0,6)], '#809077')
c.poly([(44,0),(64,0),(64,17),(56,14),(53,7)], '#405c4b')
for x,y,r in [(1,3,3),(8,1,3),(33,2,3),(40,4,3),(58,3,4),(63,7,3),(52,1,2)]:
    c.circle(x,y,r,'#526e56')
    c.line(x-1,max(0,y-1),x+1,max(0,y-1),'#738467')
# Irregular narrow contour banks separate the ripe fields.
bases=[8,13,19,26,34,43,53,64]
amps=[4,6,8,9,9,9,8,7]
def edge(i,x):
    return round(bases[i] + amps[i]*math.sin(math.pi*(x+4)/72) + 1.3*math.sin(x*.12+i*.37))
fields=['#b2a455','#c6ad53','#d8b64c','#e0ba4c','#e7bf50','#edc758','#f1cc65','#e8bd50']
banks=['#66704a','#686b3e','#706a34','#776735','#796335','#7e6436','#806135','#826035']
for i in range(len(bases)):
    pts=[(x,edge(i,x)) for x in range(64)]+[(63,64),(0,64)]
    c.poly(pts,banks[i])
    pts=[(x,edge(i,x)+2) for x in range(64)]+[(63,64),(0,64)]
    c.poly(pts,fields[i])
    # Sunlit footpath lip over the shaded vertical bank.
    for x in range(64):
        y=edge(i,x)
        if 0<=y<64: c.set(x,y,'#aea05a' if i<3 else '#c6aa5a')
    # Staggered stubble follows contour, with clear untextured breathing room.
    for x in range(1,63):
        top=edge(i,x)+3
        bot=edge(i+1,x)-1 if i+1<len(bases) else 64
        if x%3==i%3:
            for y in range(top, min(bot,64),3):
                if random.random()<.77:
                    c.set(x,y, '#9e8e3f' if i<3 else '#bf993b')
                    if y-1>top-1: c.set(x,y-1,'#e3c66d' if i<3 else '#ffe08a')
# Walking route along the right-hand shoulder, linking the contour paths.
c.path('M 58 13 L 55 19 L 56 24 L 52 30 L 54 34 L 50 40 L 52 44 L 48 50 L 49 55 L 46 63', '#887843', fill=False)
c.path('M 59 13 L 56 19 L 57 24 L 53 30 L 55 34 L 51 40 L 53 44 L 49 50 L 50 55 L 47 63', '#d2bb77', fill=False)
# Small settlement perched high on the slope, roofs seen from above.
c.path('M 11 3 L 15 9 L 26 10 L 31 7 M 22 9 L 22 13', '#a39c78',fill=False)
def house(x,y,w,h):
    c.rect(x+1,y+2,w,h,'#4c5846')
    c.rect(x,y+2,w-1,h-1,'#c5b893')
    c.rect(x+w-3,y+3,2,h-2,'#95896b')
    c.poly([(x-1,y+2),(x+2,y-1),(x+w-3,y-1),(x+w,y+2)], '#6a655c')
    c.poly([(x-1,y+2),(x+2,y-1),(x+w-3,y-1),(x+w-2,y+2)], '#a28d70')
    c.line(x+2,y-1,x+w-3,y-1,'#c6b292')
    c.set(x+2,y+h,'#53564b')
house(8,4,7,4)
house(21,3,8,4)
house(30,8,6,3)
# Low shrubs at the village edge.
for x,y in [(3,8),(5,10),(17,10),(38,11),(61,16)]:
    c.rect(x,y,3,2,'#536746');c.set(x,y-1,'#87925a')
# Two workers on separate ridges: shadows, dark legs, indigo/russet clothing,
# broad straw hats seen from above, and small harvesting tools.
def farmer(x,i,shirt):
    y=edge(i,x)
    c.line(x,y+1,x+3,y+2,'#746334')
    c.set(x-1,y+1,'#373f38');c.set(x+1,y+1,'#373f38')
    c.rect(x-1,y-2,3,3,shirt)
    c.set(x-2,y-1,'#b48450');c.set(x+2,y,'#ce9d60')
    c.line(x+3,y-2,x+3,y+1,'#6b5936')
    c.set(x+4,y-3,'#e3d8a2')
    c.line(x-2,y-3,x+2,y-3,'#9e6f34')
    c.line(x-2,y-4,x+2,y-4,'#f6d786')
    c.line(x-1,y-5,x+1,y-5,'#ffe5a3')
    c.set(x,y-4,'#e1b65d')
farmer(18,4,'#405b5a')
farmer(42,5,'#9e563b')
# Tied bundles of harvested rice on a sunny foreground plot.
for x,y in [(7,51),(11,53),(29,58),(33,59)]:
    c.line(x-1,y+2,x+2,y+2,'#b28a35')
    c.poly([(x-1,y+1),(x,y-3),(x+2,y+1)], '#ffe293')
    c.line(x,y-2,x+1,y+1,'#e4b54b')
    c.line(x,y,x+1,y,'#987333')
view(result)
finish(result)
