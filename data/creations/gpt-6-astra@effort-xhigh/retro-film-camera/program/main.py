# 32px RPG inventory icon: a well-used 35mm film camera.
result = new_canvas(32, 32, name="retro_film_camera")
c = result
ink = '#171b26'
edge = '#323747'
steel_shadow = '#697782'
steel = '#a7b2b5'
silver = '#d5d7ca'
light = '#f2ead5'
leather_dark = '#352c2c'
leather = '#534039'
leather_lit = '#705447'
leather_hi = '#8a6952'

# Rewind knob and shutter release, silhouetted above the shoulder.
c.rect(5, 6, 6, 4, ink)
c.rect(6, 6, 4, 1, silver)
c.rect(5, 7, 6, 1, steel)
c.rect(6, 8, 4, 1, steel_shadow)
c.rect(23, 6, 5, 4, ink)
c.rect(24, 5, 3, 1, ink)
c.rect(24, 6, 3, 1, light)
c.rect(24, 7, 3, 1, '#bd8a63')

# Top plate and the darker right-hand return.
c.poly([(4,9),(11,9),(12,6),(14,4),(19,4),(22,9),(27,9),(30,12),(30,24),(27,27),(4,27),(2,25),(2,12)], ink)
c.poly([(4,10),(12,10),(13,7),(15,5),(18,5),(21,10),(27,10),(28,12),(4,12)], silver)
c.line(5,10,11,10,light)
c.line(22,10,26,10,light)
c.poly([(28,12),(29,13),(29,23),(27,25),(27,14)], steel_shadow)
c.line(29,14,29,22,edge)

# Broad front plate, bottom metal rail, and leather covering.
c.rect(3, 12, 25, 12, steel)
c.rect(4, 24, 23, 2, steel_shadow)
c.line(5,25,25,25,steel)
c.line(4,24,10,24,silver)
c.rect(3, 14, 25, 10, leather_dark)
c.rect(4, 14, 23, 9, leather)
c.line(4,14,26,14,leather_lit)
c.line(4,15,4,22,leather_lit)
c.line(27,15,27,23,ink)

# Controlled, broken pixel clusters suggest pebbled leather.
for x,y in [(6,15),(8,16),(5,18),(7,19),(5,21),(8,22),(24,15),(26,17),(24,19),(26,21),(24,22)]:
    c.set(x,y,leather_lit)
for x,y in [(5,16),(7,17),(6,20),(7,22),(25,16),(24,18),(25,20),(26,22)]:
    c.set(x,y,leather_dark)
c.set(5,15,leather_hi)
c.set(24,15,leather_hi)

# Front of the prism housing, with its inset black finder.
c.poly([(13,8),(14,6),(18,6),(20,10),(20,12),(11,12)], steel)
c.line(14,6,18,6,light)
c.line(13,7,12,10,silver)
c.rect(13,9,6,3,ink)
c.rect(14,9,4,1,steel_shadow)
c.rect(14,10,4,1,'#405663')
c.set(14,10,'#9fbec2')
# Small meter window and engraved top plate detail.
c.rect(5,11,4,2,edge)
c.rect(6,11,2,1,'#667c7e')
c.line(23,12,25,12,steel_shadow)
c.set(26,12,light)

# Tiny strap lugs on both shoulders.
c.rect(1,13,2,4,ink)
c.set(1,14,steel)
c.rect(29,13,2,4,ink)
c.set(30,14,steel)

# Projecting lens barrel, stepped silhouette and cool metal rings.
c.circle(17,19,8,ink)
c.circle(16,18,8,ink)
c.circle(16,18,7,steel_shadow)
c.circle(16,18,6,edge)
# Bright upper-left edge and the lower-right barrel facets.
c.line(12,12,14,11,silver)
c.line(15,11,18,11,silver)
c.line(10,14,11,13,silver)
c.line(9,16,9,19,steel)
c.line(11,23,13,24,'#424d5c')
c.line(14,25,19,25,'#424d5c')
c.line(21,23,23,21,'#424d5c')
c.line(23,17,23,20,'#323747')
# Fine grip cuts on the lens barrel.
for x,y in [(19,12),(21,13),(22,15),(22,21),(20,23),(12,23),(10,21)]:
    c.set(x,y,ink)

# Inner bezel, glass and the offset aperture reflection.
c.circle(16,18,5,ink)
c.circle(16,18,4,'#253d50')
c.poly([(13,16),(15,14),(18,15),(19,17),(18,20),(15,21),(12,19),(12,17)], '#325f70')
c.poly([(16,15),(18,15),(19,17),(18,20),(16,21),(14,20),(16,18)], '#244457')
c.circle(16,18,2,'#152a3b')
c.rect(13,15,2,2,'#7caeb3')
c.line(14,14,16,14,'#b7d4cb')
c.set(13,15,light)
c.set(12,17,'#538b99')
c.line(17,21,19,19,'#58949e')
c.set(18,21,'#85b7b8')
# Lens mounting index, warm against the blue glass.
c.set(20,12,'#c16a48')
c.set(21,12,'#e7a56b')

view(result, scale=12, margin=0)
save('retro-film-camera', result)
finish(result)
