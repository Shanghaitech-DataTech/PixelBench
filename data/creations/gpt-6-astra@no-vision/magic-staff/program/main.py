result = new_canvas(48, 48, name="Moonwood staff")
c = result
ink = '#281d31'
shadow = '#513044'
wood = '#885039'
mid = '#b37343'
light = '#dfa65e'
glint = '#f5ce85'
purple_dark = '#4a246d'
purple = '#8242bd'
lilac = '#bd76ed'
pale = '#edd0ff'
# A continuous crooked branch, with a hooked crown.
c.poly([(9,43),(12,45),(16,41),(29,23),(32,18),(31,15),(29,12),(29,9),(32,7),(35,7),(37,9),(37,11),(35,13),(33,13),(32,16),(34,18),(38,18),(41,15),(43,11),(42,7),(40,4),(37,2),(31,2),(27,4),(24,8),(24,12),(27,18),(24,23),(12,39)],ink)
c.poly([(11,42),(12,43),(15,40),(28,22),(30,18),(29,15),(27,12),(27,8),(31,5),(36,5),(39,8),(39,12),(36,15),(34,15),(35,16),(38,16),(40,13),(41,10),(40,7),(37,4),(31,3),(28,5),(25,8),(25,12),(28,18),(25,24),(13,40)],wood)
# Warm rim on the lit side and darker twisting grain.
c.path('M 11 41 L 15 36 L 25 22 L 28 18 L 26 13 L 25 10 L 27 6 L 31 3 L 36 3',light,fill=False)
c.path('M 13 41 L 18 34 L 21 29 M 24 25 L 29 19 M 29 16 L 27 11 L 28 8 L 32 5 L 36 5 L 39 8 L 39 12 L 36 15',shadow,fill=False)
c.path('M 27 10 L 28 7 L 31 5 L 35 4 L 38 5 L 40 8 L 40 11 L 38 14 L 35 16',mid,fill=False)
c.line(28,6,31,4,glint)
c.line(11,42,12,42,mid)
c.line(16,35,19,31,mid)
c.line(21,28,24,24,mid)
c.set(26,21,glint)
c.set(26,12,glint)
c.line(28,14,29,16,mid)
c.set(37,15,light)
# Small natural knots in the shaft.
c.line(17,35,17,37,shadow)
c.set(18,34,light)
c.line(23,26,23,28,shadow)
# A violet binding on the upper grip.
c.poly([(23,24),(25,21),(29,23),(27,26)],ink)
c.line(24,23,27,25,purple)
c.line(25,22,28,23,lilac)
c.set(24,24,pale)
c.set(27,24,purple_dark)
# Faceted magical seed suspended inside the hook.
c.poly([(33,8),(35,9),(36,12),(34,14),(31,12),(31,10)],purple_dark)
c.poly([(33,8),(35,10),(35,12),(33,13),(32,11)],purple)
c.poly([(33,9),(34,10),(34,12),(32,11)],lilac)
c.line(33,9,33,10,pale)
c.set(34,12,'#d798fa')
# Crisp, separated motes and four-point magical sparks.
def spark(x,y,col,center):
    c.line(x,y-2,x,y+2,col)
    c.line(x-2,y,x+2,y,col)
    c.set(x,y,center)
spark(20,7,purple,lilac)
spark(42,21,lilac,pale)
spark(20,19,purple,lilac)
c.set(18,11,lilac)
c.set(22,3,purple_dark)
c.set(44,15,purple)
c.set(37,23,purple)
c.set(36,24,lilac)
c.set(32,28,purple_dark)
c.set(30,30,lilac)
c.set(8,34,purple)
c.set(7,35,lilac)
c.set(17,26,purple_dark)
print(c.stats_text())
print(c.matrix_text(region=(23,1,44,19)))
save('magic-staff', result)
finish(result)
