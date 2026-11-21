# Chainmail armor RPG pixel-art icon, 32x32 with transparent background.

c = new_canvas(32, 32, background=None, name="chainmail_armor")

# Palette: deep blue-black outline, cool steel shadows, and restrained highlights.
ink = "#111923"
ink2 = "#1b2733"
shadow = "#344454"
steel = "#617487"
light = "#9aabba"
glint = "#d2dbe0"
leather = "#392d2d"
accent = "#7b4e42"

# Main dark silhouette: hood/neck, broad shoulders, torso, sleeves and hem.
c.poly([(11,3),(20,3),(20,6),(23,8),(27,8),(27,10),(29,10),(29,14),
         (27,15),(27,25),(29,27),(28,29),(24,29),(23,31),(9,31),(8,29),
         (4,29),(3,27),(5,25),(5,15),(3,14),(3,10),(5,10),(5,8),(9,8),(11,6)], ink)

# Hood and collar mass.
c.poly([(11,4),(20,4),(20,7),(23,9),(21,12),(10,12),(8,9),(11,7)], shadow)
c.rect(12,4,7,2, steel)
c.rect(11,6,2,2, steel)
c.rect(19,6,2,2, shadow)
# Dark face opening under hood.
c.poly([(12,7),(19,7),(21,9),(19,11),(12,11),(10,9)], ink)
c.rect(13,8,5,2, ink2)
c.rect(12,10,8,2, ink)
# Collar rim.
c.rect(10,11,12,2, ink)
c.rect(12,11,8,1, light)
c.rect(13,12,6,1, shadow)

# Shoulder and sleeve underlayer.
c.poly([(5,10),(10,10),(12,14),(9,18),(7,25),(5,25)], shadow)
c.poly([(27,10),(22,10),(20,14),(23,18),(25,25),(27,25)], shadow)
c.rect(4,11,3,4, steel)
c.rect(25,11,3,4, steel)
c.rect(5,10,4,2, light)
c.rect(23,10,4,2, light)
c.rect(4,14,3,2, ink2)
c.rect(25,14,3,2, ink2)

# Torso base, with a tapered armored silhouette.
c.poly([(10,13),(22,13),(24,17),(24,26),(26,28),(23,29),(9,29),(6,28),(8,26),(8,17)], ink2)
c.poly([(11,14),(21,14),(23,18),(22,26),(24,28),(9,28),(10,26),(9,18)], steel)
# Deep side folds.
c.rect(8,18,2,8, shadow)
c.rect(22,18,2,8, shadow)
c.rect(10,26,12,2, shadow)
# Central chest plate seam/shading.
c.rect(15,14,2,13, shadow)
c.rect(16,14,1,12, steel)

# Chainmail rings: tiny dark openings with cool metal arcs, staggered like woven links.
def ring(x, y, tone=steel):
    # 3x3 open ring, with an offset bright edge.
    c.rect(x+1, y, 1, 1, tone)
    c.rect(x, y+1, 1, 1, tone)
    c.rect(x+2, y+1, 1, 1, shadow)
    c.rect(x+1, y+2, 1, 1, shadow)
    c.set(x+1, y+1, ink2)

# Main woven field, rows interlock through staggered placement.
for y, xs in [(15,[10,14,18,21]), (18,[8,12,16,20]), (21,[10,14,18,21]),
              (24,[8,12,16,20]), (27,[10,14,18])]:
    for x in xs:
        ring(x, y, steel if y < 24 else shadow)

# Bright steel catches on selected ring edges.
for x,y in [(11,15),(19,15),(9,18),(17,18),(11,21),(19,21),(9,24),(17,24),(15,27)]:
    c.set(x, y, light)
    c.set(x+1, y, light)

# Mail on the sleeves, arranged as smaller linked bands.
for y, xs in [(13,[5,7,25]),(16,[5,7,24,26]),(19,[5,7,24,26]),(22,[5,7,24,26]),(25,[5,7,24,26])]:
    for x in xs:
        ring(x, y, shadow)

# Shoulder plate caps give the sprite an RPG armor silhouette.
c.poly([(4,9),(8,9),(11,12),(9,14),(5,13),(4,12)], ink)
c.poly([(5,10),(8,10),(10,12),(8,13),(5,12)], steel)
c.rect(5,10,3,1, light)
c.set(9,12, light)
c.poly([(28,9),(24,9),(21,12),(23,14),(27,13),(28,12)], ink)
c.poly([(27,10),(24,10),(22,12),(24,13),(27,12)], steel)
c.rect(24,10,3,1, light)
c.set(22,12, light)

# Forearm cuffs and leather tie details.
c.rect(4,25,4,3, ink)
c.rect(5,25,3,2, shadow)
c.rect(5,25,2,1, light)
c.rect(24,25,4,3, ink)
c.rect(24,25,3,2, shadow)
c.rect(25,25,2,1, light)
c.rect(6,27,2,1, accent)
c.rect(24,27,2,1, accent)

# Bottom mail scallops, separated by the heavy outline.
c.rect(8,28,16,2, ink)
for x in [9,12,15,18,21]:
    c.rect(x,27,2,2, steel)
    c.set(x,27, light)
c.rect(10,29,2,1, shadow)
c.rect(13,29,2,1, shadow)
c.rect(16,29,2,1, shadow)
c.rect(19,29,2,1, shadow)

# A few sharp pixel highlights establish metal direction.
c.set(6,11, glint)
c.set(26,11, glint)
c.set(12,5, glint)
c.set(18,5, light)
c.set(10,14, glint)
c.set(21,14, light)

view(c)
finish(c)
