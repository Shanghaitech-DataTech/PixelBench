# Portable cassette player, hand-placed at its native 32 x 32 resolution.
result = new_canvas(32, 32, name="portable_cassette_player")
c = result
ink = '#182b3a'
shadow = '#3b5664'
steel = '#718c91'
case = '#b6c8be'
light = '#e7e7cf'
shine = '#fff5d9'
orange = '#df7048'
orange_light = '#ffb46a'
glass = '#456b77'
glass_light = '#638f98'
reel = '#d9dfc6'

# Headphone lead: bends around the right side, with a small earpiece.
c.path('M 22 5 L 22 3 L 24 1 L 28 1 L 30 3 L 30 20 L 29 22 L 28 23 L 28 25', ink, fill=False)
c.line(29,4,29,17,steel)
c.rect(21,3,3,4,ink)
c.rect(22,3,1,3,steel)
c.rect(27,24,3,4,ink)
c.rect(28,25,2,2,steel)
c.rect(27,27,3,2,ink)
c.set(28,27,light)

# Knurled volume wheel protruding above the casing.
c.rect(6,3,8,3,ink)
c.rect(7,3,6,2,steel)
for x in (7,9,11):
    c.set(x,3,light)
    c.set(x,4,shadow)

# Rounded, bevelled enclosure.
c.poly([(5,5),(23,5),(25,7),(25,28),(24,30),(4,30),(3,28),(3,7)],ink)
c.poly([(5,6),(22,6),(24,8),(24,27),(23,29),(5,29),(4,27),(4,7)],case)
c.line(5,6,22,6,shine)
c.line(4,7,4,26,light)
c.line(24,8,24,27,shadow)
c.line(6,28,23,28,steel)
c.line(5,29,23,29,shadow)

# Recessed cassette door and its glass.
c.rect(5,8,18,14,steel)
c.rect(6,8,16,1,light)
c.rect(6,9,16,12,ink)
c.rect(7,10,14,10,glass)
c.line(7,10,20,10,glass_light)
c.line(7,11,7,18,glass_light)
# Tape pack silhouette, with a taut exposed tape along the bottom.
c.line(9,16,10,18,ink)
c.line(10,18,18,18,ink)
c.line(18,18,19,16,ink)
c.line(11,17,17,17,steel)
# The two reels, each with a dark spindle and keyed holes.
for x in (10,18):
    c.circle(x,14,4,ink)
    c.circle(x,14,3,reel)
    c.line(x-1,11,x+1,11,shine)
    c.set(x-2,15,steel)
    c.set(x+2,15,steel)
    c.rect(x-1,13,3,3,shadow)
    c.set(x,14,light)
    c.set(x,12,glass)
    c.set(x-2,14,glass)
    c.set(x+2,14,glass)
# Central tape bridge and restrained window glints.
c.rect(14,13,1,3,steel)
c.set(15,11,glass_light)
c.set(14,12,glass_light)
c.line(8,19,12,19,glass_light)
c.line(18,19,20,19,glass_light)

# Transport panel: back, play, stop, and pause.
c.rect(5,23,18,4,ink)
c.rect(6,23,3,3,steel)
c.set(7,24,light)
c.set(6,25,light)
c.rect(10,23,4,3,orange)
c.set(11,23,orange_light)
c.line(11,24,11,25,shine)
c.set(12,24,shine)
c.rect(15,23,3,3,steel)
c.rect(16,24,2,2,light)
c.rect(19,23,3,3,steel)
c.line(19,24,19,25,light)
c.line(21,24,21,25,light)
# Small orange power lamp and casing screws.
c.set(6,7,orange)
c.line(8,7,11,7,shadow)
c.set(22,7,shadow)
c.set(5,27,shadow)
c.set(23,27,light)

view(result, scale=12, margin=0)
save('portable_cassette_player', result)
finish(result)
