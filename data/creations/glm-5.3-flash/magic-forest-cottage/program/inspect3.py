src = open('main.py').read()
src = src.replace("save('magic-forest-cottage', c)", "pass").replace("finish(c)", "pass")
ns = {}
exec(compile(src, 'main.py', 'exec'), ns)
c = ns['c']

w, h, raw = c.to_rgba()

# where are the very bright pixels (lum > 204)?
from collections import defaultdict
groups = defaultdict(list)
for y in range(128):
    for x in range(128):
        i = (y * w + x) * 4
        r, g, b, a = raw[i:i + 4]
        if a and 0.299 * r + 0.587 * g + 0.114 * b > 204:
            groups[(y // 8, x // 8)].append((x, y))
print('bright 8x8 blocks (block_y, block_x): count')
for k in sorted(groups):
    print(k, len(groups[k]))

def show(name, region):
    print('=' * 20, name, region)
    print(c.matrix_text(region=region))

show('chimney+smoke', (60, 8, 92, 60))
show('winch', (92, 46, 126, 70))
