import math

result = new_canvas(32, 32, name='ancient_compass')
# An opaque, stepped silhouette around a transparent inventory sprite.
ink = '#201c29'
edge = '#49302d'
shadow = '#815032'
bronze = '#b77936'
gold = '#dda64b'
light = '#f6ce73'
shine = '#ffebac'
face = '#263940'
face_hi = '#354d50'
face_dark = '#192c35'

# Small cast suspension loop, seen from above.
result.rect(13, 0, 6, 1, ink)
result.rect(11, 1, 10, 5, ink)
result.rect(12, 1, 8, 5, bronze)
result.line(13, 1, 18, 1, light)
result.line(12, 2, 12, 4, gold)
result.rect(14, 2, 4, 3, ink)
result.rect(14, 2, 4, 2, None)
result.line(19, 2, 19, 4, shadow)

# Concentric hand-sized case: a heavy outline, shaded gold bevel,
# narrow interior lip, and a recessed dark compass dial.
cx, cy = 15.5, 17
for y in range(4, 31):
    for x in range(2, 30):
        dx, dy = x-cx, y-cy
        r = math.hypot(dx, dy)
        if r > 13.65:
            continue
        illumination = (-dx*0.7-dy*0.8)/max(r,1)
        if r > 11.9:
            col = ink
        elif r > 10.1:
            if illumination > 0.65: col = shine
            elif illumination > 0.0: col = light
            elif illumination > -0.65: col = gold
            else: col = bronze
        elif r > 9.15:
            col = shadow if illumination < 0.3 else bronze
        elif r > 8.35:
            col = ink
        else:
            col = face_dark if dy < -3 else face
        result.set(x,y,col)

# Sparse imperfections in the old metal; upper-left highlights and a
# lower-right secondary bevel give the case a tangible thickness.
result.line(5, 12, 5, 15, light)
result.line(8, 8, 10, 7, shine)
result.line(10, 28, 13, 29, shadow)
result.line(19, 28, 22, 27, shadow)
result.set(25, 23, shadow)
result.set(26, 22, gold)
result.set(7, 23, shadow)
result.set(8, 24, bronze)
result.set(22, 8, bronze)

# The four bezel pins are small, square, and darkly recessed.
for x,y in [(15,6),(5,17),(26,17),(15,28)]:
    result.rect(x, y, 2, 2, shadow)
    result.set(x,y,shine if y < 20 else gold)

# Oblique scale divisions on the recessed dial.
for x,y,xx,yy in [(10,11,11,12),(21,11,20,12),
                  (9,15,10,15),(22,15,21,15),
                  (10,23,11,22),(21,23,20,22),
                  (9,20,10,20),(22,20,21,20)]:
    result.line(x,y,xx,yy,bronze)

# Compass rose: long north/south points with split metallic facets.
result.poly([(15,8),(19,16),(16,26),(12,18)], ink)
result.poly([(7,17),(15,13),(24,17),(16,21)], ink)
result.poly([(8,17),(15,14),(16,17)], light)
result.poly([(8,17),(16,17),(15,20)], bronze)
result.poly([(16,17),(16,14),(23,17)], gold)
result.poly([(16,17),(23,17),(16,20)], shadow)
result.poly([(15,9),(12,17),(15,18)], shine)
result.poly([(15,9),(19,17),(15,18)], gold)
result.poly([(15,17),(16,25),(12,18)], bronze)
result.poly([(15,17),(19,18),(16,25)], light)

# A diamond-cut crystal leaves the four compass points clearly exposed.
result.poly([(15,12),(20,17),(16,22),(11,17)], ink)
result.poly([(15,13),(19,17),(16,21),(12,17)], gold)
result.poly([(15,14),(18,17),(16,20),(13,17)], '#175980')
result.poly([(15,14),(18,17),(16,17),(13,17)], '#6de6ee')
result.poly([(13,17),(16,17),(16,20)], '#249ac6')
result.poly([(16,17),(18,17),(16,20)], '#22568d')
result.poly([(15,15),(17,17),(16,19),(14,17)], '#41c8e6')
result.set(15,14,'#d0ffff')
result.set(14,15,'#a4f7f4')
result.set(14,16,'#d0ffff')
result.set(17,17,'#72dfe9')
# Crisp tips catch the same upper-left light as the case.
result.set(15,9,shine)
result.set(8,17,light)
result.set(16,24,gold)

view(result, scale=12, margin=0)
save('ancient_golden_compass', result)
finish(result)
