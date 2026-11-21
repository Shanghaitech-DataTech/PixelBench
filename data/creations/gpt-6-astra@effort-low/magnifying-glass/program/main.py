result = new_canvas(16,16)
c=result
# diagonal leather handle and brass collar
c.poly([(9,8),(15,13),(15,15),(13,15),(8,10)], '#262433')
c.line(10,10,14,14,'#71463b')
c.line(10,11,13,14,'#a76a48')
c.set(14,13,'#bb8053')
c.line(9,9,11,11,'#e7b75e')
c.set(10,11,'#956039')
# substantial circular bronze frame
c.circle(6,6,6,'#262433')
c.circle(6,6,5,'#a36d3f')
c.circle(6,5,4,'#efc778')
c.circle(6,6,4,'#354a60')
c.circle(6,6,3,'#6093a3')
# glass shaded toward bottom right
c.poly([(4,7),(6,8),(8,6),(8,8),(6,9),(4,8)],'#407080')
c.line(4,4,6,3,'#e3f6e9')
c.line(3,5,3,6,'#b9e0dc')
c.set(7,4,'#9ac7c9')
c.set(8,5,'#9ac7c9')
# rim glints
c.line(3,2,5,1,'#ffe4a0')
c.set(2,3,'#ffe4a0')
c.line(4,11,7,11,'#cc914c')
view(result)
finish(result)
