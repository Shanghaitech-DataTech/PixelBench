result = new_canvas(16, 16, name="magnifying_glass")
# Deliberate stepped silhouettes keep the small icon crisp.
ink = '#242837'
bronze = '#8b5b34'
gold = '#d5a553'
lightgold = '#ffe0a0'
glass = '#8bc4ce'
glass_dark = '#4b8a9b'
glass_light = '#c4e6e5'
shine = '#f1fcf0'
wood = '#86513e'
woodlight = '#be8053'
# Diagonal wooden grip, with a dark one-pixel perimeter.
result.poly([(9,8),(14,13),(14,14),(13,15),(12,14),(8,10)], ink)
result.line(10,10,13,13,woodlight)
result.line(10,11,13,14,wood)
result.set(14,14,ink)
# Brass neck sits beneath the circular rim.
result.line(9,9,11,11,bronze)
result.set(10,10,gold)
# Hand-shaped circular housing, diameter eleven pixels.
outer = [(4,8),(3,9),(2,10),(1,11),(1,11),(1,11),(1,11),(1,11),(2,10),(3,9),(4,8)]
for y,(a,b) in enumerate(outer,1):
    result.line(a,y,b,y,ink)
# Metallic band inside the outline.
band = [(4,8),(3,9),(2,10),(2,10),(2,10),(2,10),(2,10),(3,9),(4,8)]
for y,(a,b) in enumerate(band,2):
    result.line(a,y,b,y,gold if y < 7 else bronze)
# A few coherent reflected light segments along the upper-left rim.
result.line(4,2,7,2,lightgold)
result.set(3,3,lightgold)
result.line(2,4,2,6,lightgold)
result.line(5,10,8,10,gold)
# Lens interior with a darker lower-right edge and icy upper-left face.
lens = [(4,8),(3,9),(3,9),(3,9),(3,9),(3,9),(4,8)]
for y,(a,b) in enumerate(lens,3):
    result.line(a,y,b,y,glass_dark)
for y,a,b in [(3,4,7),(4,3,8),(5,3,8),(6,3,8),(7,3,8),(8,4,7)]:
    result.line(a,y,b,y,glass)
result.line(4,3,7,3,glass_light)
result.line(3,4,3,6,glass_light)
result.line(4,4,5,4,shine)
result.set(4,5,shine)
result.set(7,7,glass_light)
print(result.stats_text())
print(result.matrix_text())
finish(result)
