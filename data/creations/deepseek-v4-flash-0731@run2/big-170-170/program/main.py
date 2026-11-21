from pixelbench_api import *
import random

c = input_canvas.copy(name="output")
W, H = 170, 170

def get_rgba(x, y):
    i = c.get(x, y)
    for p in c.palette():
        if p["index"] == i:
            return p["rgba"]
    return (0, 0, 0, 0)

# ---------- 1. Remove the character (person + umbrella) and fill the background
# The character stood in x57..122, y56..128 in front of the lit vending machine.
# Everything behind/around it is the machine face (glass, products, base) and
# ground; we reconstruct it by sampling the machine/background 40px to the right.
src = {}
for y in range(56, 129):
    for x in range(57, 123):
        src[(x, y)] = c.get(min(x + 40, 169), y)
for (x, y), v in src.items():
    c.set(x, y, v)

# ---------- 2. Storm-darken the scene (overcast sky, wet ground)
def darken_rect(x0, y0, x1, y1, f, t=(17, 28, 52)):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            r, g, b, a = get_rgba(x, y)
            if a == 0:
                continue
            nr = int(r * (1 - f) + t[0] * f)
            ng = int(g * (1 - f) + t[1] * f)
            nb = int(b * (1 - f) + t[2] * f)
            c.set(x, y, (nr, ng, nb, 255))

darken_rect(0, 0, 169, 44, 0.34)     # sky
darken_rect(0, 45, 169, 102, 0.20)    # buildings / machine
darken_rect(0, 103, 169, 169, 0.48)   # wet ground

# heavy cloud bands (semi-transparent haze)
for (cx0, cw, cy, ca) in [(0, 48, 1, 100), (22, 62, 13, 80), (84, 54, 6, 90), (118, 50, 20, 100),
                         (30, 70, 30, 70), (96, 60, 22, 60)]:
    for x in range(cx0, min(cx0 + cw, 170)):
        for y in range(cy, min(cy + 9, 43)):
            c.set(x, y, (138, 160, 214, ca))

# ---------- 3. Lightning in the background
def bolt(pts, main=(236, 241, 255, 255), glow=(148, 174, 236, 110)):
    for (px, py) in pts:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if 0 <= px + dx < 170 and 0 <= py + dy < 170:
                    c.set(px + dx, py + dy, glow)
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        c.line(x0, y0, x1, y1, (196, 212, 246, 170))
        c.line(x0, y0, x1, y1, main)

bolt([(55, 2), (66, 15), (60, 17), (69, 28), (63, 30), (72, 42)])
bolt([(126, 3), (118, 13), (123, 15), (115, 26), (120, 28), (111, 40)])
bolt([(33, 9), (39, 18), (36, 20), (42, 30), (38, 32), (44, 40)])
bolt([(152, 6), (148, 15), (151, 17), (145, 30)])

# ---------- 4. Rain: semi-transparent droplets everywhere
rng = random.Random(42)
for _ in range(1150):
    x = rng.randint(0, 169)
    y = rng.randint(0, 163)
    L = rng.randint(2, 5)
    dx = rng.choice((-1, 0, 0, 1))
    a = rng.randint(95, 165)
    c.line(x, y, x + dx, y + L, (170, 200, 233, a))
    if rng.random() < 0.18:
        c.set(x, y + 1, (205, 228, 248, 190))

# ---------- 5. Wet ground: clinging droplets + glints
rng = random.Random(7)
for _ in range(210):
    x = rng.randint(0, 169)
    y = rng.randint(105, 168)
    L = rng.choice((1, 1, 2))
    c.line(x, y, x, y + L, (198, 222, 244, 220))
    if rng.random() < 0.5:
        c.set(min(x + 1, 169), y, (150, 182, 222, 130))
for _ in range(70):
    x = rng.randint(0, 166)
    y = rng.randint(105, 168)
    c.line(x, y, x + 2, y + 1, (210, 232, 250, 200))

# a few bright clingy beads on the machine roof line / low wall
rng = random.Random(99)
for _ in range(40):
    x = rng.randint(45, 168)
    c.set(x, rng.randint(104, 112), (188, 214, 242, 210))

print(c.stats_text())
finish(c)
