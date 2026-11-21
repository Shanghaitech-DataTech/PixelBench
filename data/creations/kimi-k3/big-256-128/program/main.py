from pixelbench_api import *

out = input_canvas.copy(name="output")
W, H = 256, 128

def ramp(a, b, steps):
    return [tuple(int(round(a[k] + (b[k]-a[k]) * t/(steps-1))) for k in range(3)) for t in range(steps)]

sky_cols   = ramp((16, 6, 22), (120, 26, 24), 26)
land_cols  = ramp((30, 16, 32), (7, 3, 9), 20)
castle_cols= ramp((46, 28, 40), (18, 11, 18), 12)
glow_cols  = ramp((150, 20, 12), (255, 96, 48), 10)
moon_rim   = (255, 220, 170)
moon_mid   = (236, 92, 54)
moon_dark  = (158, 30, 30)
moon_hot   = (255, 120, 66)
star_col   = (255, 196, 176)
cloud_hi   = (196, 78, 66)
cloud_mid  = (116, 38, 44)
cloud_dark = (52, 18, 28)

skyidx  = [out.color(c) for c in sky_cols]
landidx = [out.color(c) for c in land_cols]
castidx = [out.color(c) for c in castle_cols]
glowidx = [out.color(c) for c in glow_cols]
i_rim   = out.color(moon_rim)
i_mid   = out.color(moon_mid)
i_dark  = out.color(moon_dark)
i_hot   = out.color(moon_hot)
i_star  = out.color(star_col)
i_chi   = out.color(cloud_hi)
i_cmid  = out.color(cloud_mid)
i_cd    = out.color(cloud_dark)

inp = input_canvas
pal = inp.palette()

def lum(r,g,b): return 0.2126*r + 0.7152*g + 0.0722*b

for y in range(H):
    for x in range(W):
        idx = inp.get(x, y)
        r,g,b,a = pal[idx]["rgba"]
        if a == 0: continue
        L = lum(r,g,b)
        is_white = L > 208
        is_cyan  = (g > 150 and b > 140 and r < 120)
        is_warm  = (r > b + 10 and r > g + 4)
        if y >= 87:
            t = min(19, max(0, int((y-87)/(127-87) * 19.999)))
            if is_warm and L > 90:
                out.set(x, y, glowidx[min(9, int((L-90)/165*9.999))])
            elif L > 150:
                out.set(x, y, landidx[max(0, t-6)])
            else:
                out.set(x, y, landidx[t])
        else:
            t = min(25, max(0, int((86-y)/86 * 25.999)))
            base = skyidx[25-t]
            if is_cyan:
                out.set(x, y, glowidx[min(9, int(L/255*9.999))])
            elif is_white:
                out.set(x, y, i_chi)
            elif L > 150:
                out.set(x, y, i_cmid)
            elif L > 96:
                out.set(x, y, i_cd)
            else:
                out.set(x, y, base)

# castle silhouette with relief
for y in range(28, 100):
    for x in range(92, 165):
        idx = inp.get(x, y)
        r,g,b,a = pal[idx]["rgba"]
        if a == 0: continue
        L = lum(r,g,b)
        was_sky = (b > r + 20) and (b > g + 10)
        if was_sky: continue
        t = min(11, max(0, int((y-28)/72 * 11.999)))
        if L > 175:
            out.set(x, y, castidx[max(0, t-6)])
        elif L > 120:
            out.set(x, y, castidx[max(0, t-3)])
        else:
            out.set(x, y, castidx[t])

# ember windows on keep
for y in range(34, 98):
    for x in range(96, 162):
        idx = inp.get(x, y)
        r,g,b,a = pal[idx]["rgba"]
        if a == 0: continue
        if r>150 and g>115 and b<170 and lum(r,g,b)>105:
            out.set(x, y, glowidx[min(9, int((lum(r,g,b)-105)/150*9.999))])

# blood moon
mcx, mcy, mr = 128, 34, 24
for y in range(mcy-mr-12, mcy+mr+12):
    for x in range(mcx-mr-12, mcx+mr+12):
        if not (0<=x<W and 0<=y<H): continue
        d = ((x-mcx)**2 + (y-mcy)**2) ** 0.5
        if mr < d <= mr+12:
            k = int((d-mr)/12 * 9.999)
            out.set(x, y, glowidx[9-min(9,k)])
for y in range(mcy-mr, mcy+mr):
    for x in range(mcx-mr, mcx+mr):
        if not (0<=x<W and 0<=y<H): continue
        d = ((x-mcx)**2 + (y-mcy)**2) ** 0.5
        if d <= mr:
            if d > mr-4:
                out.set(x, y, i_rim)
            else:
                n = (x*3 + y*5) % 9
                if n < 3:
                    out.set(x, y, i_dark)
                elif n < 6:
                    out.set(x, y, i_mid)
                else:
                    out.set(x, y, i_hot)
for cx, cy, rr in [(mcx-7, mcy-6, 7), (mcx+5, mcy+4, 5), (mcx+2, mcy-9, 4)]:
    for y in range(cy-rr, cy+rr):
        for x in range(cx-rr, cx+rr):
            if (x-cx)**2 + (y-cy)**2 <= rr*rr and (x-mcx)**2+(y-mcy)**2 <= (mr-3)**2:
                out.set(x, y, i_dark)

# stars
import random
random.seed(7)
for _ in range(170):
    x = random.randrange(W); y = random.randrange(0, 80)
    if (x-mcx)**2 + (y-mcy)**2 < (mr+5)**2: continue
    out.set(x, y, i_star)

# ---- repaint the sky bands with visible arc structure ----
# Use the original cloud-band brightness to carve curved bands across the sky
for y in range(0, 87):
    for x in range(W):
        # skip moon & halo area
        if (x-mcx)**2 + (y-mcy)**2 <= (mr+13)**2: continue
        idx = inp.get(x, y)
        r,g,b,a = pal[idx]["rgba"]
        if a == 0: continue
        L = lum(r,g,b)
        # curved band emphasis: sample along arcs centered near moon
        dx = (x - mcx) / 1.0
        dy = (y - mcy) / 0.62
        d = (dx*dx + dy*dy) ** 0.5
        band = (d / 7.0) % 1.0
        # brighten crests, darken troughs
        if L > 150:
            if band < 0.45:
                out.set(x, y, i_chi)
            else:
                out.set(x, y, i_cmid)
        elif L > 96:
            if band < 0.35:
                out.set(x, y, i_cmid)
            else:
                out.set(x, y, i_cd)

# Re-impose ember windows & moon after band pass (band pass may have overwritten spire top)
for y in range(34, 98):
    for x in range(96, 162):
        idx = inp.get(x, y)
        r,g,b,a = pal[idx]["rgba"]
        if a == 0: continue
        if r>150 and g>115 and b<170 and lum(r,g,b)>105:
            out.set(x, y, glowidx[min(9, int((lum(r,g,b)-105)/150*9.999))])

view(out)
print(out.stats_text())

finish(out)
