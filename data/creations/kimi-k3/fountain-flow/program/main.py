import math, random

random.seed(7)

W, H = 96, 92
out = new_canvas(W, H, background=None, name="output")
DX = (W - 64) // 2   # 16
out.blit(input_canvas, DX, 0)

# water colours (original c5/c6 reused; two brighter accents added)
out.color('#1d8baa', name='wdark')
out.color('#2ec7dc', name='wmid')
out.color('#6fdcec', name='wlite')
out.color('#c9f7fc', name='wspark')

# ---------------- streaming columns ----------------
def col(x, y0, y1, drift=0.0, phase=0.0, ww=0.0):
    cx = x + DX
    n = int(y1 - y0 + 1)
    for i in range(n):
        y = int(round(y0 + i))
        t = i / max(1, n - 1)
        ci = int(round(cx + drift * t + ww * math.sin(phase + t * 6.5)))
        for px in (ci - 1, ci + 1):
            out.set(px, y, 'wdark')
        out.set(ci, y, 'wmid')
        if (i * 5 + int(phase * 3)) % 17 < 4:
            out.set(ci, y, 'wlite')

# tier-1 lip (y=11) -> tier-2 surface (y=16)
for k in range(9):
    col(22 + 2 * k, 12, 15, drift=-1.2, phase=k * 1.7, ww=0.35)
# tier-2 lip (y=22) -> tier-3 surface (y=28)
for k in range(11):
    col(16 + 2 * k, 23, 27, drift=-1.6, phase=k * 1.3, ww=0.4)
# tier-3 lip (y=32) -> pedestal sides (y=46)
col(12, 33, 46, drift=-1.8, phase=0.6, ww=0.5)
col(15, 33, 46, drift=-1.6, phase=2.2, ww=0.5)
col(48, 33, 46, drift=1.6, phase=1.1, ww=0.5)
col(51, 33, 46, drift=1.8, phase=2.9, ww=0.5)
# pedestal base (y=46) -> basin water (y=53)
col(19, 47, 53, drift=-1.2, phase=0.4, ww=0.45)
col(24, 47, 52, drift=-1.0, phase=1.8, ww=0.45)
col(39, 47, 52, drift=1.0, phase=2.6, ww=0.45)
col(44, 47, 53, drift=1.2, phase=1.2, ww=0.45)

# ---------------- crown jet (into the transparent top area) ----------------
jx = 32 + DX
jet = [(0, 5), (-1, 4), (1, 4), (0, 3), (0, 2), (-1, 1), (1, 0)]
for ox, oy in jet:
    out.set(jx + ox, oy, 'wmid')
out.set(jx, 5, 'wdark')
out.set(jx, 3, 'wlite')
out.set(jx - 1, 1, 'wlite')
drops = [(-3, 2), (3, 3), (-5, 4), (5, 5), (-2, 6), (2, 1), (-4, 0), (4, 7), (-6, 6), (6, 1)]
for k, (ox, oy) in enumerate(drops):
    out.set(jx + ox, oy, 'wlite' if k % 3 == 0 else 'wmid')

# ---------------- small foam accents where columns land ----------------
def foam(cx, cy):
    cx += DX
    for k, (ox, oy) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 0)]):
        out.set(cx + ox, cy + oy, 'wspark' if k % 2 == 0 else 'wlite')

for x in (22, 28, 34, 40):
    foam(x, 15)
for x in (16, 22, 28, 34, 40, 46):
    foam(x, 27)
for x in (12, 15, 48, 51):
    foam(x, 44)
for x, y in ((19, 51), (24, 50), (39, 50), (44, 51)):
    foam(x, y)

# ---------------- restrained extra sparkle inside existing water ----------------
for k in range(34):
    zone = k % 4
    if zone == 0:
        x = random.randint(21, 42); y = random.randint(14, 16)
    elif zone == 1:
        x = random.randint(15, 48); y = random.randint(26, 28)
    elif zone == 2:
        x = random.choice([random.randint(12, 17), random.randint(46, 51)]); y = random.randint(41, 46)
    else:
        x = random.choice([random.randint(16, 25), random.randint(38, 47)]); y = random.randint(49, 53)
    px = x + DX
    if out.color_name(out.get(px, y)) in ('c5', 'c6'):
        out.set(px, y, 'wlite' if k % 3 else 'wspark')

view(out)
finish(out)
