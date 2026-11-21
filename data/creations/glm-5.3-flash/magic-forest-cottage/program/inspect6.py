src = open('main.py').read()
src = src.replace("save('magic-forest-cottage', c)", "pass").replace("finish(c)", "pass")
ns = {}
exec(compile(src, 'main.py', 'exec'), ns)
c = ns['c']

from collections import Counter
cnt = Counter()
for y in range(96, 128):
    for x in range(128):
        cnt[c.color_name(c.get(x, y))] += 1
print('bottom strip colour counts:')
for name, n in cnt.most_common():
    print(f'  {n:5d}  {name}')

print()
for pt in [(64, 118), (69, 121), (75, 124), (82, 127), (57, 110), (55, 106),
           (2, 120), (0, 125), (6, 122), (124, 122), (127, 118)]:
    print(pt, c.color_name(c.get(*pt)))
