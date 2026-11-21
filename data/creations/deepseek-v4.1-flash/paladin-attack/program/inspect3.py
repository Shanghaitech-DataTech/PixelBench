import colorsys
c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}

def sym(i):
    r,g,b,a = pal[i]
    if a == 0: return '.'
    if a < 255: return '#'   # ground shadow
    mx = max(r,g,b); mn = min(r,g,b)
    v = mx/255
    s = 0 if mx==0 else (mx-mn)/mx
    h,_,_ = colorsys.rgb_to_hsv(r/255,g/255,b/255)
    h *= 360
    if s < 0.15:
        # grey
        if v < 0.15: return '@'
        if v < 0.35: return 'D'
        if v < 0.62: return 'G'
        if v < 0.85: return 'g'
        return 'W'
    if h < 20 or h >= 340:   # red/pink-magenta
        return 'P' if v > 0.6 else 'p'
    if h < 45:               # orange/brown
        return 'B' if v > 0.5 else 'b'
    if h < 70:               # gold/yellow
        return 'Y' if v > 0.6 else 'y'
    if h < 170:              # green
        return 'E'
    if h < 260:              # blue
        return 'U'
    return 'M'               # magenta/purple

rows = []
for y in range(61):
    rows.append(''.join(sym(c.get(x,y)) for x in range(43)))
for y,r in enumerate(rows):
    print('%2d %s' % (y, r))
# legend
seen = {}
for y in range(61):
    for x in range(43):
        i = c.get(x,y)
        seen.setdefault(sym(i), set()).add(i)
for k,v in sorted(seen.items()):
    print(k, sorted(v), [pal[i] for i in sorted(v)])
