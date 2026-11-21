from pixelbench_api import *

f1 = input_canvas.copy(name='f1')
f2 = input_canvas.copy(name='f2')

acolor = f2.color('#1d181e')   # dark outline
dcolor = f2.color('#432f53')   # membrane
ecolor = f2.color('#5f5f7b')

# Clear the old drooping wing regions (cols 0-8 and 18-26)
f2.clear(0, 0, 9, 22)
f2.clear(18, 0, 9, 22)

# Left raised wing
PL = [(9,8),(6,4),(3,2),(1,0),(2,5),(5,9),(9,14)]
f2.poly(PL, dcolor, fill=True)
f2.poly(PL, acolor, fill=False)

# Right raised wing (mirror about x=13)
PR = [(17,8),(20,4),(23,2),(25,0),(24,5),(21,9),(17,14)]
f2.poly(PR, dcolor, fill=True)
f2.poly(PR, acolor, fill=False)

finish([f1, f2])
