exec(compile(open('main.py').read(), 'main.py', 'exec'), globals())

pal = {p['index']: p for p in f2.palette()}
def hexs(v):
    r = pal[v]['rgba']
    return r.lower() if isinstance(r, str) else '#%02x%02x%02x%02x' % tuple(r[:4])

FIRE = {'#b0300eff', '#f27219ff', '#f4a30cff', '#fed32cff', '#fff3b0ff'}
fire = set()
for y in range(72):
    for x in range(100):
        v = f2.get(x, y)
        if v is not None and hexs(v) in FIRE:
            fire.add((x, y))

seen = set()
comps = []
for p in sorted(fire):
    if p in seen:
        continue
    stack = [p]; comp = []
    seen.add(p)
    while stack:
        cx, cy = stack.pop()
        comp.append((cx, cy))
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                q = (cx + dx, cy + dy)
                if q in fire and q not in seen:
                    seen.add(q); stack.append(q)
    comps.append(comp)
comps.sort(key=len, reverse=True)
for c in comps:
    xs = [p[0] for p in c]; ys = [p[1] for p in c]
    print(len(c), 'bbox', min(xs), min(ys), max(xs), max(ys))

print()
print("fire pixel rows (x ranges):")
for y in range(72):
    xs = sorted(x for x, yy in fire if yy == y)
    if xs:
        segs = []
        s = xs[0]; prev = xs[0]
        for x in xs[1:]:
            if x != prev + 1:
                segs.append((s, prev)); s = x
            prev = x
        segs.append((s, prev))
        print(y, segs)
