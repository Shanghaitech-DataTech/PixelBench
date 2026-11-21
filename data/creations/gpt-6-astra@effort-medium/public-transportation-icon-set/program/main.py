result = new_canvas(64,64,'#142735',name='public_transport')
c=result
bg='#142735'; frame='#35515d'; tile='#203b49'; ink='#e6f3df'; accent='#69cfba'; dark='#142735'
# Four identical inset panels, with a two-pixel gutter.
for x,y in [(2,2),(33,2),(2,33),(33,33)]:
 c.rect(x+2,y,25,29,frame); c.rect(x,y+2,29,25,frame)
 c.rect(x+2,y+1,25,27,tile); c.rect(x+1,y+2,27,25,tile)
# Bus, front view
c.rect(8,8,17,18,ink); c.rect(10,6,13,2,ink)
c.rect(6,12,2,6,accent); c.rect(25,12,2,6,accent)
c.rect(10,8,13,3,accent)
c.rect(10,12,13,7,dark); c.rect(16,12,2,7,ink)
c.rect(10,12,6,2,'#497a86'); c.rect(18,12,5,2,'#497a86')
c.rect(10,21,3,2,accent); c.rect(20,21,3,2,accent)
c.rect(15,22,3,2,dark)
c.rect(9,26,4,2,ink); c.rect(20,26,4,2,ink)
# Subway, matching front view, rounded roof, rails
c.rect(41,6,13,2,ink); c.rect(39,8,17,16,ink)
c.rect(41,24,13,2,ink)
c.rect(44,8,7,2,accent)
c.rect(41,12,13,7,dark); c.rect(41,12,13,2,'#497a86')
c.rect(47,12,2,7,ink)
c.rect(41,21,3,2,accent); c.rect(51,21,3,2,accent)
c.rect(46,22,3,2,dark)
c.poly([(42,26),(44,26),(42,29),(40,29)],accent)
c.poly([(51,26),(53,26),(55,29),(53,29)],accent)
c.rect(43,27,9,1,accent)
# Bicycle: squared pixel wheels, two-pixel frame
for x in [9,24]:
 c.rect(x-3,49,7,2,ink); c.rect(x-3,57,7,2,ink)
 c.rect(x-5,51,2,6,ink); c.rect(x+4,51,2,6,ink)
# frame strokes via double one-pixel lines
def stroke(x0,y0,x1,y1,col):
 c.line(x0,y0,x1,y1,col); c.line(x0,y0+1,x1,y1+1,col)
stroke(9,53,14,45,accent)
stroke(9,53,18,53,accent)
stroke(14,45,18,53,accent)
stroke(14,46,22,46,accent)
stroke(18,53,22,46,accent)
stroke(21,42,24,53,accent)
c.rect(11,43,6,2,ink); c.rect(20,40,6,2,ink); c.rect(20,41,2,3,accent)
c.rect(17,52,3,3,ink)
# Walking pedestrian, same 2px minimum features
c.rect(47,37,4,5,ink); c.rect(46,38,6,3,ink)
c.poly([(46,43),(50,43),(51,48),(55,50),(54,53),(48,50),(47,47),(45,51),(41,52),(40,50),(43,48)],accent)
c.poly([(46,48),(50,49),(49,53),(53,58),(51,60),(46,55),(45,53),(42,59),(39,59),(43,51)],ink)
view(result)
finish(result)
