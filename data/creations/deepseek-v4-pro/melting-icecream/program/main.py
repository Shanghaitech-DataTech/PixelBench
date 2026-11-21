output = input_canvas.copy(name='output')

choc = output.color('#5e363e')       # main chocolate body
choc_light = output.color('#95524c') # reddish highlight
choc_dark = output.color('#613942')  # darker edge


def draw_drip(segs):
    """Draw a drip from explicit (y, x_left, x_right) segments."""
    for (y, xa, xb) in segs:
        w = xb - xa + 1
        for x in range(xa, xb + 1):
            if w >= 4:
                c = choc_light if x == xa else (choc_dark if x == xb else choc)
            elif w >= 3:
                c = choc_light if x == xa else choc
            else:
                c = choc
            output.set(x, y, c)


# Left drip, hugging the inward-sloping left edge of the cone.
draw_drip([
    (33, 22, 24), (34, 22, 24), (35, 22, 24), (36, 22, 24),
    (37, 22, 24), (38, 22, 24), (39, 22, 24), (40, 22, 24),
    (41, 23, 24), (42, 23, 24), (43, 23, 24),
    (44, 24, 24), (45, 24, 24), (46, 24, 24),
])

# Centre-left medium drip.
draw_drip([
    (33, 26, 28), (34, 26, 28), (35, 26, 28), (36, 26, 28),
    (37, 26, 28), (38, 26, 28), (39, 26, 28), (40, 26, 28),
    (41, 26, 28), (42, 26, 27), (43, 26, 27), (44, 26, 27),
    (45, 26, 27),
])

# Centre long drip reaching almost to the cone tip.
draw_drip([
    (33, 30, 33), (34, 30, 33), (35, 30, 33), (36, 30, 33),
    (37, 30, 33), (38, 30, 33), (39, 30, 33), (40, 30, 33),
    (41, 30, 33), (42, 30, 33), (43, 30, 33),
    (44, 30, 32), (45, 30, 32), (46, 30, 32), (47, 30, 32),
    (48, 30, 32), (49, 30, 32), (50, 30, 32), (51, 30, 31),
    (52, 31, 31),
])

# Right drip, hugging the inward-sloping right edge of the cone.
draw_drip([
    (33, 36, 38), (34, 36, 38), (35, 36, 38), (36, 36, 38),
    (37, 36, 38), (38, 36, 38), (39, 36, 38), (40, 36, 38),
    (41, 36, 37), (42, 36, 37), (43, 36, 37),
    (44, 35, 35), (45, 35, 35), (46, 35, 35), (47, 35, 35),
    (48, 35, 35),
])

# Small detached droplets falling below the cone tip.
output.set(29, 61, choc)
output.set(31, 62, choc)

print(output.stats_text())
finish(output)
