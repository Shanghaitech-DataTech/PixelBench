result = new_canvas(64,84,name='running_fountain')
result.blit(input_canvas,0,8)
# Water palette echoes the existing turquoise basin tiles.
deep='#16768f'
water='#24afcd'
cyan='#56dcea'
light='#acf5f3'
white='#e8ffff'
# Fountain jets, above the original finial.
result.path('M 31 11 Q 29 3 25 3 Q 21 3 20 10',deep,False)
result.path('M 32 11 Q 34 3 38 3 Q 42 3 43 10',deep,False)
result.path('M 31 10 Q 28 3 25 4 Q 22 4 21 9',cyan,False)
result.path('M 32 10 Q 35 3 38 4 Q 41 4 42 9',cyan,False)
result.line(31,9,31,2,light)
result.line(32,9,32,3,cyan)
result.set(31,1,white)
result.set(30,2,cyan)
result.set(20,12,cyan)
result.set(43,12,light)
result.rect(30,10,3,3,cyan)
result.line(31,9,31,12,light)
# Narrow sheets spilling over the lips of all three bowls.
def fall(points, edge, highlights):
    result.poly(points,water)
    for a,b in edge:
        result.line(*a,*b,cyan)
    for a,b in highlights:
        result.line(*a,*b,light)
# upper bowl to middle bowl
fall([(23,20),(26,21),(26,25),(27,27),(25,29),(22,28),(23,25)],
     [((23,21),(23,26)),((25,25),(26,28))],
     [((24,21),(24,24)),((24,26),(24,27))])
fall([(37,21),(40,20),(40,25),(41,27),(39,29),(36,28),(37,25)],
     [((39,21),(39,26)),((37,25),(37,28))],
     [((38,22),(38,25)),((39,27),(39,28))])
# middle bowl to broad bowl
fall([(18,30),(22,32),(22,36),(23,38),(20,40),(17,38),(18,35)],
     [((18,32),(18,37)),((21,34),(22,38))],
     [((19,32),(19,35)),((20,36),(20,38))])
fall([(42,32),(46,30),(46,35),(47,38),(44,40),(41,38),(42,35)],
     [((45,32),(45,37)),((42,34),(42,38))],
     [((44,32),(44,35)),((44,37),(44,38))])
# broad bowl spills down either side of the stone pedestal
fall([(14,39),(18,41),(18,47),(17,53),(19,57),(18,60),(14,60),(13,57),(14,51)],
     [((14,42),(14,49)),((14,52),(14,57)),((17,44),(17,48)),((16,53),(17,59))],
     [((15,42),(15,47)),((15,50),(15,54)),((16,56),(16,58))])
fall([(45,41),(49,39),(49,49),(50,55),(50,59),(46,61),(44,58),(46,52)],
     [((48,42),(48,49)),((48,51),(49,57)),((45,55),(45,58))],
     [((47,42),(47,47)),((47,49),(47,53)),((48,56),(48,58))])
# Broken elliptical ripples and little upward kicks at each landing.
def splash(x,y,w):
    result.line(x-w,y,x-2,y,cyan)
    result.line(x+2,y,x+w,y,cyan)
    result.line(x-w+1,y+1,x+w-1,y+1,water)
    result.line(x-1,y,x+1,y,light)
    result.set(x-w,y-1,light)
    result.set(x+w,y-1,cyan)
    result.set(x-2,y-2,cyan)
    result.set(x+2,y-2,light)
for x,y,w in [(24,28,4),(39,28,4),(20,39,4),(44,39,4),(16,59,6),(47,59,6)]:
    splash(x,y,w)
# Scattered airborne drops and wider base ripples.
for x,y in [(12,54),(20,56),(43,56),(52,54)]:
    result.set(x,y,light)
for x,y in [(12,51),(20,53),(43,52),(51,51)]:
    result.set(x,y,cyan)
result.line(11,61,14,62,cyan)
result.line(18,62,21,61,cyan)
result.line(43,62,46,63,cyan)
result.line(49,62,52,61,cyan)
view(result,scale=6,margin=0)
finish(result)
