src = input_canvas
SW, SH = src.stats()['size']
CHAR = {0: '.', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g'}
print('size', SW, SH)
for y in range(43, SH):
    print(f'{y:2d} ' + ''.join(CHAR.get(src.get(x, y), '?') for x in range(SW)))
# exact runs per row
print('--- runs (start-end:char) ---')
for y in range(45, SH):
    runs = []
    cur = None; start = 0
    for x in range(SW):
        v = src.get(x, y)
        if v != cur:
            if cur is not None and cur != 0:
                runs.append(f'{start}-{x-1}:{CHAR.get(cur)}')
            cur = v; start = x
    if cur != 0:
        runs.append(f'{start}-{SW-1}:{CHAR.get(cur)}')
    print(y, runs)
