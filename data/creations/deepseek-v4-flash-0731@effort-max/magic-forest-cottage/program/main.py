from pixelbench_api import *
import random

W = H = 128
c = new_canvas(W, H, name="magic-forest-cottage")
rng = random.Random(11)

# ---------------- SKY ----------------
sky = ['#0d0330', '#140843', '#1b0d52', '#221260', '#29176e',
       '#301c7a', '#372286', '#3d2a8f', '#422f94']
for i, cl in enumerate(sky):
    c.rect(0, i * 8, W, 8, cl)
c.rect(0, 72, W, 14, '#3f2c92')   # horizon haze

# ---------------- STARS ----------------
stars = ['#d9d2f5', '#fff0b8', '#b8aee8']
for _ in range(78):
    x = rng.randint(1, 126)
    y = rng.randint(1, 64)
    if (x - 94) ** 2 + (y - 24) ** 2 < 26 ** 2:
        continue
    c.set(x, y, rng.choice(stars))
for _ in range(5):
    x = rng.randint(4, 120); y = rng.randint(3, 40)
    if (x - 94) ** 2 + (y - 24) ** 2 < 30 ** 2:
        continue
    c.set(x, y, '#e8e0ff'); c.set(x - 1, y, '#e8e0ff'); c.set(x + 1, y, '#e8e0ff')
    c.set(x, y - 1, '#e8e0ff'); c.set(x, y + 1, '#e8e0ff')

# ---------------- MOON ----------------
c.circle(94, 24, 21, (110, 95, 190, 26))
c.circle(94, 24, 17, (150, 130, 220, 40))
c.circle(94, 24, 13, (196, 176, 236, 62))
c.circle(94, 24, 11, '#f3e8b8')
c.circle(92, 22, 7, '#faf3d4')
c.circle(95, 27, 6, '#ecd89c')
c.set(91, 24, '#d9c892'); c.set(97, 21, '#d9c892'); c.set(95, 29, '#d9c892')
c.set(98, 18, '#d9c892')

# ---------------- BACKGROUND FOREST / HILLS ----------------
c.ellipse(26, 82, 62, 16, '#231548')
c.ellipse(100, 80, 72, 18, '#1e1140')
for (px, pw, ph, pc) in [(10, 64, 72, '#1a0f3e'), (22, 58, 78, '#241748'),
                        (88, 60, 74, '#1a0f3e'), (116, 62, 70, '#241748'),
                        (70, 56, 80, '#1a0f3e'), (34, 62, 76, '#241748')]:
    top = 56
    c.poly([(px, top + (ph - top) // 2), (px + pw // 2, top), (px + pw, top + (ph - top) // 2)], pc)

# ---------------- GROUND ----------------
ground = [(74, '#33246b'), (84, '#2c1e5e'), (94, '#261a52'), (104, '#21164a'),
          (114, '#1c1240'), (124, '#180f38')]
for y, cl in ground:
    c.rect(0, y, W, 10, cl)
c.rect(0, 72, W, 4, '#3a2a7e')

# ---------------- COTTAGE ----------------
# walls
c.rect(36, 62, 42, 40, '#5d3c28')
c.rect(36, 62, 42, 40, '#4e2f1e')
c.rect(36, 86, 42, 16, '#3a3346')           # stone base area
for yy in range(66, 86, 5):
    c.rect(36, yy, 42, 1, '#46281a')
for xx in (44, 50, 64, 70):
    c.rect(xx, 62, 1, 24, '#46281a')
# roof
c.poly([(8, 66), (57, 30), (106, 66)], '#3a1420')
c.poly([(8, 66), (57, 30), (106, 66), (102, 72), (57, 38), (12, 72)], '#2b0e18')
c.poly([(36, 62), (57, 36), (78, 62)], '#4e2f1e')
c.poly([(36, 62), (57, 36), (78, 62)], '#6d4933')
c.line(52, 38, 62, 34, '#4a1c28')
# chimney
c.rect(70, 20, 7, 26, '#3b2536')
c.rect(68, 17, 11, 5, '#2c1a2c')
c.rect(70, 22, 7, 3, '#4a3040')
# smoke
c.circle(80, 12, 4, (150, 140, 190, 90))
c.circle(86, 7, 5, (150, 140, 190, 70))
# moss on roof
moss = ['#2e4a2c', '#3a5a35', '#46703e']
for mx, my, mrx, mry in [(18, 58, 5, 3), (27, 50, 6, 3), (38, 41, 5, 3), (76, 41, 5, 3),
                       (88, 50, 6, 3), (97, 58, 5, 3), (14, 62, 4, 3), (102, 62, 4, 3)]:
    c.ellipse(mx, my, mrx, mry, rng.choice(moss))
c.ellipse(56, 34, 6, 2, '#3a5a35')
# stone lower wall
stones = ['#5a5266', '#4c4457', '#665d72']
for row, sy in enumerate(range(86, 100, 6)):
    sx = 34 + (row % 2) * 4
    while sx < 80:
        sw = rng.randint(8, 12)
        c.rect(sx, sy, min(sw, 80 - sx), 5, rng.choice(stones))
        sx += sw + 1
c.rect(34, 100, 46, 4, '#2f2a3c')
# door
c.rect(52, 78, 10, 25, '#33201a')
c.circle(57, 77, 5, '#33201a')
c.rect(53, 79, 8, 9, '#c07e3e')
c.rect(53, 89, 8, 14, '#33201a')
# windows + glow
for wx in (41, 63):
    c.rect(wx - 2, 68, 12, 14, (255, 150, 70, 60))
    c.rect(wx - 4, 66, 16, 18, (255, 160, 90, 34))
    c.rect(wx, 70, 8, 8, '#3a2a1c')
    c.rect(wx + 1, 71, 6, 6, '#ffb45c')
    c.rect(wx + 1, 71, 6, 2, '#ffcf7e')
    c.rect(wx + 3, 71, 1, 6, '#ff9a3c')
    c.rect(wx + 1, 74, 6, 1, '#ff9a3c')
    c.rect(wx + 1, 71, 6, 1, '#ffb45c')

# ---------------- TREES ----------------
lt = '#2b1a2e'
c.poly([(2, 127), (20, 127), (17, 84), (20, 54), (17, 34), (12, 20), (6, 14), (0, 20),
       (2, 34), (8, 52), (8, 84)], lt)
c.line(15, 60, 27, 36, lt); c.line(14, 40, 24, 22, lt); c.line(12, 84, 24, 58, lt)
c.line(9, 26, 16, 14, lt); c.line(15, 58, 24, 36, lt)
c.line(6, 30, 12, 18, lt)
c.line(12, 100, 15, 40, '#3a2639'); c.line(14, 60, 20, 38, '#3a2639')
c.line(16, 74, 20, 50, '#3a2639')
def clump(cx, cy, r, dk, md, lt2):
    c.circle(cx, cy, r, dk)
    c.circle(cx - 2, cy + 2, r - 2, md)
    c.circle(cx + 2, cy + 1, max(2, r - 3), dk)
    for ox, oy in [(-r // 2, -r // 2), (-1, -r + 1), (r // 2, -r // 3)]:
        c.circle(cx + ox, cy + oy, max(2, r // 3), lt2)
clump(24, 18, 11, '#3a1830', '#4d1f38', '#5d2436')
clump(33, 30, 9, '#4d1f38', '#5d2436', '#772b3e')
clump(18, 34, 9, '#3a1830', '#4d1f38', '#5d2436')
clump(12, 22, 8, '#2f1430', '#4d1f38', '#5d2436')
clump(28, 12, 7, '#3a1830', '#5d2436', '#772b3e')

rt = '#2b1a2e'
c.poly([(110, 127), (128, 127), (126, 92), (122, 58), (112, 32), (102, 20), (96, 28),
       (104, 38), (112, 60)], rt)
c.line(120, 60, 128, 34, rt)
c.line(118, 96, 126, 60, rt)
c.line(108, 40, 104, 24, rt)
c.line(116, 30, 124, 20, rt)
c.line(114, 62, 124, 42, '#3a2639')
clump(118, 16, 9, '#3a1830', '#4d1f38', '#5d2436')
clump(127, 28, 9, '#2f1430', '#4d1f38', '#5d2436')
clump(110, 20, 7, '#4d1f38', '#5d2436', '#772b3e')
clump(126, 24, 6, '#3a1830', '#5d2436', '#772b3e')

# ---------------- MIST (behind foreground path / well / door) ----------------
c.ellipse(64, 80, 68, 6, (157, 146, 201, 52))
c.ellipse(30, 88, 42, 5, (128, 118, 176, 70))
c.ellipse(102, 90, 48, 5, (128, 118, 176, 58))
c.ellipse(64, 97, 60, 6, (100, 92, 150, 60))
c.ellipse(18, 76, 34, 4, (157, 146, 201, 44))
c.ellipse(110, 84, 34, 4, (157, 146, 201, 48))

# ---------------- FOREGROUND: warm ground glow ----------------
c.rect(30, 102, 34, 8, (255, 160, 90, 30))
c.rect(66, 104, 34, 8, (255, 160, 90, 26))

# ---------------- PATH (stone slabs to door) ----------------
for (px, py, pw, ph) in [(50, 98, 16, 7), (45, 105, 22, 8), (38, 113, 28, 8), (30, 121, 34, 9)]:
    c.rect(px, py, pw, ph, '#3a3346')
    c.rect(px + 1, py + 1, pw - 2, ph - 2, '#4e4660')
    c.rect(px + 2, py + 2, pw - 4, ph - 4, '#5d5470')
    c.rect(px + 3, py + 3, pw - 6, ph - 4, '#6b6280')

# ---------------- WELL (crisp, in front of fog) ----------------
c.ellipse(102, 100, 14, 7, '#5c5468')
c.ellipse(102, 99, 12, 5, '#6c6480')
c.ellipse(102, 99, 8, 3, '#0d0a1e')
c.ellipse(102, 100, 6, 2, '#0d0a1e')
c.rect(92, 72, 4, 26, '#543821')
c.rect(109, 72, 4, 26, '#543821')
c.rect(93, 73, 1, 24, '#6b4a2e')
c.rect(110, 73, 1, 24, '#6b4a2e')
c.rect(91, 68, 23, 3, '#3a1420')
c.rect(91, 68, 23, 1, '#4a1c28')
c.rect(96, 76, 13, 5, '#75542f')
c.rect(96, 77, 13, 2, '#8a6a44')
c.rect(91, 76, 4, 5, '#543821')
c.line(90, 74, 92, 78, '#543821')
c.line(114, 74, 112, 78, '#543821')
c.line(102, 81, 102, 90, '#8a6a44')
c.rect(100, 90, 5, 6, '#4a2f22')

# ---------------- DOOR step + warm doorway light (in front of fog) ----------------
c.rect(52, 78, 10, 25, '#33201a')
c.rect(53, 79, 8, 9, '#75542f')
c.rect(53, 81, 8, 4, '#75542f')
c.rect(53, 89, 8, 14, '#33201a')
c.rect(49, 96, 16, 4, '#543821')
c.rect(48, 100, 18, 3, '#33201a')
c.circle(57, 77, 5, '#33201a')

# ---------------- FOREGROUND DETAIL ----------------
tuft = ['#3b2e5e', '#453768']
for _ in range(26):
    x = rng.randint(2, 124); y = rng.randint(104, 126)
    g = rng.choice(tuft)
    c.set(x, y, g); c.set(x + 1, y - 1, g); c.set(x - 1, y - 1, g)
for (x, y) in [(58, 66), (46, 90), (74, 112), (36, 106), (88, 116), (66, 124), (30, 78), (100, 104)]:
    c.circle(x, y, 2, (255, 200, 110, 70))
    c.set(x, y, '#ffd98a')
for (x, y) in [(74, 118), (28, 112), (52, 122), (40, 116), (82, 108)]:
    c.set(x, y, '#ffd98a')
    c.set(x + 1, y, '#772b3e'); c.set(x - 1, y, '#772b3e')
    c.set(x, y + 1, '#772b3e')

print(c.matrix_text(region=(44, 62, 114, 104)))
finish(c)
