import math, random
rng = random.Random(18)
result = new_canvas(64,64,background='#5f7970',name='harvest_terraces')
c = result
P = {
'far':'#6e8980','far_l':'#87998a','far_d':'#59796f',
'wood':'#35574e','wood_m':'#456b57','leaf':'#5f7b55','leaf_l':'#83905e',
'bank_d':'#45553a','bank':'#637044','grass':'#8a8a46','earth':'#916c36',
'gold_d':'#b28a3c','gold':'#d2a64a','gold_l':'#e6bc56','sun':'#f3d37a','pale':'#f6dda0',
'ochre':'#b77e32','straw':'#cf9841','shadow':'#72572f',
'roof_d':'#633f32','roof':'#956047','roof_l':'#be8055','wall':'#d6bf8d','wall_d':'#a99269',
'ink':'#344744','blue':'#426a74','blue_l':'#739394','red':'#9f4e37','skin':'#d9a36c'
}
# Quiet, cooler upper mountains, seen from above.
c.poly([(0,0),(64,0),(64,10),(56,9),(50,12),(40,10),(31,12),(25,10),(16,14),(0,15)],P['far'])
c.poly([(0,1),(8,2),(16,6),(22,7),(27,11),(21,14),(8,16),(0,14)],P['far_d'])
c.poly([(23,0),(36,0),(42,3),(51,4),(63,1),(63,6),(52,8),(42,7),(34,5)],P['far_l'])
c.path('M0 10 Q9 5 17 10 Q22 11 29 16 L26 22 L0 24 Z',P['wood_m'])
c.path('M0 13 Q8 9 14 12 Q18 14 20 20 L12 26 L0 26 Z',P['wood'])
# Small angular tree crowns break the distant hill silhouette.
for x,y,s in [(1,10,3),(7,9,3),(12,12,3),(18,14,2),(24,12,2),(29,11,2),(59,9,3),(63,12,2)]:
    c.poly([(x-s,y+2),(x-s,y),(x-1,y),(x-1,y-2),(x+1,y-2),(x+1,y-1),(x+s,y),(x+s,y+3),(x,y+4)],P['wood_m'])
    c.line(x-s+1,y,x,y-1,P['leaf'])
    c.set(x+1,y+2,P['wood'])
# Small leaf clusters keep the wooded hollow organic but subdued.
for x,y in [(2,16),(4,12),(9,13),(13,16),(7,20),(1,21),(16,18),(20,15),(24,14)]:
    c.line(x,y,x+2,y,P['wood_m'])
    c.set(x+1,y-1,P['leaf'])
    c.set(x+3,y+1,P['wood'])
# Faint contour traces in the hills beyond the houses.
c.path('M2 3 Q10 3 15 6 Q22 10 28 7 Q32 4 38 4', '#7f9280',fill=False)
c.path('M21 1 Q28 4 32 2 L35 1', '#7f9280',fill=False)
c.path('M47 2 Q55 5 63 3', '#9aa18a',fill=False)
# A high shelf supports the little village.
c.path('M23 15 Q29 10 38 10 Q46 9 55 12 L63 14 L63 23 L24 23 Z','#9b9b67')
c.path('M26 17 Q37 14 44 14 Q52 13 63 17 L63 22 L25 22 Z','#b7ac70')
c.path('M29 17 Q40 11 49 14 L59 17', '#d2bd85',fill=False)
# Monotone cubic interpolation gives each terrace a continuous mountain contour.
xs=[0,8,16,24,32,40,48,56,63]
profiles=[
[22,23,23,21,17,15,16,18,20],
[27,28,27,24,21,20,21,23,24],
[35,36,33,29,27,26,27,29,30],
[44,44,41,37,34,33,34,36,37],
[54,53,50,46,42,41,42,45,46],
[65,64,61,57,53,52,53,56,58],
[78,77,73,69,65,64,65,68,70]
]
def curve(vals):
    out=[]
    for x in range(64):
        i=min(7,next((j for j in range(8) if xs[j]<=x<=xs[j+1]),7))
        t=(x-xs[i])/(xs[i+1]-xs[i])
        a,b=vals[i],vals[i+1]
        m0=(vals[i+1]-vals[max(0,i-1)])/(xs[i+1]-xs[max(0,i-1)])*(xs[i+1]-xs[i])
        m1=(vals[min(8,i+2)]-vals[i])/(xs[min(8,i+2)]-xs[i])*(xs[i+1]-xs[i])
        out.append(round((2*t**3-3*t*t+1)*a+(t**3-2*t*t+t)*m0+(-2*t**3+3*t*t)*b+(t**3-t*t)*m1))
    return out
edges=[curve(p) for p in profiles]
fields=['#b9a458','#c8a34c',P['gold'], '#dcb04c',P['gold_l'],'#e8bd55']
# Each retaining wall has a lit lip, green crest, and deep earthen face.
for band in range(6):
    for x in range(64):
        top=edges[band][x]
        bottom=edges[band+1][x]
        for y in range(max(0,top),min(64,bottom)):
            color=fields[band]
            if y==top: color=P['gold_d'] if band<3 else P['straw']
            if y==bottom-3: color=P['grass']
            if y==bottom-2: color=P['bank']
            if y==bottom-1: color=P['bank_d']
            c.set(x,y,color)
# Hand-sized crop clusters, arranged along the curved terraces.
for band in range(6):
    for x in range(2,63):
        top,bottom=edges[band][x],edges[band+1][x]
        if (x+band*3)%6==0:
            y=top+2
            if y<bottom-3 and y<63:
                c.set(x,y,P['sun'] if band>=2 else '#dfc773')
                if x+1<64: c.set(x+1,y-1,P['sun'] if band>=2 else '#dfc773')
                if band>=3 and y+1<bottom-3: c.set(x,y+1,P['straw'])
        if band>=2 and (x+band)%9==0:
            y=bottom-5
            if y>top+2 and y<63:
                c.line(x,y,min(63,x+2),y,P['gold_d'])
                c.set(x+1,y-1,P['sun'])
# The near banks show dark soil under the grass, and clumps of ripe rice.
for band in range(3,6):
    for x in range(64):
        y=edges[band][x]
        if y<64:
            c.set(x,y, '#8d7137' if band==3 else '#957235')
            if x%11 in (0,1,2) and y+1<64:
                c.set(x,y+1,P['gold_d'])
for band in range(2,6):
    for x in range(3,61):
        if (x+3*band)%8 != 0: continue
        y=edges[band][x]+3
        if y+1>=min(64,edges[band+1][x]-3): continue
        c.set(x,y+1,P['ochre'])
        c.set(x,y,P['sun'])
        c.set(x-1,y-1,P['sun'])
        c.set(x+1,y-1,P['pale'] if band>=4 else P['sun'])
# Deliberate cut swathes: short warm bands echo the contour, with a few stubble ticks.
for band, xa, xb in [(1,2,10),(2,38,47),(3,6,15),(4,29,38),(5,3,18),(5,51,60)]:
    for x in range(xa,xb+1):
        y=edges[band][x]+2
        if y<64:
            c.set(x,y,P['straw'])
            if y+1<edges[band+1][x]-3 and y+1<64:c.set(x,y+1,P['gold'])
            if x%3==0 and y+1<64:c.set(x,y+1,P['sun'])
# Intermittent grasses grow from the narrow ridge lips.
for band in range(1,6):
    for x in range(1,63):
        y=edges[band][x]-2
        if (x*7+band*5)%23==0 and y<64:
            c.set(x,y-1,P['bank'])
            c.set(x+1,y,P['leaf_l'])
# A short diagonal stair links the upper village to the first terrace.
for x,y in [(29,17),(28,18),(27,19),(26,20),(25,21)]:
    c.line(x,y,x+2,y,'#c6b67b')
    c.set(x+2,y+1,P['earth'])
# Three small houses, roofs seen from above.
def house(x,y,w,h):
    c.poly([(x-1,y+4),(x+w,y+4),(x+w+2,y+7),(x+2,y+7),(x-1,y+5)],'#85865b')
    c.rect(x,y+2,w,h,P['wall_d'])
    c.rect(x,y+2,w-2,h,P['wall'])
    c.rect(x+w-3,y+3,2,h-1,P['roof_d'])
    c.poly([(x-2,y+2),(x+1,y-2),(x+w-2,y-2),(x+w+1,y+2),(x+w,y+3),(x-2,y+3)],P['roof_d'])
    c.poly([(x-1,y+1),(x+1,y-1),(x+w-2,y-1),(x+w,y+2),(x,y+2)],P['roof'])
    c.line(x+1,y-1,x+w-2,y-1,P['roof_l'])
    c.line(x,y,x+w-1,y+1,P['roof_l'])
    c.set(x+1,y+4,P['ink'])
house(35,9,7,4)
house(46,6,6,4)
house(54,12,6,3)
# A few footpath stones, hedges, and a pole beside the village.
c.line(32,10,32,14,P['wood'])
c.set(31,10,P['leaf'])
c.set(30,12,P['leaf'])
c.line(43,13,45,13,'#d2bd85')
c.set(48,14,'#d2bd85')
c.set(51,15,'#d2bd85')
# Harvest bundles sitting upright on the field margins.
def sheaf(x,y):
    c.line(x-2,y+2,x+2,y+2,P['gold_d'])
    c.poly([(x,y-3),(x+2,y-2),(x+1,y),(x+2,y+2),(x-2,y+2),(x-1,y)],P['ochre'])
    c.line(x,y-2,x-1,y+1,P['sun'])
    c.set(x+1,y-2,P['pale'])
    c.line(x-1,y,x+1,y,P['shadow'])
sheaf(9,39)
sheaf(36,48)
sheaf(55,60)
# Two farmers: tiny indigo / rust jackets, limbs, and broad straw hats.
def farmer(x,y,coat,highlight):
    c.line(x-2,y+5,x+3,y+5,P['bank_d'])
    c.set(x-1,y+4,P['ink']); c.set(x+1,y+4,P['ink'])
    c.rect(x-1,y+1,3,3,coat)
    c.set(x-1,y+2,highlight)
    c.set(x-2,y+2,P['skin']); c.set(x+2,y+2,P['skin'])
    c.set(x,y+1,P['skin'])
    # A brown perimeter lets the broad hats read against ripe rice.
    c.line(x-1,y-2,x+1,y-2,P['shadow'])
    c.line(x-2,y-1,x+2,y-1,P['shadow'])
    c.line(x-3,y,x+3,y,P['shadow'])
    c.line(x-2,y+1,x+2,y+1,P['shadow'])
    c.line(x-1,y-1,x+1,y-1,P['pale'])
    c.line(x-2,y,x+2,y,P['sun'])
    c.line(x-1,y+1,x+1,y+1,P['gold_l'])
    c.set(x+1,y+2,P['ink'])
farmer(20,28,P['blue'],P['blue_l'])
farmer(46,38,P['red'],'#cc7950')
# One curved sickle and a walking staff are clean single-pixel accents.
c.line(23,31,24,30,P['shadow']); c.set(24,29,P['pale'])
c.line(43,40,43,45,P['shadow']); c.set(43,40,P['skin'])
# More distinct cut stems and splayed bases on the harvested sheaves.
for x,y in [(9,39),(36,48),(55,60)]:
    c.set(x-2,y-2,P['sun']);c.set(x+2,y-3,P['sun'])
    c.set(x,y-3,P['pale']);c.set(x-2,y+2,P['straw'])
    c.set(x+2,y+2,P['straw'])
assert result.stats()['size'] == (64,64) or result.stats()['size'] == [64,64]
assert result.stats()['colors_used'] <= 86
print(result.stats_text())
view(result,scale=8,margin=0)
save('rice-terraces-during-harvest',result)
finish(result)
