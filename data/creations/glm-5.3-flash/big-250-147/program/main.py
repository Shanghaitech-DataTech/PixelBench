import math, colorsys

w, h, rgba = input_canvas.to_rgba()

def gp(x, y):
    i = (y*w + x)*4
    return rgba[i], rgba[i+1], rgba[i+2], rgba[i+3]

# ---------------- 1. sky mask: flood fill from the top through mauve sky ----------------
YLIM = 80

def spreadable(x, y):
    r, g, b, a = gp(x, y)
    if y > YLIM: return False
    if (r - g) > 68: return False
    if g < 70: return False
    if (r + g + b) < 240: return False
    if r >= 190 and g <= 135 and b <= 150: return False
    return True

sky = [[False]*w for _ in range(h)]
stack = []
for x in range(w):
    if spreadable(x, 0):
        sky[0][x] = True
        stack.append((x, 0))
while stack:
    x, y = stack.pop()
    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if 0 <= nx < w and 0 <= ny < h and not sky[ny][nx] and spreadable(nx, ny):
            sky[ny][nx] = True
            stack.append((nx, ny))

# grow the sky into the warm horizon-glow band (the sunset glow is sky, not buildings)
for _ in range(6):
    add = []
    for y in range(1, YLIM + 1):
        rs = sky[y]; up = sky[y-1]; up2 = sky[y-2] if y >= 2 else None
        for x in range(w):
            if rs[x]: continue
            r, g, b, a = gp(x, y)
            if r >= 140 and (r - g) >= 34 and (r + g + b) >= 300:
                if up[x] or (up2 is not None and up2[x]) or (x > 0 and rs[x-1]) or (x < w-1 and rs[x+1]):
                    add.append((x, y))
    if not add:
        break
    for x, y in add:
        sky[y][x] = True

# erase tiny isolated non-sky specks (noise) inside the sky region
add = []
for y in range(0, YLIM + 1):
    for x in range(w):
        if sky[y][x]:
            continue
        cnt = 0
        for dy in (-2, -1, 0, 1, 2):
            yy = y + dy
            if yy < 0 or yy >= h:
                continue
            srow = sky[yy]
            for dx in (-2, -1, 0, 1, 2):
                xx = x + dx
                if 0 <= xx < w and srow[xx]:
                    cnt += 1
        if cnt >= 18:
            add.append((x, y))
for x, y in add:
    sky[y][x] = True
print("sky px:", sum(1 for y in range(h) for x in range(w) if sky[y][x]))

# ---------------- 2. colour mappings ----------------
def sky_blue(y):
    t = min(1.0, max(0.0, y / 80.0))
    return (60 + 92 * t**1.12, 126 + 74 * t**1.05, 206 + 34 * t)

def haze_col(l):
    t = max(0.0, min(1.0, (l - 0.36) / 0.34))
    return (int(112 + 64*t + 0.5), int(136 + 67*t + 0.5), int(170 + 62*t + 0.5))

def win_col(g):
    t = max(0.0, min(1.0, (g - 50) / 100.0))
    return (int(50 + 60*t + 0.5), int(64 + 70*t + 0.5), int(88 + 76*t + 0.5))

def dark_col(r, g, b):
    l = (max(r, g, b) + min(r, g, b)) / 2 / 255
    l2 = 0.10 + l * 0.62
    s2 = 0.14 + l * 0.5
    r2, g2, b2 = colorsys.hls_to_rgb(224/360.0, l2, s2)
    return (int(r2*255 + 0.5), int(g2*255 + 0.5), int(b2*255 + 0.5))

def cool_col(r, g, b):
    hh, ll, ss = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    if ll > 0.33:
        ll = 0.33 + (ll - 0.33) * 0.40
    if ll < 0.10: hue_t, s_t = 235, 0.10
    elif ll < 0.25: hue_t, s_t = 233, 0.20
    elif ll < 0.40: hue_t, s_t = 229, 0.22
    else: hue_t, s_t = 225, 0.24
    s_t = min(0.34, s_t + ss * 0.08)
    r2, g2, b2 = colorsys.hls_to_rgb(hue_t/360.0, ll, s_t)
    return (int(r2*255 + 0.5), int(g2*255 + 0.5), int(b2*255 + 0.5))

# ---------------- 3. repaint ----------------
out = input_canvas.copy(name="output")
for y in range(h):
    for x in range(w):
        r, g, b, a = gp(x, y)
        if sky[y][x]:
            sr, sg, sb = sky_blue(y)
            n = (((x*7 + y*13) % 3) - 1) * 2
            out.set(x, y, (int(sr) + n, int(sg) + n, int(sb) + n))
            continue
        l = (max(r, g, b) + min(r, g, b)) / 2 / 255
        warm = (r - g) >= 36
        # a) open sky left over in the skyline band
        if y <= 76 and l >= 0.37:
            sr, sg, sb = sky_blue(y)
            n = (((x*7 + y*13) % 3) - 1) * 2
            out.set(x, y, (int(sr) + n, int(sg) + n, int(sb) + n)); continue
        # b) hazy gap between the mid-ground buildings (was sunset glow)
        if 68 <= x <= 132 and 77 <= y <= 100 and l >= 0.36 and r >= g:
            out.set(x, y, haze_col(l)); continue
        # c) light bluish haze of the distant city
        if l >= 0.45 and y <= 96 and b >= r - 30:
            out.set(x, y, haze_col(l)); continue
        # d) bright warm edges below the horizon band -> lit windows
        if warm and r >= 146 and (r + g + b) >= 315 and y > 76:
            out.set(x, y, win_col(g)); continue
        # e) mid warm specks in the lower city -> lit windows
        if warm and y > 78:
            out.set(x, y, win_col(g)); continue
        # f) dark bodies -> cool blue-grey silhouettes
        if l < 0.36:
            out.set(x, y, dark_col(r, g, b)); continue
        out.set(x, y, cool_col(r, g, b))

# ---------------- 4. a few small clouds (clear day) ----------------
CLOUD = (250, 252, 255)
CBASE = (203, 223, 243)

def cloud(cx, cy, s):
    out.ellipse(cx, cy + 1, int(9*s), 3, CBASE)
    out.ellipse(cx - int(6*s), cy - 1, int(5*s), 3, CLOUD)
    out.ellipse(cx + int(6*s), cy - 1, int(5*s), 3, CLOUD)
    out.ellipse(cx, cy - int(2*s), int(6*s), 3, CLOUD)
    out.ellipse(cx, cy, int(8*s), 3, CLOUD)

cloud(38, 15, 1.1)
cloud(66, 36, 0.7)
cloud(204, 13, 0.9)

# ---------------- 5. diagnostics ----------------
w2, h2, rgba2 = out.to_rgba()
def gp2(x, y):
    i = (y*w2 + x)*4
    return rgba2[i], rgba2[i+1], rgba2[i+2], rgba2[i+3]

def char_for(c):
    r, g, b, a = c
    hh, ll, ss = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    if ll > 0.90: return "W"
    if ll > 0.76: return "w"
    if ll < 0.15: return "#"
    if ll < 0.30: return "%"
    if ss < 0.15: return "0"
    deg = hh * 360
    if deg < 20 or deg >= 340: return "R"
    if deg < 45: return "O"
    if deg < 70: return "Y"
    if deg < 160: return "G"
    if deg < 200: return "C"
    if deg < 260: return "B"
    if deg < 300: return "P"
    return "M"

print("RESULT map (5x6 blocks):")
for by in range(0, h2, 6):
    line = ""
    for bx in range(0, w2, 5):
        rs = gs = bs = n = 0
        for y in range(by, min(by+6, h2)):
            for x in range(bx, min(bx+5, w2)):
                r, g, b, a = gp2(x, y)
                rs += r; gs += g; bs += b; n += 1
        line += char_for((rs//n, gs//n, bs//n, 255))
    print("%3d %s" % (by, line))

mx = 0
for y in range(8, 61):
    for x in range(100, 151):
        g = gp2(x, y)[1]
        if g > mx: mx = g
print("max G in old sun area:", mx)
warm_left = 0
for y in range(h2):
    for x in range(w2):
        r, g, b, a = gp2(x, y)
        if r - g > 30:
            warm_left += 1
print("warm pixels left (r-g>30):", warm_left)
print(out.stats_text())
finish(out)
