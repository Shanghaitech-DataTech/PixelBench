c = input_canvas
W, H = c.stats()['size']
bg = c.color('c0')
seen = [[False]*W for _ in range(H)]
comps = []
for y in range(H):
    for x in range(W):
        if seen[y][x]:
            continue
        idx = c.get(x, y)
        seen[y][x] = True
        if idx == bg:
            continue
        stack = [(x, y)]
        pix = []
        while stack:
            px, py = stack.pop()
            pix.append((px, py))
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = px+dx, py+dy
                if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx]:
                    seen[ny][nx] = True
                    if c.get(nx, ny) != bg:
                        stack.append((nx, ny))
        comps.append(pix)
for i, pix in enumerate(comps):
    xs = [p[0] for p in pix]
    ys = [p[1] for p in pix]
    print(i, 'size', len(pix), 'bbox', min(xs), min(ys), max(xs), max(ys))

for idx_info in c.palette():
    i = idx_info['index']
    xs = [x for y in range(H) for x in range(W) if c.get(x, y) == i]
    if xs:
        print(i, c.color_name(i), 'count', len(xs), 'xmin', min(xs), 'xmax', max(xs))
