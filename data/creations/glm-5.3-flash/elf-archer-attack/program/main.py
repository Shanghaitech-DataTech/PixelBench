W, H = 52, 47

# ---------------- palette (sampled from the input sprite) ----------------
K   = '#121311'   # near-black outline
KB  = '#7b4231'   # brown outline / hair shadow
A2  = '#422110'   # dark brown
HR  = '#f3f4b6'   # pale hair
HR2 = '#faf3c9'   # hair light
SK  = '#c5956a'   # skin
SK2 = '#e0c89e'   # skin light
SK3 = '#f1d8b3'   # skin lightest
GN  = '#529439'   # green cloth
GL  = '#9cde5a'   # green light
GD  = '#304915'   # green dark outline
P   = '#a9794f'   # leather
PD  = '#8e7058'   # leather dark
PO  = '#bc6c0c'   # bow wood light
PR  = '#74341c'   # bow wood dark
Y   = '#ffe75a'   # gold
M   = '#c30074'   # magenta
MK  = '#ef5ba1'   # pink
MD  = '#9e005d'   # dark magenta
MP  = '#f6adcd'   # pale pink
MDD = '#55002a'   # darkest magenta
WHT = '#ffffff'
ST  = '#f1f7f7'   # bowstring
SH  = '#17003599' # ground shadow
E   = '#3c3c3c'   # dark grey legging

# ---------------- helpers ----------------
def put(c, x, y, col):
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, col)

def stamp(c, rows, ox, oy, mp):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch != '.':
                put(c, ox + i, oy + j, mp[ch])

def tline(c, x0, y0, x1, y1, w, col):
    dx = abs(x1-x0); dy = abs(y1-y0)
    sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx - dy; x, y = x0, y0; r = (w-1)//2
    while True:
        for j in range(-r, r+1):
            for i in range(-r, r+1):
                put(c, x+i, y+j, col)
        if x == x1 and y == y1: break
        e2 = 2*err
        if e2 > -dy: err -= dy; x += sx
        if e2 < dx: err += dx; y += sy

def line_px(x0, y0, x1, y1):
    pts = []; dx = abs(x1-x0); dy = abs(y1-y0)
    sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx-dy; x, y = x0, y0
    while True:
        pts.append((x, y))
        if x == x1 and y == y1: break
        e2 = 2*err
        if e2 > -dy: err -= dy; x += sx
        if e2 < dx: err += dx; y += sy
    return pts

# ================= FRAME 1 : the original picture =================
f1 = new_canvas(W, H, background=None, name='frame1_ready')
f1.blit(input_canvas, 6, 0)

# ================= FRAME 2 : full draw =================
f2 = new_canvas(W, H, background=None, name='frame2_full_draw')

# ---- 1. ground shadow ----
f2.rect(12, 44, 22, 1, SH)
f2.rect(9, 45, 27, 1, SH)
f2.rect(12, 46, 23, 1, SH)

# ---- 2. arrow shafts (behind the quiver) ----
for (x0, y0, x1, y1) in [(6, 19, 1, 12), (9, 19, 5, 8)]:
    for (x, y) in line_px(x0, y0, x1, y1):
        put(f2, x, y, A2)

# ---- 3. quiver (magenta leather) on the lower back ----
for i in range(15):
    y = 18 + i
    cx = 9 - (3*i)//14
    for x in range(cx-3, cx+4):
        if i == 0:
            put(f2, x, y, MD)
        elif x == cx-3 or x == cx+3 or i == 14:
            put(f2, x, y, MDD)
        else:
            put(f2, x, y, M)
    if 0 < i < 14:
        put(f2, cx-1, y, MK)

# ---- 4. fletchings ----
for (cx, cy) in [(1, 12), (5, 8)]:
    put(f2, cx-1, cy-1, MK); put(f2, cx, cy-1, M); put(f2, cx+1, cy-1, MK)
    put(f2, cx-1, cy, M);   put(f2, cx, cy, MP);   put(f2, cx+1, cy, M)
    put(f2, cx, cy+1, MD)

# ---- 5. draw arm : upper arm (behind the torso) ----
tline(f2, 16, 12, 10, 10, 5, GD)
tline(f2, 16, 12, 10, 10, 3, GN)

# ---- 6. legs (wide braced stance) ----
tline(f2, 18, 25, 12, 39, 5, K)
tline(f2, 18, 25, 12, 39, 3, E)
tline(f2, 21, 25, 27, 39, 5, K)
tline(f2, 21, 25, 27, 39, 3, E)

# ---- 7. boots ----
f2.rect(9, 39, 8, 5, K);  f2.rect(10, 40, 6, 2, P); f2.rect(10, 42, 6, 1, PR)
f2.rect(25, 39, 8, 5, K); f2.rect(26, 40, 6, 2, P); f2.rect(26, 42, 6, 1, PR)

# ---- 8. neck ----
f2.rect(21, 9, 5, 2, SK)
put(f2, 20, 9, KB); put(f2, 20, 10, KB)
put(f2, 26, 9, KB); put(f2, 26, 10, KB)

# ---- 9. draw forearm (in front of the neck) ----
tline(f2, 10, 10, 24, 10, 5, GD)
tline(f2, 10, 10, 24, 10, 3, GN)

# ---- 10. torso / tunic ----
TORSO = [
    "dGGGGGGGGGd",
    "dGLGGGGGGGd",
    "dGLGGGGGGGd",
    "dGGGGGGGGGd",
    "dGGGGGGGGGd",
    "dGGGGGGGGGd",
    "dGGGGGGGGGd",
    "dGGGGGGGGGd",
    "dGGGGGGGGGd",
    "dPPPPPPPPPd",
    "dQQQQQQQQQd",
    "dEEEEEEEEEd",
    "dEEEEEEEEEd",
    "dEEEEEEEEEd",
    "dEEEEEEEEEd",
]
stamp(f2, TORSO, 14, 11, {'d': GD, 'G': GN, 'L': GL, 'P': P, 'Q': PD, 'E': E})

# ---- 11. quiver strap across the chest ----
for (x, y) in line_px(22, 11, 15, 20):
    put(f2, x, y, PD)
    put(f2, x, y+1, PR)

# ---- 12. bowstring, pulled back to the jaw ----
for (x, y) in line_px(34, 1, 24, 11):
    put(f2, x, y, ST)
for (x, y) in line_px(24, 11, 31, 38):
    put(f2, x, y, ST)

# ---- 13. bow, fully open ----
UPPER = [(34,1),(35,2),(35,3),(36,4),(36,5),(37,6),(37,7),(37,8),
         (38,9),(38,10),(38,11),(39,12),(39,13),(39,14),(40,15)]
LOWER = [(40,22),(39,23),(39,24),(39,25),(38,26),(38,27),(38,28),
         (37,29),(37,30),(37,31),(36,32),(36,33),(35,34),(34,35),
         (34,36),(33,37),(32,38),(31,38)]
for (x, y) in UPPER + LOWER:
    put(f2, x, y, K)
    put(f2, x+1, y, Y)
    put(f2, x+2, y, KB)
for y in range(15, 23):
    put(f2, 40, y, K); put(f2, 41, y, PD); put(f2, 42, y, PR)

# ---- 14. bow arm : locked straight forward ----
tline(f2, 24, 13, 39, 18, 5, GD)
tline(f2, 24, 13, 39, 18, 3, GN)

# ---- 15. head, profile facing right ----
HEAD = [
    "....bHHHHb....",
    "..bHHHHHHb....",
    "..bHHHHHSSSb..",
    ".bHHHHHSSSSSb.",
    ".bHHHHSSSSSSSb",
    ".bHHHSSSSSSSSb",
    "..bHHSSSSSSb..",
    "...bHSSSSSSb..",
    "....bSSSSb....",
]
stamp(f2, HEAD, 16, 0, {'b': KB, 'H': HR, 'S': SK})
put(f2, 26, 4, K)       # eye
put(f2, 26, 7, A2)      # mouth
# pointed ear
put(f2, 16, 4, SK2); put(f2, 16, 5, SK); put(f2, 17, 5, SK); put(f2, 17, 6, SK)
put(f2, 15, 4, KB); put(f2, 15, 5, KB); put(f2, 16, 6, KB)

# ---- 16. hands ----
# draw fist anchored at the jaw
for x in range(22, 27):
    put(f2, x, 9, SK)
for y in (10, 11, 12):
    put(f2, 22, y, K); put(f2, 23, y, SK); put(f2, 24, y, SK2)
    put(f2, 25, y, SK); put(f2, 26, y, K)
for x in range(22, 27):
    put(f2, x, 13, SK)
put(f2, 22, 9, K); put(f2, 26, 9, K)
put(f2, 22, 13, K); put(f2, 26, 13, K)
# bow fist wrapped around the grip
put(f2, 39, 15, K); put(f2, 40, 15, SK); put(f2, 41, 15, K)
for y in (16, 17, 18, 19, 20):
    put(f2, 38, y, K); put(f2, 39, y, SK); put(f2, 40, y, SK2)
    put(f2, 41, y, SK); put(f2, 42, y, K)
put(f2, 39, 21, K); put(f2, 40, 21, SK); put(f2, 41, 21, K)

print("F1:", f1.stats_text())
print("F2:", f2.stats_text())
finish([f1, f2])
