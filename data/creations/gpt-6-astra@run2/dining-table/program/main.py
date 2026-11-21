# Cozy family dining table, drawn at native 64 x 64 resolution.
result = new_canvas(64, 64, name='family_dining_table')
c = result
O = '#302329'
D = '#59362e'
M = '#855036'
W = '#ae7143'
L = '#d59a59'
H = '#efbc77'
G = '#bf824a'
R = '#a84e42'
RH = '#d57a58'
RS = '#743b37'
CREAM = '#ead6a2'
# The far chair: carved back, two open slats, a rust-red cushion.
c.rect(25, 4, 15, 18, O)
c.rect(27, 3, 11, 2, O)
c.rect(27, 4, 11, 4, W)
c.line(28, 4, 36, 4, L)
c.line(27, 7, 37, 7, M)
c.rect(27, 9, 3, 5, W)
c.rect(35, 9, 3, 5, W)
c.rect(30, 9, 5, 4, None)
c.line(27, 9, 27, 12, L)
c.rect(26, 14, 13, 7, M)
c.rect(28, 14, 9, 5, R)
c.line(29, 14, 36, 14, RH)
c.line(28, 18, 36, 18, RS)
# Side chairs, facing in toward the table.
def side_chair(left=True):
    q = new_canvas(16, 24)
    q.poly([(2,3),(5,1),(8,1),(8,4),(14,4),(15,6),(15,18),(13,20),(7,20),(7,22),(2,22),(1,20),(1,5)], O)
    q.rect(2, 5, 4, 15, W)
    q.line(2, 5, 2, 18, L)
    q.line(5, 5, 5, 20, M)
    q.rect(3, 3, 3, 2, L)
    q.rect(7, 6, 7, 12, M)
    q.rect(8, 7, 6, 9, R)
    q.line(8, 7, 12, 7, RH)
    q.line(8, 8, 8, 14, RH)
    q.line(8, 16, 13, 16, RS)
    q.rect(7, 18, 6, 2, D)
    q.set(3, 21, M)
    if not left:
        q.mirror('h')
    return q
c.blit(side_chair(), 1, 23)
c.blit(side_chair(False), 47, 23)
# Table feet and apron, visible below the tabletop.
c.rect(15, 42, 6, 10, O)
c.rect(16, 44, 3, 7, M)
c.line(16, 46, 16, 49, W)
c.rect(44, 42, 6, 10, O)
c.rect(45, 44, 3, 7, M)
c.line(45, 46, 45, 49, W)
c.poly([(14,24),(50,24),(50,46),(47,49),(17,49),(14,46)], O)
c.rect(16, 42, 33, 4, M)
c.line(18, 47, 46, 47, D)
c.line(17, 45, 47, 45, W)
# Solid, chamfered honey-oak tabletop with a heavy dark edge.
c.poly([(16,17),(48,17),(51,20),(51,42),(48,45),(16,45),(13,42),(13,20)], O)
c.poly([(16,18),(48,18),(50,20),(50,41),(47,44),(17,44),(14,41),(14,20)], M)
c.poly([(17,19),(47,19),(49,21),(49,40),(47,42),(17,42),(15,40),(15,21)], L)
c.line(17, 19, 47, 19, H)
c.line(15, 21, 15, 39, H)
# Plank seams and controlled grain strokes.
for y in [25, 33, 40]:
    c.line(16, y, 48, y, W)
    c.line(17, y+1, 48, y+1, G)
c.line(18, 22, 24, 22, H)
c.line(21, 23, 26, 23, G)
c.line(39, 22, 45, 22, G)
c.line(41, 23, 47, 23, H)
c.line(17, 29, 22, 29, G)
c.line(18, 30, 24, 30, H)
c.line(40, 28, 46, 28, G)
c.line(43, 29, 47, 29, H)
c.line(18, 37, 24, 37, G)
c.line(19, 38, 22, 38, H)
c.line(40, 37, 47, 37, G)
c.line(42, 38, 45, 38, H)
# Linen runner, soft gold with a stitched terracotta border.
c.rect(26, 19, 13, 24, '#bc8a55')
c.rect(27, 19, 11, 24, CREAM)
c.line(28, 19, 28, 42, '#b9704b')
c.line(36, 19, 36, 42, '#b9704b')
c.line(30, 20, 34, 20, '#fff0c7')
c.rect(27, 43, 11, 3, '#c9ae7d')
c.line(28, 43, 28, 45, '#a45d43')
c.line(36, 43, 36, 45, '#a45d43')
for x in [28,30,32,34,36]:
    c.set(x, 46, CREAM)
for x,y in [(31,23),(32,22),(33,23),(32,24),(31,39),(32,38),(33,39),(32,40)]:
    c.set(x,y,'#b9704b')
# Bowl shadow and glazed ceramic bowl.
c.ellipse(33, 35, 9, 3, '#94603d')
c.poly([(24,30),(41,30),(40,35),(37,38),(28,38),(25,35)], O)
c.poly([(25,31),(40,31),(38,35),(36,37),(29,37),(26,34)], '#549594')
c.line(28, 36, 36, 36, '#39676e')
c.line(27, 34, 29, 35, '#92c4b2')
c.ellipse(32, 30, 9, 4, O)
c.ellipse(32, 30, 8, 3, '#c7d7bc')
c.ellipse(32, 30, 6, 2, '#547c72')
# A pear, an apple, an orange, and a little bunch of grapes.
c.poly([(28,29),(27,27),(28,24),(28,22),(30,22),(31,25),(32,27),(31,29)], '#536c37')
c.poly([(28,27),(29,24),(29,23),(30,25),(31,27),(30,29),(28,29)], '#a8b751')
c.set(29, 24, '#d7d482')
c.line(29, 21, 30, 20, D)
c.circle(35, 27, 3, '#9c3d33')
c.circle(35, 26, 2, '#da6543')
c.set(34, 25, '#f5a36a')
c.line(35, 24, 35, 23, D)
c.line(36, 23, 38, 22, '#64834a')
c.circle(30, 30, 3, '#bb6431')
c.circle(30, 29, 2, '#efa34a')
c.set(29, 28, '#ffcf72')
for x,y in [(36,30),(38,29),(38,31),(36,32),(37,33)]:
    c.circle(x,y,1,'#645078')
    c.set(x,y,'#9c759b')
c.set(38, 28, '#6f8c49')
# Near chair: the seat is visible behind a low slatted backrest.
c.poly([(26,47),(38,47),(40,49),(40,59),(38,61),(26,61),(24,59),(24,49)], O)
c.rect(26, 48, 13, 9, W)
c.rect(27, 48, 11, 7, R)
c.line(28, 48, 36, 48, RH)
c.line(27, 49, 27, 52, RH)
c.line(28, 54, 36, 54, RS)
c.rect(25, 53, 3, 7, M)
c.rect(37, 53, 2, 7, M)
c.line(25, 54, 25, 58, L)
c.rect(29, 55, 3, 3, O)
c.rect(33, 55, 3, 3, O)
c.rect(26, 58, 12, 3, W)
c.line(27, 58, 37, 58, L)
c.line(27, 60, 37, 60, M)
c.set(25, 59, L)
view(result)
save('dining-table', result)
finish(result)
