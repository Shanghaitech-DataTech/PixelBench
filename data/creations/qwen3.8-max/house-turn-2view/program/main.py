import math
from pixelbench_api import *

# palette (matched to input)
OUT = '#161C2E'   # dark outline
WD  = '#6C513A'   # dark wood
WM  = '#97763D'   # mid wood / thatch seam
TAN = '#BDA759'   # tan (ridge / shaded thatch)
BR  = '#98694E'   # door brown
GOLD= '#DCAA46'   # lit thatch gold
PALE= '#F9E279'   # pale yellow (window glow / arch hi)
YEL = '#E1D968'   # yellow arch trim
GT  = '#BBAE93'   # grey-tan shade
CR  = '#E1DCA3'   # cream wall
SH  = (22, 28, 46, 69)  # soft ground shadow

# house dims (world units)
W, D, H, R = 60, 80, 44, 38      # width, depth, wall height, roof rise
OV, FT, RW, RR = 5, 6, 3, 2      # roof overhang, fascia thk, ridge half-width, ridge raise
E = math.radians(45)             # fixed camera elevation (high angle)
SE, CE = math.sin(E), math.cos(E)
L = math.hypot(W / 2, R)
UX, UZ = (W / 2) / L, -R / L
EX, EZ = W / 2 + OV * UX, H + OV * UZ

def rot(p, th):
    x, y, z = p
    a = math.radians(th)
    ca, sa = math.cos(a), math.sin(a)
    return (x * ca - y * sa, x * sa + y * ca, z)

def proj(p, th):
    x, y, z = rot(p, th)
    return (x, -(y * SE + z * CE))

def nvis(n, th):
    nx, ny, nz = n
    a = math.radians(th)
    ca, sa = math.cos(a), math.sin(a)
    nx2, ny2 = nx * ca - ny * sa, nx * sa + ny * ca
    return ny2 * (-CE) + nz * SE > 0.01

def depth(pts, th):
    s = 0.0
    for p in pts:
        x, y, z = rot(p, th)
        s += y * CE - z * SE
    return s / len(pts)

def tline(cv, a, b, col, t=1):
    x0, y0 = a; x1, y1 = b
    cv.line(x0, y0, x1, y1, col)
    for i in range(1, t):
        if abs(x1 - x0) >= abs(y1 - y0):
            cv.line(x0, y0 + i, x1, y1 + i, col)
        else:
            cv.line(x0 + i, y0, x1 + i, y1, col)

def oline(cv, pts, col, t=1):
    n = len(pts)
    for i in range(n):
        tline(cv, pts[i], pts[(i + 1) % n], col, t)

def arcpts(cu, cv_, spring, r, n=8):
    # semicircle in wall coords (u,v): from (cu+r, spring) to (cu-r, spring)
    out = []
    for i in range(n + 1):
        a = math.pi * i / n
        out.append((cu + r * math.cos(a), cv_, spring + r * math.sin(a)))
    return out

def wall3(side, u, v):
    # wall-local (u along wall, v up) -> world
    if side == 'F':
        return (u, 0, v)
    if side == 'E':
        return (W / 2, u, v)
    if side == 'W':
        return (-W / 2, D - u, v)
    return (u, D, v)

def build_frame(th):
    items = []  # (group, depth, op)  op = ('fill', pts2d, col) | ('oline', pts2d, col, t) | ('tline', a2d, b2d, col, t)
    P = lambda p: proj(p, th)

    def add(g, dp, op):
        items.append((g, dp, op))

    def fp(pts3):
        return [P(p) for p in pts3]

    # ground shadow
    shp = []
    for i in range(24):
        a = 2 * math.pi * i / 24
        shp.append((math.cos(a) * (W / 2 + 14), D / 2 + math.sin(a) * (D / 2 + 12), 0))
    add(0, 999, ('fill', fp(shp), SH))

    # ---- walls ----
    # front (gable) wall
    front = [(-W/2,0,0),(W/2,0,0),(W/2,0,H),(0,0,H+R),(-W/2,0,H)]
    if nvis((0,-1,0), th):
        dp = depth(front, th)
        add(1, dp, ('fill', fp(front), CR))
        add(1, dp, ('fill', fp([wall3('F', W/2-7, 2), wall3('F', W/2, 2), wall3('F', W/2, H), wall3('F', W/2-7, H)]), GT))
        # arch trim + door
        arch_o = [wall3('F',-13,0), wall3('F',13,0), wall3('F',13,16)] + [wall3('F',u,v) for (u,_,v) in arcpts(0,0,16,13)[1:-1]] + [wall3('F',-13,16)]
        add(1, dp, ('fill', fp(arch_o), YEL))
        arch_i = [wall3('F',-11,0), wall3('F',11,0), wall3('F',11,16)] + [wall3('F',u,v) for (u,_,v) in arcpts(0,0,16,11)[1:-1]] + [wall3('F',-11,16)]
        add(1, dp, ('fill', fp(arch_i), PALE))
        door = [wall3('F',-9,0), wall3('F',9,0), wall3('F',9,14)] + [wall3('F',u,v) for (u,_,v) in arcpts(0,0,14,9)[1:-1]] + [wall3('F',-9,14)]
        add(1, dp, ('fill', fp(door), BR))
        for u in (-5, 0, 5):
            add(1, dp, ('tline', P(wall3('F',u,1)), P(wall3('F',u,13)), WD, 1))
        add(1, dp, ('fill', fp([wall3('F',-9,5), wall3('F',9,5), wall3('F',9,8), wall3('F',-9,8)]), GOLD))
        add(1, dp, ('fill', fp([wall3('F',-9,10), wall3('F',9,10), wall3('F',9,12), wall3('F',-9,12)]), GOLD))
        add(1, dp, ('oline', fp(door), OUT, 1))
        add(1, dp, ('oline', fp(arch_o), OUT, 2))
        add(1, dp, ('oline', fp(front), OUT, 1))
    # east wall (window side)
    east = [(W/2,0,0),(W/2,D,0),(W/2,D,H),(W/2,0,H)]
    if nvis((1,0,0), th):
        dp = depth(east, th)
        add(1, dp, ('fill', fp(east), CR))
        add(1, dp, ('fill', fp([wall3('E',0,2), wall3('E',5,2), wall3('E',5,H), wall3('E',0,H)]), GT))
        add(1, dp, ('fill', fp([wall3('E',0,H-3), wall3('E',D,H-3), wall3('E',D,H), wall3('E',0,H)]), GT))
        for u0 in (16, 46):
            add(1, dp, ('fill', fp([wall3('E',u0-1,13), wall3('E',u0+13,13), wall3('E',u0+13,29), wall3('E',u0-1,29)]), OUT))
            add(1, dp, ('fill', fp([wall3('E',u0+1,15), wall3('E',u0+11,15), wall3('E',u0+11,27), wall3('E',u0+1,27)]), PALE))
            add(1, dp, ('tline', P(wall3('E',u0+6,15)), P(wall3('E',u0+6,27)), OUT, 1))
            add(1, dp, ('tline', P(wall3('E',u0+1,21)), P(wall3('E',u0+11,21)), OUT, 1))
            add(1, dp, ('fill', fp([wall3('E',u0-2,29), wall3('E',u0+14,29), wall3('E',u0+14,31), wall3('E',u0-2,31)]), TAN))
        add(1, dp, ('oline', fp(east), OUT, 1))
    # west wall (shaded)
    west = [(-W/2,0,0),(-W/2,D,0),(-W/2,D,H),(-W/2,0,H)]
    if nvis((-1,0,0), th):
        dp = depth(west, th)
        add(1, dp, ('fill', fp(west), GT))
        add(1, dp, ('oline', fp(west), OUT, 1))
    back = [(-W/2,D,0),(W/2,D,0),(W/2,D,H),(0,D,H+R),(-W/2,D,H)]
    if nvis((0,1,0), th):
        dp = depth(back, th)
        add(1, dp, ('fill', fp(back), GT))
        add(1, dp, ('oline', fp(back), OUT, 1))

    # ---- roof planes ----
    roofE = [(EX,-OV,EZ),(EX,D+OV,EZ),(0,D+OV,H+R),(0,-OV,H+R)]
    if nvis((R,0,W/2), th):
        dp = depth(roofE, th)
        add(2, dp, ('fill', fp(roofE), GOLD))
        for y in range(0, D + 1, 7):
            add(2, dp, ('tline', P((0,y,H+R)), P((EX,y,EZ)), WM, 1))
        for y in (6, 20, 34, 48, 62):
            p0 = (0 + (EX-0)*0.15, y, H+R + (EZ-H-R)*0.15)
            p1 = (0 + (EX-0)*0.55, y, H+R + (EZ-H-R)*0.55)
            add(2, dp, ('tline', P(p0), P(p1), PALE, 1))
        f = 0.68
        pe = (EX*f, -OV, H+R + (EZ-H-R)*f)
        pe2 = (EX*f, D+OV, H+R + (EZ-H-R)*f)
        add(2, dp, ('tline', P(pe), P(pe2), WM, 1))
        add(2, dp, ('oline', fp(roofE), OUT, 2))
    roofW = [(-EX,-OV,EZ),(-EX,D+OV,EZ),(0,D+OV,H+R),(0,-OV,H+R)]
    if nvis((-R,0,W/2), th):
        dp = depth(roofW, th)
        add(2, dp, ('fill', fp(roofW), TAN))
        for y in range(0, D + 1, 7):
            add(2, dp, ('tline', P((0,y,H+R)), P((-EX,y,EZ)), WM, 1))
        for y in (10, 38, 66):
            p0 = (-EX*0.2, y, H+R + (EZ-H-R)*0.2)
            p1 = (-EX*0.6, y, H+R + (EZ-H-R)*0.6)
            add(2, dp, ('tline', P(p0), P(p1), GOLD, 1))
        add(2, dp, ('oline', fp(roofW), OUT, 2))

    # ---- trim: eave + rake boards ----
    dpt = 0.0
    add(3, dpt, ('tline', P((EX,-OV,EZ)), P((EX,D+OV,EZ)), WM, 3))
    add(3, dpt, ('tline', P((-EX,-OV,EZ)), P((-EX,D+OV,EZ)), WM, 3))
    add(3, dpt, ('tline', P((EX,-OV,EZ)), P((0,-OV,H+R)), WM, 3))
    add(3, dpt, ('tline', P((-EX,-OV,EZ)), P((0,-OV,H+R)), WM, 3))
    add(3, dpt, ('tline', P((EX,D+OV,EZ)), P((0,D+OV,H+R)), WM, 2))
    add(3, dpt, ('tline', P((-EX,D+OV,EZ)), P((0,D+OV,H+R)), WM, 2))

    # ---- ridge ----
    ridge = [(-RW,-OV-2,H+R+RR),(RW,-OV-2,H+R+RR),(RW,D+OV+2,H+R+RR),(-RW,D+OV+2,H+R+RR)]
    dpr = depth(ridge, th)
    add(4, dpr, ('fill', fp(ridge), TAN))
    add(4, dpr, ('tline', P((-1,-OV-2,H+R+RR)), P((-1,D+OV+2,H+R+RR)), WD, 1))
    add(4, dpr, ('tline', P((2,-OV-2,H+R+RR)), P((2,D+OV+2,H+R+RR)), WM, 1))
    add(4, dpr, ('oline', fp(ridge), OUT, 1))

    items.sort(key=lambda it: (it[0], -it[1]))
    return items

def bbox_of(items):
    xs = []; ys = []
    for _, _, op in items:
        pts = op[1] if op[0] != 'tline' else [op[1], op[2]]
        for (x, y) in pts:
            xs.append(x); ys.append(y)
    return min(xs), min(ys), max(xs), max(ys)

frames = {}
for th, nm in ((-45, 'f45'), (-90, 'f90')):
    frames[nm] = build_frame(th)

bbs = {nm: bbox_of(it) for nm, it in frames.items()}
cw = int(max(b[2] - b[0] for b in bbs.values())) + 10
ch = int(max(b[3] - b[1] for b in bbs.values())) + 10
print('canvas', cw, ch, bbs)

outs = []
for nm, th in (('f45', -45), ('f90', -90)):
    cv = new_canvas(cw, ch, name=nm)
    x0, y0, x1, y1 = bbs[nm]
    ox = (cw - (x1 - x0)) / 2 - x0
    oy = (ch - (y1 - y0)) / 2 - y0
    for _, _, op in frames[nm]:
        if op[0] == 'fill':
            cv.poly([(round(x + ox), round(y + oy)) for (x, y) in op[1]], op[2], True)
        elif op[0] == 'oline':
            oline(cv, [(round(x + ox), round(y + oy)) for (x, y) in op[1]], op[2], op[3])
        else:
            tline(cv, (round(op[1][0] + ox), round(op[1][1] + oy)), (round(op[2][0] + ox), round(op[2][1] + oy)), op[3], op[4])
    outs.append(cv)

view(outs[0])
view(outs[1])
finish(outs)
