c = input_canvas
W, H = c.stats()['size']

HEX = {}
for p in c.palette():
    HEX[p['index']] = '#%02x%02x%02x' % tuple(p['rgba'][:3])
def idx(h):
    for k, v in HEX.items():
        if v == h:
            return k
    raise KeyError(h)

SKIN = set(idx(h) for h in ('#fdd5b7', '#eaa377', '#d28560'))
EYE = set(idx(h) for h in ('#50d4ec', '#f2f8f9', '#5187b3', '#293d4b'))
HAIR = [idx(h) for h in ('#050100', '#160701', '#290e02', '#421603', '#5f1f04', '#792806')]
HAIRSET = set(HAIR)
J_DARK = idx('#281820')
K_RED = idx('#9e3e37')

RAMP = {}
for a, b in (('#ffffff', '#e0f4fa'), ('#e0f4fa', '#a8b2c1'), ('#a8b2c1', '#767b90'),
             ('#767b90', '#545665'), ('#fbece6', '#f2f8f9'), ('#f2f8f9', '#a8b2c1'),
             ('#fdd5b7', '#eaa377'), ('#eaa377', '#d28560'), ('#d28560', '#9e3e37'),
             ('#50d4ec', '#5187b3'), ('#5187b3', '#293d4b'), ('#293d4b', '#281820'),
             ('#792806', '#5f1f04'), ('#5f1f04', '#421603'), ('#421603', '#290e02'),
             ('#290e02', '#160701'), ('#160701', '#050100'), ('#9e3e37', '#281820')):
    RAMP[idx(a)] = idx(b)

src = [[c.get(x, y) for x in range(W)] for y in range(H)]
CX = 32.5

# ------------------------------------------------------- frame 1: 3/4 view
def three_quarter(name, kn=1.0, kf=0.58, rim=3):
    """Turn the character 45 deg to its own left: its left side (viewer's
    right) is foreshortened, the near side keeps its full width."""
    out = new_canvas(W, H, name=name)
    total = CX * (kn + kf)
    off = round((W - 1 - total) / 2.0)
    for y in range(H):
        rmax = -1
        for x in range(W):
            d = x - off
            if d < 0 or d > total:
                continue
            s = d / kn if d <= CX * kn else CX + (d - CX * kn) / kf
            sx = int(round(s))
            if 0 <= sx < W:
                v = src[y][sx]
                if v != 0:
                    out.set(x, y, v)
                    rmax = x
        for x in range(rmax - rim + 1, rmax + 1):
            if x < 0:
                continue
            v = out.get(x, y)
            if v in RAMP:
                out.set(x, y, RAMP[v])
    return out

f1 = three_quarter('f1')
f2 = f1.copy(name='f2')
f2.mirror('h')

# ------------------------------------------------------- frame 3: rear view
def hair_tone(y, d, rad):
    """volumetric shading of the back of the head: the same brown ramp the
    sprite already uses for its hair, lighter at the crown and the centre,
    darker towards the rim and the nape, with faint vertical strand breaks"""
    if y <= 32:
        base = 3
    elif y <= 42:
        base = 2
    else:
        base = 1
    t = d / max(rad, 1.0)
    extra = 0 if t < 0.42 else (1 if t < 0.78 else 2)
    if t < 0.78 and int(round(d)) % 6 == 0:
        extra += 1
    return HAIR[max(0, min(len(HAIR) - 1, base - extra))]

def rear_view(name):
    out = c.copy(name=name)
    out.mirror('h')

    # --- back of the head: face replaced by the hair mass
    for y in range(24, 52):
        rad = 0.0
        for x in range(W):
            if src[y][x] in SKIN or src[y][x] in EYE:
                rad = max(rad, abs(x - CX))
        if rad <= 0:
            continue
        lo, hi = int(CX - rad) - 2, int(CX + rad) + 3
        for x in range(max(0, lo), min(W, hi)):
            v = out.get(x, y)
            if v in HAIRSET:
                continue
            kill = (v in SKIN or v in EYE or v == J_DARK or (v == K_RED and y <= 46))
            if not kill:
                continue
            col = hair_tone(y, abs(x - CX), rad)
            out.set(x, y, col)

    # --- neck / chest skin becomes hair falling down the back
    for y in range(52, 74):
        x = 0
        while x < W:
            if out.get(x, y) in SKIN:
                x0 = x
                while x < W and out.get(x, y) in SKIN:
                    x += 1
                x1 = x - 1
                if x0 - 1 <= CX <= x1 + 1:
                    for xx in range(x0, x1 + 1):
                        out.set(xx, y, HAIR[1] if y > 58 else HAIR[2])
            else:
                x += 1
    return out

f3 = rear_view('f3')

def show(canv, label, step=2, y0=0, y1=None):
    y1 = H if y1 is None else y1
    used = sorted(set(canv.get(x, y) for y in range(y0, y1) for x in range(W)))
    chars = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
    L = {k: chars[i] for i, k in enumerate(used)}
    print("==", label, {L[k]: HEX.get(k, 'tr') for k in used})
    for y in range(y0, y1, step):
        row = ''.join(L[canv.get(x, y)] if canv.get(x, y) != 0 else '.' for x in range(0, W, step))
        print(f"{y:3d} {row}")

show(f1, 'f1 3/4 left', step=2)
show(f1, 'f1 head', step=1, y0=28, y1=54)
show(f3, 'f3 rear', step=2)
for f in (f1, f2, f3):
    print(f.stats_text())
save('turn3view_f1', f1)
save('turn3view_f2', f2)
save('turn3view_f3', f3)
finish([f1, f2, f3])
