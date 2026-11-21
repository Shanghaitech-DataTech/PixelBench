def poly_mask(pts):
    m = set()
    n = len(pts)
    ys = [p[1] for p in pts]
    for y in range(int(min(ys)), int(max(ys)) + 1):
        xs = []
        for i in range(n):
            x1, y1p = pts[i]
            x2, y2p = pts[(i + 1) % n]
            if (y1p <= y < y2p) or (y2p <= y < y1p):
                t = (y - y1p) / (y2p - y1p)
                xs.append(x1 + (x2 - x1) * t)
        xs.sort()
        for i in range(0, len(xs) - 1, 2):
            for x in range(int(round(xs[i])), int(round(xs[i + 1])) + 1):
                m.add((x, y))
    return m

P = poly_mask([(42, 86), (56, 86), (59, 104), (61, 112), (35, 112), (37, 104)])
for y in (86, 90, 95, 100, 104, 108, 111):
    xs = sorted(x for (x, yy) in P if yy == y)
    print(y, (min(xs), max(xs)) if xs else None, len(xs))
