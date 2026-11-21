from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, background=(20, 8, 40), name="scene")

# ---------- palette ----------
SKY_TOP = c.color((16, 6, 34), "sky_top")
SKY_MID = c.color((34, 14, 60), "sky_mid")
SKY_LOW = c.color((52, 24, 82), "sky_low")
MOON = c.color((238, 236, 214), "moon")
MOON_SH = c.color((205, 205, 190), "moon_sh")
MIST = c.color((110, 92, 150), "mist")
MIST2 = c.color((84, 66, 124), "mist2")
TREE_DK = c.color((26, 16, 34), "tree_dark")
TREE = c.color((44, 26, 48), "tree")
LEAF_A = c.color((70, 30, 44), "leaf_a")   # dark red-brown
LEAF_B = c.color((96, 44, 52), "leaf_b")
LEAF_C = c.color((60, 36, 70), "leaf_c")   # purple
WOOD = c.color((74, 50, 36), "wood")
WOOD_DK = c.color((50, 32, 24), "wood_dk")
WOOD_LT = c.color((98, 70, 46), "wood_lt")
STONE = c.color((96, 92, 104), "stone")
STONE_DK = c.color((64, 62, 74), "stone_dk")
STONE_LT = c.color((126, 124, 134), "stone_lt")
MOSS = c.color((58, 92, 52), "moss")
MOSS_DK = c.color((38, 64, 38), "moss_dk")
WIN = c.color((255, 170, 60), "win")
WIN_DK = c.color((214, 110, 30), "win_dk")
GROUND = c.color((40, 30, 52), "ground")
GROUND_DK = c.color((28, 20, 38), "ground_dk")
PATH = c.color((84, 80, 90), "path")
PATH_DK = c.color((58, 54, 66), "path_dk")
WIN_GLOW = c.color((120, 70, 50), "glow")

# ---------- sky gradient ----------
for y in range(H):
    t = y / (H - 1)
    q = round(t * 11) / 11  # 12 bands
    if q < 0.5:
        k = q / 0.5
        col = (round(16 + 18 * k), round(6 + 8 * k), round(34 + 26 * k))
    else:
        k = (q - 0.5) / 0.5
        col = (round(34 + 18 * k), round(14 + 10 * k), round(60 + 22 * k))
    c.rect(0, y, W, 1, col)

# stars
import random
random.seed(7)
for _ in range(70):
    x, y = random.randrange(W), random.randrange(0, 78)
    if c.get(x, y) is not None or True:
        c.set(x, y, (150, 130, 190) if random.random() < 0.5 else (200, 190, 220))

# ---------- moon ----------
mx, my = 96, 24
c.circle(mx, my, 9, MOON)
c.circle(mx - 3, my - 3, 3, MOON_SH)
c.circle(mx + 2, my + 1, 2, MOON_SH)
c.set(mx - 1, my + 4, MOON_SH)
# moon halo
c.circle(mx, my, 12, (70, 50, 100), fill=False)

# ---------- mist bands ----------
for (yy, hh, col) in [(70, 5, MIST2), (78, 6, MIST), (88, 7, MIST2), (100, 6, MIST)]:
    for x in range(W):
        w = (x * 13 + yy * 7) % 9
        if w < 6:
            c.rect(x, yy, 1, hh - (w % 3), col)

# ---------- twisted ancient trees ----------
def tree(base_x, base_y, s, flip):
    # trunk
    for i in range(int(30 * s)):
        x = base_x + int(i * 0.3 * s) * (1 if flip else -1)
        y = base_y - i
        wdt = max(1, int((5 - i * 0.12) * s))
        c.rect(max(0, x - wdt // 2), y, wdt, 1, TREE if i % 3 else TREE_DK)
    # branches
    for (bx, by, ex, ey) in [(0, -18, 14, -30), (0, -22, -12, -34), (0, -14, 10, -18), (0, -26, 8, -38)]:
        c.line(base_x + int(bx * s) * (1 if flip else -1), base_y + int(by * s),
               base_x + int(ex * s) * (1 if flip else -1), base_y + int(ey * s), TREE_DK)

def canopy(cx, cy, r):
    for i in range(14):
        a = random.random() * 6.28
        d = random.random() * r
        x, y = int(cx + d * 0.9 * (1 if random.random() < .5 else -1)), int(cy + d * 0.6)
        col = random.choice([LEAF_A, LEAF_B, LEAF_C, TREE_DK])
        c.circle(x, y, random.randrange(2, 5), col)

random.seed(3)
tree(14, 108, 1.4, False); canopy(14, 62, 16)
tree(118, 104, 1.2, True); canopy(118, 66, 14)
tree(58, 46, 0.8, False); canopy(56, 20, 12)
tree(2, 96, 0.9, True); canopy(4, 70, 10)
tree(126, 92, 0.8, False); canopy(124, 68, 9)

# ---------- ground ----------
c.rect(0, 100, W, 28, GROUND)
for x in range(W):
    for y in range(100, H, 3):
        if (x * 7 + y * 5) % 11 < 4:
            c.set(x, y, GROUND_DK)
# horizon soft
c.rect(0, 100, W, 1, (46, 34, 58))

# ---------- cottage ----------
# body
c.rect(38, 74, 44, 28, WOOD)
for y in range(74, 102):
    c.line(38, y, 81, y, WOOD_DK if (y % 4 == 3) else WOOD)
# timber frame
for x in (38, 81):
    c.rect(x, 74, 1, 28, WOOD_DK)
c.rect(38, 74, 44, 1, WOOD_DK)
c.rect(38, 88, 44, 1, WOOD_DK)
for x in (50, 62, 74):
    c.rect(x, 74, 1, 14, WOOD_DK)
# stone base
c.rect(38, 96, 44, 6, STONE_DK)
for x in range(38, 82, 5):
    c.rect(x, 96, 4, 6, STONE if x % 2 else STONE_DK)

# steep mossy roof
for i in range(26):
    y = 74 - i
    x0 = 34 - i
    x1 = 86 + i
    if x1 - x0 < 1:
        break
    c.rect(x0, y, x1 - x0, 1, WOOD_DK)
# moss on roof
for i in range(0, 26):
    y = 74 - i
    if y < 44:
        break
    x0 = 34 - i
    x1 = 86 + i
    for x in range(x0, x1):
        if (x * 3 + y * 5) % 7 < 3:
            c.set(x, y, MOSS)
        elif (x * 3 + y * 5) % 7 < 4:
            c.set(x, y, MOSS_DK)
# roof ridge
c.rect(59, 44, 4, 2, WOOD_DK)
# chimney
c.rect(66, 46, 6, 14, STONE_DK)
c.rect(65, 45, 8, 2, STONE)
for x in range(65, 73):
    if x % 2:
        c.set(x, 44, STONE_DK)
# chimney smoke
for i in range(8):
    c.circle(68 + (i % 3) - 1, 40 - i * 3, 2 + i // 3, MIST2 if i % 2 else MIST)

# windows with warm light
def window(x, y, w, h):
    c.rect(x - 1, y - 1, w + 2, h + 2, WOOD_DK)
    c.rect(x, y, w, h, WIN)
    c.rect(x, y + h // 2, w, 1, WIN_DK)
    c.rect(x + w // 2, y, 1, h, WIN_DK)
    # glow on wall
    c.rect(x - 2, y + h + 1, w + 4, 1, WIN_GLOW)

window(44, 78, 7, 8)
window(66, 78, 7, 8)
window(56, 92, 6, 6)
# door
# door on right side
c.rect(70, 88, 8, 14, WOOD_DK)
c.rect(71, 89, 6, 13, WOOD)
c.set(75, 95, WIN)
c.rect(70, 88, 8, 1, WOOD_LT)

# light spill on ground
c.rect(44, 102, 34, 3, (70, 50, 60))
c.rect(48, 105, 26, 2, (54, 40, 54))

# ---------- stone-slab path ----------
px = 58
for i, y in enumerate(range(102, 128, 3)):
    w = 8 + i
    x0 = 56 - i
    for x in range(x0, x0 + w):
        if (x + y) % 2 == 0:
            c.set(x, y, PATH)
        else:
            c.set(x, y, PATH_DK)
# path edges
c.line(56, 102, 50, 127, PATH_DK)
c.line(64, 102, 70, 127, PATH_DK)

# ---------- stone well with wooden winch ----------
wx, wy = 16, 96
# well base
c.rect(wx, wy, 14, 8, STONE)
for x in range(wx, wx + 14, 3):
    c.rect(x, wy, 2, 8, STONE_LT if x % 2 else STONE_DK)
c.rect(wx - 1, wy - 1, 16, 2, STONE_DK)
# dark interior
c.rect(wx + 2, wy - 2, 10, 3, (20, 14, 26))
# posts
c.rect(wx + 1, wy - 12, 1, 11, WOOD_DK)
c.rect(wx + 12, wy - 12, 1, 11, WOOD_DK)
# roof of well
c.rect(wx - 1, wy - 14, 16, 2, WOOD)
c.rect(wx + 1, wy - 16, 12, 2, WOOD_DK)
for x in range(wx, wx + 14):
    if (x * 3) % 5 < 2:
        c.set(x, wy - 13, MOSS_DK)
# winch axle + rope + bucket
c.rect(wx + 1, wy - 10, 12, 1, WOOD)
c.rect(wx + 5, wy - 11, 4, 3, WOOD_LT)
c.line(wx + 6, wy - 8, wx + 6, wy - 3, (150, 130, 100))
c.rect(wx + 4, wy - 3, 4, 3, WOOD_DK)
# crank
c.line(wx + 13, wy - 10, wx + 15, wy - 8, WOOD_LT)

# ---------- foreground details ----------
# mushrooms / grass tufts
random.seed(11)
for _ in range(26):
    x, y = random.randrange(W), random.randrange(102, 127)
    c.set(x, y, MOSS_DK)
    c.set(x, y + 1, MOSS_DK)
for (mx2, my2) in [(88, 108), (30, 118), (104, 120)]:
    c.rect(mx2, my2, 1, 2, (200, 190, 170))
    c.rect(mx2 - 1, my2 - 1, 3, 1, (180, 60, 50))

# fireflies
for (fx, fy) in [(30, 60), (100, 50), (70, 40), (20, 84), (110, 88), (48, 56)]:
    c.set(fx, fy, (255, 220, 120))
    c.set(fx + 1, fy, (180, 140, 80))

print(c.stats_text())
save("magic-forest-cottage", c)
finish(c)
