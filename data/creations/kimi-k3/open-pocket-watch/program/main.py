from pixelbench_api import *
import math

c = new_canvas(64, 64, background='#0e0b08', name='pocket_watch')

# ---------------- background ----------------
c.circle(30, 34, 27, '#191309')          # soft warm glow
c.circle(29, 33, 23, '#211a0e')

# drop shadows (light from upper-left)
c.circle(32, 38, 21, '#0a0806')          # case shadow, offset down-right
c.ellipse(58, 39, 5, 14, '#0a0806')      # lid shadow

def arc(cx, cy, r0, r1, a0, a1, col):
    for r in range(r0, r1 + 1):
        for a in range(a0, a1 + 1):
            x = round(cx + r * math.cos(math.radians(a)))
            y = round(cy + r * math.sin(math.radians(a)))
            c.set(x, y, col)

# ---------------- open lid (behind case, hinged right) ----------------
c.ellipse(56, 36, 6, 14, '#2e1f08')                 # dark rim
c.ellipse(56, 36, 5, 13, '#d8a23a')                 # gold face
c.ellipse(57, 37, 4, 12, '#b57f28')                 # lower-right shade crescent
c.ellipse(54, 34, 3, 11, '#f0c964')                 # upper-left light crescent
c.ellipse(56, 36, 2, 7, '#a8742a', fill=False)      # engraved oval
c.circle(56, 36, 1, '#ffe491')                      # centre emblem
for y in range(23, 50):                             # rim highlight / shade
    t = (y - 36) / 14.0
    if abs(t) <= 1:
        xr = 6 * math.sqrt(1 - t * t)
        xl = round(56 - xr); xrr = round(56 + xr)
        if 27 <= y <= 34:
            c.set(xl + 1, y, '#ffe491')
        if 40 <= y <= 45:
            c.set(xrr - 1, y, '#83591a')

# ---------------- case ----------------
c.circle(30, 36, 21, '#2e1f08')          # outer dark outline
c.circle(30, 36, 20, '#e0aa3e')          # gold ring
arc(30, 36, 19, 20, 190, 262, '#ffe491') # bright upper-left rim
arc(30, 36, 18, 18, 198, 256, '#f7cd63')
arc(30, 36, 18, 20, 15, 80, '#83591a')   # lower-right shade
arc(30, 36, 20, 20, 25, 72, '#5c3f10')

c.circle(30, 36, 17, '#241d12')          # inner bezel line
c.circle(30, 36, 16, '#f4e9ce')          # chapter ring (dial)
arc(30, 36, 14, 16, 195, 260, '#fbf3dd') # ring light
arc(30, 36, 14, 16, 20, 75, '#c7b48c')   # ring shade
arc(30, 36, 16, 16, 28, 70, '#9a8a68')

# hinge knuckles between case and lid
c.rect(50, 29, 2, 3, '#83591a'); c.set(50, 29, '#ffe491')
c.rect(50, 40, 2, 3, '#83591a'); c.set(50, 40, '#d8a23a')

# ---------------- movement plate ----------------
c.circle(30, 36, 13, '#96682a')
c.circle(30, 36, 13, '#5c3f10', fill=False)
arc(30, 36, 12, 13, 15, 78, '#5c3f10')   # recess shadow
arc(30, 36, 13, 13, 195, 258, '#c1922f') # recess light
for yy in range(24, 49):                 # brushed texture, subtle
    for xx in range(18, 43):
        if (xx - 30) ** 2 + (yy - 36) ** 2 <= 151:
            if (xx + yy) % 6 == 0:
                c.set(xx, yy, '#83591a')
            elif xx < 28 and yy < 34 and (xx + yy) % 7 == 0:
                c.set(xx, yy, '#c1922f')

# screws
for sx, sy in [(18, 32), (40, 41)]:
    c.set(sx, sy, '#d8dce2'); c.set(sx + 1, sy, '#8f959e')
    c.set(sx, sy + 1, '#8f959e'); c.set(sx + 1, sy + 1, '#45484c')

# ---------------- gear train ----------------
def gear(cx, cy, r, base='#ebb446', dark='#4a320e', lite='#ffd970',
         n=8, phase=0, spokes=False, jewel=True):
    if n:
        for k in range(n):
            a = math.radians(k * 360 / n + phase)
            x = round(cx + (r + 1) * math.cos(a))
            y = round(cy + (r + 1) * math.sin(a))
            c.set(x, y, base)
            if k == n * 5 // 8:            # upper-left tooth catches light
                c.set(x, y, lite)
            if k == n // 8:                # lower-right tooth in shade
                c.set(x, y, dark)
    c.circle(cx, cy, r, dark)
    c.circle(cx, cy, r - 1, base)
    c.set(cx - 1, cy - (r - 1), lite)
    if r >= 3:
        c.set(cx - (r - 1), cy - 1, lite)
        c.set(cx - 1, cy - 1, lite)
    if spokes:
        c.line(cx - r + 1, cy, cx + r - 1, cy, dark)
        c.line(cx, cy - r + 1, cx, cy + r - 1, dark)
        c.circle(cx, cy, 1, base)
    c.set(cx, cy, '#c22538' if jewel else dark)

gear(25, 32, 5, n=8, phase=0,  spokes=True)          # mainspring barrel
gear(34, 39, 4, n=8, phase=22, spokes=True)          # centre wheel
gear(27, 43, 3, n=8, phase=0)                        # third wheel
gear(37, 29, 2, base='#8f959e', dark='#45484c',
     lite='#d8dce2', n=4, phase=45)                  # steel escape wheel
gear(21, 40, 2, n=6)                                 # small gold wheel

# ---------------- tick marks ----------------
for k in range(12):
    th = math.radians(k * 30)
    dx, dy = math.sin(th), -math.cos(th)
    x0 = round(30 + 15 * dx); y0 = round(36 + 15 * dy)
    x1 = round(30 + 16 * dx); y1 = round(36 + 16 * dy)
    c.line(x0, y0, x1, y1, '#241d12')
    if k % 3 == 0:                                   # major ticks
        x2 = round(30 + 14 * dx); y2 = round(36 + 14 * dy)
        c.line(x2, y2, x1, y1, '#241d12')
        px, py = round(-dy), round(dx)
        if px or py:
            c.line(x0 + px, y0 + py, x1 + px, y1 + py, '#241d12')

# ---------------- hands (10:10), gold-framed dark core ----------------
c.line(30, 36, 23, 31, '#d8a23a')          # hour: gold body
c.line(29, 37, 22, 32, '#d8a23a')
c.line(30, 36, 23, 31, '#241d12')          # dark core
c.line(30, 36, 40, 30, '#d8a23a')          # minute: gold body
c.line(29, 37, 39, 31, '#d8a23a')
c.line(30, 36, 40, 30, '#241d12')          # dark core
c.line(30, 36, 28, 38, '#241d12')          # counterweight tail
c.set(30, 36, '#ffe491')                   # centre pin

# ---------------- crown, bow, chain ----------------
c.rect(29, 15, 3, 2, '#5c3f10')            # stem
c.rect(28, 11, 5, 5, '#2e1f08')            # crown outline
c.rect(29, 12, 3, 3, '#e0aa3e')
c.set(30, 12, '#83591a'); c.set(30, 13, '#83591a'); c.set(30, 14, '#83591a')
c.set(29, 12, '#ffe491'); c.set(29, 13, '#f7cd63')   # glint
c.circle(30, 8, 3, '#e0aa3e', fill=False)  # bow ring
c.set(28, 6, '#ffe491'); c.set(32, 10, '#83591a')
c.set(30, 10, '#b57f28')                   # connector link

chain = [(30, 5), (28, 3), (25, 2), (22, 1), (19, 1), (16, 2), (13, 4),
         (10, 6), (8, 9), (6, 12), (4, 15), (2, 18), (0, 21)]
for i in range(len(chain) - 1):
    c.line(chain[i][0], chain[i][1], chain[i + 1][0], chain[i + 1][1], '#e0aa3e')
for i, p in enumerate(chain):
    if i % 3 == 0:
        c.set(p[0], p[1] - 1, '#ffe491')   # glint
    elif i % 3 == 1:
        c.set(p[0] + 1, p[1] + 1, '#83591a')  # shaded link

# ---------------- specular sparkles ----------------
c.set(16, 22, '#fff6d8')                   # big glint on case rim
for px, py in [(15, 22), (17, 22), (16, 21), (16, 23)]:
    c.set(px, py, '#ffe491')
c.set(21, 27, '#fff6d8')                   # glint on big gear tooth
c.set(52, 27, '#fff6d8')                   # glint on lid rim

print(c.stats_text())
view(c)
finish(c)
