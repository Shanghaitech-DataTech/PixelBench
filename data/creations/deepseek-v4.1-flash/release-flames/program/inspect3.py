c = input_canvas
W, H = 47, 63
pal = {p['index']: p for p in c.palette()}
fireidx = set()
for idx, p in pal.items():
    r = p['rgba']
    hexs = r if isinstance(r, str) else '#%02x%02x%02x%02x' % tuple(r[:4])
    if hexs.lower() in ('#f27219ff', '#f4a30cff', '#fed32cff'):
        fireidx.add(idx)
print(fireidx)
pts = [(x, y) for y in range(H) for x in range(W) if c.get(x, y) in fireidx]
print("minx", min(p[0] for p in pts))
for y in range(H):
    xs = [x for x, yy in pts if yy == y]
    if xs:
        print(y, xs)
