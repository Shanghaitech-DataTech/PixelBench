result = new_canvas(64, 32, name="city_bus")
c = result
outline='#172a38'
body='#e4ebe6'
shade='#a4bdbb'
teal='#248f98'
darkteal='#16616e'
glass='#294b60'
lightglass='#507b8d'
# Roof and body silhouette, facing right
c.poly([(5,7),(55,7),(58,8),(60,11),(61,22),(59,25),(4,25),(2,23),(2,11),(3,8)],outline)
c.rect(5,8,50,1,shade)
c.rect(3,10,57,13,body)
c.rect(4,9,53,2,body)
c.rect(4,23,55,1,shade)
# roof air conditioning unit
c.rect(17,5,24,2,outline)
c.rect(18,5,22,1,shade)
c.rect(21,4,15,1,shade)
c.line(7,9,53,9,'#ffffff')
# side windows, unified dark band
c.rect(4,11,54,8,outline)
for x,w in [(5,8),(15,8),(25,7),(34,8),(44,5)]:
    c.rect(x,12,w,6,glass)
    c.rect(x,12,w,1,lightglass)
    c.line(x,16,x+3,13,'#3d6579')
    c.line(x+2,17,x+5 if w>5 else x+4,15,'#3d6579')
# blue lower skirt
c.rect(3,20,57,3,teal)
c.rect(4,23,55,1,darkteal)
c.line(4,19,49,19,'#ffffff')
# rear exit, paired folding panels
c.rect(24,11,10,13,outline)
c.rect(25,12,3,6,glass)
c.rect(30,12,3,6,glass)
c.line(25,12,27,12,lightglass)
c.line(30,12,32,12,lightglass)
c.rect(25,19,3,4,shade)
c.rect(30,19,3,4,shade)
c.line(25,22,27,22,darkteal)
c.line(30,22,32,22,darkteal)
c.set(27,19,body)
c.set(30,19,body)
# front entrance with glass almost to floor
c.rect(50,11,8,13,outline)
c.rect(51,12,2,9,glass)
c.rect(55,12,2,9,glass)
c.line(51,12,52,12,lightglass)
c.line(55,12,56,12,lightglass)
c.line(51,22,56,22,shade)
c.set(52,18,'#9ababe')
c.set(55,18,'#9ababe')
# angled forward windscreen and nose
c.line(58,11,59,17,glass)
c.line(59,13,59,16,lightglass)
c.rect(58,18,2,3,body)
c.rect(60,19,1,3,shade)
# electronic destination board above forward windows
c.rect(38,10,19,3,outline)
c.line(40,11,42,11,'#ffc85d')
c.set(40,12,'#e7a642')
c.set(42,12,'#e7a642')
c.line(45,11,49,11,'#ffc85d')
c.line(51,11,54,11,'#ffc85d')
# side panel detailing
c.line(5,21,9,21,darkteal)
c.set(6,20,shade)
c.line(36,21,40,21,darkteal)
c.line(36,22,40,22,darkteal)
# Wheel wells and two rubber wheels
for x in (13,45):
    c.rect(x-4,22,9,3,outline)
    c.circle(x,24,4,outline)
    c.circle(x,24,3,'#25313d')
    c.circle(x,24,2,'#7f969e')
    c.line(x-1,23,x+1,23,'#d7e1df')
    c.set(x,24,'#405665')
    c.set(x,26,'#506974')
    c.line(x-2,28,x+2,28,outline)
# lights, bumpers, and mirror
c.rect(2,19,2,3,'#ad4b43')
c.set(2,19,'#ff966c')
c.rect(59,21,2,2,'#ffe7a0')
c.set(60,21,'#fff8de')
c.rect(58,24,3,1,outline)
c.rect(2,23,3,1,outline)
c.set(7,19,'#e6af4c')
c.set(48,19,'#e6af4c')
c.line(59,11,62,11,outline)
c.rect(62,11,1,3,outline)
view(result, scale=8, margin=0)
finish(result)
