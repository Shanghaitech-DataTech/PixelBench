import runpy, sys
ns = runpy.run_path('main.py')
f1 = ns['f2']
f2 = ns['f1']
for y in range(96):
    print('%3d %s' % (y, ''.join('#' if (f1.get(x, y) != 0 and f1.get(x, y) == f2.get(x, y)) else ('B' if f1.get(x, y) != 0 else '.') for x in range(88))))
