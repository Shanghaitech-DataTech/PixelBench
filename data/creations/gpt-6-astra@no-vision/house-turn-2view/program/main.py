# Two views of the same warm, outlined house in a fixed elevated projection.
INK = '#161c2e'
SHADOW = '#161c2e45'
ROOF = '#97763d'
ROOF_L = '#bda759'
ROOF_D = '#6c513a'
WALL = '#dcaa46'
WALL_L = '#f9e279'
WALL_D = '#98694e'
TRIM = '#e1d968'
GLASS = '#bbae93'


def setup(name):
    return new_canvas(160, 160, name=name)


def frame45():
    c = setup('turn_45')
    # Grounding shadow
    c.ellipse(82, 139, 56, 10, SHADOW)
    # Front wall and right-hand wall
    c.poly([(28, 77), (78, 89), (78, 139), (28, 126)], WALL, True)
    c.poly([(78, 89), (127, 65), (127, 115), (78, 139)], WALL_D, True)
    c.poly([(28, 77), (78, 89), (78, 139), (28, 126)], INK, False)
    c.poly([(78, 89), (127, 65), (127, 115), (78, 139)], INK, False)
    # Front gable and roof planes; the roof top remains visible from above.
    c.poly([(28, 77), (59, 48), (78, 89)], ROOF_L, True)
    c.poly([(59, 48), (101, 57), (127, 65), (78, 89)], ROOF, True)
    c.poly([(28, 77), (59, 48), (101, 57), (127, 65), (78, 89)], INK, False)
    c.line(59, 48, 78, 89, ROOF_D)
    c.line(28, 77, 78, 89, ROOF_D)
    # Front window
    c.poly([(38, 91), (53, 95), (53, 111), (38, 107)], INK, True)
    c.poly([(40, 93), (51, 96), (51, 108), (40, 105)], GLASS, True)
    c.line(45, 95, 45, 107, TRIM)
    c.line(40, 99, 51, 102, TRIM)
    # Front door
    c.poly([(58, 105), (73, 109), (73, 137), (58, 133)], INK, True)
    c.poly([(60, 108), (71, 111), (71, 134), (60, 131)], ROOF_D, True)
    c.line(60, 108, 60, 131, WALL_L)
    c.set(68, 122, WALL_L)
    # Window on the right-hand wall
    c.poly([(91, 91), (111, 81), (111, 99), (91, 109)], INK, True)
    c.poly([(94, 92), (108, 84), (108, 97), (94, 104)], GLASS, True)
    c.line(101, 88, 101, 100, TRIM)
    c.line(94, 98, 108, 91, TRIM)
    # Eaves and corner definition
    c.line(28, 77, 28, 126, INK)
    c.line(78, 89, 78, 139, INK)
    return c


def frame90():
    c = setup('turn_90')
    c.ellipse(81, 139, 52, 9, SHADOW)
    # Quarter-turn: the former right wall faces the viewer; no front wall or door.
    c.poly([(36, 79), (119, 79), (119, 132), (36, 132)], WALL_D, True)
    c.poly([(36, 79), (119, 79), (119, 132), (36, 132)], INK, False)
    # The roof is still seen from above, with its long ridge receding in depth.
    c.poly([(29, 72), (55, 42), (130, 64), (105, 81)], ROOF_L, True)
    c.poly([(55, 42), (126, 55), (143, 65), (105, 81)], ROOF, True)
    c.poly([(29, 72), (55, 42), (126, 55), (143, 65), (105, 81)], INK, False)
    c.line(55, 42, 105, 81, ROOF_D)
    c.line(29, 72, 105, 81, ROOF_D)
    # Single window on the visible right-hand wall
    c.poly([(65, 91), (91, 91), (91, 115), (65, 115)], INK, True)
    c.poly([(68, 94), (88, 94), (88, 112), (68, 112)], GLASS, True)
    c.line(78, 94, 78, 112, TRIM)
    c.line(68, 102, 88, 102, TRIM)
    # A restrained sill and stone courses keep the side wall readable.
    c.line(62, 118, 94, 118, WALL_L)
    c.line(43, 125, 111, 125, ROOF)
    c.line(36, 79, 36, 132, INK)
    c.line(119, 79, 119, 132, INK)
    return c

f1 = frame45()
f2 = frame90()
print(f1.stats_text())
print(f1.matrix_text(region=(24,40,130,140)))
print(f2.stats_text())
print(f2.matrix_text(region=(25,38,145,140)))
finish([f1, f2])
