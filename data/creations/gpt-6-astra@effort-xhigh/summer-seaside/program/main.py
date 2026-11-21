import math
import random

# A small, deliberately stepped summer palette.
C = {
    'sky_top':'#58b6e7', 'sky':'#68c2ed', 'sky_low':'#82d1ef',
    'sky_haze':'#9bdcf1', 'cloud_shadow':'#c4e8ed', 'cloud_mid':'#e2f3ee',
    'white':'#fffef0', 'sun_halo':'#98d9e8', 'sun':'#ffe58a', 'sun_light':'#fff5b7',
    'deep':'#227bb1', 'deep_dark':'#216eaa', 'blue':'#258dbc',
    'blue_light':'#38a1c5', 'sea_mid':'#2ba4bd', 'sea':'#35b8bf',
    'teal':'#4bc8bf', 'wash':'#7ddbc8', 'wash_dark':'#61cdbc',
    'foam_shadow':'#acedd5', 'foam':'#ebfbe5', 'glint':'#c8eee0',
    'sand':'#f4d58a', 'sand_light':'#ffe4a0', 'sand_dark':'#e6bc73',
    'wet':'#dbb77a', 'wet_light':'#eaca88', 'grain':'#ceaa70',
    'shadow':'#c1ad86', 'shadow_dark':'#ad9877',
    'red_dark':'#b34244', 'red_shadow':'#d34e50', 'red':'#ef6358', 'red_light':'#ff8970',
    'ivory_shadow':'#cfded2', 'ivory':'#f4f2dc',
    'wood_dark':'#a4784f', 'wood':'#c89558', 'wood_light':'#f5cf85',
    'navy':'#254d69', 'towel_dark':'#397e98', 'towel':'#4eabc0', 'towel_light':'#74cad0'
}
c = new_canvas(128, 128, C['sky_top'], name='summer_seaside')
# Clear sky in broad pixel bands.
c.rect(0, 15, 128, 17, C['sky'])
c.rect(0, 32, 128, 10, C['sky_low'])
c.rect(0, 42, 128, 6, C['sky_haze'])

# Sunny disk and short, separate rays.
c.circle(107, 18, 12, C['sun_halo'])
c.circle(107, 18, 9, C['sun'])
c.circle(106, 17, 7, C['sun_light'])
c.rect(105, 4, 3, 2, C['sun_light'])
c.rect(106, 31, 2, 3, C['sun_light'])
c.rect(92, 17, 3, 2, C['sun_light'])
c.rect(120, 17, 3, 2, C['sun_light'])
for x,y,dx,dy in [(96,7,1,1),(117,7,-1,1),(96,28,1,-1),(117,28,-1,-1)]:
    c.line(x,y,x+dx,y+dy,C['sun_light'])

# Stepped cumulus silhouettes, with cool flat undersides.
def cloud(points, midpoints, top_points):
    c.poly(points, C['cloud_shadow'])
    c.poly(midpoints, C['cloud_mid'])
    c.poly(top_points, C['white'])
cloud(
 [(8,24),(8,21),(12,21),(12,17),(17,17),(17,13),(25,13),(25,15),(29,15),(29,19),(35,19),(35,22),(40,22),(40,26),(36,26),(36,28),(13,28),(13,26),(8,26)],
 [(9,21),(13,21),(13,17),(18,17),(18,14),(24,14),(24,16),(28,16),(28,20),(34,20),(34,23),(38,23),(38,25),(12,25),(12,24),(9,24)],
 [(13,20),(14,17),(18,17),(18,14),(24,14),(24,16),(27,16),(27,21),(31,21),(31,23),(12,23),(12,21)]
)
cloud(
 [(49,12),(52,12),(52,9),(57,9),(57,7),(63,7),(63,9),(67,9),(67,12),(72,12),(72,15),(68,15),(68,17),(51,17),(51,15),(49,15)],
 [(50,13),(53,13),(53,10),(58,10),(58,8),(62,8),(62,10),(66,10),(66,13),(70,13),(70,15),(51,15)],
 [(54,13),(54,10),(58,10),(58,8),(62,8),(62,10),(65,10),(65,13)]
)
# A little distant horizontal cloud on the left.
c.rect(0,37,17,2,C['cloud_mid'])
c.rect(4,35,9,2,C['cloud_mid'])
c.rect(5,35,6,2,C['white'])
c.rect(1,37,12,1,C['white'])

# Two gulls, each a shallow angular M, caught in the daylight.
for pts in [[(47,28),(49,27),(51,28),(53,31),(55,28),(58,27),(60,28)],
            [(74,24),(76,24),(78,26),(80,24),(83,23),(85,24)]]:
    for a,b in zip(pts,pts[1:]): c.line(*a,*b,C['navy'])
    for a,b in zip(pts[:3],pts[1:3]): c.line(a[0],a[1]-1,b[0],b[1]-1,C['white'])

# Sea bands and a wandering diagonal shore.
shore = [round(82 + 0.105*x + 1.8*math.sin(x/14.0) + 0.6*math.sin(x/4.3)) for x in range(128)]
c.rect(0,46,128,82,C['sand'])
for x in range(128):
    y = shore[x]
    c.line(x,46,x,y,C['wash'])
    c.line(x,y+1,x,y+4,C['wet'])
    c.set(x,y+5,C['wet_light'])
for y0,y1,key in [(46,49,'deep_dark'),(50,56,'deep'),(57,64,'blue'),(65,71,'sea_mid'),(72,78,'sea'),(79,83,'teal')]:
    for x in range(128):
        c.line(x,y0,x,min(y1,shore[x]),C[key])
c.line(0,46,127,46,C['deep'])

# Thin horizontal water facets; longer and brighter as they approach.
rng = random.Random(32)
for y in range(49,86):
    if y%2==0: continue
    for i in range(7 if y<65 else 5):
        x=rng.randrange(128)
        length=rng.randrange(2,7 if y<65 else 12)
        if y > shore[x]-5: continue
        key = ('blue' if y<56 else 'blue_light' if y<65 else 'sea' if y<72 else 'teal' if y<79 else 'wash')
        c.line(x,y,min(127,x+length),y,C[key])
# Few long distance wavelets.
for x,y,n in [(5,52,10),(32,55,7),(103,51,13),(48,60,8),(8,64,12),(111,63,11),(62,67,7)]:
    c.line(x,y,x+n,y,C['blue_light'])

# Sunlight, broken up into flat little sparks on the water.
for x,y,n in [(106,49,3),(103,53,5),(109,56,4),(101,60,7),(112,64,5),
              (103,68,4),(117,71,6),(96,73,5),(109,77,8),(121,82,4)]:
    c.line(x,y,x+n,y,C['glint'] if y>63 else C['blue_light'])

# The outer breaker: a mint face, a slender white curling crest.
for x in range(128):
    y=shore[x]-12 + round(math.sin(x/11.0))
    c.line(x,y,x,y+2,C['wash_dark'])
    if (x//7)%5 != 1:
        c.set(x,y,C['foam_shadow'])
        if (x//4)%7 != 2: c.set(x,y-1,C['foam'])
    if x%13<4: c.set(x,y+3,C['teal'])

# Shore break. The foam makes small lobes and holes, never a smooth stroke.
for x in range(128):
    y=shore[x]
    c.line(x,y-3,x,y-1,C['foam_shadow'])
    c.line(x,y-1,x,y+1,C['foam'])
    if x%15 in [0,1,2,3,4]: c.set(x,y+2,C['foam'])
    if x%11 in [3,4]: c.set(x,y-3,C['foam'])
    if x%19 in [8,9,10]: c.set(x,y,C['wash'])
    if x%23 in [16,17]: c.set(x,y+3,C['foam_shadow'])
for x,y,n in [(7,78,5),(22,80,3),(45,81,5),(64,84,3),(77,84,7),(87,87,4),(105,89,5),(117,90,3),
              (59,89,3),(70,92,2),(93,95,3),(115,98,4)]:
    c.line(x,y,x+n,y,C['foam'])

# A tiny sailboat, far out beyond the breakers.
c.line(82,43,82,58,C['wood_dark'])
c.set(82,43,C['white'])
c.poly([(81,45),(81,56),(74,56)], C['white'])
c.poly([(80,49),(80,55),(76,55)], C['ivory'])
c.poly([(84,47),(88,56),(84,56)], C['cloud_mid'])
c.line(84,49,87,55,C['white'])
c.line(74,57,89,57,C['navy'])
c.poly([(74,58),(89,58),(86,60),(77,60)],C['white'])
c.line(77,60,86,60,C['navy'])
c.line(76,62,88,62,C['blue_light'])
c.line(81,64,85,64,C['blue_light'])
c.line(83,44,85,44,C['red'])

# Warm grains are clustered, leaving restful open sand.
for i in range(77):
    x=rng.randrange(2,126); y=rng.randrange(90,127)
    if y<shore[x]+7: continue
    key = 'sand_light' if i%3 else 'sand_dark'
    c.line(x,y,min(126,x+rng.choice([0,1,1,2])),y,C[key])
for x,y in [(10,100),(56,105),(43,124),(103,99),(121,123)]:
    c.line(x,y,x+2,y,C['grain']); c.set(x+3,y-1,C['sand_light'])

# The umbrella's broad cool shadow and the slender wooden pole.
c.poly([(3,108),(11,104),(29,104),(43,109),(45,112),(36,116),(14,117),(4,114)],C['shadow'])
c.poly([(13,111),(22,108),(36,110),(39,113),(28,115),(16,114)],C['shadow_dark'])
c.line(19,118,36,111,C['shadow_dark'])
c.rect(34,79,3,33,C['wood_dark'])
c.rect(35,79,2,32,C['wood'])
c.line(36,80,36,110,C['wood_light'])
c.line(34,111,37,111,C['wood_dark'])

# The canopy silhouette: five radial red-and-white fabric panels.
c.poly([(4,85),(7,79),(14,73),(23,69),(33,66),(37,66),(47,69),(55,74),(61,80),(65,86),
        (60,85),(55,84),(49,87),(43,87),(36,85),(29,87),(22,87),(16,84),(10,85)],C['red_dark'])
# Left red panel.
c.poly([(5,83),(8,79),(15,73),(24,69),(34,67),(27,72),(22,77),(17,83),(12,83),(8,84)],C['red'])
c.poly([(8,80),(15,74),(24,70),(31,68),(25,72),(20,76),(16,80)],C['red_light'])
# Left ivory panel.
c.poly([(34,67),(27,72),(22,77),(17,83),(23,85),(28,85),(29,78),(31,72)],C['ivory'])
c.poly([(34,68),(30,74),(27,82),(24,84),(19,82),(23,77),(28,72)],C['white'])
c.line(18,83,23,85,C['ivory_shadow'])
c.line(23,85,28,85,C['ivory_shadow'])
# Middle red panel.
c.poly([(34,67),(31,74),(29,80),(28,85),(35,83),(43,86),(42,79),(38,71)],C['red'])
c.poly([(34,68),(33,75),(32,82),(36,82),(39,83),(38,76)],C['red_light'])
c.line(29,85,35,83,C['red_shadow'])
c.line(36,84,42,86,C['red_shadow'])
# Right ivory panel.
c.poly([(36,67),(41,70),(47,77),(54,83),(49,85),(44,86),(42,78),(38,71)],C['white'])
c.poly([(45,79),(50,83),(53,83),(49,85),(44,85)],C['ivory_shadow'])
# Right red panel.
c.poly([(38,67),(47,70),(54,75),(60,81),(63,84),(55,82),(48,76),(42,70)],C['red'])
c.line(45,70,53,75,C['red_light'])
c.line(55,82,63,84,C['red_shadow'])
# Finial and tiny bright seam accents.
c.rect(33,64,3,3,C['wood_dark'])
c.set(34,64,C['wood_light'])
c.line(31,67,36,67,C['white'])

# Striped cotton towel, in perspective on the sand.
TL=(67,103); TR=(86,98); BL=(79,122); BR=(101,116)
c.poly([(68,104),(88,100),(103,117),(80,124)],C['sand_dark'])
def mix(a,b,t): return (round(a[0]+(b[0]-a[0])*t),round(a[1]+(b[1]-a[1])*t))
c.poly([TL,TR,BR,BL],C['ivory'])
for i in range(7):
    a=mix(TL,BL,i/7); b=mix(TR,BR,i/7)
    d=mix(TL,BL,(i+1)/7); e=mix(TR,BR,(i+1)/7)
    if i%2==0:
        c.poly([a,b,e,d],C['towel'])
        c.line(*a,*b,C['towel_light'])
    else:
        c.line(*a,*b,C['white'])
c.line(*BL,*BR,C['towel_dark'])
for t in [0,.16,.32,.48,.64,.8,1]:
    x,y=mix(BL,BR,t); c.line(x,y+1,x+1,y+2,C['ivory'])
    x,y=mix(TL,TR,t); c.line(x-1,y-2,x,y-1,C['ivory'])

# A pair of navy flip-flops with coral Y straps.
def flipflop(x,y):
    c.poly([(x+1,y+2),(x+4,y),(x+6,y+2),(x+7,y+9),(x+6,y+12),(x+2,y+13),(x,y+10),(x,y+5)],C['sand_dark'])
    c.poly([(x,y+1),(x+3,y),(x+5,y+2),(x+6,y+9),(x+5,y+11),(x+2,y+12),(x,y+10),(x-1,y+4)],C['navy'])
    c.poly([(x+1,y+2),(x+3,y+1),(x+4,y+3),(x+5,y+9),(x+4,y+10),(x+2,y+10),(x+1,y+8)],C['towel_dark'])
    c.line(x,y+5,x+3,y+8,C['red_dark'])
    c.line(x+3,y+8,x+5,y+4,C['red_dark'])
    c.line(x,y+4,x+3,y+7,C['red_light'])
    c.line(x+3,y+7,x+5,y+3,C['red_light'])
    c.set(x+3,y+8,C['red'])
flipflop(106,109)
flipflop(117,105)

# One little scallop shell and a few sparkles of dry sand.
c.line(51,118,56,118,C['sand_dark'])
c.poly([(51,116),(52,114),(54,113),(56,115),(56,117),(53,118)],C['ivory'])
c.line(54,114,54,117,C['red_light'])
c.set(52,115,C['white']); c.set(56,116,C['wood_light'])
for x,y in [(10,123),(60,99),(47,111),(114,102),(124,119)]:
    c.line(x,y,x+2,y,C['sand_light'])

result = c
w, h, rgba = result.to_rgba()
visible_colours = {tuple(rgba[i:i+4]) for i in range(0, len(rgba), 4) if rgba[i+3] > 0}
assert (w, h) == (128, 128)
assert len(visible_colours) <= 86
print(f'Validated: {w}x{h}, {len(visible_colours)} visible colours.')
view(result, scale=4, margin=0)
save('summer_seaside', result)
finish(result)
