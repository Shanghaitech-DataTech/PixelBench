from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')
pal = c.palette()

def col(name, rgb):
    return c.color(rgb, name=name)

col('night0', (6, 4, 16))
col('night1', (13, 9, 28))
col('night2', (22, 16, 44))
col('night3', (33, 25, 62))
col('night4', (47, 36, 86))
col('night5', (63, 50, 108))
col('moon_rim', (68, 12, 20))
col('moon_dark', (112, 20, 28))
col('moon_mid', (162, 30, 38))
col('moon_bright', (224, 48, 54))
col('moon_glowp', (255, 88, 70))
col('ember', (255, 120, 46))
col('win', (255, 150, 58))
col('winhot', (255, 196, 120))
col('castle', (10, 8, 20))
col('castle2', (23, 18, 40))
col('castle3', (42, 34, 68))
col('hill', (7, 6, 14))
col('earth', (17, 13, 28))
col('star', (232, 226, 248))
col('stard', (120, 112, 148))

# ---- 1. Recolour whole picture into night palette (keeps original structure) ----
night = ['night0', 'night1', 'night2', 'night3', 'night4', 'night5']
for y in range(128):
    for x in range(256):
        i = c.get(x, y)
        rg = pal[i]['rgba']
        if rg[3] == 0:
            out.set(x, y, None)
            continue
        r, g, b = rg[0], rg[1], rg[2]
        lum = (r * 3 + g * 6 + b) // 10
        warm = r - b
        if y < 44:
            if lum > 150:
                out.set(x, y, 'stard')
            else:
                base = 0 if y < 8 else 1 if y < 18 else 2 if y < 30 else 3
                k = base + (lum // 45) - 1
                if k < 0: k = 0
                if k > 5: k = 5
                out.set(x, y, night[k])
        else:
            if y >= 112:
                if lum > 150 or (warm > 30 and lum > 80):
                    out.set(x, y, 'moon_dark')
                elif warm > 20:
                    out.set(x, y, 'earth')
                else:
                    out.set(x, y, 'hill')
            else:
                if warm > 50 and r > 110:
                    out.set(x, y, 'win' if lum > 140 else 'ember')
                elif lum > 200:
                    out.set(x, y, 'winhot')
                elif lum > 150:
                    out.set(x, y, 'castle3')
                elif lum > 95:
                    out.set(x, y, 'castle2')
                else:
                    out.set(x, y, 'castle')

# ---- 2. Stars ----
stars = [(30, 8), (52, 14), (70, 5), (88, 18), (158, 10), (186, 6), (210, 16),
        (234, 10), (18, 24), (46, 30), (238, 32), (200, 26), (14, 40), (60, 46),
        (196, 44), (224, 60), (8, 58), (244, 48), (34, 52), (240, 20), (66, 30),
        (176, 24), (90, 44), (150, 20), (206, 8), (40, 18), (250, 40), (222, 58)]
for (sx, sy) in stars:
    out.set(sx, sy, 'star')
# a couple of cross sparkles
for (sx, sy) in [(70, 5), (210, 16)]:
    out.set(sx - 1, sy, 'stard'); out.set(sx + 1, sy, 'stard')
    out.set(sx, sy - 1, 'stard'); out.set(sx, sy + 1, 'stard')

# ---- 3. Blood moon (hanging) ----
out.circle(120, 34, 32, 'moon_rim')
out.circle(120, 34, 29, 'moon_dark')
out.circle(120, 34, 25, 'moon_mid')
out.circle(116, 30, 20, 'moon_bright')
out.circle(98, 18, 6, 'moon_glowp')
# craters / marbling
out.circle(105, 24, 4, 'moon_mid')
out.circle(130, 41, 4, 'moon_mid')
out.circle(112, 46, 3, 'moon_mid')
out.circle(138, 28, 3, 'moon_dark')
out.circle(122, 20, 2, 'moon_dark')
out.circle(134, 50, 3, 'moon_dark')
out.circle(103, 38, 2, 'moon_dark')
out.circle(116, 36, 2, 'moon_dark')
out.circle(128, 24, 2, 'moon_dark')
out.set(96, 46, 'moon_dark')

# ---- 4. Dark clouds across the moon ----
out.rect(92, 48, 30, 2, 'night3')
out.rect(138, 52, 22, 2, 'night3')
out.rect(104, 55, 12, 2, 'night2')
out.rect(146, 46, 16, 2, 'night2')
out.rect(88, 54, 10, 2, 'night2')

# ---- 5. Back ridge / mountains ----
out.poly([(0, 110), (36, 102), (72, 106), (110, 100), (150, 104), (196, 108),
         (234, 103), (255, 108), (255, 127), (0, 127)], 'hill')

# ---- 6. Demon King's castle ----
# far left tower
out.poly([(92, 88), (84, 100), (100, 100)], 'castle')
out.rect(86, 98, 12, 14, 'castle')
out.poly([(69, 92), (62, 102), (76, 102)], 'castle')
out.rect(64, 100, 10, 12, 'castle')
# left tower
out.poly([(105, 72), (96, 84), (114, 84)], 'castle')
out.rect(98, 82, 14, 30, 'castle')
out.rect(112, 96, 12, 16, 'castle2')
# main keep / hall
out.rect(116, 78, 28, 34, 'castle2')
for mx in (116, 124, 132, 140):
    out.rect(mx, 76, 5, 2, 'castle')
# central great tower
out.rect(120, 58, 16, 54, 'castle')
out.rect(118, 60, 20, 3, 'castle')
out.rect(124, 54, 8, 4, 'castle')
out.poly([(128, 42), (118, 60), (138, 60)], 'castle')
out.poly([(122, 48), (118, 56), (126, 56)], 'castle')
# right tower
out.poly([(152, 76), (143, 88), (161, 88)], 'castle')
out.rect(146, 86, 12, 26, 'castle')
out.poly([(172, 92), (164, 102), (180, 102)], 'castle')
out.rect(166, 100, 12, 12, 'castle')
# corner bastions on the hall
out.poly([(116, 90), (112, 100), (120, 100)], 'castle')
out.poly([(144, 94), (140, 104), (148, 104)], 'castle')

# gate
out.poly([(119, 112), (119, 96), (127, 88), (135, 96), (135, 112)], 'ember')
out.poly([(121, 112), (121, 97), (127, 90), (133, 97), (133, 112)], (2, 1, 5))
out.set(124, 100, 'winhot'); out.set(130, 104, 'winhot')
out.rect(126, 98, 1, 2, 'win')

# ---- 7. Glowing windows / embers ----
for (wx, wy) in [(122, 66), (130, 66), (123, 74), (131, 72), (102, 88), (108, 94),
                (102, 100), (154, 90), (160, 96), (154, 104), (170, 106), (90, 104),
                (68, 106), (120, 86), (136, 86), (120, 96), (132, 98), (124, 103),
                (128, 108), (122, 112), (133, 116), (102, 110), (158, 112)]:
    out.set(wx, wy, 'win')
for (wx, wy) in [(124, 70), (128, 78), (106, 92), (150, 94), (122, 92), (134, 92),
                (126, 100), (130, 116)]:
    out.set(wx, wy, 'ember')
# banners
out.poly([(128, 38), (124, 46), (132, 46)], 'win')
out.poly([(105, 68), (101, 76), (109, 76)], 'win')
out.poly([(152, 72), (148, 80), (156, 80)], 'win')
out.poly([(92, 84), (88, 92), (96, 92)], 'win')
out.poly([(172, 88), (168, 96), (176, 96)], 'win')

# ---- 8. Foreground ground + blood-moon reflections ----
out.rect(0, 118, 256, 10, 'hill')
out.rect(104, 114, 12, 1, 'moon_rim')
out.rect(112, 116, 14, 1, 'moon_dark')
out.rect(120, 119, 16, 1, 'moon_mid')
out.rect(108, 121, 8, 1, 'moon_rim')
out.rect(126, 123, 12, 1, 'moon_dark')
out.rect(116, 125, 8, 1, 'moon_rim')
out.rect(104, 117, 6, 1, 'moon_dark')
out.rect(132, 116, 6, 1, 'moon_dark')
out.rect(96, 120, 6, 1, 'moon_rim')
out.rect(140, 118, 8, 1, 'moon_dark')
out.rect(120, 127, 14, 1, 'moon_mid')

# rising embers near the castle
for (ex, ey) in [(150, 52), (156, 46), (96, 58), (88, 50), (162, 38), (80, 66),
                (170, 64), (60, 74), (176, 52)]:
    out.set(ex, ey, 'ember')
for (ex, ey) in [(146, 48), (92, 54), (158, 42), (66, 70), (172, 48)]:
    out.set(ex, ey, 'winhot')

print(out.stats_text())
finish(out)
