output=input_canvas.copy(name='output')
shadow='#789fa9'
mid='#bad5d8'
white='#edf5ed'
light='#ffffff'
# Snow follows the sloping upper surfaces of the boughs.
def cap(points, widths):
    lower=[(x,y+w) for (x,y),w in zip(points,widths)]
    output.poly(points+list(reversed(lower)),shadow)
    output.poly(points+[(x,y+max(1,w-2)) for (x,y),w in reversed(list(zip(points,widths)))],mid)
    upper=points+[(x,y+max(1,w-4)) for (x,y),w in reversed(list(zip(points,widths)))]
    output.poly(upper,white)
# Each tier has its own asymmetrical spread and scalloped lip.
cap([(41,1),(40,5),(37,8)],[2,3,1])
cap([(41,5),(43,9),(45,11)],[2,3,1])
cap([(40,13),(38,17),(35,21)],[3,4,1])
cap([(41,14),(44,20),(49,24)],[3,4,1])
cap([(40,25),(36,29),(33,33),(27,36)],[3,5,4,1])
cap([(41,26),(45,32),(50,36),(56,39)],[3,5,4,1])
cap([(39,39),(35,44),(30,48),(24,51),(21,53)],[4,6,5,3,1])
cap([(42,40),(46,46),(53,51),(61,55)],[4,6,4,1])
cap([(40,53),(36,57),(31,63),(24,67),(17,71),(12,73)],[4,6,6,5,3,1])
cap([(42,54),(47,60),(54,66),(62,71),(69,75)],[4,6,6,4,1])
cap([(38,70),(33,74),(27,79),(20,83),(14,86)],[4,6,6,4,1])
cap([(40,69),(46,75),(52,79),(60,84),(69,87)],[4,6,6,4,1])
cap([(37,85),(32,90),(26,96),(18,100),(10,104),(3,106)],[4,7,6,5,3,1])
cap([(40,85),(46,91),(52,96),(62,101),(72,105),(78,108)],[4,6,6,5,3,1])
cap([(39,100),(35,105),(29,110),(23,114),(17,116)],[4,6,6,4,1])
cap([(41,101),(46,107),(51,112),(58,117),(65,119)],[4,6,6,4,1])
# Small bright resting ridges break up the larger caps.
for x,y,w in [(39,3,2),(37,16,2),(35,29,3),(34,44,3),(35,58,3),(48,62,2),(30,77,3),(46,77,2),(29,94,3),(53,98,3),(33,108,3)]:
    output.line(x,y,x+w,y,light)
view(output)
finish(output)
