result = new_canvas(64,64,name='Family dining table')
c=result
ink='#302126'
dark='#63392d'
shade='#8d4b32'
wood='#b97040'
light='#d99958'
glow='#efbc77'
grain='#a66139'
# The far chair: backrest, two rails and a square seat.
c.rect(25,3,14,4,ink)
c.rect(24,5,3,14,ink); c.rect(37,5,3,14,ink)
c.rect(26,4,12,2,light); c.line(27,4,36,4,glow)
c.rect(27,7,2,7,wood); c.rect(35,7,2,7,wood)
c.rect(30,7,4,6,shade); c.rect(31,7,2,6,light)
c.rect(24,13,16,9,ink)
c.rect(25,14,14,5,light); c.rect(26,15,12,3,wood)
c.line(25,19,38,19,shade)
c.rect(25,20,3,5,ink); c.rect(36,20,3,5,ink)
# Side chairs, each with an outer backrest and an inset seat.
for right in (False, True):
    def rect(x,y,w,h,col):
        c.rect(64-x-w if right else x,y,w,h,col)
    rect(5,30,13,14,ink)
    rect(6,31,11,9,wood)
    rect(7,31,9,2,glow)
    rect(7,34,9,5,light)
    rect(6,40,11,3,shade)
    rect(6,43,3,6,ink); rect(14,43,3,6,ink)
    rect(7,43,1,4,wood); rect(15,43,1,4,wood)
    rect(2,24,5,21,ink)
    rect(3,25,3,18,shade)
    rect(3,25,2,15,light)
    rect(3,26,1,12,glow)
    rect(2,23,5,4,ink)
    rect(3,24,3,2,light)
    rect(3,43,3,6,ink)
    rect(4,43,1,4,wood)
# Table legs and thick front apron.
c.rect(16,43,5,12,ink); c.rect(17,45,3,8,shade)
c.line(17,46,17,52,light)
c.rect(43,43,5,12,ink); c.rect(44,45,3,8,shade)
c.line(44,46,44,52,light)
c.poly([(13,22),(16,19),(48,19),(51,22),(51,45),(48,49),(16,49),(13,46)],ink)
c.rect(16,43,32,5,shade)
c.line(17,47,46,47,dark)
c.line(14,42,14,45,wood); c.line(49,42,49,45,wood)
# Chamfered top and its warm bevel.
c.poly([(16,17),(48,17),(51,20),(51,41),(48,45),(16,45),(13,42),(13,20)],ink)
c.poly([(16,18),(47,18),(50,21),(50,40),(47,43),(16,43),(14,41),(14,21)],light)
c.poly([(17,20),(47,20),(48,21),(48,40),(46,42),(17,42),(16,40),(16,22)],wood)
c.line(17,19,47,19,glow); c.line(15,21,15,39,glow)
c.line(17,43,47,43,shade)
# Plank joints and sparse, hand-placed grain.
c.line(17,26,47,26,grain); c.line(17,27,47,27,light)
c.line(17,34,47,34,grain); c.line(17,35,47,35,light)
for x,y,length in [(20,22,7),(37,22,7),(19,24,4),(39,29,6),(18,31,4),(21,38,6),(35,39,8),(18,40,3),(43,37,3)]:
    c.line(x,y,x+length,y,grain)
c.line(21,21,26,21,light)
c.line(36,37,41,37,light)
c.line(22,39,25,39,light)
# Bowl cast shadow, glazed ceramic body and rim.
c.ellipse(33,33,10,3,grain)
c.ellipse(32,30,10,6,ink)
c.ellipse(32,30,9,5,'#547b77')
c.rect(27,34,10,2,ink)
c.line(28,34,36,34,'#37605f')
c.ellipse(32,28,10,4,ink)
c.ellipse(32,28,9,3,'#e9d8ac')
c.ellipse(32,28,7,2,'#ac9169')
# Fruit: pear, apples, and a curved bunch of bananas.
c.poly([(29,21),(31,21),(32,24),(34,26),(33,29),(28,29),(27,27),(28,24)],ink)
c.poly([(29,22),(30,22),(31,25),(32,26),(32,28),(28,28),(28,26),(29,24)],'#a8ba58')
c.line(29,23,29,25,'#d8db80'); c.line(30,21,31,19,dark)
c.circle(27,28,3,ink); c.circle(27,28,2,'#c34d3b'); c.set(26,27,'#f58b59')
c.line(27,25,26,24,dark)
c.circle(35,27,3,ink); c.circle(35,27,2,'#df6442'); c.set(34,26,'#ffac69')
c.line(35,24,36,23,dark); c.line(36,24,38,24,'#718d43')
c.path('M 36 30 L 39 28 L 40 24 L 42 25 L 41 29 L 38 32 L 33 32 L 32 30 Z',ink)
c.path('M 34 30 L 38 30 L 40 27 L 40 25 L 41 25 L 40 29 L 37 31 L 34 31 Z','#edb94f')
c.line(35,30,38,30,'#ffe394')
# Front face of the bowl stays visible beneath the fruit.
c.line(25,31,27,32,'#99b8a4'); c.line(28,33,35,33,'#78a394')
# Near chair seat, feet, open slats and broad backrest.
c.rect(25,47,14,9,ink)
c.rect(26,48,12,6,light)
c.line(27,48,36,48,glow)
c.rect(27,50,10,4,wood)
c.rect(25,54,3,8,ink); c.rect(36,54,3,8,ink)
c.line(26,55,26,60,light); c.line(37,55,37,60,wood)
c.rect(29,53,2,5,ink); c.rect(33,53,2,5,ink)
c.line(29,54,29,56,light); c.line(33,54,33,56,light)
c.rect(24,56,16,5,ink)
c.rect(25,57,14,3,wood)
c.line(26,57,37,57,glow)
c.line(27,59,36,59,shade)
view(result)
finish(result)
