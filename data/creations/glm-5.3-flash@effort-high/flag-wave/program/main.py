import math

inp = input_canvas
W, H = 64, 64
OX, OY = 8, 4

RED        = 2
ORANGE     = 3
DARK       = 1
SHADE      = inp.color('#a83a28', name='shade')
SHADE_DARK = inp.color('#7f2b1e', name='shade_dark')

# ---- frame 1: untouched copy of the input, placed on 64x64 ---------------
f1 = new_canvas(W, H, background=None, name='f1')
f1.blit(inp, OX, OY)

# ---- rebuild the flag as a separate layer --------------------------------
flag = new_canvas(W, H, background=None, name='flag')
FX0, FY0, FX1, FY1 = 20, 0, 47, 35
for y in range(FY0, FY1 + 1):
    for x in range(FX0, FX1 + 1):
        i = inp.get(x, y)
        if i == 3:
            flag.set(x - FX0, y - FY0, SHADE)
        elif i == 1:
            flag.set(x - FX0, y - FY0, SHADE_DARK)
        elif i != 0:
            flag.set(x - FX0, y - FY0, i)
flag_w = FX1 - FX0 + 1
flag_h = FY1 - FY0 + 1

# 3) wave the flag: vertical displacement of whole columns (cloth ripple)
AMP, CYCLE = 5, 16
frames = []
for t, phase in enumerate((0.0, math.pi)):
    wv = new_canvas(W, H, background=None, name=f'wave{t}')
    for x in range(flag_w):
        g = x / (flag_w - 1)
        dy = round(AMP * (g ** 1.4) * math.sin(2 * math.pi * (x / CYCLE) + phase))
        for y in range(flag_h):
            i = flag.get(x, y)
            if i != 0:
                wv.set(x, y + dy, i)
    frames.append(wv)

# 4) composite: pole layer (f1) on the bottom, waved flag on top
f2 = f1.copy(name='f2'); f2.blit(frames[0], OX + FX0, OY + FY0)
f3 = f1.copy(name='f3'); f3.blit(frames[1], OX + FX0, OY + FY0)

for c_ in (f1, f2, f3):
    print(c_.stats_text())

finish([f1, f2, f3])
