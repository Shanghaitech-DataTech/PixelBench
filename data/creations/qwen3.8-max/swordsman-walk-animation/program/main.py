# Red-haired swordsman walk cycle -- 64x32 (two 32x32 frames), 16-bit RPG style.

OUTLINE = True
OCOL = '#191322'

PAL = {
    'K': '#191322',
    'H': '#d8402a', 'h': '#ff8352', 'd': '#8e2418',      # hair
    'S': '#f7cb9c', 's': '#cf9463',                      # skin
    'C': '#2e3d84', 'c': '#4f66bb', 'N': '#1b2554',      # cape
    'T': '#8a6238', 't': '#b98a52',                      # tunic / sleeve
    'P': '#4a4f66', 'p': '#343a4e',                      # pants
    'B': '#3b2a1a', 'G': '#e8b23a', 'g': '#a5761c',      # belt / gold
    'O': '#4e3826', 'o': '#2f2116',                      # boots
    'L': '#eef4fa', 'M': '#a9b7c6', 'D': '#6c7a89',      # blade
    'E': '#241a2c',
}


def limb(cv, pts, w, col):
    """Thick polyline: width is added in +x so vertical limbs stay chunky."""
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        for k in range(w):
            cv.line(x0 + k, y0, x1 + k, y1, col)


def draw_char(cv, ox, dy, pose):
    """Draw the swordsman into a 32x32 area whose left edge is ox.
    dy = vertical bounce of the body, pose = 'A' (contact) or 'B' (passing)."""

    # ------------------------------------------------------------------ cape
    if pose == 'A':
        cape = [(ox + 14, 12 + dy), (ox + 19, 13 + dy), (ox + 20, 18 + dy),
                (ox + 18, 23 + dy), (ox + 16, 26 + dy), (ox + 14, 23 + dy),
                (ox + 12, 26 + dy), (ox + 9, 24 + dy), (ox + 7, 20 + dy),
                (ox + 4, 18 + dy), (ox + 7, 16 + dy), (ox + 6, 13 + dy),
                (ox + 10, 12 + dy)]
        shade = [(ox + 8, 19 + dy), (ox + 11, 21 + dy), (ox + 12, 24 + dy),
                 (ox + 12, 26 + dy), (ox + 9, 24 + dy), (ox + 7, 20 + dy)]
        fold = [(ox + 17, 14 + dy), (ox + 19, 18 + dy), (ox + 18, 22 + dy),
                (ox + 16, 18 + dy)]
    else:
        cape = [(ox + 14, 12 + dy), (ox + 19, 13 + dy), (ox + 20, 17 + dy),
                (ox + 19, 21 + dy), (ox + 16, 24 + dy), (ox + 14, 21 + dy),
                (ox + 11, 24 + dy), (ox + 8, 21 + dy), (ox + 5, 18 + dy),
                (ox + 8, 15 + dy), (ox + 7, 12 + dy), (ox + 10, 12 + dy)]
        shade = [(ox + 6, 17 + dy), (ox + 9, 19 + dy), (ox + 11, 22 + dy),
                 (ox + 11, 24 + dy), (ox + 8, 21 + dy), (ox + 5, 18 + dy)]
        fold = [(ox + 17, 14 + dy), (ox + 19, 17 + dy), (ox + 18, 20 + dy),
                (ox + 16, 17 + dy)]
    cv.poly(cape, PAL['C'])
    cv.poly(shade, PAL['N'])
    cv.poly(fold, PAL['c'])

    # ------------------------------------------------------------- far arm
    if pose == 'A':
        limb(cv, [(ox + 15, 14 + dy), (ox + 13, 17 + dy), (ox + 12, 19 + dy)], 2, PAL['p'])
        cv.rect(ox + 11, 19 + dy, 2, 2, PAL['s'])
    else:
        limb(cv, [(ox + 15, 14 + dy), (ox + 14, 17 + dy), (ox + 13, 19 + dy)], 2, PAL['p'])
        cv.rect(ox + 12, 19 + dy, 2, 2, PAL['s'])

    # ------------------------------------------------------------ back leg
    if pose == 'A':
        limb(cv, [(ox + 14, 19), (ox + 11, 23), (ox + 11, 26)], 3, PAL['p'])
        cv.rect(ox + 9, 27, 5, 2, PAL['O'])
        cv.rect(ox + 9, 28, 5, 1, PAL['o'])
    else:
        limb(cv, [(ox + 14, 19), (ox + 18, 23), (ox + 19, 26)], 3, PAL['p'])
        cv.rect(ox + 19, 27, 5, 2, PAL['O'])
        cv.rect(ox + 19, 28, 5, 1, PAL['o'])

    # ----------------------------------------------------------- front leg
    if pose == 'A':
        limb(cv, [(ox + 16, 19), (ox + 20, 23), (ox + 21, 26)], 3, PAL['P'])
        cv.rect(ox + 20, 27, 5, 2, PAL['O'])
        cv.rect(ox + 20, 28, 5, 1, PAL['o'])
    else:
        limb(cv, [(ox + 16, 19), (ox + 13, 23), (ox + 12, 26)], 3, PAL['P'])
        cv.rect(ox + 10, 27, 5, 2, PAL['O'])
        cv.rect(ox + 10, 28, 5, 1, PAL['o'])

    # --------------------------------------------------------------- torso
    cv.poly([(ox + 13, 13 + dy), (ox + 19, 13 + dy), (ox + 19, 18 + dy),
             (ox + 18, 20 + dy), (ox + 13, 20 + dy), (ox + 12, 16 + dy)], PAL['T'])
    cv.poly([(ox + 17, 13 + dy), (ox + 19, 13 + dy), (ox + 19, 18 + dy),
             (ox + 17, 19 + dy)], PAL['t'])          # lit front of chest
    cv.rect(ox + 13, 18 + dy, 6, 1, PAL['B'])        # belt
    cv.set(ox + 17, 18 + dy, PAL['G'])               # buckle
    cv.line(ox + 13, 20 + dy, ox + 18, 20 + dy, PAL['B'])   # tunic hem shade

    # ---------------------------------------------------------------- head
    cv.ellipse(ox + 15, 6 + dy, 4, 3, PAL['H'])      # hair mass
    # spiky top
    cv.poly([(ox + 12, 5 + dy), (ox + 11, 2 + dy), (ox + 15, 4 + dy)], PAL['H'])
    cv.poly([(ox + 16, 4 + dy), (ox + 18, 2 + dy), (ox + 19, 5 + dy)], PAL['H'])
    # hair streaming back (to the left)
    if pose == 'A':
        cv.poly([(ox + 11, 5 + dy), (ox + 6, 6 + dy), (ox + 10, 8 + dy),
                 (ox + 5, 10 + dy), (ox + 11, 10 + dy)], PAL['H'])
        cv.poly([(ox + 10, 7 + dy), (ox + 7, 8 + dy), (ox + 10, 9 + dy)], PAL['d'])
    else:
        cv.poly([(ox + 11, 5 + dy), (ox + 5, 5 + dy), (ox + 10, 8 + dy),
                 (ox + 6, 11 + dy), (ox + 11, 10 + dy)], PAL['H'])
        cv.poly([(ox + 10, 7 + dy), (ox + 7, 7 + dy), (ox + 10, 9 + dy)], PAL['d'])
    # face
    cv.rect(ox + 15, 7 + dy, 5, 3, PAL['S'])
    cv.rect(ox + 16, 10 + dy, 3, 1, PAL['S'])        # chin
    cv.set(ox + 20, 8 + dy, PAL['S'])                # nose
    cv.set(ox + 19, 9 + dy, PAL['s'])                # cheek shade
    cv.rect(ox + 15, 9 + dy, 1, 2, PAL['s'])         # jaw / ear shade
    # fringe over the brow
    cv.rect(ox + 14, 5 + dy, 6, 2, PAL['H'])
    cv.set(ox + 19, 7 + dy, PAL['H'])
    cv.set(ox + 13, 5 + dy, PAL['h'])                # hair highlight
    cv.set(ox + 14, 4 + dy, PAL['h'])
    cv.set(ox + 12, 6 + dy, PAL['h'])
    # eyes last so nothing covers them
    cv.set(ox + 18, 8 + dy, PAL['E'])
    cv.set(ox + 19, 8 + dy, PAL['E'])
    # neck
    cv.rect(ox + 15, 11 + dy, 3, 1, PAL['s'])

    # ------------------------------------------------------------ near arm
    if pose == 'A':
        limb(cv, [(ox + 16, 14 + dy), (ox + 18, 16 + dy), (ox + 19, 18 + dy)], 2, PAL['t'])
        cv.rect(ox + 19, 17 + dy, 2, 2, PAL['S'])
        hx, hy2 = ox + 19, 18 + dy
    else:
        limb(cv, [(ox + 16, 14 + dy), (ox + 18, 17 + dy), (ox + 18, 19 + dy)], 2, PAL['t'])
        cv.rect(ox + 18, 18 + dy, 2, 2, PAL['S'])
        hx, hy2 = ox + 18, 19 + dy

    # ---------------------------------------------------------------- sword
    cv.line(hx - 1, hy2 + 1, hx, hy2, PAL['B'])      # grip
    cv.set(hx - 2, hy2 + 2, PAL['G'])                # pommel
    cv.line(hx, hy2 - 2, hx + 2, hy2, PAL['G'])      # cross guard
    cv.line(hx + 1, hy2 - 2, hx + 2, hy2 - 1, PAL['g'])
    bx, by = hx + 2, hy2 - 2
    cv.line(bx, by, bx + 8, by - 8, PAL['L'])        # blade bright edge
    cv.line(bx, by + 1, bx + 7, by - 6, PAL['M'])    # blade body
    cv.set(bx + 9, by - 9, PAL['L'])                 # tip
    cv.set(bx + 8, by - 7, PAL['D'])                 # edge shade


def build_frame(pose, dy):
    tmp = new_canvas(32, 32, name='tmp_' + pose)
    draw_char(tmp, 0, dy, pose)
    if not OUTLINE:
        return tmp
    ol = tmp.copy(name='ol_' + pose)
    ol.outline(OCOL)
    out = new_canvas(32, 32, name='out_' + pose)
    for ddx, ddy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        out.blit(ol, ddx, ddy)
    out.blit(tmp, 0, 0)
    return out


fa = build_frame('A', 0)
fb = build_frame('B', 0)

result = new_canvas(64, 32, name='swordsman_walk')
result.blit(fa, 0, 0)
result.blit(fb, 32, 0)

print(result.stats_text())
print("=== frame A head ===")
print(fa.matrix_text(region=(13, 3, 24, 14)))
print("=== frame B head ===")
print(fb.matrix_text(region=(13, 3, 24, 14)))
view(result, scale=8)
view(fa, scale=12, margin=0)
view(fb, scale=12, margin=0)
save('swordsman_walk', result)
finish(result)
