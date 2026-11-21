from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="out")

# ---------- palette ----------
def col(spec): return c.color(spec)

# sky
c.rect(0, 0, 128, 28, '#141a30')
c.rect(0, 28, 128, 15, '#2c2a52')
c.rect(0, 43, 128, 15, '#4a3a62')
c.rect(0, 58, 128, 13, '#7a4f56')
c.rect(0, 71, 128, 11, '#b06a48')
c.rect(0, 82, 128, 7, '#d8884a')

# sun
c.circle(63, 84, 13, '#f7c25e')
c.circle(63, 84, 10, '#ffd97f')
c.circle(63, 84, 6, '#ffeaa0')

# ground
c.rect(0, 89, 128, 39, '#1e1224')
c.rect(0, 89, 128, 1, '#3a2a3c')
c.rect(0, 90, 128, 1, '#2a1c2e')

# distant silhouette peaks near horizon for drama
c.rect(0, 78, 14, 10, '#20162a')
c.rect(116, 76, 12, 12, '#20162a')

# ---------- paste helpers ----------
def paste(sprite, x, y, mapping):
    for j, row in enumerate(sprite):
        for i, ch in enumerate(row):
            if ch != '.' and ch != ' ':
                v = mapping[ch]
                c.set(x+i, y+j, v)

# ---------- knight ----------
km = {
 'k': '#1a0b0d', 'r': '#c22a2a', 'R': '#7c1b1b', 'H': '#e9503c',
 'M': '#c9c9dd', 'm': '#8a8a9a', 'W': '#f4f0ff', 'g': '#d8a63c',
 's': '#e6b98a', 'S': '#c29368',
}
K = [
'..................HH',
'.................HHHH',
'................HHHHHH',
'...............HHHHHHHH',
'..............kkkkkkkkk',
'.............krrrrrrrrrrk',
'.............krrkWWkkkkrk',
'.............krrkkkkkkkrk',
'..............kkkkkkkkkk',
'...........kkkkkkkkkkkkk',
'...........kkkkkkkkkkkkk',
'.....kkkkkkkkkkkkkkkkkkk',
'.....kkrrrrrrrrrrrrrrrrrk',
'.....krrrrrrrrrrrrrrrrrrk',
'.....krrrrrrrrrrrrrrrrrrrk',
'.....krrrrrrrrrrrrrrrrrrkr',
'.....krrrrrrrrrrrrrrrrrrkr',
'.....krrrrrrrrrrrrrrrrrrkr',
'.....krrrrrrrrrrrrrrrrrrkr',
'.....krrrrrrrrrrrrrrrrrrkr',
'......kkkkkkkkkkkkkkkkkkk',
'......kkkkkkkkkkkkkkkkkkk',
'......kkrrrrrrrrrrrrrrrrrr',
'......kkrrrrrrrrrrrrrrrrrk',
'.......kkrrrrrrrrrrrrrrrrk',
'.......kkrrrrrrrrrrrrrrrk',
'.......kkrrrrrrrrrrrrrrrkk',
'.......kkrrrrrrrrrrrrrrrr',
'.......kkrrrrrrrrrrrrrrr',
'........kkrrrrrrrrrrrrrr',
'........kkrrrrrrrrrrrrr',
'........kkkkkkkkkkkkkkk',
'........kkkkkkkkkkkkk',
'.....kkkkkkkkkkkkkkkk',
'.....kkkkkkkkkkkkkkkk',
'....kkkkkkkkkkkkkkkkk',
'....kkkkkkkkkkkkkkkkk',
'....kkkkkkkkkkkkkkkkk',
'...kkkkkkkkkkkkkkkkkk',
]

# sword blade on inner (right) flank: k33 M34 M35 k36, rows 9..28
for yy in range(9, 27):
    for xx, ch in [(-0, 'k'), (1, 'M'), (2, 'M'), (3, 'k')]:
        pass

paste(K, 14, 57, km)

# knight sword projecting into the center gap (right side)
sx = 48
for yy in range(9, 27):
    c.set(sx, yy+57, km['k'])
    c.set(sx+1, yy+57, km['M'])
    c.set(sx+2, yy+57, km['M'])
    c.set(sx+3, yy+57, km['k'])
c.line(sx+2, 27, sx+5, 27, km['g'])
c.set(sx+2, 28, km['m'])
c.set(sx+2, 29, km['g'])

# ---------- rogue ----------
rm = {
 'k': '#142018', 'G': '#3d9c4a', 'g': '#2a6b33', 'L': '#63c264',
 's': '#e0b088', 'W': '#f2f0ff', 'm': '#4a3a30', 'y': '#d8a63c',
 'r': '#93302a', 'b': '#18140f', 'M': '#c8c8dc', 'w': '#ffffff',
}
R = [
'....................kk',
'...................kLLk',
'..................kLLGGk',
'.................kLLGGGGk',
'................kLLGGGGGk',
'..............kkGGGGGGGkk',
'.............kkGGLLLLGGGk',
'............kkGGsssssGGGk',
'............kGGGssWWssGGk',
'............kGGGsssssGGGk',
'............kGGGGGGGGGGk',
'.............kkGGGGGGGGGk',
'...........kkGGGGGGGGGGGkk',
'..........kLLGGGGGGGGGGGGk',
'..........kLLLGGGGGGGGGGLLk',
'..........kLLLLGGGGGGGGGLLk',
'..........kLLLLLGGGGGGGGLL k',
'..........kLLLLLGGGGGGGGLLLk',
'..........kLLLLLGGGGGGGGLLLk',
'..........kLLLLLGGGGGGGGLLLk',
'..........kLLLLLGGGGGGGGLLLk',
'..........kkLLLLGGGGGGGGLLLk',
'...........kkLLLLGGGGGGGGLLk',
'...........kkLLLLGGGGGGGGGLLk',
'...........kkLLLLGGGGGGGGGLk',
'............kkLLLLGGGGGGGLLk',
'............kkLLLLGGGGGGGLLk',
'.............kkLLLLGGGGGGGLk',
'.............kkLLLLGGGGGGGLkk',
'..............kkLLLLGGGGGGGLk',
'..............kkLLLLGGGGGGLLk',
'...............kkLLLLGGGGGLk',
'...............kkLLLLGGGGGk',
'................kkLLLLLLGGkk',
'................kkLLLLLLGGk',
'.................kkLLLLGGGk',
'.................kkkkkkkkkk',
'.................kkkkkkkkkk',
'.................kkkkkkkkkk',
]
rx = 70
paste(R, rx, 57, rm)

# rogue sword projecting into the center gap (left side)
for yy in range(9, 27):
    c.set(76, yy+57, rm['k'])
    c.set(77, yy+57, rm['M'])
    c.set(78, yy+57, rm['M'])
    c.set(79, yy+57, rm['k'])
c.set(77, 27, rm['y'])
c.set(76, 27, rm['y'])
c.set(77, 28, rm['m'])
c.set(77, 29, rm['y'])

print(c.stats_text())
print("COLS", c.stats()['colors_used'])

def bbox(colr):
    idx = c.color(colr)
    xs, ys = [], []
    for y in range(H):
        for x in range(W):
            if c.get(x,y) == idx:
                xs.append(x); ys.append(y)
    if not xs: return None
    return (min(xs), min(ys), max(xs), max(ys))

for colr in ['#c22a2a', '#3d9c4a', '#63c264', '#142018', '#1a0b0d', '#e9503c']:
    print(colr, bbox(colr))

# ---------- dramatic finishing touches ----------
# dust clouds at feet
for (dx, dy) in [(38, 89), (42, 90), (76, 90), (80, 89)]:
    c.circle(dx, dy, 2, '#6a4a58')
    c.circle(dx, dy, 3, '#553a48')

# speed / wind lines behind each character
for yy in range(70, 86, 3):
    c.set(5, yy, '#2c2a52')
    c.set(115, yy, '#2c2a52')

# wind streak near horizon
c.line(100, 41, 116, 41, '#4a3a62')

# verify
print(c.stats_text())
print("final colors:", c.stats()['colors_used'])

finish(c)
