import sys
c = input_canvas
W, H = 47, 63
pal = {p['index']: p for p in c.palette()}

def transp(idx):
    if idx is None:
        return True
    rgba = pal[idx]['rgba']
    if isinstance(rgba, str):
        return rgba[-2:].lower() == '00'
    return len(rgba) > 3 and rgba[3] == 0

print("size", W, H)
# fire colored pixels location
fire = []
for y in range(H):
    for x in range(W):
        v = c.get(x, y)
        if transp(v):
            continue
        rgba = pal[v]['rgba']
        hexs = rgba if isinstance(rgba, str) else '#%02x%02x%02x%02x' % tuple(rgba[:4])
        if hexs.lower() in ('#f27219ff', '#f4a30cff', '#fed32cff'):
            fire.append((x, y, hexs))
print("fire pixel count", len(fire))
if fire:
    xs = [f[0] for f in fire]; ys = [f[1] for f in fire]
    print("fire bbox", min(xs), min(ys), max(xs), max(ys))
# per-row extents of opaque
for y in range(H):
    row = [x for x in range(W) if not transp(c.get(x, y))]
    if row:
        # find gaps
        segs = []
        s = row[0]; prev = row[0]
        for x in row[1:]:
            if x != prev + 1:
                segs.append((s, prev)); s = x
            prev = x
        segs.append((s, prev))
        print(y, segs)
print(pal[0], pal[1])
