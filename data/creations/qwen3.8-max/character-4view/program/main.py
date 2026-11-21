# Cheerleader character sheet - 4 views in a 2x2 grid on 64x64
# top-left: front, top-right: back, bottom-left: left side, bottom-right: right side

OUTLINE = '#241529'

PAL = {
    'o':   OUTLINE,      # dark outline
    'sk':  '#f7cda6',    # skin
    'skd': '#dda87e',    # skin shadow
    'hr':  '#f2bb4f',    # hair (blonde)
    'hrd': '#c0822c',    # hair dark
    'rd':  '#e0443c',    # red top / shoes
    'rdd': '#a52b2c',    # red dark
    'wh':  '#f7f7f7',    # white skirt / socks
    'whd': '#c9d0dc',    # white shadow
    'pm':  '#ffd83d',    # pom pom
    'pmd': '#e0a52a',    # pom pom dark
    'pml': '#fff4ab',    # pom pom light
    'bl':  '#ef9b9b',    # blush
    'mo':  '#b8485a',    # mouth
}
KEYS = ('o', 'sk', 'skd', 'hr', 'hrd', 'rd', 'rdd', 'wh', 'whd',
        'pm', 'pmd', 'pml', 'bl', 'mo')


def solid(col):
    """Palette dict where every role maps to one colour (for silhouettes)."""
    return {k: col for k in KEYS}


def helpers(c, ox, oy):
    def r(x, y, w, h, col):
        return c.rect(ox + x, oy + y, w, h, col)

    def s(x, y, col):
        return c.set(ox + x, oy + y, col)

    def l(x0, y0, x1, y1, col):
        return c.line(ox + x0, oy + y0, ox + x1, oy + y1, col)

    def ci(cx, cy, rad, col):
        return c.circle(ox + cx, oy + cy, rad, col)

    def po(pts, col, fill=True):
        return c.poly([(ox + a, oy + b) for a, b in pts], col, fill=fill)

    def halo(pts, col):
        """Draw a polygon dilated by 1px in all 8 directions (local outline)."""
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    c.poly([(ox + a + dx, oy + b + dy) for a, b in pts], col, fill=True)
    return r, s, l, ci, po, halo


def pompom(c, P, ox, oy, cx, cy, far=False):
    r, s, l, ci, po, halo = helpers(c, ox, oy)
    base = P['pmd'] if far else P['pm']
    lite = P['pm'] if far else P['pml']
    ci(cx, cy, 3, base)
    for dx, dy in ((3, 3), (-3, 3), (3, -3), (-3, -3)):
        s(cx + dx, cy + dy, base)
    # highlight upper-left
    s(cx - 1, cy - 2, lite)
    s(cx - 2, cy - 1, lite)
    s(cx, cy - 1, lite)
    s(cx - 1, cy - 1, lite)
    # shadow lower-right
    if not far:
        s(cx + 1, cy + 2, P['pmd'])
        s(cx + 2, cy + 1, P['pmd'])
        s(cx, cy + 2, P['pmd'])


# ---------------------------------------------------------------- front view
def front_view(c, P, ox=0, oy=0):
    r, s, l, ci, po, halo = helpers(c, ox, oy)
    o, sk, skd = P['o'], P['sk'], P['skd']
    hr, hrd = P['hr'], P['hrd']
    rd, rdd = P['rd'], P['rdd']
    wh, whd = P['wh'], P['whd']

    # legs
    r(12, 25, 3, 4, sk)
    r(17, 25, 3, 4, sk)
    s(14, 25, skd); s(14, 26, skd)
    s(17, 25, skd); s(17, 26, skd)
    # socks
    r(12, 27, 3, 2, wh); r(17, 27, 3, 2, wh)
    r(12, 27, 3, 1, rd); r(17, 27, 3, 1, rd)
    # shoes
    r(10, 29, 5, 2, rd); r(17, 29, 5, 2, rd)
    r(10, 30, 5, 1, wh); r(17, 30, 5, 1, wh)
    s(13, 29, wh); s(18, 29, wh)

    # arms (behind torso)
    l(11, 15, 6, 9, sk); l(12, 16, 7, 8, sk)
    l(20, 15, 25, 9, sk); l(19, 16, 24, 8, sk)

    # torso
    r(11, 13, 10, 7, sk)          # skin base (shoulders + midriff)
    r(11, 14, 10, 5, rd)          # top
    r(14, 14, 4, 1, sk)           # neckline
    r(19, 15, 2, 3, rdd)          # right side shade
    r(11, 18, 10, 1, wh)          # white hem band
    # star emblem
    r(15, 15, 2, 1, wh)
    r(13, 16, 6, 1, wh)
    r(14, 17, 4, 1, wh)
    s(13, 17, wh); s(18, 17, wh)

    # skirt
    po([(11, 20), (20, 20), (22, 24), (9, 24)], wh)
    l(13, 20, 11, 23, whd)
    l(18, 20, 20, 23, whd)
    l(15, 20, 15, 23, whd)
    l(16, 20, 16, 23, whd)
    r(9, 24, 14, 1, rd)
    s(10, 23, whd); s(21, 23, whd)

    # neck
    r(14, 10, 4, 3, sk)
    r(14, 11, 4, 1, skd)

    # head
    r(11, 3, 10, 7, hr)
    r(12, 2, 8, 1, hr)
    r(12, 10, 8, 1, hr)
    r(12, 6, 8, 4, sk)            # face
    r(13, 10, 6, 1, sk)           # jaw
    r(12, 5, 8, 1, hr)            # fringe line
    s(12, 6, hr); s(13, 6, hr); s(19, 6, hr)
    r(11, 3, 1, 8, hrd)           # side hair dark
    r(20, 3, 1, 8, hrd)
    s(13, 3, hrd); s(17, 3, hrd); s(15, 2, hrd)
    # face details
    r(13, 7, 1, 2, o); r(18, 7, 1, 2, o)
    s(12, 9, P['bl']); s(19, 9, P['bl'])
    r(15, 9, 2, 1, P['mo'])

    # (single centre ponytail hides behind the head in this view)

    # pom poms on top
    pompom(c, P, ox, oy, 6, 6)
    pompom(c, P, ox, oy, 25, 6)


# ----------------------------------------------------------------- back view
def back_view(c, P, ox=0, oy=0):
    r, s, l, ci, po, halo = helpers(c, ox, oy)
    o, sk, skd = P['o'], P['sk'], P['skd']
    hr, hrd = P['hr'], P['hrd']
    rd, rdd = P['rd'], P['rdd']
    wh, whd = P['wh'], P['whd']

    # legs
    r(12, 25, 3, 4, sk)
    r(17, 25, 3, 4, sk)
    s(14, 25, skd); s(14, 26, skd)
    s(17, 25, skd); s(17, 26, skd)
    # socks
    r(12, 27, 3, 2, wh); r(17, 27, 3, 2, wh)
    r(12, 27, 3, 1, rd); r(17, 27, 3, 1, rd)
    # shoes (seen from behind)
    r(11, 29, 4, 2, rd); r(17, 29, 4, 2, rd)
    r(11, 30, 4, 1, wh); r(17, 30, 4, 1, wh)
    s(12, 29, rdd); s(19, 29, rdd)

    # arms
    l(11, 15, 6, 9, sk); l(12, 16, 7, 8, sk)
    l(20, 15, 25, 9, sk); l(19, 16, 24, 8, sk)

    # torso
    r(11, 13, 10, 7, sk)
    r(11, 14, 10, 5, rd)
    r(14, 14, 4, 1, sk)           # back neckline
    r(19, 15, 2, 3, rdd)
    r(11, 18, 10, 1, wh)
    r(13, 16, 6, 1, rdd)          # subtle back seam

    # skirt
    po([(11, 20), (20, 20), (22, 24), (9, 24)], wh)
    l(13, 20, 11, 23, whd)
    l(18, 20, 20, 23, whd)
    l(15, 20, 15, 23, whd)
    l(16, 20, 16, 23, whd)
    r(9, 24, 14, 1, rd)

    # neck (shadowed from behind)
    r(14, 10, 4, 3, skd)

    # head: all hair
    r(11, 3, 10, 7, hr)
    r(12, 2, 8, 1, hr)
    r(12, 10, 8, 1, hr)
    r(11, 3, 1, 8, hrd)
    r(20, 3, 1, 8, hrd)
    s(13, 4, hrd); s(17, 4, hrd); s(15, 3, hrd)
    l(12, 9, 19, 9, hrd)

    # ponytail hanging down the back (own local outline)
    tail = [(14, 3), (17, 3), (18, 6), (19, 11), (17, 16), (15, 17),
            (13, 15), (13, 10), (13, 6)]
    halo(tail, o)
    po(tail, hr)
    r(13, 5, 6, 1, rd)            # hair band
    r(14, 4, 4, 1, rd)
    l(15, 7, 15, 15, hrd)
    l(17, 8, 16, 14, hrd)
    s(14, 12, hrd); s(16, 11, hrd)

    pompom(c, P, ox, oy, 6, 6)
    pompom(c, P, ox, oy, 25, 6)


# ------------------------------------------------------- left side (profile)
def left_view(c, P, ox=0, oy=0):
    r, s, l, ci, po, halo = helpers(c, ox, oy)
    o, sk, skd = P['o'], P['sk'], P['skd']
    hr, hrd = P['hr'], P['hrd']
    rd, rdd = P['rd'], P['rdd']
    wh, whd = P['wh'], P['whd']

    # far pom + far arm (deepest, drawn first, shaded)
    l(19, 14, 24, 7, skd)
    l(19, 15, 25, 8, skd)
    pompom(c, P, ox, oy, 25, 5, far=True)

    # legs
    r(15, 25, 3, 4, skd)          # far leg
    r(11, 25, 4, 4, sk)           # near leg
    s(14, 25, skd); s(14, 26, skd)
    # socks
    r(15, 27, 3, 2, whd); r(11, 27, 4, 2, wh)
    r(11, 27, 4, 1, rd); r(15, 27, 3, 1, rdd)
    # shoes pointing left
    r(13, 29, 6, 2, rdd)          # far shoe
    r(9, 29, 6, 2, rd)            # near shoe
    r(9, 30, 6, 1, wh)
    r(14, 30, 5, 1, whd)
    s(11, 29, wh)

    # torso
    r(12, 13, 8, 7, sk)
    r(13, 14, 7, 5, rd)
    s(12, 15, sk); s(12, 16, sk)
    r(19, 15, 1, 3, rdd)
    r(13, 18, 7, 1, wh)
    s(12, 17, rd)                 # bust
    s(11, 16, rd)

    # skirt (profile, flares both ways)
    po([(12, 20), (19, 20), (21, 24), (9, 24)], wh)
    l(14, 20, 12, 23, whd)
    l(17, 20, 19, 23, whd)
    r(9, 24, 13, 1, rd)

    # neck
    r(14, 10, 4, 3, sk)
    r(17, 11, 1, 2, skd)

    # head profile (facing left)
    r(12, 3, 8, 7, hr)            # hair mass
    r(13, 2, 6, 1, hr)            # crown
    r(12, 10, 8, 1, hr)
    r(12, 5, 5, 5, sk)            # face  x12..16 y5..9
    r(13, 10, 4, 1, sk)           # jaw
    s(11, 7, sk)                  # nose
    r(17, 3, 3, 8, hrd)           # back of hair darker
    r(12, 4, 5, 1, hr)            # fringe
    s(12, 5, hr); s(13, 5, hr)
    s(16, 4, hrd)
    # face details
    s(13, 6, o); s(13, 7, o)      # eye
    s(14, 8, P['bl'])             # blush
    s(12, 9, P['mo'])             # mouth

    # ponytail behind, hanging down over the back
    tail = [(17, 4), (20, 6), (21, 10), (20, 14), (18, 15), (17, 11), (16, 7)]
    halo(tail, o)
    po(tail, hr)
    s(18, 5, rd); s(19, 6, rd)    # hair band
    l(19, 8, 19, 13, hrd)

    # near arm + pom (frontmost)
    l(13, 15, 7, 8, sk)
    l(12, 14, 6, 9, sk)
    pompom(c, P, ox, oy, 6, 6)


# ------------------------------------------------------------------- assembly
def build(view_fn):
    sil = new_canvas(32, 32)
    art = new_canvas(32, 32)
    OP = solid(OUTLINE)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            view_fn(sil, OP, dx, dy)
    view_fn(art, PAL, 0, 0)
    return flatten([sil, art])


front_q = build(front_view)
back_q = build(back_view)
left_q = build(left_view)
right_q = left_q.copy(name="right")
right_q.mirror(axis="h")

result = new_canvas(64, 64, name="cheerleader_4view")
result.blit(front_q, 0, 0)
result.blit(back_q, 32, 0)
result.blit(left_q, 0, 32)
result.blit(right_q, 32, 32)

print(result.stats_text())
view(result)
save('cheerleader_4view', result)
finish(result)
