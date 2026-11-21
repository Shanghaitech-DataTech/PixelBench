import math

# ---------------- canvas ----------------
W = H = 48
c = new_canvas(W, H, name="portal")

BAYER4 = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def bthr(x, y):
    return (BAYER4[y % 4][x % 4] + 0.5) / 16.0


def clamp(v, a, b):
    return a if v < a else (b if v > b else v)


CX = CY = 23.5
AX, AY = 16.5, 18.5          # outer radius of the portal ring

RING = ['#2a0f52', '#3f1878', '#5a22a8', '#7b3fd4', '#9b63ee', '#c9a0ff']
SWIRL = ['#2a0f52', '#3d1673', '#53209a', '#6b2bc4',
         '#8544d8', '#a066f5', '#c49bff', '#e6d5ff', '#fdfbff']

grid = {}
for y in range(H):
    for x in range(W):
        dx = x - CX
        dy = y - CY
        nx = dx / AX
        ny = dy / AY
        p = math.hypot(nx, ny)
        if p > 1.19:
            continue
        th = math.atan2(ny, nx)
        colr = None

        if p >= 1.0:
            # ---- glowing halo + soft falloff ----
            if p < 1.052:
                colr = '#ecdcff'
            elif p < 1.095:
                colr = '#b98cf7'
            elif p < 1.135:
                if bthr(x, y) < 0.55:
                    colr = '#6a34b8'
            elif p < 1.170:
                if bthr(x, y) < 0.30:
                    colr = '#3f1878'
            else:
                if bthr(x, y) < 0.13:
                    colr = '#2a0f52'

        elif p >= 0.78:
            # ---- the ring, lit from the top-left ----
            L = clamp(0.55 - 0.32 * nx - 0.42 * ny, 0.0, 1.0)
            t = (p - 0.78) / 0.22
            if t > 0.60:
                L *= 0.60
            elif t < 0.18:
                L = min(1.0, L * 1.20)
            base = L * 5.0
            i = int(base)
            if base - i > bthr(x, y):
                i += 1
            colr = RING[int(clamp(i, 0, 5))]

        else:
            # ---- spiral vortex inside the opening ----
            pc = max(p, 0.06)
            v = math.sin(th - 4.20 * math.log(pc) + 2.4)
            ridge = max(0.0, v) ** 1.4
            amp = clamp((p - 0.10) / 0.16, 0.0, 1.0)
            radial = 1.0 - p / 0.78
            base = 2.15 + 2.3 * radial ** 1.3
            base += 3.2 * ridge * amp
            base += 2.6 * (1.0 - clamp(p / 0.25, 0.0, 1.0)) ** 1.5
            if p > 0.66:
                base -= (p - 0.66) / 0.12 * 1.0
            # white-hot throat at the very centre
            base += 1.3 * (1.0 - clamp(p / 0.10, 0.0, 1.0)) ** 1.5
            base = clamp(base, 0.0, 8.0)
            base = clamp(base, 0.0, 8.0)
            i = int(base)
            if base - i > bthr(x, y):
                i += 1
            colr = SWIRL[int(clamp(i, 0, 8))]

        if colr is not None:
            grid[(x, y)] = colr

# ---- energy motes drifting in the halo ----
MOTES = [(0.35, 1.10), (1.30, 1.16), (2.55, 1.12),
         (3.55, 1.17), (4.65, 1.11), (5.45, 1.14)]
for ang, pr in MOTES:
    mx = int(round(CX + AX * pr * math.cos(ang)))
    my = int(round(CY + AY * pr * math.sin(ang)))
    grid[(mx, my)] = '#f7f2ff'
    grid[(mx - 1, my)] = '#c9a0ff'
    grid[(mx, my + 1)] = '#c9a0ff'

for (x, y), colr in sorted(grid.items(), key=lambda kv: (kv[0][1], kv[0][0])):
    if 0 <= x < W and 0 <= y < H:
        c.set(x, y, colr)

print(c.stats_text())

# ---- text observation: luminance ramp ----
RAMP = " .:-=+*#%@"


def lum(hexs):
    r = int(hexs[1:3], 16)
    g = int(hexs[3:5], 16)
    b = int(hexs[5:7], 16)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0


for y in range(H):
    row = ""
    for x in range(W):
        h = grid.get((x, y))
        if h is None:
            row += "."
        else:
            row += RAMP[int(clamp(lum(h), 0, 0.999) * len(RAMP))]
    print(row)

# ---- colour-index map (chars ranked by luminance) ----
used = {}
for h in grid.values():
    used[h] = used.get(h, 0) + 1
order = sorted(used, key=lambda h: lum(h))
sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij"
lookup = {h: sym[i] for i, h in enumerate(order)}
print("legend:", [(sym[i], h, used[h]) for i, h in enumerate(order)])
for y in range(H):
    print("".join(lookup.get(grid.get((x, y)), ".") for x in range(W)))

save("teleport_portal", c)
finish(c)
