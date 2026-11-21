output = input_canvas.copy(name='output')
shadow='#87b7c5'
mid='#c4dfe3'
white='#f2f8ee'
# Snow settles along the upper surfaces of each drooping bough.
def cap(points, depths):
    lower=[(x,y+d) for (x,y),d in zip(points,depths)]
    output.poly(points+list(reversed(lower)),shadow)
    lower2=[(x,y+max(1,d-1)) for (x,y),d in zip(points,depths)]
    output.poly(points+list(reversed(lower2)),mid)
    for i in range(len(points)-1):
        x,y=points[i]; xx,yy=points[i+1]
        output.line(x,y,xx,yy,white)
        if depths[i]>3:
            output.line(x,y+1,xx,yy+1,white)
# Crown: small accumulated caps, widening down the tree.
cap([(41,0),(40,3),(38,5)],[2,2,1])
cap([(41,3),(43,6),(45,8)],[2,2,1])
cap([(40,9),(38,12),(35,15)],[3,3,1])
cap([(41,10),(44,15),(48,18)],[3,3,1])
cap([(39,18),(36,22),(32,25)],[4,3,1])
cap([(40,19),(44,24),(48,27),(52,28)],[4,4,3,1])
cap([(38,29),(34,33),(30,36),(25,38)],[4,4,3,1])
cap([(40,29),(44,35),(50,39),(55,41)],[4,4,3,1])
cap([(37,40),(33,44),(28,48),(22,51)],[5,5,4,1])
cap([(40,42),(46,48),(53,53),(61,56)],[5,5,4,1])
cap([(35,53),(30,58),(23,63),(16,67)],[5,5,4,1])
cap([(39,56),(45,60),(51,65),(59,69),(66,71)],[5,5,5,3,1])
cap([(33,65),(28,71),(21,76),(13,79),(9,82)],[5,6,4,3,1])
cap([(39,70),(46,75),(54,79),(62,83),(71,86)],[5,5,5,3,1])
cap([(32,81),(27,86),(20,90),(13,95),(7,97)],[5,5,5,3,1])
cap([(38,85),(44,89),(50,94),(58,98),(66,101),(74,103)],[5,6,5,4,3,1])
cap([(29,95),(24,101),(17,106),(10,110),(3,113),(0,115)],[5,6,5,4,3,1])
cap([(36,99),(40,104),(45,108)],[5,5,2])
cap([(52,104),(59,109),(66,113),(74,116),(80,117)],[5,5,4,3,1])
cap([(36,110),(31,115),(25,120),(20,123)],[5,5,4,1])
cap([(38,111),(43,117),(49,121),(54,123)],[5,5,3,1])
# Short irregular hanging edges give the snow its weight.
for x,y in [(34,36),(44,38),(29,49),(50,54),(25,65),(47,65),(22,78),(56,83),(24,92),(46,95),(18,109),(61,113),(32,118)]:
    output.rect(x,y,2,2,mid)
view(output)
finish(output)
