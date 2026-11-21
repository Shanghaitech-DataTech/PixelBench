result = new_canvas(32, 32, name='e-scooter-rider')
# Compact palette: ink outlines, cool clothing, warm skin, bright scooter.
ink='#202b40'
metal='#597084'
light='#aac6ce'
cyan='#42d9cc'
shade='#178d9e'
skin='#efb387'
skinshadow='#c47c68'
helmet='#f7c953'
helmshade='#dc8c38'
# Wheels, spaced widely beneath the standing deck.
for x in (8,26):
    result.circle(x,27,3,ink)
    result.circle(x,27,1,metal)
    result.set(x,26,light)
# Deck and rear fender.
result.line(5,24,9,24,ink)
result.line(4,25,6,24,ink)
result.rect(8,24,15,3,ink)
result.rect(9,24,13,1,light)
result.rect(9,25,14,1,cyan)
# Tall swept steering column and front fork.
result.line(25,14,27,26,ink)
result.line(26,14,28,25,ink)
result.line(26,16,27,24,metal)
result.line(22,26,26,23,ink)
result.line(23,25,26,22,cyan)
result.rect(23,13,6,2,ink)
result.set(28,13,light)
# Legs: rear leg leans back; front knee bends forward.
result.poly([(13,15),(18,15),(19,18),(18,21),(17,23),(17,24),(13,24),(13,22),(15,18),(12,18)],ink)
result.poly([(12,15),(16,16),(14,20),(12,23),(13,24),(8,24),(9,21),(10,17)],ink)
result.line(12,18,10,22,'#435a7c')
result.line(16,18,16,21,'#607a9a')
result.rect(8,23,5,1,light)
result.rect(14,23,5,1,light)
result.set(18,22,ink)
# Jacket leaning slightly into the handlebars.
result.poly([(14,8),(18,9),(19,12),(17,17),(11,17),(11,13)],ink)
result.poly([(14,10),(17,10),(17,13),(15,16),(12,15),(12,13)],shade)
result.line(14,10,12,13,cyan)
result.line(12,14,12,15,cyan)
# Neck.
result.rect(16,7,3,3,ink)
result.rect(17,7,1,3,skinshadow)
# Outstretched arm, bent slightly at the elbow.
result.line(17,10,20,13,ink)
result.line(17,11,20,14,ink)
result.line(20,13,25,12,ink)
result.line(20,14,25,13,ink)
result.line(18,11,20,13,cyan)
result.line(21,13,24,12,skin)
result.set(25,12,skin)
# Head in profile, nose points right.
result.poly([(14,3),(19,3),(20,5),(20,6),(21,7),(20,8),(19,9),(16,8),(14,6)],ink)
result.rect(16,4,4,3,skin)
result.rect(17,7,3,1,skin)
result.set(20,6,skin)
result.set(19,5,ink)
result.set(16,6,skinshadow)
# Helmet shell with forward visor and fastening strap.
result.poly([(12,3),(14,1),(18,1),(20,3),(20,4),(13,5),(12,4)],ink)
result.rect(14,2,5,2,helmet)
result.rect(13,3,3,1,helmet)
result.line(13,4,20,4,helmshade)
result.line(15,2,17,2,'#fff0a8')
result.set(14,3,helmshade)
result.line(15,5,16,7,ink)
result.set(17,8,ink)
view(result, scale=12)
finish(result)
