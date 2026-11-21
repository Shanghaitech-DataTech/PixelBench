import math, random
from pixelbench_api import *

W, H = 64, 64

sheet = new_canvas(W, H, name="explosion")

# ============ Frame 1: bright yellow fireball at center (left half, center ~(16,32)) ============
f1_cx = 16
# Draw largest radius first so the bright core ends on top
for r, col in [
    (11, "#ff8c1a"),
    (10, "#ffaa33"),
    (8,  "#ffcc00"),
    (6,  "#ffe066"),
    (4,  "#fff7b0"),
    (2,  "#ffffff"),
]:
    sheet.circle(f1_cx, 32, r, col, fill=True)

# Outer jagged flame fringe
random.seed(1)
for i in range(60):
    ang = random.random() * 6.28318
    rr = random.randint(11, 13)
    x = int(f1_cx + rr * math.cos(ang))
    y = int(32 + rr * math.sin(ang))
    if abs(x - f1_cx) > 8 or abs(y - 32) > 8:
        sheet.set(x, y, "#ffaa33")

# Small rising ember sparks around frame 1
for i in range(16):
    ang = random.random() * 6.28318
    dist = random.randint(13, 17)
    x = int(f1_cx + dist * math.cos(ang))
    y = int(32 + dist * math.sin(ang))
    if 0 <= x < W and 0 <= y < H and abs(x - f1_cx) > 8 or abs(y - 32) > 8:
        sheet.set(x, y, "#ffcc44")

# ============ Frame 2: expanding orange-red blast with sparks (right half, center ~(48,32)) ============
f2_cx = 48
for r, col in [
    (14, "#cc220f"),
    (13, "#e63311"),
    (12, "#ff5522"),
    (11, "#ff7733"),
    (9,  "#ff8822"),
    (7,  "#ffaa33"),
    (5,  "#ffcc33"),
    (3,  "#fff0a0"),
    (1,  "#ffffff"),
]:
    sheet.circle(f2_cx, 32, r, col, fill=True)

# Radiating blast spikes / expanding wave
for i in range(10):
    ang = i * 6.28318 / 10
    for rr in range(14, 16):
        x = int(f2_cx + rr * math.cos(ang))
        y = int(32 + rr * math.sin(ang))
        if 0 <= x < W and 0 <= y < H:
            sheet.set(x, y, "#ff7733")

# Red shockwave ring
sheet.circle(f2_cx, 32, 15, "#ff4422", fill=False)

# Sparks flying outward (distinct small dots)
random.seed(7)
for i in range(44):
    ang = random.random() * 6.28318
    dist = random.randint(16, 22)
    x = int(f2_cx + dist * math.cos(ang))
    y = int(32 + dist * math.sin(ang))
    if 0 <= x < W and 0 <= y < H:
        sheet.set(x, y, "#ffdd66" if random.random() < 0.45 else "#ff8833")

# A few tiny hot white sparks
for i in range(12):
    ang = random.random() * 6.28318
    dist = random.randint(14, 20)
    x = int(f2_cx + dist * math.cos(ang))
    y = int(32 + dist * math.sin(ang))
    if 0 <= x < W and 0 <= y < H:
        sheet.set(x, y, "#ffffff")

print(sheet.stats_text())
print(sheet.matrix_text(region=(35, 18, 63, 46), indices=False))

save("explosion", sheet)
finish(sheet)
