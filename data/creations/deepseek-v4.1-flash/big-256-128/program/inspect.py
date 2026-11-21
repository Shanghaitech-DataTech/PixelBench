from pixelbench_api import *

c = canvas("output")
pal = c.palette()
def ch(x, y):
    r, g, b, a = pal[c.get(x, y)]['rgba']
    lum = (r*0.3 + g*0.6 + b*0.1)
    return ' .:-=+*#%@'[min(9, max(0, int(lum/16)))]

def dump(x0, y0, x1, y1, step=1):
    print('    ' + ''.join(str(x % 10) for x in range(x0, x1, step)))
    for y in range(y0, y1, step):
        print(f'{y:3d} ' + ''.join(ch(x, y) for x in range(x0, x1, step)))

dump(96, 0, 176, 60)
