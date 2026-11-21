import random, traceback

try:
    random.seed(20240607)

    W = H = 256
    GROUND_Y = 218
    SKY_END = 194

    def lerp_hex(a, b, t):
        ar, ag, ab = int(a[1:3], 16), int(a[3:5], 16), int(a[5:7], 16)
        br, bg2, bb = int(b[1:3], 16), int(b[3:5], 16), int(b[5:7], 16)
        return '#%02x%02x%02x' % (round(ar + (br - ar) * t),
                                  round(ag + (bg2 - ag) * t),
                                  round(ab + (bb - ab) * t))

    # ================= BACKGROUND : forest clearing =================
    bg = new_canvas(W, H, name='bg')

    SKY_TOP, SKY_BOT = '#57683f', '#1f2d1c'
    N = 10
    for i in range(N):
        y0 = i * SKY_END // N
        y1 = (i + 1) * SKY_END // N
        bg.rect(0, y0, W, y1 - y0, lerp_hex(SKY_TOP, SKY_BOT, i / (N - 1)))

    # ---- god rays (opaque, stepped fade, behind the treeline) ----
    def ray(x0, w0, shift):
        segs = ['#d8eeb2', '#aac689', '#7c9c64', '#5a744c']
        n = len(segs)
        for i, col in enumerate(segs):
            ya = i * SKY_END // n
            yb = (i + 1) * SKY_END // n
            sh = int(shift * ya / H)
            sh2 = int(shift * yb / H)
            bg.poly([(x0 + sh, ya), (x0 + w0 + sh, ya),
                     (x0 + w0 + sh2, yb), (x0 + sh2, yb)], col)

    ray(96, 64, 40)
    ray(58, 22, 44)
    ray(112, 28, 50)
    ray(166, 18, 40)
    # dust motes in the shafts
    for _ in range(50):
        x0, w0, shift = random.choice([(58, 22, 44), (112, 28, 50), (166, 18, 40)])
        y = random.randint(6, SKY_END - 4)
        x = random.randint(x0, x0 + w0) + int(shift * y / H)
        bg.set(x, y, '#eefbcd')

    # ---- treeline silhouettes ----
    bg.rect(0, SKY_END - 6, W, GROUND_Y - SKY_END + 6, '#1b2a15')
    for x in range(2, 254, 7):
        if 64 <= x <= 198:
            continue
        hgt = random.randint(20, 56)
        col = random.choice(['#141f0e', '#182612'])
        bg.poly([(x, GROUND_Y), (x + 7, GROUND_Y), (x + 3, GROUND_Y - hgt)], col)
        if random.random() < 0.4:
            bg.ellipse(x + 3, GROUND_Y - hgt, 5, 4, col)

    # ---- ground ----
    G_TOP, G_BOT = '#2f2515', '#120d07'
    M = 6
    for i in range(M):
        y0 = GROUND_Y + i * (H - GROUND_Y) // M
        y1 = GROUND_Y + (i + 1) * (H - GROUND_Y) // M
        bg.rect(0, y0, W, y1 - y0, lerp_hex(G_TOP, G_BOT, i / (M - 1)))

    # pool of light on the clearing floor
    bg.ellipse(152, 236, 60, 13, '#3a2d19')
    bg.ellipse(150, 233, 36, 8, '#443519')

    for _ in range(700):
        x = random.randrange(W)
        y = random.randrange(GROUND_Y, H)
        bg.set(x, y, random.choice(['#241b0e', '#3a2d18', '#2a2011']))
    for _ in range(160):
        x = random.randrange(W)
        yb = random.randrange(GROUND_Y + 4, H)
        ln = random.randint(2, 6)
        col = random.choice(['#2f401c', '#26331a'])
        for k in range(ln):
            bg.set(x + (k // 3) * random.choice((-1, 0, 1)), yb - k, col)

    # glowing mushrooms
    for mx, my in ((36, 240), (214, 243), (58, 248)):
        bg.circle(mx, my, 3, '#31481f')
        bg.rect(mx, my, 1, 3, '#b7ae8e')
        bg.rect(mx - 1, my - 1, 3, 2, '#79c94f')
        bg.set(mx, my - 2, '#c9f79b')

    # ================= TREANT =================
    t = new_canvas(W, H, name='treant')

    BARK = '#3a2a18'
    BARK_DK = '#2a1d10'
    BARK_DK2 = '#241a0e'
    BARK_LT = '#4e3a22'
    BARK_LT2 = '#5f472a'
    LEAF = '#223318'
    LEAF_DK = '#1a2712'
    LEAF_LT = '#31491f'
    LEAF_LT2 = '#40602a'
    MOSS = '#3d5a26'
    MOSS_LT = '#54762f'
    VINE = '#2a421c'
    SOCKET = '#151009'
    EYE = '#8dff5e'
    EYE_CORE = '#dcffc0'
    MAW = '#0e0906'
    TOOTH = '#4a3620'
    OUTLINE = '#0b0805'

    # trunk
    t.poly([(102, 222), (99, 180), (100, 140), (104, 108), (110, 88), (118, 78),
            (140, 78), (148, 88), (154, 108), (158, 140), (159, 180), (156, 222)],
           BARK)
    # root legs + toes
    t.poly([(102, 200), (54, 244), (112, 224)], BARK)
    t.poly([(56, 242), (42, 252), (62, 246)], BARK)
    t.poly([(66, 240), (58, 254), (74, 246)], BARK)
    t.poly([(154, 200), (202, 244), (144, 224)], BARK)
    t.poly([(200, 242), (214, 252), (194, 246)], BARK)
    t.poly([(190, 240), (198, 254), (182, 246)], BARK)
    t.poly([(120, 212), (114, 244), (132, 244), (128, 212)], BARK)
    t.poly([(114, 242), (106, 252), (120, 246)], BARK)
    t.poly([(132, 242), (142, 252), (128, 246)], BARK)
    # small roots rising around the base
    t.poly([(76, 240), (60, 222), (82, 238)], BARK_DK)
    t.poly([(46, 244), (30, 230), (50, 242)], BARK_DK)
    t.poly([(180, 240), (196, 224), (174, 238)], BARK_DK)
    t.poly([(212, 244), (226, 232), (208, 242)], BARK_DK)
    # arms raised, claw twigs
    t.poly([(104, 108), (60, 52), (52, 44), (58, 36), (96, 66), (112, 92)], BARK)
    t.poly([(54, 44), (40, 26), (50, 42)], BARK)
    t.poly([(58, 40), (56, 20), (62, 38)], BARK)
    t.poly([(62, 44), (74, 28), (64, 46)], BARK)
    t.poly([(78, 60), (70, 44), (84, 56)], BARK)
    t.poly([(152, 108), (196, 52), (204, 44), (198, 36), (160, 66), (144, 92)], BARK)
    t.poly([(202, 44), (216, 26), (206, 42)], BARK)
    t.poly([(198, 40), (200, 20), (194, 38)], BARK)
    t.poly([(194, 44), (182, 28), (192, 46)], BARK)
    t.poly([(176, 58), (186, 42), (172, 56)], BARK)
    # branch stubs into canopy
    t.poly([(118, 82), (112, 58), (120, 56), (126, 80)], BARK)
    t.poly([(140, 82), (146, 58), (138, 56), (132, 80)], BARK)
    t.poly([(126, 80), (128, 52), (132, 52), (134, 80)], BARK)

    tw, th, tpx = t.to_rgba()
    bark_idx = t.color(BARK)

    def opaque(x, y):
        return 0 <= x < tw and 0 <= y < th and tpx[4 * (y * tw + x) + 3] > 0

    def is_bark(x, y):
        return opaque(x, y) and t.get(x, y) == bark_idx

    # edge shading, light from upper-left
    for y in range(th):
        x = 0
        while x < tw:
            if opaque(x, y) and t.get(x, y) == bark_idx:
                x0 = x
                while x < tw and opaque(x, y) and t.get(x, y) == bark_idx:
                    x += 1
                x1 = x - 1
                for i in range(2):
                    if x0 + i <= x1:
                        t.set(x0 + i, y, BARK_LT if i == 0 else BARK_LT2)
                    if x1 - i >= x0:
                        t.set(x1 - i, y, BARK_DK if i == 0 else BARK_DK2)
            else:
                x += 1

    # gnarled vertical streaks
    for _ in range(90):
        x = random.randrange(10, 246)
        y = random.randrange(20, 240)
        length = random.randint(4, 16)
        col = random.choice([BARK_DK, BARK_DK, BARK_LT2])
        for k in range(length):
            if not is_bark(x, y + k):
                break
            t.set(x, y + k, col)
            if random.random() < 0.3:
                x += random.choice((-1, 1))
    # speckle
    for _ in range(500):
        x = random.randrange(tw)
        y = random.randrange(th)
        if is_bark(x, y):
            t.set(x, y, random.choice(['#332413', '#42301b', BARK_DK2]))
    # knots
    for kx, ky in ((112, 160), (146, 172), (124, 196), (140, 128)):
        t.ellipse(kx, ky, 3, 4, BARK_DK2)
        t.ellipse(kx, ky, 1, 2, '#1c130a')
        t.set(kx - 3, ky + 2, BARK_LT)
    # darkening near ground
    for y in range(204, 226):
        for x in range(tw):
            if is_bark(x, y) and random.random() < 0.45:
                t.set(x, y, BARK_DK2)

    # canopy
    t.ellipse(128, 34, 54, 20, LEAF)
    t.ellipse(88, 48, 30, 15, LEAF)
    t.ellipse(170, 46, 32, 16, LEAF)
    t.ellipse(128, 52, 38, 15, LEAF)
    t.ellipse(62, 60, 16, 10, LEAF)
    t.ellipse(196, 58, 16, 10, LEAF)
    for cx, cy, rx, ry in ((128, 34, 54, 20), (88, 48, 30, 15), (170, 46, 32, 16),
                           (128, 52, 38, 15), (62, 60, 16, 10), (196, 58, 16, 10)):
        t.ellipse(cx - rx // 3, cy - ry // 3, rx // 2, ry // 2, LEAF_LT)
        t.ellipse(cx - rx // 2, cy - ry // 2, rx // 3, ry // 3, LEAF_LT2)
        t.ellipse(cx + rx // 3, cy + ry // 3, rx // 2, max(1, ry // 3), LEAF_DK)
    leaf_set = {t.color(LEAF), t.color(LEAF_LT), t.color(LEAF_DK)}
    for _ in range(400):
        x = random.randrange(40, 220)
        y = random.randrange(12, 70)
        if opaque(x, y) and t.get(x, y) in leaf_set:
            t.set(x, y, random.choice([LEAF_LT2, LEAF_DK, LEAF_LT]))

    # moss
    for mx, my, rx, ry in ((110, 22, 16, 6), (146, 26, 14, 5), (84, 40, 10, 4),
                           (176, 38, 11, 4), (128, 16, 20, 5), (110, 90, 8, 4),
                           (148, 90, 8, 4), (70, 236, 8, 3), (188, 238, 8, 3)):
        t.ellipse(mx, my, rx, ry, MOSS)
        t.ellipse(mx - rx // 3, my - ry // 2, max(1, rx // 2), max(1, ry // 2), MOSS_LT)

    # hanging vines
    def vine(x, y0, length):
        xx = x
        for k in range(length):
            t.set(xx, y0 + k, VINE)
            if k % 4 == 2:
                t.set(xx - 1, y0 + k, VINE)
                t.set(xx + 1, y0 + k + 1, VINE)
            if random.random() < 0.3:
                xx += random.choice((-1, 1))

    for vx, vy, vl in ((80, 60, 30), (100, 64, 44), (150, 64, 38), (172, 58, 30),
                       (192, 62, 24), (66, 52, 22), (206, 60, 20)):
        vine(vx, vy, vl)

    # face
    t.rect(106, 104, 44, 5, BARK_DK2)
    for nx in (110, 118, 126, 134, 142):
        t.set(nx, 109, BARK_DK2)
    t.line(110, 113, 123, 117, '#0e0a06')
    t.line(133, 117, 145, 113, '#0e0a06')
    # eerie green glow pooling around the eyes (opaque)
    t.ellipse(117, 120, 7, 6, '#2c4a1e')
    t.ellipse(139, 120, 7, 6, '#2c4a1e')
    t.ellipse(117, 120, 5, 4, '#3f6a28')
    t.ellipse(139, 120, 5, 4, '#3f6a28')
    t.ellipse(117, 120, 4, 3, SOCKET)
    t.ellipse(139, 120, 4, 3, SOCKET)
    t.ellipse(117, 120, 2, 2, EYE)
    t.ellipse(139, 120, 2, 2, EYE)
    t.set(117, 120, EYE_CORE)
    t.set(139, 120, EYE_CORE)
    t.line(127, 118, 128, 138, BARK_DK)
    t.line(129, 118, 130, 138, BARK_LT2)
    t.line(108, 127, 112, 136, BARK_DK2)
    t.line(147, 127, 143, 136, BARK_DK2)
    # jagged maw
    t.poly([(110, 141), (150, 141), (146, 149), (138, 154), (128, 159),
            (118, 154), (114, 149)], MAW)
    for tx in (113, 121, 129, 137, 143):
        t.poly([(tx, 141), (tx + 4, 141), (tx + 2, 146)], TOOTH)
    for tx in (120, 130, 139):
        t.poly([(tx, 152), (tx + 3, 152), (tx + 1, 148)], '#3a2a16')

    # dark outline against transparency
    t.outline(OUTLINE)

    # ================= FOREGROUND =================
    fg = new_canvas(W, H, name='fg')
    FG = '#0b120a'
    for x in range(0, W, 2):
        if random.random() < 0.75:
            ln = random.randint(3, 9)
            if x < 40 or x > 216:
                ln += random.randint(2, 8)
            bend = random.choice((-1, 0, 1))
            for k in range(ln):
                xx = max(0, min(W - 1, x + (k * bend) // 4))
                fg.set(xx, 255 - k, FG)
    for fx, sgn in ((16, 1), (240, -1)):
        for a in range(-2, 3):
            for k in range(14 + abs(a) * 2):
                xx = max(0, min(W - 1, fx + sgn * (k // 2) + a * (k // 5)))
                fg.set(xx, 255 - k - abs(a), FG)
    for hx, hlen in ((8, 52), (247, 44)):
        xx = hx
        for k in range(hlen):
            fg.set(xx, k, '#0e1a0c')
            if k % 5 == 3:
                fg.set(max(0, xx - 1), k, '#0e1a0c')
                fg.set(min(W - 1, xx + 1), k, '#122409')
            if random.random() < 0.35:
                xx = max(0, min(W - 1, xx + random.choice((-1, 1))))
    fg.poly([(0, 8), (60, 26), (60, 30), (0, 14)], FG)
    for lx, ly in ((30, 20), (46, 26), (58, 30), (18, 15)):
        fg.ellipse(lx, ly, 5, 3, FG)
        fg.set(lx - 2, ly - 1, FG)
    fg.poly([(255, 16), (206, 32), (206, 36), (255, 22)], FG)
    for lx, ly in ((232, 26), (216, 31)):
        fg.ellipse(lx, ly, 4, 3, FG)

    # ================= COMPOSITE =================
    result = flatten([bg, t, fg], name='result')
    print(result.stats_text())

    # ---- observation dumps ----
    print('--- face region ---')
    print(result.matrix_text(region=(100, 100, 160, 162)))
    print('--- base / roots region ---')
    print(result.matrix_text(region=(24, 210, 232, 256)))
    save('ancient-treant-boss', result)
    finish(result)
except Exception:
    traceback.print_exc()
