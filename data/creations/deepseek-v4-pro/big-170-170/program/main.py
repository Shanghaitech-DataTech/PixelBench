from pixelbench_api import *
from collections import Counter

out = input_canvas.copy(name='output')
W, H = 170, 170

# ============ 1. Remove the character ============
def bg_color_for(y):
    cnt = Counter()
    for x in range(60, 75):
        idx = out.get(x, y)
        if idx is not None:
            cnt[idx] += 1
    if not cnt:
        return 'c12'
    return out.color_name(cnt.most_common(1)[0][0])

# fill area left of the machine that was hidden behind the character
col = bg_color_for(60)
for x in range(75, 86):
    out.set(x, 60, col)

for y in range(61, 114):
    col = bg_color_for(y)
    for x in range(75, 90):
        out.set(x, y, col)

# ============ 2. Rebuild the vending machine front ============
GLASS = 'c13'
REFL = 'c38'
LEFT_D = 'c37'
LEFT_P = 'c41'
RIGHT_P = 'c41'
RIGHT_D = 'c37'
TOP_D = 'c37'
TOP_P = 'c41'
BOT_D = 'c37'

for y in range(61, 114):
    for x in range(90, 116):
        out.set(x, y, GLASS)

for y in range(61, 114):
    out.set(90, y, LEFT_D)
    out.set(91, y, LEFT_P)
    out.set(114, y, RIGHT_P)
    out.set(115, y, RIGHT_D)

for x in range(90, 116):
    out.set(x, 61, TOP_D)
    out.set(x, 62, TOP_P)

for x in range(90, 116):
    out.set(x, 112, BOT_D)
    out.set(x, 113, BOT_D)

for y in range(63, 112):
    out.set(94, y, REFL)
    out.set(95, y, REFL)
    out.set(110, y, REFL)
    out.set(111, y, REFL)

rows = [
    (64, 68, ['c117', 'c156', 'c231', 'c216']),
    (72, 76, ['c163', 'c221', 'c249', 'c214']),
    (80, 84, ['c122', 'c157', 'c233', 'c253']),
    (88, 92, ['c164', 'c162', 'c235', 'c220']),
    (96, 100, ['c118', 'c223', 'c232', 'c245']),
]
item_x = [93, 98, 103, 108]

for y0, y1, cols in rows:
    for y in range(y0, y1 + 1):
        for i, x0 in enumerate(item_x):
            for x in range(x0, x0 + 3):
                out.set(x, y, cols[i])

for y0, y1, cols in rows:
    for i, x0 in enumerate(item_x):
        out.set(x0, y0, 'c255')

for y in range(101, 112):
    for x in range(92, 114):
        out.set(x, y, 'c13')
for x in range(92, 114):
    out.set(x, 103, 'c42')
    out.set(x, 104, 'c12')
    out.set(x, 105, 'c12')
    out.set(x, 106, 'c42')
    out.set(x, 108, 'c42')

# ============ 3. Thunderstorm darkening ============
storm = new_canvas(W, H)
storm.rect(0, 0, W, H, (18, 28, 44, 70), fill=True)
out = flatten([out, storm], name='result')

# ============ 4. Wet ground with clinging droplets ============
wet = out.color((70, 100, 130, 60), name='wet_tint')
gleam = out.color((175, 210, 240, 90), name='gleam')
gleam_bright = out.color((225, 245, 255, 150), name='gleam_bright')

# dark wet tint over the foreground ground
for y in range(110, H):
    for x in range(0, W, 2):
        out.set(x, y, wet)

# glossy reflection streaks / clinging droplets on the ground
streaks = [
    (8, 128, 2, 7), (24, 150, 2, 8), (36, 120, 3, 6), (52, 160, 2, 8),
    (70, 118, 2, 6), (88, 140, 2, 7), (100, 116, 3, 6), (118, 152, 2, 8),
    (130, 124, 2, 7), (146, 158, 2, 8), (160, 120, 2, 6),
    (18, 115, 1, 3), (62, 168, 1, 3), (108, 165, 1, 3), (152, 134, 1, 3),
]
for x, y, w, h in streaks:
    out.rect(x, y, w, h, gleam, fill=True)

# bright droplet sparkles
sparkles = [(14, 133), (33, 162), (58, 126), (79, 147), (94, 121), (123, 156),
            (139, 131), (166, 163), (44, 118), (71, 169), (112, 160), (157, 140)]
for x, y in sparkles:
    out.set(x, y, gleam_bright)
    out.set(x + 1, y, gleam)

# puddle reflection below the machine
for y in range(114, 124):
    for x in range(90, 116, 2):
        if (x + y) % 4 == 0:
            out.set(x, y, gleam)
out.rect(92, 118, 22, 2, gleam, fill=True)
out.rect(96, 121, 14, 1, gleam_bright, fill=True)

# ============ 5. Semi-transparent rain ============
rain = out.color((150, 185, 225, 85), name='rain')
rain_bright = out.color((205, 230, 255, 135), name='rain_bright')

import random
rng = random.Random(20240512)
for _ in range(160):
    x = rng.randrange(0, W)
    y = rng.randrange(0, H - 12)
    length = rng.choice([4, 5, 6, 7, 8])
    col = rain if rng.random() < 0.7 else rain_bright
    # diagonal streak (falling to the left)
    for k in range(length):
        out.set(x - k, y + 2 * k, col)
        if rng.random() < 0.3:
            out.set(x - k + 1, y + 2 * k, col)

# ============ 6. Lightning in the background ============
bolt_glow = out.color((215, 230, 255, 120), name='bolt_glow')
bolt_core = out.color((245, 250, 255, 235), name='bolt_core')

# main bolt
main_pts = [(46, 0), (42, 10), (49, 19), (41, 31), (50, 43), (43, 54), (47, 63)]
for i in range(len(main_pts) - 1):
    x0, y0 = main_pts[i]
    x1, y1 = main_pts[i + 1]
    # glow
    out.line(x0 - 1, y0, x1 - 1, y1, bolt_glow)
    out.line(x0 + 1, y0, x1 + 1, y1, bolt_glow)
    out.line(x0, y0 - 1, x1, y1 - 1, bolt_glow)
    out.line(x0, y0 + 1, x1, y1 + 1, bolt_glow)
    # core
    out.line(x0, y0, x1, y1, bolt_core)

# branches
branch1 = [(49, 19), (57, 26), (53, 32)]
branch2 = [(41, 31), (33, 39), (36, 47)]
branch3 = [(50, 43), (60, 49)]
for branch in (branch1, branch2, branch3):
    for i in range(len(branch) - 1):
        x0, y0 = branch[i]
        x1, y1 = branch[i + 1]
        out.line(x0 - 1, y0, x1 - 1, y1, bolt_glow)
        out.line(x0 + 1, y0, x1 + 1, y1, bolt_glow)
        out.line(x0, y0, x1, y1, bolt_core)

# bright flash around bolt tip
for dy in range(-2, 3):
    out.set(46, 2 + dy, bolt_core)
    out.set(43, 52 + dy, bolt_core)

print(out.stats_text())
finish(out)
