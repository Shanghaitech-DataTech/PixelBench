result = new_canvas(64,32,name='city_bus')
c=result
# Compact modern low-floor body; nose points right.
ink='#172734'
edge='#354956'
white='#e2ebe7'
shade='#a5bbc0'
teal='#168e92'
light='#41b5b1'
glass='#244856'
shine='#68959e'
c.poly([(4,7),(55,7),(59,10),(60,14),(61,23),(58,25),(4,25),(2,23),(2,10)],ink)
c.rect(4,8,50,2,white)
c.line(6,7,52,7,shade)
# Roof climate unit.
c.rect(15,5,20,2,edge)
c.rect(17,4,15,2,shade)
c.line(18,4,30,4,white)
c.line(17,6,33,6,'#6a848d')
c.poly([(4,10),(55,10),(58,12),(59,20),(59,23),(4,23)],white)
c.rect(3,18,55,5,teal)
c.line(4,18,57,18,light)
c.rect(4,23,54,1,'#116773')
# Passenger glazing with uninterrupted top band.
c.rect(5,10,49,7,ink)
for x,w in [(6,7),(15,7),(24,7),(42,7)]:
    c.rect(x,11,w,5,glass)
    c.line(x,11,x+w-1,11,shine)
    c.line(x,12,x+2,14,'#3b6572')
    c.line(x+w-2,15,x+w-1,15,'#416b77')
# Rear passenger doors, dark frames and separate leaves.
c.rect(32,10,9,14,ink)
for x in [33,37]:
    c.rect(x,11,3,6,glass)
    c.line(x,11,x+2,11,shine)
    c.rect(x,18,3,5,'#bed0d0')
    c.line(x,19,x+2,19,'#7b989e')
c.set(35,17,white)
c.set(37,17,white)
c.line(33,23,39,23,'#718b92')
# Front entrance directly behind the windscreen.
c.rect(50,10,7,14,ink)
c.rect(51,11,2,6,glass)
c.rect(54,11,2,6,glass)
c.line(51,11,55,11,shine)
c.rect(51,18,2,5,'#bed0d0')
c.rect(54,18,2,5,'#bed0d0')
c.line(51,23,55,23,'#718b92')
c.set(52,17,white)
c.set(54,17,white)
# Sloped driver windshield and subtle mirror.
c.poly([(57,11),(58,13),(59,17),(57,17)],glass)
c.line(57,12,58,15,shine)
c.line(59,12,61,12,ink)
c.rect(61,12,1,3,edge)
# Small destination display over the middle windows.
c.rect(23,9,8,4,ink)
c.rect(24,10,2,1,'#ffc76b')
c.set(25,11,'#ffc76b')
c.line(28,10,29,10,'#d89745')
c.set(28,11,'#d89745')
# Rear vents and body details.
c.line(6,20,11,20,'#116773')
c.line(6,22,10,22,'#116773')
c.rect(3,18,1,3,'#c84953')
c.set(3,18,'#ff9473')
c.rect(58,19,2,2,'#fff1ba')
c.set(59,21,'#eab368')
c.rect(58,23,3,1,edge)
c.rect(2,23,4,1,edge)
c.line(23,21,28,21,'#72cfbe')
# Two recessed wheel arches and rubber tyres.
for x in [16,46]:
    c.circle(x,24,4,ink)
    c.circle(x,24,3,'#202b35')
    c.line(x-2,22,x-1,21,'#455460')
    c.circle(x,24,2,'#91a8af')
    c.line(x-1,23,x+1,23,'#dae5e3')
    c.set(x,24,'#485e6b')
    c.set(x+1,25,'#5d7783')
view(result,scale=8,margin=0)
save('city_bus',result)
finish(result)
