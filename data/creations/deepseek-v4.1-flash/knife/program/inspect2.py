from collections import deque, Counter
w, h, data = input_canvas.to_rgba()
px = [[tuple(data[(y*w+x)*4:(y*w+x)*4+4]) for x in range(w)] for y in range(h)]
seen = [[False]*w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if px[y][x][3] > 0 and not seen[y][x]:
            q = deque([(x,y)]); seen[y][x]=True; cells=[]
            while q:
                cx,cy = q.popleft(); cells.append((cx,cy))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=cx+dx,cy+dy
                    if 0<=nx<w and 0<=ny<h and not seen[ny][nx] and px[ny][nx][3]>0:
                        seen[ny][nx]=True; q.append((nx,ny))
            xs=[c[0] for c in cells]; ys=[c[1] for c in cells]
            cnt = Counter(px[cy][cx] for cx,cy in cells)
            comps.append((len(cells),(min(xs),min(ys),max(xs),max(ys)),cnt.most_common(6)))
comps.sort(reverse=True)
for n,bb,cc in comps:
    print(n, bb, cc)
