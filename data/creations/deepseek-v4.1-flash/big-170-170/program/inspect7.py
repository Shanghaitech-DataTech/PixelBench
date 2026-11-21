c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
W, H = 170, 170
lum = [[0]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        r, g, b, a = pal[c.get(x, y)]
        lum[y][x] = 0.299*r + 0.587*g + 0.114*b

def comps(mask, minsize=40):
    seen = [[False]*W for _ in range(H)]
    out = []
    for y in range(H):
        for x in range(W):
            if mask[y][x] and not seen[y][x]:
                stack = [(x, y)]; seen[y][x] = True
                pix = []
                while stack:
                    cx, cy = stack.pop()
                    pix.append((cx, cy))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < W and 0 <= ny < H and mask[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True; stack.append((nx, ny))
                if len(pix) >= minsize:
                    xs = [p[0] for p in pix]; ys = [p[1] for p in pix]
                    out.append((len(pix), min(xs), min(ys), max(xs), max(ys)))
    out.sort(reverse=True)
    return out

for th in (70, 100, 130):
    mask = [[lum[y][x] > th for x in range(W)] for y in range(H)]
    print("=== lum >", th)
    for s in comps(mask)[:18]:
        print("   size=%-5d bbox=(%d,%d)-(%d,%d)" % s)
