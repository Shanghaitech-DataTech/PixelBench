# Edit task: add vines and a cloaked mage with a glowing staff at the tower archway.
output = input_canvas.copy(name='output')

# ---- register palette colours ----
cloak_main = output.color((70, 40, 96), name='cloak_main')
cloak_shadow = output.color((44, 24, 62), name='cloak_shadow')
cloak_highlight = output.color((122, 80, 155), name='cloak_highlight')
staff_wood = output.color((96, 66, 38), name='staff_wood')
staff_dark = output.color((56, 40, 24), name='staff_dark')
glow_far = output.color((74, 158, 184), name='glow_far')
glow_mid = output.color((140, 220, 240), name='glow_mid')
glow_near = output.color((210, 245, 252), name='glow_near')
glow_core = output.color((255, 255, 250), name='glow_core')
vine_stem = output.color((34, 96, 52), name='vine_stem')
vine_leaf = output.color((72, 152, 72), name='vine_leaf')
vine_leaf2 = output.color((112, 192, 96), name='vine_leaf2')
foot = output.color((18, 16, 20), name='foot')
shadow = output.color((10, 20, 15), name='mage_shadow')


def vine(c, pts, stem, leaf1, leaf2):
    """Winding stem with leaf clusters."""
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        c.line(x0, y0, x1, y1, stem)
        c.line(x0 + 1, y0, x1 + 1, y1, stem)
        mx, my = (x0 + x1) // 2, (y0 + y1) // 2
        side = 1 if i % 2 == 0 else -1
        c.ellipse(mx + side * 3, my, 2, 1, leaf1)
        c.ellipse(mx + side * 4, my - 2, 1, 2, leaf2)
        c.ellipse(mx - side * 3, my + 2, 2, 1, leaf1)
    for i, (x, y) in enumerate(pts):
        side = 1 if i % 2 == 0 else -1
        c.ellipse(x + side * 3, y, 2, 1, leaf1)
        c.ellipse(x + side * 4, y - 2, 1, 2, leaf2)
        c.ellipse(x - side * 3, y + 2, 2, 1, leaf1)


# ---- a layer of vines on the tower walls ----
vine1 = [(14, 38), (20, 52), (10, 64), (16, 78), (9, 90), (15, 102),
         (21, 114), (13, 128), (19, 142), (16, 154)]
vine2 = [(128, 42), (121, 56), (127, 70), (118, 84), (125, 96),
         (116, 110), (122, 124), (114, 138), (120, 150)]
vine3 = [(44, 150), (54, 144), (64, 147), (72, 142)]
vine4 = [(8, 70), (12, 84), (7, 98), (11, 112)]
vine5 = [(134, 80), (130, 92), (135, 106), (129, 120)]

vine(output, vine1, vine_stem, vine_leaf, vine_leaf2)
vine(output, vine2, vine_stem, vine_leaf, vine_leaf2)
vine(output, vine3, vine_stem, vine_leaf, vine_leaf2)
vine(output, vine4, vine_stem, vine_leaf, vine_leaf2)
vine(output, vine5, vine_stem, vine_leaf, vine_leaf2)

# ---- cloaked mage, seen from behind, walking into the archway ----
# ground shadow
output.ellipse(65, 190, 12, 2, shadow)

# cloak body (widening down to the hem)
output.poly([(58, 168), (72, 168), (78, 188), (52, 188)], cloak_main)
# ragged hem
output.poly([(52, 188), (60, 185), (66, 189), (72, 185), (78, 188)], cloak_main)

# hood
output.ellipse(65, 160, 5, 6, cloak_main)
output.ellipse(62, 158, 2, 3, cloak_highlight)

# cloak fold shading (viewer-left)
output.poly([(56, 170), (59, 170), (60, 188), (54, 188)], cloak_shadow)
# rim light on viewer-right, lit by the staff
output.poly([(76, 169), (78, 169), (78, 188), (75, 188)], cloak_highlight)

# glowing staff (held at the mage's side, viewer-right)
output.line(80, 149, 80, 188, staff_dark)
output.line(81, 149, 81, 188, staff_dark)
output.line(80, 149, 80, 188, staff_wood)
# hand/cloak overlapping the staff
output.ellipse(80, 170, 2, 3, cloak_main)

# feet
output.ellipse(63, 189, 2, 1, foot)
output.ellipse(70, 189, 2, 1, foot)

# orb and glow
output.circle(80, 142, 8, glow_far)
output.circle(80, 142, 5, glow_mid)
output.circle(80, 142, 3, glow_near)
output.circle(80, 142, 1, glow_core)

# sparkle + rim glints from the orb
output.set(76, 138, glow_near)
output.set(84, 140, glow_mid)
output.set(82, 146, glow_near)
output.set(70, 159, glow_near)
output.set(70, 161, glow_mid)
output.set(71, 162, glow_near)

# faint pool of light on the floor under the staff
output.ellipse(80, 188, 8, 2, glow_far)

print(output.stats_text())
finish(output)
