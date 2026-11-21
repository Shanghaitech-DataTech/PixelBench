# Helmeted e-scooter rider, right-facing, native 32 x 32 sprite.
result = new_canvas(32, 32, name="e-scooter-rider")
c = result
ink = '#182738'
steel = '#425970'
lightsteel = '#91b3be'
teal = '#208e9b'
aqua = '#46bdba'
shine = '#9ce7cc'
yellow = '#f6bd4f'
helmetlight = '#ffe28b'
helmetshade = '#cf7b34'
skin = '#efac7d'
skinlight = '#ffd09b'
skinshade = '#bd7159'
pants = '#364460'
pantslight = '#5b6886'
shoe = '#e3e8d5'

# Scooter: small paired wheels, standing deck, and tall handlebar stem.
for x in (8, 27):
    c.rect(x-1, 26, 3, 5, ink)
    c.rect(x-2, 27, 5, 3, ink)
    c.rect(x-1, 27, 3, 3, steel)
    c.set(x, 28, lightsteel)
    c.set(x-1, 27, '#668b9b')
c.poly([(7,25),(24,25),(26,23),(28,23),(29,26),(27,27),(8,27),(6,26)], ink)
c.line(9,25,24,25,shine)
c.line(9,26,25,26,teal)
c.line(25,25,27,24,aqua)
c.line(27,14,28,25,ink)
c.line(26,14,27,24,ink)
c.line(26,15,27,23,lightsteel)
c.set(27,24,teal)
c.rect(24,12,6,2,ink)
c.line(26,12,28,12,steel)
c.set(29,12,teal)

# Trousers: one bent rear leg and one planted forward leg.
c.poly([(13,17),(18,17),(19,20),(21,23),(21,24),(23,24),(23,26),(18,26),(17,22),(16,21),(15,23),(16,24),(17,24),(17,26),(12,26),(11,22)], ink)
c.poly([(14,18),(16,18),(15,21),(13,22),(14,24),(12,24),(12,22)], pants)
c.line(14,19,13,21,pantslight)
c.poly([(16,18),(18,18),(18,20),(20,23),(20,24),(18,24),(17,21),(15,20)], pants)
c.line(17,19,19,22,pantslight)
c.line(13,24,15,24,shoe)
c.line(13,25,16,25,lightsteel)
c.line(19,24,21,24,shoe)
c.line(19,25,22,25,lightsteel)

# Jacket silhouette, leaning forward over the deck.
c.poly([(15,9),(18,9),(20,11),(20,14),(19,16),(18,19),(12,18),(12,15),(13,12)], ink)
c.poly([(15,10),(17,10),(19,12),(18,15),(17,17),(13,17),(13,15)], teal)
c.poly([(15,11),(17,11),(18,12),(16,14),(14,15),(14,13)], aqua)
c.line(13,17,17,18,steel)
c.set(14,16,aqua)

# Neck and face. The projecting nose and eye define the direction.
c.rect(17,8,4,4,ink)
c.rect(18,9,2,2,skinshade)
c.poly([(18,5),(22,5),(22,7),(24,8),(23,9),(22,9),(22,11),(19,11),(17,9),(17,6)], ink)
c.poly([(19,6),(21,6),(21,8),(23,8),(23,9),(21,9),(21,10),(19,10),(18,8)], skin)
c.line(20,6,21,6,skinlight)
c.set(21,7,ink)
c.set(22,8,skinlight)
c.set(19,9,skinshade)
c.set(18,7,skinlight)

# Rounded golden helmet with a short forward brim and chin strap.
c.poly([(17,2),(21,2),(23,4),(23,6),(24,6),(24,7),(19,7),(18,9),(16,8),(15,6),(15,4)], ink)
c.poly([(17,3),(21,3),(22,4),(22,5),(17,6),(16,5),(16,4)], yellow)
c.line(17,3,20,3,helmetlight)
c.set(16,4,helmetlight)
c.line(17,6,22,6,helmetshade)
c.line(19,5,22,5,yellow)
c.set(17,7,yellow)
c.line(18,7,19,9,ink)
c.set(20,10,skinshade)
# A light pixel ahead of the eye keeps the profile readable at native size.
c.set(20,7,skin)
c.set(21,7,ink)
c.set(22,7,skinlight)
c.set(23,7,ink)
c.set(22,8,skinlight)
c.set(21,9,skinshade)

# Bent sleeve, bare forearm and hand gripping the handlebar.
c.poly([(18,11),(20,11),(22,14),(24,14),(24,12),(26,12),(26,15),(24,16),(21,16),(18,14)], ink)
c.poly([(18,12),(19,12),(21,14),(20,15),(18,13)], aqua)
c.set(19,14,teal)
c.line(22,15,24,15,skin)
c.line(24,14,25,13,skinlight)
c.set(25,12,skin)

view(result, scale=12, margin=0)
save('e-scooter-rider', result)
finish(result)
