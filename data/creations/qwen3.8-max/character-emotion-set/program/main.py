# Character emotion set - 64x64, 2x2 grid of big-head portraits.
# Each portrait is drawn on a 34x34 scratch canvas (content in local 0..29 at
# offset 2,2), outlined, then blitted into its quadrant.

OUT     = '#221a2e'
SKIN    = '#f7cda4'
SKIN_SH = '#dda377'
NOSE    = '#c9825c'
HAIR    = '#2f9c8a'
HAIR_HI = '#74e0c8'
HAIR_SH = '#1b6559'
CLOTH   = '#4a5bc7'
CLOTH_SH= '#323f9c'
COLLAR  = '#f2efe4'
COLLAR_SH='#c8c4b6'
EYE_W   = '#fdfdff'
IRIS    = '#e08b2e'
MOUTH   = '#8c3b34'
MOUTH_DK= '#571f1e'
TONGUE  = '#d4695e'
BLUSH   = '#ef9a86'
BROW    = '#1b6559'


def sp(c, ox, oy, data, col):
    """data = list of (y, x0, x1) inclusive horizontal spans."""
    for y, x0, x1 in data:
        c.rect(ox + x0, oy + y, x1 - x0 + 1, 1, col)


def px(c, ox, oy, pts, col):
    for x, y in pts:
        c.set(ox + x, oy + y, col)


HEAD = [(4, 10, 19), (5, 8, 21), (6, 7, 22), (7, 6, 23), (8, 5, 24),
        (9, 5, 24), (10, 5, 24), (11, 5, 24), (12, 5, 24), (13, 5, 24),
        (14, 5, 24), (15, 5, 24), (16, 5, 24), (17, 5, 24), (18, 5, 24),
        (19, 6, 23), (20, 7, 22), (21, 9, 20), (22, 11, 18)]

HAIR_MASS = [(2, 11, 18), (3, 9, 20), (4, 8, 21), (5, 7, 22), (6, 6, 23),
             (7, 5, 24), (8, 5, 24),
             (9, 5, 7), (9, 13, 16), (9, 22, 24),
             (10, 5, 6), (10, 14, 15), (10, 23, 24),
             (11, 5, 6), (11, 23, 24),
             (12, 5, 6), (12, 23, 24),
             (13, 5, 6), (13, 23, 24),
             (14, 5, 6), (14, 23, 24),
             (15, 5, 6), (15, 23, 24),
             (16, 5, 6), (16, 23, 24)]

HAIR_LIT = [(4, 10, 13), (5, 8, 11), (6, 7, 9), (7, 6, 7), (5, 19, 20), (6, 20, 21)]

HAIR_DARK = [(8, 8, 21)] + [(y, 6, 6) for y in range(10, 17)] + [(y, 23, 23) for y in range(10, 17)]

JACKET = [(25, 8, 21), (26, 6, 23), (27, 5, 24), (28, 4, 25), (29, 3, 26)]
JACKET_SH = [(27, 22, 24), (28, 21, 25), (29, 20, 26), (26, 21, 23)]
SHIRT = [(25, 10, 19), (26, 11, 18), (27, 12, 17), (28, 13, 16), (29, 14, 15)]
SHIRT_SH = [(26, 11, 11), (26, 18, 18), (27, 12, 12), (27, 17, 17),
            (28, 13, 13), (28, 16, 16), (29, 14, 14)]


def base(c, ox, oy):
    # neck (behind head)
    sp(c, ox, oy, [(y, 12, 17) for y in range(21, 26)], SKIN_SH)
    sp(c, ox, oy, [(23, 12, 17)], NOSE)
    # torso
    sp(c, ox, oy, JACKET, CLOTH)
    sp(c, ox, oy, JACKET_SH, CLOTH_SH)
    sp(c, ox, oy, SHIRT, COLLAR)
    sp(c, ox, oy, SHIRT_SH, COLLAR_SH)
    # ears
    sp(c, ox, oy, [(y, 3, 5) for y in range(14, 18)], SKIN)
    sp(c, ox, oy, [(y, 24, 26) for y in range(14, 18)], SKIN)
    px(c, ox, oy, [(4, 16), (25, 16)], SKIN_SH)
    # head
    sp(c, ox, oy, HEAD, SKIN)
    # fringe cast shadow on forehead
    sp(c, ox, oy, [(9, 8, 12), (9, 17, 21)], SKIN_SH)
    # hair
    sp(c, ox, oy, HAIR_MASS, HAIR)
    sp(c, ox, oy, HAIR_DARK, HAIR_SH)
    sp(c, ox, oy, HAIR_LIT, HAIR_HI)
    # nose (shared by every emotion)
    px(c, ox, oy, [(14, 17), (15, 17)], NOSE)


def calm(c, ox, oy):
    # flat relaxed brows
    sp(c, ox, oy, [(12, 8, 12), (12, 17, 21)], BROW)
    # half-lidded eyes
    sp(c, ox, oy, [(14, 8, 12), (14, 17, 21)], OUT)
    sp(c, ox, oy, [(15, 8, 12), (16, 8, 12)], EYE_W)
    sp(c, ox, oy, [(15, 17, 21), (16, 17, 21)], EYE_W)
    sp(c, ox, oy, [(15, 9, 11), (16, 9, 11)], IRIS)
    sp(c, ox, oy, [(15, 18, 20), (16, 18, 20)], IRIS)
    px(c, ox, oy, [(10, 15), (19, 15)], EYE_W)
    sp(c, ox, oy, [(18, 9, 11), (18, 18, 20)], SKIN_SH)
    # small closed mouth
    sp(c, ox, oy, [(19, 12, 17)], MOUTH)
    sp(c, ox, oy, [(20, 13, 16)], SKIN_SH)


def smiling(c, ox, oy):
    # raised arched brows
    px(c, ox, oy, [(8, 12), (9, 11), (10, 11), (11, 11), (12, 12)], BROW)
    px(c, ox, oy, [(17, 12), (18, 11), (19, 11), (20, 11), (21, 12)], BROW)
    # happy closed eyes (upward domes)
    sp(c, ox, oy, [(15, 9, 11), (16, 8, 12)], OUT)
    sp(c, ox, oy, [(15, 18, 20), (16, 17, 21)], OUT)
    sp(c, ox, oy, [(17, 9, 11), (17, 18, 20)], SKIN_SH)
    # blushing cheeks
    sp(c, ox, oy, [(17, 7, 8), (18, 7, 9)], BLUSH)
    sp(c, ox, oy, [(17, 21, 22), (18, 20, 22)], BLUSH)
    # open grin
    sp(c, ox, oy, [(18, 11, 18), (19, 11, 18), (20, 12, 17)], MOUTH_DK)
    sp(c, ox, oy, [(18, 12, 17)], EYE_W)
    sp(c, ox, oy, [(20, 13, 16)], TONGUE)


def angry(c, ox, oy):
    # eyes first so the slanted brows cut over them
    sp(c, ox, oy, [(14, 8, 12), (14, 17, 21)], OUT)
    sp(c, ox, oy, [(15, 8, 9), (16, 8, 12), (17, 8, 12)], EYE_W)
    sp(c, ox, oy, [(15, 20, 21), (16, 17, 21), (17, 17, 21)], EYE_W)
    sp(c, ox, oy, [(15, 10, 12), (15, 17, 19)], OUT)
    sp(c, ox, oy, [(16, 9, 11), (17, 9, 11)], IRIS)
    sp(c, ox, oy, [(16, 18, 20), (17, 18, 20)], IRIS)
    px(c, ox, oy, [(8, 15), (21, 15), (10, 16), (19, 16)], EYE_W)
    # heavy slanted brows
    for o in (0, 1):
        c.line(ox + 7, oy + 10 + o, ox + 12, oy + 13 + o, BROW)
        c.line(ox + 22, oy + 10 + o, ox + 17, oy + 13 + o, BROW)
    # flushed cheeks
    sp(c, ox, oy, [(18, 7, 9), (18, 20, 22)], BLUSH)
    # gritted teeth scowl
    sp(c, ox, oy, [(19, 11, 18), (20, 12, 17)], MOUTH_DK)
    sp(c, ox, oy, [(19, 12, 17)], EYE_W)


def surprised(c, ox, oy):
    # high arched brows (two rows thick)
    for o in (0, 1):
        px(c, ox, oy, [(7 + o, 11), (8 + o, 10), (9 + o, 10), (10 + o, 10), (11 + o, 10), (12 + o, 11)], BROW)
        px(c, ox, oy, [(22 - o, 11), (21 - o, 10), (20 - o, 10), (19 - o, 10), (18 - o, 10), (17 - o, 11)], BROW)
    # wide open eyes
    sp(c, ox, oy, [(13, 8, 12), (13, 17, 21)], OUT)
    sp(c, ox, oy, [(14, 8, 12), (15, 8, 12), (16, 8, 12), (17, 9, 11)], EYE_W)
    sp(c, ox, oy, [(14, 17, 21), (15, 17, 21), (16, 17, 21), (17, 18, 20)], EYE_W)
    sp(c, ox, oy, [(15, 9, 11), (16, 9, 11)], IRIS)
    sp(c, ox, oy, [(15, 18, 20), (16, 18, 20)], IRIS)
    px(c, ox, oy, [(10, 15), (10, 16), (19, 15), (19, 16)], OUT)
    px(c, ox, oy, [(9, 15), (18, 15)], EYE_W)
    # small round open mouth
    sp(c, ox, oy, [(18, 14, 15), (19, 13, 16), (20, 13, 16), (21, 14, 15)], MOUTH_DK)


FACES = {'calm': calm, 'smiling': smiling, 'angry': angry, 'surprised': surprised}


def portrait(emo):
    t = new_canvas(34, 34, name='scratch_' + emo)
    base(t, 2, 2)
    FACES[emo](t, 2, 2)
    t.outline(OUT)
    return t


result = new_canvas(64, 64, name='emotion_set')
for emo, cx, cy in [('calm', 1, 1), ('smiling', 33, 1),
                    ('angry', 1, 33), ('surprised', 33, 33)]:
    result.blit(portrait(emo), cx - 2, cy - 2)

print(result.stats_text())
view(result)
save('emotion_set', result, indexed=True)
finish(result)
