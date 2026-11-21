result = new_canvas(32, 32, name='leather_spellbook')
c = result
O = '#211e29'
S = '#51313a'
L = '#864535'
H = '#b86b46'
G = '#95713f'
Y = '#e5b966'
P = '#eddbaf'
T = '#72c9b6'
# The stepped silhouette includes the leather spine and the closed page block.
c.poly([(8,2),(28,5),(26,25),(23,29),(3,26),(3,8)], O)
c.line(3,8,8,2,O)
# Back board and tightly closed pages.
c.poly([(5,21),(25,24),(23,28),(4,25)], S)
c.poly([(7,22),(25,25),(23,27),(5,24)], P)
c.line(7,24,22,26,G)
c.set(23,25,Y)
c.line(4,25,23,28,O)
c.line(5,26,22,28,S)
# Rounded spine, with two raised binding bands.
c.poly([(4,8),(8,4),(7,20),(5,24),(4,24)], S)
c.line(5,8,7,6,H)
c.line(4,11,6,9,G)
c.line(4,12,6,10,Y)
c.line(4,19,6,17,G)
c.line(4,20,6,18,Y)
c.line(4,23,5,24,H)
# Front leather cover; outline remains a continuous one-pixel rim.
c.poly([(8,3),(27,6),(25,24),(6,21)], O)
c.poly([(9,4),(26,7),(24,22),(7,20)], L)
c.line(10,4,25,6,H)
c.line(8,7,7,18,H)
c.line(8,20,23,22,S)
c.line(25,9,24,18,S)
# Inset blind-tooled border, interrupted only by corner hardware.
c.line(10,7,23,9,S)
c.line(23,9,22,20,S)
c.line(10,18,22,20,H)
c.line(10,8,9,18,S)
# Four folded brass corner plates.
c.poly([(8,4),(13,5),(12,7),(10,6),(8,9)], G)
c.line(8,4,12,5,Y)
c.line(8,5,8,7,Y)
c.set(10,6,P)
c.poly([(23,6),(26,7),(26,12),(24,11),(24,9),(22,8)], G)
c.line(24,7,26,7,Y)
c.line(25,8,25,10,Y)
c.set(25,8,P)
c.poly([(7,16),(9,17),(9,19),(12,20),(11,21),(7,20)], G)
c.line(7,17,7,19,Y)
c.line(8,20,11,20,Y)
c.poly([(22,19),(24,18),(24,22),(20,22),(20,21),(22,21)], G)
c.line(23,20,23,22,Y)
c.line(21,22,23,22,Y)
# Central arcane lozenge and inset turquoise jewel.
c.poly([(17,9),(21,14),(16,19),(12,14)], S)
c.poly([(17,10),(20,14),(16,18),(13,14)], O)
c.poly([(17,11),(19,14),(16,17),(14,14)], G)
c.line(17,11,14,14,Y)
c.line(14,14,16,17,Y)
c.poly([(17,12),(18,14),(16,16),(15,14)], T)
c.set(17,12,P)
c.set(16,16,S)
# Short leather clasp wraps around the fore edge.
c.poly([(23,14),(27,14),(27,18),(23,17)], O)
c.rect(23,15,3,2,S)
c.set(23,15,H)
c.rect(25,15,1,2,Y)
# Sparse wear marks in the hide.
c.set(12,10,H)
c.set(20,8,H)
c.set(11,16,H)
c.set(20,18,S)
print(c.stats_text())
print(c.matrix_text())
save('leather-spellbook', result)
finish(result)
