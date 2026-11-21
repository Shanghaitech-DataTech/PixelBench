src = input_canvas
out = src.copy(name='output')
pal = out.palette()
BG = (252, 252, 252)

# ---- silhouette of the original drawing (for reference / clamping) ----
span = {}
for y in range(64):
    xs = [x for x in range(64) if tuple(pal[out.get(x, y)]['rgba'][:3]) != BG]
    span[y] = (min(xs), max(xs)) if xs else None

# ---- chocolate tones ----
BASE = out.color('#5d3a41', name='choco_base')    # chocolate body
LIGHT = out.color('#95524c', name='choco_light')  # lit chocolate
DARK = out.color('#43242c', name='choco_dark')    # shadow side

cap = {}     # y -> set(x) : melted layer over the cone
tongue = {}  # y -> set(x) : dripping tongues


def add(d, y, a, b=None):
    if b is None:
        b = a
    s = d.setdefault(y, set())
    for x in range(a, b + 1):
        s.add(x)


# ---- melted chocolate layer over the top of the cone ----
for y in range(33, 37):
    add(cap, y, 20, 41)

# ---- dripping tongues ----
# D1 : short drip, left side
add(tongue, 37, 21, 24)          # pooling shoulder
for y in (38, 39):
    add(tongue, y, 22, 24)
add(tongue, 40, 22, 23)
add(tongue, 41, 23)

# D2 : long drip - runs down the middle to the tip and hangs off it
add(tongue, 37, 28, 33)          # pooling shoulder
for y in range(38, 45):
    add(tongue, y, 29, 32)
for y in (45, 46):
    add(tongue, y, 28, 32)       # swollen bead
for y in (47, 48, 49, 50):
    add(tongue, y, 29, 31)
for y in range(51, 54):
    add(tongue, y, 28, 31)
for y in range(54, 59):
    add(tongue, y, 30, 31)       # neck over the tip
for y in range(59, 62):
    add(tongue, y, 29, 32)       # rounded drop hanging off the tip
add(tongue, 62, 30, 31)

# D3 : medium drip, right side
add(tongue, 37, 36, 39)          # pooling shoulder
for y in range(38, 41):
    add(tongue, y, 36, 38)
for y in (41, 42, 43):
    add(tongue, y, 37, 38)

# ---- paint ----
for y, xs in cap.items():
    for x in xs:
        out.set(x, y, BASE)
    out.set(41, y, LIGHT)        # lit right-hand edge of the coating

for y, xs in tongue.items():
    run = sorted(xs)
    start = 0
    for i in range(1, len(run) + 1):
        if i == len(run) or run[i] != run[i - 1] + 1:
            a, b = run[start], run[i - 1]
            for x in range(a, b + 1):
                out.set(x, y, BASE)
            if b - a + 1 >= 3:
                out.set(a, y, DARK)      # shaded left side
                out.set(b, y, LIGHT)     # lit right side
            start = i

# ---- diff check: only the cone area should change ----
changed = []
for y in range(64):
    for x in range(64):
        if out.get(x, y) != src.get(x, y):
            changed.append((x, y))
if changed:
    print('changed pixels: %d, bbox x %d-%d y %d-%d' % (
        len(changed),
        min(p[0] for p in changed), max(p[0] for p in changed),
        min(p[1] for p in changed), max(p[1] for p in changed)))
else:
    print('no changes!')

print(out.stats_text())
pal2 = out.palette()
for y in range(28, 64):
    line = ''
    for x in range(14, 50):
        i = out.get(x, y)
        r, g, b, a = pal2[i]['rgba']
        if (r, g, b) == BG:
            line += '.'
        elif (r, g, b) == (93, 58, 65):
            line += '#'
        elif (r, g, b) == (149, 82, 76):
            line += '*'
        elif (r, g, b) == (67, 36, 44):
            line += '@'
        else:
            line += '-'
    print('%2d %s' % (y, line))

save('melting-icecream', out)
finish(out)
