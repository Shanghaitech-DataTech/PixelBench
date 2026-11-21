# Monarch butterfly, built at its native 32 x 32 pixel resolution.
result = new_canvas(32, 32, background=None, name="monarch-butterfly")
ink = '#211d29'
vein = '#39252b'
orange = '#f58a24'
gold = '#ffb847'
light = '#ffd06a'
red = '#db591e'
rust = '#a63c25'
cream = '#fff0ca'
white = '#fff9e9'
bluegray = '#666371'

# One wing pair; reflect the actual pixels for clean bilateral symmetry.
# The lower wings sit behind the large triangular forewings.
result.poly([(13,16),(15,19),(14,24),(12,28),(10,29),(7,29),(4,27),(2,24),(2,22),(3,20),(6,18)], ink)
result.poly([(12,18),(13,20),(12,24),(11,27),(8,27),(5,25),(4,23),(4,21),(7,19)], orange)
result.poly([(12,19),(12,23),(10,26),(8,26),(7,24),(8,21)], red)
result.poly([(5,21),(7,20),(8,21),(6,24),(5,23)], gold)
# Veins fan out across the rounded hindwing.
result.line(12,19,5,22,vein)
result.line(12,19,7,26,vein)
result.line(12,20,11,27,vein)
result.set(5,26,cream)
result.set(7,28,white)
result.set(10,28,cream)
result.set(3,23,white)
result.set(4,20,cream)
result.set(12,26,cream)

# Tall, pointed forewing, with a broad dark outer margin.
result.poly([(14,16),(12,11),(9,8),(6,5),(4,3),(2,3),(1,5),(0,8),(0,12),(1,15),(3,18),(6,20),(10,21),(14,19)], ink)
result.poly([(4,5),(7,8),(10,11),(12,14),(13,17),(12,19),(9,19),(6,17),(3,14),(2,10),(2,7)], orange)
# Warm light at the tips; deeper orange towards the thorax.
result.poly([(4,5),(7,8),(9,10),(7,11),(4,8),(3,7)], gold)
result.poly([(3,9),(5,10),(8,13),(7,14),(4,12),(3,12)], gold)
result.poly([(9,12),(12,14),(13,17),(12,19),(10,18),(10,15)], red)
result.poly([(4,14),(8,16),(12,19),(9,19),(6,17)], red)
# Structural wing veins: long radial cells and their small cross branches.
result.line(4,5,6,10,vein)
result.line(6,10,13,18,vein)
result.line(3,9,6,11,vein)
result.line(6,11,10,13,vein)
result.line(10,13,12,14,vein)
result.line(3,13,8,15,vein)
result.line(8,15,13,18,vein)
result.line(6,17,10,17,vein)
# Ivory dots on the black borders, each placed on the pixel grid.
for x,y,col in [(2,5,white),(1,8,cream),(1,11,white),(2,14,cream),(3,16,white),(5,18,cream),(7,19,white),(10,20,cream)]:
    result.set(x,y,col)
result.set(4,4,cream)
result.set(6,6,light)
result.set(8,8,cream)
result.set(10,10,light)

# Mirror both wings about the two-pixel-wide central body.
result.select(0,0,15,32).flip('h').copy_to(17,0,result)

# Slender body and clubbed antennae.
result.line(15,12,13,9,ink)
result.line(13,9,12,7,ink)
result.line(16,12,18,9,ink)
result.line(18,9,19,7,ink)
result.set(11,6,ink)
result.set(12,6,ink)
result.set(19,6,ink)
result.set(20,6,ink)
result.rect(15,11,2,3,ink)
result.rect(14,14,4,5,ink)
result.rect(15,19,2,8,ink)
result.set(15,27,ink)
result.set(15,12,bluegray)
result.set(15,14,cream)
result.set(16,14,cream)
result.set(15,16,bluegray)
result.set(15,18,bluegray)
result.set(15,21,'#9a765e')
result.set(15,24,bluegray)

view(result, scale=12, margin=0)
save('monarch-butterfly', result)
finish(result)
