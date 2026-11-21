base = input_canvas
W, H = 66, 119

HEX = {
 'b':'#050100','c':'#a8b2c1','d':'#545665','e':'#e0f4fa','f':'#fdd5b7',
 'g':'#290e02','h':'#767b90','i':'#421603','j':'#ffffff','k':'#281820',
 'l':'#160701','m':'#eaa377','n':'#9e3e37','o':'#d28560','p':'#5f1f04',
 'q':'#792806','r':'#fbece6','s':'#f2f8f9','t':'#0b2139','u':'#293d4b',
 'v':'#492544','w':'#50d4ec','x':'#5187b3'}
I = {n: base.color(v) for n, v in HEX.items()}
TRANS = base.color((0, 0, 0, 0))
SKIN = {I[n] for n in 'fmonsuvwxk'}
SKIN_OUT = SKIN - {I['k']}
K = I['k']

def snap(c, x0, x1, y0, y1):
    return [[c.get(x, y) for x in range(x0, x1 + 1)] for y in range(y0, y1 + 1)]

def make_turn(near_left, name):
    """near_left=True: character turned to ITS left -> near cheek is viewer-left,
    features shift toward viewer-right. near_left=False: mirrored."""
    f = base.copy(name=name)
    # 1) hide the far ear (opposite side of the turn direction), incl. its tip
    xs = range(50, 66) if near_left else range(0, 16)
    for y in range(33, 47):
        for x in xs:
            if f.get(x, y) in SKIN:
                f.set(x, y, None)
    # 2) outline the newly exposed far silhouette edge where it is skin
    for y in range(33, 47):
        rng = range(65, 29, -1) if near_left else range(0, 36)
        edge = None
        for x in rng:
            if f.get(x, y) != TRANS:
                edge = x
                break
        if edge is None:
            continue
        ex = edge + 1 if near_left else edge - 1
        if 0 <= ex < W and f.get(ex, y) == TRANS and f.get(edge, y) in SKIN_OUT:
            f.set(ex, y, K)
    # 3) yaw warp of the head (rows 0..49, neck stays put) inside band x 9..56:
    #    near half of the face expands, far half compresses, midline shifts
    #    toward the side the character now faces.
    B0, B1 = 9, 56
    C = 32.5
    shift = 7.0
    sn = snap(f, B0, B1, 0, 49)
    for y in range(50):
        row = sn[y]
        for t in range(B0, B1 + 1):
            if near_left:
                if t <= C + shift:
                    s = B0 + (t - B0) * (C - B0) / (C + shift - B0)
                else:
                    s = C + (t - C - shift) * (B1 - C) / (B1 - C - shift)
            else:
                if t >= C - shift:
                    s = C + (t - C + shift) * (B1 - C) / (B1 - C + shift)
                else:
                    s = B0 + (t - B0) * (C - B0) / (C - shift - B0)
            s = max(B0, min(B1, int(round(s))))
            f.set(t, y, row[s - B0])
    return f

def make_rear(name):
    """Rear view: every skin pixel of the head/neck is replaced by continuing
    hair texture (donor rows taken from the hair above so strands flow).
    Ears stay. Then the whole view is mirrored, because the long hair that
    falls over the character's left shoulder appears on the viewer's left
    when the character is seen from directly behind."""
    f = base.copy(name=name)
    for y in range(24, 55):
        for x in range(16, 50):
            if f.get(x, y) in SKIN:
                yd = y - 22 if y - 22 <= 23 else y - 31
                f.set(x, y, f.get(x, yd))
    f.mirror(axis="h")
    return f

f1 = make_turn(True, 'f1_quarter_left')
f2 = make_turn(False, 'f2_quarter_right')
f3 = make_rear('f3_rear')

for f in (f1, f2, f3):
    print(f.stats_text())
    print(f.matrix_text(region=(0, 22, 65, 54)))
    print('=' * 72)

finish([f1, f2, f3])
