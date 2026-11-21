import os, json

# Clear stale recovered outputs so this run's finish() is the only submission source.
base = os.path.dirname(os.getcwd())
wp = os.path.join(base, 'workspace.json')
if os.path.exists(wp):
    try:
        d = json.load(open(wp))
        d['outputs'] = []
        d['submission'] = {}
        json.dump(d, open(wp, 'w'))
    except Exception as e:
        print('ws clear failed:', e)

f1 = input_canvas.copy(name='output')

# Frame 2: heavy downward swing on a larger canvas (room for trail + step).
W, H = 56, 64
f2 = new_canvas(W, H, background=None, name='attack')
f2.blit(input_canvas, 6, 3)

GOLD  = f2.color((255, 204, 67))
WHITE = f2.color((255, 255, 255))
CREAM = f2.color((255, 239, 198))
SHAD  = f2.color((192, 128, 8))
OUTL  = f2.color((16, 16, 16))
BOOT  = f2.color((51, 45, 50))

# --- white motion trail: arc sweeping down-right from the raised hilt ---
trail = [
    (33, 7), (35, 8), (37, 10), (39, 12), (41, 14), (42, 16), (43, 18),
    (44, 20), (45, 22), (46, 24), (46, 26), (47, 28), (47, 30), (47, 32),
]
for i, (x, y) in enumerate(trail):
    f2.set(x, y, WHITE)
    f2.set(x + 1, y, WHITE)
    if i > 0:
        px, py = trail[i - 1]
        if py < y:
            f2.set(px, y, WHITE)
            f2.set(px + 1, y, WHITE)
# fading outer edge of the trail
for (x, y) in trail[::2]:
    f2.set(x + 2, y, CREAM)
    f2.set(x + 2, y + 1, CREAM)

# --- weapon swung down: blade from hilt (33,19) to tip (47,33) ---
blade = [(33, 19), (35, 21), (37, 23), (39, 25), (41, 27), (43, 29), (45, 31), (47, 33)]
for i, (x, y) in enumerate(blade):
    f2.set(x, y, GOLD)
    f2.set(x + 1, y, GOLD)
    if i > 0:
        px, py = blade[i - 1]
        if py < y:
            f2.set(px, y, GOLD)
            f2.set(px + 1, y, GOLD)
# blade highlight / edge
for (x, y) in blade:
    f2.set(x + 2, y, WHITE)
# crossguard
f2.rect(31, 18, 4, 1, SHAD)
f2.set(32, 17, SHAD); f2.set(34, 17, SHAD)

# --- left foot stepped forward (down-right of the stance) ---
f2.rect(24, 58, 7, 3, BOOT)
f2.rect(23, 59, 8, 2, BOOT)
f2.set(23, 61, OUTL); f2.set(30, 61, OUTL)
f2.set(24, 57, OUTL); f2.set(25, 57, OUTL); f2.set(26, 57, OUTL)

print(f1.stats_text())
print(f2.stats_text())

finish([f1, f2])
