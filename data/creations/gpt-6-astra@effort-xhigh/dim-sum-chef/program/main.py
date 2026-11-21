# 32px dim sum chef. Crisp single-pixel contours, upper-left light.
result = new_canvas(32, 32, name="dim_sum_chef")
c = result
ink = '#282b38'
hair = '#38313b'
hairlight = '#59414a'
clothshadow = '#7796a0'
clothmid = '#b3cbd0'
cloth = '#e0e8df'
white = '#fff6df'
skinshadow = '#b87558'
skin = '#dfa176'
skinlight = '#f3c493'
cheek = '#d88b6b'
apronedge = '#314c59'
apronshadow = '#3e6872'
apron = '#57858a'
apronlight = '#76a1a1'
redshadow = '#873b43'
red = '#c35550'
redlight = '#e77961'
basketedge = '#624033'
basketshadow = '#a7683d'
basket = '#ca8e4b'
basketlight = '#edbb68'
baskethigh = '#ffda8a'
bunshadow = '#c4a47b'
bunmid = '#e9d4a3'
bun = '#fff0c7'

# Shoes and trousers, visibly separate below the apron.
c.rect(9, 26, 6, 4, ink)
c.rect(17, 26, 6, 4, ink)
c.rect(10, 27, 4, 3, '#455665')
c.rect(18, 27, 4, 3, '#455665')
c.rect(10, 27, 2, 2, '#657680')
c.rect(18, 27, 2, 2, '#657680')
c.rect(8, 29, 7, 2, ink)
c.rect(17, 29, 7, 2, ink)
c.line(9, 29, 12, 29, '#58616b')
c.line(18, 29, 21, 29, '#58616b')

# Jacket and rounded sleeves behind the apron and arms.
c.poly([(11,13),(20,13),(24,15),(26,17),(27,20),(26,23),(23,24),(22,28),(9,28),(8,24),(5,23),(4,20),(5,17),(7,15)], ink)
c.poly([(11,14),(20,14),(23,15),(25,18),(26,20),(24,22),(21,22),(21,27),(10,27),(10,22),(7,22),(5,20),(6,17),(8,15)], clothmid)
c.poly([(11,14),(20,14),(23,16),(24,19),(21,20),(10,20),(6,19),(7,16)], cloth)
c.line(7,17,6,19,white)
c.line(24,17,25,20,clothshadow)
c.line(6,20,8,21,clothshadow)
c.line(23,21,25,20,clothshadow)

# Teal apron straps and a broad hem, with flour marks added below.
c.rect(10,14,2,5,apronedge)
c.line(10,14,10,18,apronlight)
c.rect(20,14,2,5,apronedge)
c.line(20,14,20,18,apron)
c.poly([(11,17),(20,17),(22,26),(22,29),(9,29),(9,26)],apronedge)
c.poly([(12,18),(19,18),(21,26),(21,28),(10,28),(10,26)],apron)
c.line(10,25,10,27,apronlight)
c.line(21,25,21,28,apronshadow)
c.line(11,28,20,28,apronshadow)
# Small, irregular flour smears read against colored fabric.
c.rect(12,25,2,2,clothmid)
c.set(11,26,cloth)
c.set(12,25,white)
c.set(14,27,clothmid)
c.set(17,26,clothmid)
c.line(18,26,19,26,cloth)
c.set(18,25,clothmid)
c.set(19,27,apronlight)

# Neck, chef's red neckerchief and folded collar.
c.rect(13,12,6,3,ink)
c.rect(14,12,4,3,skinshadow)
c.line(14,13,17,13,skin)
c.poly([(11,14),(13,14),(15,16),(12,16)],white)
c.poly([(18,14),(20,14),(19,16),(16,16)],white)
c.line(13,14,15,15,red)
c.line(18,14,16,15,redshadow)
c.rect(15,15,2,2,red)
c.set(15,15,redlight)
c.set(16,17,redshadow)

# Face silhouette and little ears.
c.rect(9,9,14,3,ink)
c.set(9,10,skin)
c.set(22,10,skinshadow)
c.poly([(11,6),(20,6),(22,8),(22,11),(20,13),(18,14),(13,14),(10,12),(9,8)],ink)
c.poly([(11,7),(20,7),(21,8),(21,11),(19,13),(13,13),(11,11),(10,8)],skin)
c.rect(12,8,8,4,skinlight)
c.line(13,12,18,12,skinlight)
c.set(20,11,skinshadow)
c.set(19,12,skinshadow)
c.rect(10,7,12,2,hair)
c.set(10,9,hair)
c.set(21,9,hair)
c.set(11,8,hairlight)
# Quiet friendly expression; dark eyes with a tiny curved smile.
c.set(12,9,skinshadow)
c.set(19,9,skinshadow)
c.set(13,10,ink)
c.set(18,10,ink)
c.set(12,11,cheek)
c.set(19,11,cheek)
c.set(16,11,skinshadow)
c.line(14,12,17,12,hairlight)
c.set(14,12,skinshadow)
c.set(17,12,skinshadow)

# Tall toque with three scalloped crowns and a shaded folded band.
c.poly([(10,1),(13,1),(14,0),(18,0),(19,1),(21,1),(23,3),(23,5),(21,6),(21,8),(10,8),(10,6),(8,5),(8,3)],ink)
c.poly([(10,2),(13,2),(14,1),(18,1),(19,2),(21,2),(22,3),(22,5),(20,6),(11,6),(9,5),(9,3)],cloth)
c.rect(11,2,3,3,white)
c.rect(14,1,4,4,white)
c.line(10,3,10,4,white)
c.line(19,3,20,3,white)
c.line(22,3,22,5,clothmid)
c.set(20,5,clothmid)
c.set(13,5,clothmid)
c.line(11,6,20,6,clothmid)
c.line(11,7,20,7,cloth)
c.line(11,7,13,7,white)
c.set(20,7,clothshadow)

# Hands: warm skin outside the dark perimeter of the basket.
c.poly([(5,20),(7,19),(9,20),(9,23),(7,24),(5,23)],ink)
c.rect(5,21,3,2,skinshadow)
c.rect(6,20,2,3,skin)
c.line(6,20,7,20,skinlight)
c.set(6,21,skinlight)
c.poly([(24,19),(26,20),(27,21),(27,23),(24,24),(22,23),(22,21)],ink)
c.rect(24,20,2,3,skin)
c.set(25,20,skinlight)
c.set(26,21,skinshadow)
c.set(24,23,skinshadow)

# Open bamboo steamer: dark inside, warm rim, curved woven side.
c.poly([(11,18),(20,18),(23,19),(24,21),(23,24),(21,25),(10,25),(8,24),(7,21),(8,19)],basketedge)
c.poly([(10,19),(21,19),(23,20),(22,22),(9,22),(8,20)],basketshadow)
c.line(10,19,21,19,basketlight)
c.line(9,20,22,20,basketedge)

# Three individual steamed buns, each outlined in a darker dough tone.
def bun_left():
    c.poly([(10,17),(12,16),(14,17),(15,19),(14,21),(10,21),(9,20),(9,18)],basketedge)
    c.poly([(10,18),(11,17),(13,17),(14,18),(14,20),(10,20)],bunmid)
    c.line(11,17,12,17,bun)
    c.rect(10,18,4,2,bun)
    c.set(12,18,bunshadow)
    c.set(11,19,bunmid)
def bun_right():
    c.poly([(18,17),(20,16),(22,17),(23,19),(22,21),(18,21),(17,20),(17,18)],basketedge)
    c.poly([(18,18),(19,17),(21,17),(22,18),(22,20),(18,20)],bunmid)
    c.line(19,17,20,17,bun)
    c.rect(18,18,4,2,bun)
    c.set(20,18,bunshadow)
    c.set(19,19,bunmid)
bun_left()
bun_right()
# Separate central bun sits slightly forward, a pixel lower.
c.poly([(15,18),(17,18),(18,19),(18,21),(17,22),(14,22),(13,21),(13,20)],basketedge)
c.rect(14,20,4,1,bunmid)
c.line(15,19,16,19,bun)
c.line(14,20,17,20,bun)
c.set(16,20,bunshadow)
c.line(14,21,17,21,bunmid)

# Front rim, horizontal bamboo courses, and vertical bindings.
c.line(8,21,9,22,basketlight)
c.line(22,22,23,21,basketlight)
c.line(10,22,21,22,baskethigh)
c.line(9,23,22,23,basket)
c.line(10,24,21,24,basketshadow)
c.line(10,23,12,23,basketlight)
c.line(14,23,17,23,basketlight)
c.line(19,23,21,23,basketlight)
c.set(12,24,basket)
c.set(19,24,basket)
c.set(13,23,basketshadow)
c.set(18,23,basketshadow)
# Thumbs curl upward at the sides; outlines keep fingers off the food.
c.set(7,21,ink)
c.set(7,22,skinlight)
c.set(24,21,ink)
c.set(24,22,skinlight)

# Close the rounded basket base and pick out its bamboo bindings.
c.line(10,25,21,25,basketedge)
c.set(9,24,basketedge)
c.set(22,24,basketedge)
c.line(10,23,21,23,basket)
c.line(10,24,21,24,basketshadow)
c.line(11,23,13,23,basketlight)
c.line(18,23,20,23,basketlight)
c.line(13,23,13,24,baskethigh)
c.line(19,23,19,24,basketlight)
c.set(16,11,skin)
# A fine dusting around the larger flour patches.
c.set(12,26,white)
c.set(13,26,clothmid)
c.set(16,28,clothmid)

print(result.stats_text())
view(result, scale=12, margin=1)
save('dim_sum_chef', result)
finish(result)
