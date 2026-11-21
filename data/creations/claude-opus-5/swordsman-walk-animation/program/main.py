OUTL = '#241a26'
SKIN = '#f0c090'
SKIN_S = '#c08860'
HAIR = '#d8381c'
HAIR_D = '#9c2410'
HAIR_L = '#f07840'
TUNIC = '#3f7f4f'
TUNIC_L = '#58a066'
TUNIC_D = '#255238'
CAPE = '#1e2e62'
CAPE_D = '#121c3c'
CAPE_L = '#36509a'
BELT = '#7a5428'
PANTS = '#5a648a'
PANTS_D = '#2e3450'
BOOT = '#6a4420'
BOOT_D = '#44290f'
BLADE_L = '#e8f0ff'
BLADE = '#a8b6cc'
BLADE_D = '#5a6680'
GOLD = '#dcac34'
GOLD_D = '#9a7212'
EYE = '#2a1c2a'


def hl(c, x0, x1, y, col):
    c.rect(x0, y, x1 - x0 + 1, 1, col)


def draw_cape(c, pose, dy):
    if pose == 0:
        pts = [(16, 12 + dy), (13, 13 + dy), (11, 17), (9, 22), (10, 26),
               (13, 25), (15, 20), (17, 15 + dy)]
        c.poly(pts, CAPE, fill=True)
        c.poly(pts, CAPE_D, fill=False)
        c.line(15, 16 + dy, 12, 24, CAPE_L)
        c.line(14, 18, 12, 22, CAPE_D)
    else:
        pts = [(16, 12 + dy), (13, 13 + dy), (11, 18), (11, 23), (13, 26),
               (15, 22), (17, 15 + dy)]
        c.poly(pts, CAPE, fill=True)
        c.poly(pts, CAPE_D, fill=False)
        c.line(15, 16 + dy, 13, 24, CAPE_L)
        c.line(14, 19, 13, 22, CAPE_D)


def draw_head(c, dy):
    hl(c, 14, 19, 4 + dy, HAIR)
    hl(c, 13, 20, 5 + dy, HAIR)
    hl(c, 13, 20, 6 + dy, HAIR)
    hl(c, 13, 17, 7 + dy, HAIR)
    hl(c, 18, 20, 7 + dy, SKIN)
    hl(c, 13, 15, 8 + dy, HAIR)
    hl(c, 16, 20, 8 + dy, SKIN)
    c.set(19, 8 + dy, EYE)
    hl(c, 13, 14, 9 + dy, HAIR)
    hl(c, 15, 20, 9 + dy, SKIN)
    c.set(21, 9 + dy, SKIN)
    hl(c, 13, 14, 10 + dy, HAIR_D)
    hl(c, 15, 20, 10 + dy, SKIN)
    c.set(20, 10 + dy, SKIN_S)
    hl(c, 13, 14, 11 + dy, HAIR_D)
    hl(c, 15, 19, 11 + dy, SKIN)
    hl(c, 15, 18, 4 + dy, HAIR_L)
    c.set(14, 5 + dy, HAIR_L)
    c.set(13, 6 + dy, HAIR_L)
    hl(c, 16, 18, 12 + dy, SKIN_S)


def draw_torso(c, dy):
    for y in range(13, 19):
        x0 = 14 if y < 17 else 15
        hl(c, x0, 20, y + dy, TUNIC)
    hl(c, 17, 19, 13 + dy, TUNIC_L)
    c.set(19, 14 + dy, TUNIC_L)
    for y in range(13, 19):
        c.set(14 if y < 17 else 15, y + dy, TUNIC_D)
    hl(c, 15, 20, 19 + dy, BELT)
    c.set(19, 19 + dy, GOLD_D)
    hl(c, 15, 20, 20 + dy, PANTS)
    hl(c, 15, 20, 21 + dy, PANTS)
    c.set(16, 12 + dy, GOLD)
    c.set(17, 12 + dy, GOLD_D)


def draw_frame(pose):
    """Body only; the sword is added after outlining."""
    c = new_canvas(32, 32, name='b%d' % pose)
    dy = 0 if pose == 0 else -1
    draw_cape(c, pose, dy)
    if pose == 0:
        # rear leg trailing back
        hl(c, 16, 17, 22, PANTS_D)
        hl(c, 15, 16, 23, PANTS_D)
        hl(c, 14, 15, 24, PANTS_D)
        hl(c, 13, 14, 25, PANTS_D)
        hl(c, 12, 13, 26, PANTS_D)
        hl(c, 12, 13, 27, PANTS_D)
        hl(c, 10, 14, 28, BOOT_D)
        hl(c, 10, 14, 29, BOOT_D)
        # front leg forward, heel landing
        hl(c, 19, 20, 22, PANTS)
        hl(c, 20, 21, 23, PANTS)
        hl(c, 21, 22, 24, PANTS)
        hl(c, 21, 22, 25, PANTS)
        hl(c, 21, 22, 26, PANTS)
        hl(c, 20, 23, 27, BOOT)
        hl(c, 20, 24, 28, BOOT)
        hl(c, 20, 24, 29, BOOT_D)
    else:
        # rear leg straight under the body, carrying the weight
        for y in range(21, 27):
            hl(c, 15, 17, y, PANTS_D)
        hl(c, 14, 18, 27, BOOT_D)
        hl(c, 13, 18, 28, BOOT_D)
        hl(c, 13, 18, 29, BOOT_D)
        # front leg lifted and passing forward
        hl(c, 19, 20, 21, PANTS)
        hl(c, 19, 21, 22, PANTS)
        hl(c, 20, 21, 23, PANTS)
        hl(c, 20, 21, 24, PANTS)
        hl(c, 20, 21, 25, PANTS)
        hl(c, 20, 23, 26, BOOT)
        hl(c, 20, 24, 27, BOOT)
        hl(c, 21, 24, 28, BOOT_D)
        # keep the two legs readable where they meet
        c.set(18, 21, OUTL)
        c.set(18, 22, OUTL)
        c.set(19, 23, OUTL)
        c.set(19, 24, OUTL)
        c.set(19, 25, OUTL)
        c.set(19, 26, OUTL)
    draw_torso(c, dy)
    draw_head(c, dy)
    # rear arm swings opposite the front leg
    if pose == 0:
        c.set(14, 13, TUNIC_D)
        c.set(13, 14, TUNIC_D)
        c.set(13, 15, TUNIC_D)
        c.set(13, 16, SKIN_S)
    else:
        c.set(15, 13, TUNIC_D)
        c.set(15, 14, TUNIC_D)
        c.set(16, 15, TUNIC_D)
        c.set(16, 16, SKIN_S)
    # sword arm
    if pose == 0:
        c.set(20, 15, TUNIC_L)
        c.set(21, 16, TUNIC)
        c.set(21, 17, SKIN_S)
    else:
        c.set(20, 14, TUNIC_L)
        c.set(21, 15, TUNIC)
        c.set(21, 16, SKIN_S)
    return c


def draw_sword(c, hx, hy):
    # fist
    c.rect(hx - 1, hy, 2, 2, SKIN)
    c.set(hx - 1, hy + 1, SKIN_S)
    c.set(hx - 2, hy, OUTL)
    c.set(hx - 2, hy + 2, OUTL)
    hl(c, hx - 1, hx + 1, hy + 2, OUTL)
    c.set(hx - 1, hy - 1, OUTL)
    # pommel and crossguard
    c.set(hx + 1, hy - 1, GOLD)
    c.set(hx + 1, hy, GOLD)
    c.set(hx + 1, hy + 1, GOLD_D)
    c.set(hx + 2, hy + 1, OUTL)
    # long blade, 45 degrees up-right
    for i in range(6):
        x = hx + 2 + i
        y = hy - 1 - i
        c.set(x, y, BLADE_L)
        c.set(x, y + 1, BLADE)
        c.set(x, y + 2, BLADE_D)
    c.set(hx + 8, hy - 7, BLADE_L)
    c.set(hx + 8, hy - 6, BLADE_D)


def outlined(fig, name):
    pal = {p['index']: p['rgba'] for p in fig.palette()}
    sil = new_canvas(32, 32, name=name + '_sil')
    for y in range(32):
        for x in range(32):
            rgba = pal.get(fig.get(x, y))
            if rgba and rgba[3] > 0:
                sil.set(x, y, OUTL)
    base = new_canvas(32, 32, name=name)
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        base.blit(sil, dx, dy)
    base.blit(fig, 0, 0)
    return base


frames = []
for pose in (0, 1):
    g = outlined(draw_frame(pose), 'g%d' % pose)
    draw_sword(g, 22, 18 if pose == 0 else 17)
    frames.append(g)

result = new_canvas(64, 32, name='output')
result.blit(frames[0], 0, 0)
result.blit(frames[1], 32, 0)

view(result)
view(frames[0])
view(frames[1])
print(result.stats_text())
save('swordsman-walk', result)
finish(result)
