# A tiny moss-backed woodland slime. Native 32 x 32 sprite.
result = new_canvas(32, 32, name="forest_slime_monster")
ink = '#17362e'
bark = '#634b38'
wood = '#b68b55'
woodlight = '#e0bd7b'
# Antlers sit behind the crown: short, forked twigs.
result.poly([(9,12),(9,8),(6,6),(6,3),(8,3),(8,5),(10,7),(10,4),(12,4),(12,9),(11,12)], ink)
result.line(7,4,7,5,woodlight)
result.line(7,6,10,9,wood)
result.line(10,8,10,11,bark)
result.line(11,5,11,8,woodlight)
result.set(10,9,wood)
result.poly([(19,12),(19,9),(21,7),(21,3),(23,3),(23,6),(25,4),(26,5),(23,8),(21,10),(21,12)], ink)
result.line(22,4,22,7,woodlight)
result.line(22,7,25,5,wood)
result.line(21,8,20,10,wood)
result.set(20,11,bark)
# A single red-capped mushroom growing from its back.
result.rect(25,10,3,6,ink)
result.rect(26,10,1,5,'#d9c48c')
result.set(26,12,'#f1dda2')
result.rect(24,7,4,1,ink)
result.rect(23,8,6,1,ink)
result.rect(22,9,8,3,ink)
result.rect(23,8,5,2,'#c84d44')
result.rect(23,10,6,1,'#8e373b')
result.rect(24,7,3,1,'#df6b50')
result.set(24,8,'#ffe3b0')
result.set(27,9,'#ffe3b0')
result.set(25,10,'#e7775b')
# Rounded silhouette, with a softly scalloped, weight-bearing base.
body = new_canvas(32,32,name='slime_body')
rows = {10:(12,18),11:(9,21),12:(8,23),13:(7,24),14:(6,25),15:(5,26),16:(4,27),17:(4,27),18:(4,27),19:(4,27),20:(4,27),21:(4,27),22:(3,28),23:(3,28),24:(3,28),25:(3,28),26:(4,27),27:(5,26)}
for y,(a,b) in rows.items():
    body.rect(a,y,b-a+1,1,'#397a55')
body.rect(6,28,6,1,'#397a55')
body.rect(14,28,7,1,'#397a55')
body.rect(23,28,3,1,'#397a55')
# Underbelly and right-hand translucency, drawn as clean pixel clusters.
body.poly([(24,13),(25,16),(25,20),(24,23),(21,25),(14,26),(7,25),(4,23),(4,26),(7,28),(25,28),(28,25),(28,21),(27,16)], '#28604a')
body.poly([(26,18),(27,21),(28,24),(26,26),(22,27),(15,27),(13,26),(21,25),(24,23)], '#204b3f')
body.poly([(7,16),(9,13),(12,12),(19,12),(22,14),(23,17),(20,19),(12,19),(9,22),(6,22),(5,20)], '#4c9460')
body.poly([(9,13),(12,11),(18,11),(21,13),(20,15),(16,16),(12,15),(10,17),(7,17)], '#79a64e')
# Moss forms little hanging lobes over the upper surface.
body.poly([(8,14),(10,12),(14,11),(18,11),(21,13),(22,15),(20,15),(20,17),(18,17),(17,15),(15,15),(14,17),(12,16),(12,14),(10,15),(10,18),(8,17)], '#729748')
body.rect(12,12,5,1,'#abc45f')
body.rect(10,13,3,1,'#abc45f')
body.rect(9,14,2,2,'#91b653')
body.rect(16,12,3,2,'#91b653')
body.rect(17,14,3,1,'#91b653')
body.set(13,13,'#c8d979')
body.set(8,16,'#91b653')
# Outline only the body, preserving the accessory colours.
body.outline(ink)
result.blit(body,0,0)
# Face: two warm, luminous eyes in dark green sockets.
for x in (10,19):
    result.rect(x,18,3,5,'#26503b')
    result.rect(x-1,19,5,3,'#26503b')
    result.rect(x,19,3,3,'#e0ca57')
    result.rect(x+1,18,1,1,'#c1b64b')
    result.rect(x,19,2,2,'#fff4aa')
    result.set(x+2,20,'#ffdf71')
    result.set(x+1,22,'#86a24a')
# A small, unambiguous cheerful mouth.
result.set(14,22,ink)
result.set(18,22,ink)
result.rect(15,23,3,1,ink)
result.set(16,24,'#8ab267')
# Cheek specks and broad jelly reflections.
result.rect(7,22,2,1,'#8cba76')
result.rect(23,22,2,1,'#659a62')
result.rect(6,18,1,3,'#8cba76')
result.set(7,17,'#b5d68b')
result.rect(6,24,2,1,'#4c9460')
result.rect(8,26,3,1,'#5a9562')
result.rect(15,26,4,1,'#43805a')
result.set(25,24,'#43805a')
# A few moss grains, kept away from the facial features.
result.set(22,15,'#92ad53')
result.set(23,16,'#729748')
result.set(13,15,'#91b653')
view(result, scale=12, margin=2, edges='all')
save('forest_slime_monster',result)
finish(result)
