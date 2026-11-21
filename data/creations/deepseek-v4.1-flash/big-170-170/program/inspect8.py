c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
W, H = 170, 170
lum = [[0.0]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        r, g, b, a = pal[c.get(x, y)]
        lum[y][x] = 0.299*r + 0.587*g + 0.114*b
edge = [[0]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        tot = 0.0; n = 0
        for dy in range(-3, 4):
            for dx in range(-3, 4):
                nx, ny = x+dx, y+dy
                if 0 <= nx < W and 0 <= ny < H and not (dx == 0 and dy == 0):
                    tot += lum[ny][nx]; n += 1
        edge[y][x] = lum[y][x] - tot/n
out = []
for by in range(0, H, 2):
    row = ""
    for bx in range(0, W, 2):
        vals = [edge[by+a][bx+b] for a in (0, 1) for b in (0, 1)]
        mn = min(vals); mx = max(vals)
        row += '#' if mn < -14 else ('+' if mn < -7 else ('o' if mx > 12 else '.'))
    out.append(row)
print("    " + "".join(str((i//10)%10) if i % 10 == 0 else ' ' for i in range(85)))
print("    " + "".join(str(i%10) for i in range(85)))
for i, r in enumerate(out):
    print("%3d " % (i*2) + r)
