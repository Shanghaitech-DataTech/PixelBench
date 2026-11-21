from pixelbench_api import *
import numpy as np

# ---- palette -------------------------------------------------------------
OUT    = '#241a1f'   # dark outline / eyes
SKIN   = '#f6c9a0'
SKINSH = '#dda07a'
HAIR   = '#5b3a29'
HAIRHI = '#7d543a'
BROW   = '#4a2c1e'
WHITE  = '#ffffff'
SHIRT  = '#3f6d8f'
SHIRTD = '#2c4f6b'
COLLAR = '#e9e6df'
BLUSH  = '#ec9280'
MOUTH  = '#8c4a4a'
MOUTHD = '#6e2f36'
RED    = '#e0483a'
SWEAT  = '#8fd4f2'

# fringe: last hair row per column (zigzag bangs, raised to free the brow zone)
FRINGE = {7: 7, 8: 8, 9: 9, 10: 10, 11: 9, 12: 8, 13: 7, 14: 8, 15: 9,
          16: 10, 17: 9, 18: 8, 19: 7, 20: 8, 21: 9, 22: 10, 23: 9,
          24: 8, 25: 7}


# ---- shared character (identical in all four portraits) ------------------
def base(c):
    c.ellipse(16, 12, 11, 11, HAIR)          # hair mass
    c.ellipse(16, 14, 9, 10, SKIN)           # face
    for x in range(7, 26):                   # zigzag bangs
        top = 5 if 8 <= x <= 24 else 6
        c.line(x, top, x, FRINGE[x], HAIR)
    for (x, y) in [(10, 5), (11, 4), (12, 4), (13, 3), (14, 3)]:
        c.set(x, y, HAIRHI)                  # hair shine
    c.rect(14, 24, 4, 1, SKINSH)             # neck shadow
    c.rect(14, 25, 4, 1, SKIN)               # neck
    c.poly([(2, 30), (2, 28), (5, 27), (10, 26), (22, 26),
            (27, 27), (30, 28), (30, 30)], SHIRT)   # shoulders / shirt
    c.rect(13, 26, 7, 1, COLLAR)             # collar band
    c.set(8, 28, SHIRTD); c.set(9, 29, SHIRTD)
    c.set(24, 28, SHIRTD); c.set(23, 29, SHIRTD)
    c.set(16, 18, SKINSH)                    # nose
    c.rect(15, 23, 3, 1, SKINSH)             # chin shade


# ---- expressions ---------------------------------------------------------
def emo_calm(c):
    c.line(11, 13, 14, 13, BROW)             # flat relaxed brows
    c.line(18, 13, 21, 13, BROW)
    for cx in (12, 20):                      # soft oval eyes + catchlight
        c.line(cx - 1, 15, cx + 1, 15, OUT)
        c.line(cx - 2, 16, cx + 2, 16, OUT)
        c.line(cx - 1, 17, cx + 1, 17, OUT)
        c.set(cx - 1, 15, WHITE)
    c.set(14, 20, MOUTH); c.set(18, 20, MOUTH)      # small gentle smile
    c.line(15, 21, 17, 21, MOUTH)
    c.set(10, 19, BLUSH); c.set(11, 19, BLUSH)
    c.set(21, 19, BLUSH); c.set(22, 19, BLUSH)


def emo_smile(c):
    c.set(11, 13, BROW); c.set(12, 12, BROW)  # raised arches
    c.set(13, 12, BROW); c.set(14, 13, BROW)
    c.set(18, 13, BROW); c.set(19, 12, BROW)
    c.set(20, 12, BROW); c.set(21, 13, BROW)
    for cx in (12, 20):                       # happy closed eyes
        c.set(cx - 2, 16, OUT); c.line(cx - 1, 15, cx + 1, 15, OUT)
        c.set(cx + 2, 16, OUT)
    c.ellipse(16, 21, 3, 1, MOUTHD)           # open laugh
    c.line(14, 21, 18, 21, WHITE)             # teeth
    c.line(10, 19, 12, 19, BLUSH); c.line(20, 19, 22, 19, BLUSH)


def emo_angry(c):
    c.line(9, 11, 13, 13, BROW)               # steep V brows
    c.line(23, 11, 19, 13, BROW)
    c.rect(10, 15, 5, 2, OUT)                 # narrowed eyes
    c.rect(18, 15, 5, 2, OUT)
    c.rect(13, 20, 7, 3, OUT)                 # snarl, gritted teeth
    c.rect(14, 21, 5, 1, WHITE)
    c.set(16, 21, OUT)
    for (x, y) in [(13, 20), (19, 20), (13, 22), (19, 22)]:
        c.set(x, y, SKIN)                     # round the mouth corners
    c.set(22, 6, RED); c.line(21, 7, 23, 7, RED)    # anger vein
    c.set(22, 8, RED)


def emo_surprised(c):
    c.set(10, 12, BROW); c.set(11, 11, BROW)  # high arches
    c.set(12, 11, BROW); c.set(13, 12, BROW)
    c.set(18, 12, BROW); c.set(19, 11, BROW)
    c.set(20, 11, BROW); c.set(21, 12, BROW)
    for cx in (12, 20):                       # wide eyes, tiny pupils
        c.rect(cx - 2, 14, 5, 5, OUT)
        c.set(cx - 2, 14, SKIN); c.set(cx + 2, 14, SKIN)
        c.set(cx - 2, 18, SKIN); c.set(cx + 2, 18, SKIN)
        c.rect(cx - 1, 15, 3, 3, WHITE)
        c.set(cx, 16, OUT)
    c.ellipse(16, 21, 1, 1, MOUTHD)           # small "o" mouth
    c.set(29, 5, SWEAT)                       # sweat drop beside the head
    c.rect(28, 6, 3, 3, SWEAT)
    c.set(29, 9, SWEAT)
    c.set(28, 7, WHITE)


# ---- assemble the 2x2 sheet ---------------------------------------------
sheet = new_canvas(64, 64, None, name="emotions")
sprites = []
for i, fn in enumerate([emo_calm, emo_smile, emo_angry, emo_surprised]):
    t = new_canvas(32, 32, None)
    base(t)
    fn(t)
    t.outline(OUT)
    sprites.append(t)
    sheet.blit(t, (i % 2) * 32, (i // 2) * 32)

# ---- verification --------------------------------------------------------
print(sheet.stats_text())
w, h, rgba = sheet.to_rgba()
a = np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(h, w, 4)

# 1) transparency check
transp = np.count_nonzero(a[:, :, 3] == 0)
print("transparent pixels:", transp, "of", w * h)

# 2) palette size (visible colours must stay <= 86)
vis = a[a[:, :, 3] > 0]
uniq = {(int(p[0]), int(p[1]), int(p[2]), int(p[3])) for p in vis}
print("distinct visible colours:", len(uniq))

# 3) quadrant isolation: each 32x32 quadrant must have zero ink in the
#    opposite quadrant's rows/cols (no bleed across the 2x2 seams)
for qi, (x0, y0) in enumerate([(0, 0), (32, 0), (0, 32), (32, 32)]):
    q = a[y0:y0 + 32, x0:x0 + 32, 3]
    print("quadrant", qi, "visible px:", int(np.count_nonzero(q > 0)))

# 4) per-sprite outline integrity: every visible pixel that borders
#    transparency (or the sprite edge) must itself be the OUT colour
out_rgba = (0x24, 0x1a, 0x1f, 0xFF)
for qi, (x0, y0) in enumerate([(0, 0), (32, 0), (0, 32), (32, 32)]):
    s = a[y0:y0 + 32, x0:x0 + 32]
    vis_m = s[:, :, 3] > 0
    leaks = []
    for y in range(32):
        for x in range(32):
            if not vis_m[y, x]:
                continue
            near = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
            edge = any(ny < 0 or ny > 31 or nx < 0 or nx > 31
                       or not vis_m[ny, nx] for ny, nx in near)
            if edge and tuple(s[y, x]) != out_rgba:
                leaks.append((x, y))
    print("sprite", qi, "boundary pixels not dark-outlined:", len(leaks),
          leaks[:8])

# 5) identical silhouettes across the four portraits
#    (ignore the surprise sweat drop, an emotion prop outside the head)
masks = []
for (x0, y0) in [(0, 0), (32, 0), (0, 32), (32, 32)]:
    m = a[y0:y0 + 32, x0:x0 + 32, 3] > 0
    m[0:11, 27:32] = False          # sweat-drop zone
    masks.append(m)
same = all((masks[0] == m).all() for m in masks[1:])
print("identical silhouette across portraits (excl. sweat drop):", same)

# 6) the four portraits never touch: gaps along the internal seams
col31 = np.count_nonzero(a[:, 31, 3] > 0)
col32 = np.count_nonzero(a[:, 32, 3] > 0)
row31 = np.count_nonzero(a[31, :, 3] > 0)
row32 = np.count_nonzero(a[32, :, 3] > 0)
print("ink on seam cols 31/32:", col31, col32, "| rows 31/32:", row31, row32)

finish(sheet)
