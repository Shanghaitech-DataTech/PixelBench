result = new_canvas(64,64, '#9dcdd8', name='country_road')
# Open sky and small clouds.
result.rect(0,17,64,8,'#bedbd9')
result.rect(6,6,12,2,'#edf0da').rect(9,4,6,2,'#edf0da').rect(4,8,17,1,'#d7e7df')
result.rect(42,9,14,2,'#edf0da').rect(46,7,6,2,'#edf0da')
# Layered hills.
result.poly([(0,22),(7,18),(16,17),(26,21),(35,20),(44,16),(54,15),(63,19),(63,32),(0,32)],'#709d85')
result.poly([(0,25),(10,22),(20,23),(31,27),(43,23),(55,22),(63,24),(63,36),(0,36)],'#8ca85c')
result.poly([(0,29),(15,27),(30,30),(46,27),(63,29),(63,64),(0,64)],'#708d43')
result.poly([(0,31),(15,30),(26,33),(41,30),(63,31),(63,39),(0,39)],'#a2ae62')
# Road curves into the distance at the right.
result.poly([(63,23),(57,24),(53,26),(52,28),(58,31),(64,33),(64,56),(0,56),(0,34),(44,34),(54,32),(48,29),(49,26),(55,24)],'#c9bd95')
result.poly([(63,24),(57,25),(54,27),(54,28),(61,31),(63,32),(63,53),(0,53),(0,36),(45,36),(57,33),(58,31),(51,29),(51,27),(56,25)],'#777b7b')
result.rect(0,45,64,8,'#828584')
result.line(0,52,63,52,'#d8d1af')
for x in [0,24,48]: result.rect(x,49,13,1,'#e5d9ab')
# Field fence behind the bike.
result.line(0,29,43,31,'#d2c18d')
result.line(0,32,43,34,'#ae9869')
for x in [2,12,23,34,43]:
    y=28+x//20
    result.rect(x,y,1,7,'#706247')
    result.set(x,y,'#e1cea1')
# Roadside trees in the distance.
for x,y,r in [(1,21,3),(28,23,2),(60,20,3)]:
    result.rect(x,y,1,7,'#625e43')
    result.circle(x,y,r,'#4f7954')
    result.circle(x-1 if x else x,y-1,r-1,'#608b5b')
# Grass clusters on the near verge.
for x,y in [(2,58),(9,61),(18,57),(28,60),(41,57),(51,61),(60,57)]:
    result.line(x,y,x-1,y-2,'#4f733b')
    result.line(x,y,x+1,y-3,'#4f733b')
    result.set(x+2,y,'#b6bb6b')
result.ellipse(15,47,9,2,'#626b64')
result.ellipse(50,47,8,2,'#626b64')
# Remove only the source's white backdrop, including gaps between spokes.
for y in range(64):
    for x in range(64):
        p=input_canvas.get(x,y)
        if p != 1:
            result.set(x,y,p)
view(result)
finish(result)
