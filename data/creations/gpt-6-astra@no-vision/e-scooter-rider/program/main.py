c = new_canvas(32, 32, name='rider')
ink = '#202b35'
black = '#141d26'
metal = '#697d86'
light = '#b5d0d0'
teal = '#27a89c'
teal_l = '#67d5bd'
teal_d = '#18776f'
skin = '#f4b88c'
skin_d = '#ce805e'
pants = '#394c67'
pants_l = '#5f7790'
red = '#ed735b'
# Wheels and hubs
c.circle(6, 27, 3, ink)
c.circle(26, 27, 3, ink)
c.circle(6, 27, 2, '#566a72')
c.circle(26, 27, 2, '#566a72')
c.set(6, 27, light)
c.set(26, 27, light)
# Rear fender and platform
c.poly([(3,24),(4,23),(8,23),(10,25),(9,26),(7,25),(4,25)], ink)
c.line(5,24,8,24, metal)
c.poly([(8,24),(23,24),(25,22),(26,23),(24,27),(9,27),(8,26)], ink)
c.line(9,25,23,25, light)
c.line(10,26,21,26, metal)
c.set(9,24,red)
# Steering stem leans toward front wheel
c.line(22,14,25,24, ink)
c.line(23,14,26,24, ink)
c.line(23,16,25,23, light)
c.line(24,23,26,25,metal)
# Handlebar and grip
c.line(20,13,25,13,ink)
c.line(21,12,24,12,black)
c.set(25,13,teal_l)
# Back leg and shoe, behind the front leg
c.poly([(11,16),(15,16),(16,19),(13,22),(12,24),(9,24),(9,22),(11,19),(10,18)],ink)
c.poly([(12,18),(14,18),(14,19),(11,23),(10,23)],pants_l)
c.line(9,24,13,24,black)
# Front leg, slightly bent
c.poly([(14,16),(18,16),(18,19),(17,21),(18,23),(20,23),(20,24),(15,24),(14,22),(14,20),(13,19)],ink)
c.poly([(15,18),(17,18),(16,20),(16,22),(17,23),(15,23),(15,20)],pants)
c.set(16,19,pants_l)
c.line(16,24,20,24,black)
# Jacket torso leaning forward
c.poly([(11,10),(14,9),(17,10),(19,13),(18,17),(16,19),(10,18),(9,16),(9,13)],ink)
c.poly([(11,11),(14,10),(16,11),(17,13),(16,17),(14,18),(10,17),(10,13)],teal)
c.line(11,12,11,16,teal_l)
c.line(12,18,16,18,teal_d)
# Arm reaches to handlebar
c.poly([(16,11),(18,11),(19,14),(21,14),(22,13),(23,13),(23,15),(21,16),(18,16),(16,14)],ink)
c.poly([(17,12),(18,13),(19,15),(21,15),(21,14),(19,14),(18,12)],teal_l)
c.set(22,14,skin)
c.set(23,14,skin_d)
# Neck and face facing right
c.rect(14,8,3,3,ink)
c.rect(15,8,2,2,skin_d)
c.poly([(12,4),(16,3),(19,5),(19,7),(20,7),(20,8),(18,8),(18,9),(15,10),(12,8)],ink)
c.poly([(13,5),(17,5),(18,6),(18,7),(19,7),(19,8),(17,8),(17,9),(15,9),(13,8)],skin)
c.set(18,6,ink)
c.set(16,8,skin_d)
# Helmet with brim
c.poly([(10,6),(10,4),(11,2),(13,1),(16,1),(18,2),(19,4),(19,5),(20,5),(20,6),(14,6),(13,7),(10,7)],ink)
c.poly([(11,5),(11,4),(12,2),(15,2),(17,3),(18,4),(18,5)],teal)
c.line(12,3,15,3,teal_l)
c.line(11,6,19,6,teal_d)
c.set(13,6,light)
# Helmet strap
c.line(12,7,13,9,ink)
c.set(14,9,skin_d)
print(c.stats_text())
finish(c)
