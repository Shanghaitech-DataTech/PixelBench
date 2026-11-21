from pixelbench_api import *


def dump(c, step=2, x0=0, y0=0, x1=128, y1=128, show_legend=True):
    pal = c.palette()
    names = {}
    for p in pal:
        names[p['index']] = p['name'] or p['rgba']
    # assign a stable letter per distinct name
    order = []
    for p in pal:
        n = names[p['index']]
        if n not in order:
            order.append(n)
    letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    name2ch = {}
    for i, n in enumerate(order):
        name2ch[n] = letters[i % len(letters)]
    print(f"--- step={step} ({x0},{y0})-({x1},{y1})")
    print('     ' + ''.join(str((x // step) % 10) for x in range(x0, x1, step)))
    for y in range(y0, y1, step):
        row = []
        for x in range(x0, x1, step):
            i = c.get(x, y)
            row.append(name2ch[names[i]])
        print(f'{y:4d} ' + ''.join(row))
    if show_legend:
        print("legend: " + "  ".join(f"{name2ch[n]}={n}" for n in order))
