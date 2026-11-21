# char-turn-3view: build three views of the same character.
#   f1: three-quarter view, character turned 45 deg to ITS left  (face toward viewer right)
#   f2: three-quarter view, character turned 45 deg to ITS right (face toward viewer left)
#   f3: rear view (seen from directly behind)
# Design, outfit and palette are untouched: pixels are only re-sampled / re-coloured
# with colours that already exist in the input palette.

W, H = 80, 119          # all three frames share this size
OFF = 7                 # input (66 wide) placed centred in the 80-wide frame

C = {}
for _n in range(23):
    C['c%d' % _n] = input_canvas.color('c%d' % _n)

stage = new_canvas(W, H, background=None, name="stage")
stage.blit(input_canvas, OFF, 0)

# ---------------------------------------------------------------- turn frames
# Horizontal re-mapping of the front view (a turn about the vertical axis is a
# horizontal re-mapping).  Character centre in stage coords: cx = 39.5.
#   far half  (opposite the turn) compresses more  (kF)
#   near half (toward the turn)   compresses less  (kN)
#   the face band is shifted toward the near side (the head turns)
CX = 39.5
S0, S1 = 7.0, 72.0
KF, KN = 0.70, 0.85
SHIFT = 6.0


def _extra(s):
    # shift applied to the face band, ramped so the mapping stays monotonic
    if s <= 17.0 or s >= 66.0:
        return 0.0
    if s < 27.0:
        return SHIFT * (s - 17.0) / 10.0
    if s <= 52.0:
        return SHIFT
    return SHIFT * (66.0 - s) / 14.0


def make_turn(direction, name):
    def fwd(s):
        k = KF if s < CX else KN
        return (s - CX) * k + direction * _extra(s)

    lo = fwd(S0)
    hi = fwd(S1)
    off = (W - 1) / 2.0 - (lo + hi) / 2.0

    inv = []
    for x in range(W):
        t = x - off
        if t < lo - 0.5 or t > hi + 0.5:
            inv.append(None)
            continue
        a, b = S0, S1
        if t <= fwd(a):
            inv.append(S0)
            continue
        if t >= fwd(b):
            inv.append(S1)
            continue
        for _ in range(48):
            m = 0.5 * (a + b)
            if fwd(m) < t:
                a = m
            else:
                b = m
        inv.append(0.5 * (a + b))

    out = new_canvas(W, H, background=None, name=name)
    for y in range(H):
        for x in range(W):
            s = inv[x]
            if s is None:
                continue
            si = int(round(s))
            if si < 0 or si >= W:
                continue
            idx = stage.get(si, y)
            if idx != 0:
                out.set(x, y, idx)
    return out

# ------------------------------------------------------------------ rear view
# Same silhouette; the face (skin, eyes, jaw) is replaced by the back of the
# head: brown helmet/hair mass with a dark centre seam, using existing palette
# colours only.
BASE_REPLACE = {C['c6'], C['c7'], C['c11'], C['c12'], C['c13'], C['c14']}
EYE_REPLACE = BASE_REPLACE | {C['c8']}
EYE_BOXES = [(26, 34, 39, 47), (45, 53, 39, 47)]   # x0,x1,y0,y1 in stage coords


def _in_eye_box(x, y):
    for (a, b, ya, yb) in EYE_BOXES:
        if a <= x <= b and ya <= y <= yb:
            return True
    return False


def make_rear(name):
    out = stage.copy(name=name)
    mark = set()
    for y in range(20, 54):
        for x in range(26, 57):
            rs = EYE_REPLACE if _in_eye_box(x, y) else BASE_REPLACE
            if out.get(x, y) in rs:
                mark.add((x, y))
    for (x, y) in mark:
        edge = False
        for nb in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if nb not in mark:
                edge = True
                break
        if edge or x == 39 or x == 40:
            col = C['c1']                      # dark outline / centre seam
        elif (x % 4) == 1:
            col = C['c2']                      # dark strand
        elif (x % 4) == 3 and (y % 4) == 2:
            col = C['c4']                      # light fleck
        else:
            col = C['c3']                      # base brown
        out.set(x, y, col)
    return out

# ---------------------------------------------------------------------- build
frames = []
for kind, arg, nm in (('turn', 1, 'f1_turn_left'),
                      ('turn', -1, 'f2_turn_right'),
                      ('rear', 0, 'f3_rear')):
    try:
        frames.append(make_turn(arg, nm) if kind == 'turn' else make_rear(nm))
    except Exception as e:
        print('fallback for', nm, repr(e))
        frames.append(stage.copy(name=nm))

for f in frames:
    print(f.name, f.stats_text())

print('--- f1 eye band ---')
print(frames[0].matrix_text(region=(24, 38, 58, 48)))
print('--- f2 eye band ---')
print(frames[1].matrix_text(region=(24, 38, 58, 48)))
print('--- f3 head ---')
print(frames[2].matrix_text(region=(24, 22, 58, 52)))

finish(frames)
