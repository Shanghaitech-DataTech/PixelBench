from pixelbench_api import *

c = input_canvas

def runs(x0, x1, y):
    # return string marking cols by class
    s = []
    for x in range(x0, x1+1):
        i = c.get(x, y)
        s.append('B' if i in (1,16,33,36,38,49,58,59,73,75,94,97,99,101,138,139) else
                ('D' if i in (53,58,91,95,12,42,141,142,143,152,124,108,93,37,23) else
                 ('G' if i in (104,111,115,40,73,128,123,22,2,21,107,29) else '.')))
    return ''.join(s)

for y in range(186, 218, 2):
    print(y, runs(33, 72, y))
