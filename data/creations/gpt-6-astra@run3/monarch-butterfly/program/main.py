result = new_canvas(32, 32, name='monarch')
ink = '#211d29'
edge = '#40303a'
orange = '#f58a25'
light = '#ffc052'
red = '#d9551c'
cream = '#fff1d5'
# Paint one wing pair and reflect each pixel for exact bilateral anatomy.
w = new_canvas(32,32,name='wing')
w.poly([(2,2),(5,2),(9,4),(12,8),(14,13),(14,19),(10,19),(6,17),(3,14),(1,9),(1,4)],ink)
w.poly([(5,15),(11,16),(14,19),(14,23),(12,27),(9,29),(6,28),(3,25),(2,21),(3,18)],ink)
# Long forewing cells separated by the dark branching veins.
w.poly([(4,4),(6,5),(10,9),(12,13),(12,15),(9,12),(6,8)],orange)
w.poly([(3,6),(5,9),(8,13),(11,16),(7,15),(4,12),(3,9)],orange)
w.poly([(7,5),(9,6),(11,9),(12,12),(10,10)],light)
w.poly([(4,13),(7,16),(11,18),(8,18),(5,16)],red)
w.line(4,5,6,7,light)
w.line(4,10,5,12,light)
w.set(8,11,light)
# Rounded lower wings: fan-shaped orange cells.
w.poly([(5,18),(8,19),(12,19),(9,21),(5,21),(4,20)],orange)
w.poly([(4,22),(8,22),(11,20),(9,24),(6,25),(5,24)],orange)
w.poly([(11,22),(12,21),(12,25),(10,27),(8,27),(10,24)],orange)
w.line(5,19,7,19,light)
w.line(5,23,6,24,light)
w.set(10,26,red)
w.set(7,26,red)
# Ivory spots on the black outer margins.
for x,y in [(3,3),(2,6),(2,9),(3,12),(5,15),(4,18),(3,21),(4,24),(6,27),(9,28),(12,26)]:
    w.set(x,y,cream)
w.set(5,3,'#d5c7b7')
w.set(8,5,cream)
w.set(11,8,'#d5c7b7')
w.set(13,12,cream)
for y in range(32):
    for x in range(15):
        col = w.get(x,y)
        result.set(x,y,col)
        result.set(31-x,y,col)
# Slender segmented thorax and abdomen.
result.line(15,12,15,24,ink)
result.line(16,12,16,24,ink)
result.rect(14,14,4,5,ink)
result.rect(15,10,2,3,ink)
result.set(15,11,'#a08b7e')
result.line(15,14,15,18,'#66504b')
result.set(15,20,'#907065')
result.set(16,22,'#66504b')
result.line(15,25,16,25,ink)
# Fine outward-curving antennae.
result.line(15,10,14,7,ink)
result.line(14,7,12,6,ink)
result.line(16,10,17,7,ink)
result.line(17,7,19,6,ink)
view(result, scale=12, margin=0)
finish(result)
