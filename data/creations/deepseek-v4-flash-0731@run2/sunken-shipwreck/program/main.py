from pixelbench_api import new_canvas, finish
import random

rng = random.Random(11)
c = new_canvas(64, 64, name="wreck")

# ---------- water gradient ----------
WATER = (['#6FC3E0'] * 4 + ['#54AFD3'] * 6 + ['#429BC6'] * 6 + ['#3386B4'] * 8
         + ['#2772A2'] * 8 + ['#1F5F90'] * 10 + ['#1A4F7E'] * 22)
for y, wc in enumerate(WATER):
    c.rect(0, y, 64, 1, wc)

# light shafts
for x0 in (7, 24, 41, 57):
    c.dither(x0, 0, 3, 40, ['#7CC9E3', '#54AFD3'], pattern='checker')

# water sparkles
for _ in range(36):
    x = rng.randint(0, 63); y = rng.randint(0, 47)
    if rng.random() < 0.4:
        c.set(x, y, '#7CC9E3')
    else:
        c.set(x, y, '#1F5F90')

# ---------- sand base ----------
for y in range(50, 64):
    tone = '#A89255' if y < 53 else '#C1A86C' if y < 57 else '#D3BC83' if y < 61 else '#E3D09A'
    c.rect(0, y, 64, 1, tone)

# seaweed behind hull
c.path("M 4 62 Q 2 54 4 46 Q 3 40 5 34", '#145733', fill=False)
c.path("M 6 60 Q 4 53 6 45 Q 5 39 7 33", '#1E6B3F', fill=False)
c.path("M 60 62 Q 62 55 60 47 Q 61 41 59 36", '#145733', fill=False)

# hull shadow on the sand
c.ellipse(32, 53, 25, 3, '#6E5E30')

# ---------- hull ----------
c.poly([(6, 42), (8, 34), (12, 29), (22, 26), (34, 26), (46, 30), (53, 37),
       (56, 44), (54, 50), (46, 54), (34, 56), (22, 55), (12, 51), (7, 47)], '#7A4C26')
c.path("M 8 34 L 12 29 L 22 26 L 34 26 L 46 30 L 53 37", '#8F5E32', fill=False)
c.poly([(10, 45), (18, 43), (30, 42), (42, 44), (50, 48), (46, 53), (38, 55),
        (26, 53), (13, 50)], '#512F15')

# planks
c.path("M 8 36 L 22 32 L 36 32 L 48 37", '#3E2310', fill=False)
c.path("M 10 41 L 24 37 L 38 38 L 50 43", '#3E2310', fill=False)
c.path("M 12 47 L 26 44 L 40 45 L 50 49", '#3E2310', fill=False)
c.path("M 9 40 L 23 36 L 37 37 L 49 42", '#7A4C26', fill=False)

# exposed ribs
c.line(26, 30, 25, 51, '#8F5E32')
c.line(38, 32, 38, 52, '#8F5E32')

# broken gap in the hull
c.poly([(30, 38), (34, 37), (38, 40), (36, 46), (32, 48), (29, 44)], '#231408')
c.line(31, 39, 30, 45, '#8F5E32')
c.line(34, 39, 34, 46, '#8F5E32')

# portholes, rust, patina, coral patch on hull
c.circle(16, 39, 1, '#231408')
c.circle(24, 38, 1, '#231408')
c.line(20, 41, 20, 45, '#8A4A28')
c.line(44, 43, 44, 49, '#8A4A28')
c.line(28, 37, 28, 41, '#8A4A28')
c.line(12, 44, 12, 48, '#8A4A28')
c.line(36, 41, 36, 40, '#8A4A28')
c.set(9, 43, '#8A4A28')
c.set(41, 33, '#8A4A28')
c.set(46, 32, '#8A4A28')
c.circle(23, 28, 1, '#3E7A6A')
c.circle(36, 28, 1, '#3E7A6A')
c.circle(48, 35, 1, '#3E7A6A')
c.set(13, 33, '#3E7A6A')
c.set(20, 31, '#3E7A6A')
c.circle(45, 44, 2, '#EF7F4A')
c.set(42, 41, '#C93F5E')

# ---------- bury the hull in sand ----------
c.poly([(2, 60), (2, 50), (8, 48), (18, 46), (28, 45), (40, 46), (50, 48),
       (58, 51), (62, 52), (62, 60)], '#A89255')
c.path("M 4 50 L 12 48 L 22 46 L 30 45 L 38 45 L 48 47 L 56 50", '#C1A86C', fill=False)

# sand ripples + speckles
c.path("M 2 54 L 10 53 L 18 54 L 26 53 L 34 54 L 42 53 L 50 54 L 58 53 L 62 54", '#8C783F', fill=False)
c.path("M 0 57 L 8 56 L 16 57 L 24 56 L 32 57 L 40 56 L 48 57 L 56 56 L 63 57", '#A89255', fill=False)
c.path("M 0 59 L 8 60 L 16 59 L 24 60 L 32 59 L 40 60 L 48 59 L 56 60 L 63 59", '#A89255', fill=False)
c.path("M 0 61 L 8 62 L 16 61 L 24 62 L 32 61 L 40 62 L 48 61 L 56 62 L 63 61", '#E3D09A', fill=False)
for _ in range(50):
    x = rng.randint(0, 63); y = rng.randint(52, 62)
    c.set(x, y, rng.choice(['#6E5E30', '#E3D09A', '#A89255']))

# ---------- broken mast, yardarm, tattered sail ----------
c.line(30, 28, 24, 9, '#512F15')
c.line(31, 28, 25, 9, '#512F15')
c.set(24, 8, '#512F15')
c.set(23, 7, '#512F15')
c.set(25, 11, '#3E2310')
c.line(19, 13, 31, 11, '#3E2310')
c.line(19, 14, 31, 12, '#512F15')
c.poly([(20, 14), (23, 13), (25, 15), (23, 17), (21, 16)], '#9AAEA8')
c.set(22, 15, '#9AAEA8')
c.line(8, 34, 3, 27, '#3E2310')

# ---------- foreground seaweed ----------
c.path("M 2 63 Q 4 57 2 51 Q 3 46 2 43", '#145733', fill=False)
c.path("M 3 62 Q 5 56 3 50", '#1E6B3F', fill=False)
c.path("M 59 63 Q 57 57 59 51 Q 58 47 60 44", '#145733', fill=False)
c.path("M 61 61 Q 59 55 61 49", '#1E6B3F', fill=False)

# ---------- coral clusters ----------
c.circle(12, 54, 4, '#E86A9C')
c.circle(12, 51, 2, '#F7A3BC')
c.circle(15, 53, 1, '#EF7F4A')
c.circle(49, 52, 3, '#C93F5E')
c.circle(51, 50, 2, '#EF7F4A')

# ---------- bubbles ----------
for (bx, by) in [(13, 29), (16, 24), (19, 19), (27, 23), (34, 26),
                (44, 17), (49, 21), (12, 26), (22, 16)]:
    c.set(bx, by, '#AFE0EE')

# ---------- school of fish ----------
fish = [(37, 14), (41, 16), (34, 16), (38, 18), (43, 18), (32, 18), (36, 20),
        (40, 20), (30, 20), (35, 22), (39, 22), (28, 22), (33, 24), (37, 24),
        (35, 15), (40, 17), (44, 19), (30, 19), (34, 21), (38, 23), (42, 21),
        (31, 23), (36, 25)]
for (fx, fy) in fish:
    c.set(fx, fy, '#E0861F')
    c.set(fx + 1, fy, '#FFB03A')
    c.set(fx + 2, fy, '#FFB03A')
    c.set(fx + 2, fy - 1, '#FFB03A')

print(c.stats_text())
print(c.matrix_text(region=(26, 6, 47, 26)))
print(c.matrix_text(region=(2, 24, 62, 48)))
finish(c)
