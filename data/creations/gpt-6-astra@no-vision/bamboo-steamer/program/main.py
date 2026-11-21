result = new_canvas(32, 32, name='bamboo_steamer')
c = result
O='#50352c'
D='#825235'
B='#ae7542'
M='#d39b55'
G='#edbc70'
H='#ffdc91'
I='#694837'
S='#b3c9cb'
W='#e0e9df'
P='#fff0ce'
Q='#e5c99b'
R='#ba9166'
# Small, separated steam curls.
c.line(5,1,4,3,S).line(4,3,5,4,W)
c.line(25,1,24,3,W).line(24,3,25,4,S)
c.line(29,7,28,9,W).line(28,9,29,10,S).set(29,11,S)
# Raised bamboo lid, its near edge descending toward the right.
c.poly([(2,7),(4,5),(9,4),(15,5),(22,8),(28,12),(28,14),(25,16),(19,15),(11,12),(4,10),(2,9)],O)
c.poly([(3,7),(6,5),(10,5),(16,6),(22,9),(27,12),(25,14),(19,13),(11,10),(5,9)],G)
c.poly([(4,9),(11,11),(19,14),(25,15),(27,13),(27,14),(25,15),(19,14),(11,11)],B)
c.line(4,9,11,12,D).line(11,12,20,15,D).line(20,15,25,15,D)
c.line(4,7,9,5,H).line(10,5,17,7,H).line(18,7,25,11,H)
# Woven slats, following the lid's plane.
c.line(7,6,22,12,M).line(6,8,19,13,M)
c.line(12,6,9,9,B).line(17,8,14,11,B).line(22,10,20,13,B)
c.line(8,7,11,8,H).line(15,9,18,10,H).line(22,12,24,13,H)
# Small raised loop handle.
c.poly([(12,4),(12,2),(14,1),(17,2),(18,4),(17,6),(14,5)],O)
c.poly([(13,3),(14,2),(16,3),(17,4),(16,5),(14,4)],M)
c.set(14,3,H).set(15,3,O).set(16,4,O)
# Basket body and the dark, open interior.
c.ellipse(16,25,13,5,O)
c.rect(3,20,27,6,O)
c.ellipse(16,20,13,5,O)
c.ellipse(16,25,12,4,B)
c.rect(4,21,25,5,M)
c.ellipse(16,20,12,4,G)
c.ellipse(16,20,10,3,I)
c.line(7,18,10,17,H).line(23,18,26,19,H)
# Three individual pleated dumplings: left, right, then front.
def dumpling(x,y):
    c.poly([(x-4,y+3),(x-4,y+1),(x-3,y),(x-2,y-2),(x,y-3),(x+2,y-2),(x+3,y),(x+4,y+1),(x+4,y+3),(x+2,y+4),(x-2,y+4)],O)
    c.poly([(x-3,y+2),(x-3,y+1),(x-2,y-1),(x,y-2),(x+2,y-1),(x+3,y+1),(x+3,y+3),(x+1,y+3),(x-2,y+3)],P)
    c.line(x-2,y+2,x+2,y+2,Q)
    c.line(x-1,y-1,x-2,y+1,R)
    c.line(x+1,y-1,x+2,y+1,Q)
    c.set(x,y-1,Q).set(x,y,P)
    c.set(x+3,y+2,Q)
dumpling(9,18)
dumpling(23,18)
dumpling(16,21)
# Front lip passes in front of the dumpling bases.
c.path('M 3 21 L 5 23 L 9 25 L 15 26 L 21 26 L 27 24 L 29 22 L 29 25 L 27 27 L 21 29 L 11 29 L 5 27 L 3 25 Z',O)
c.path('M 4 23 L 9 26 L 15 27 L 21 27 L 27 25 L 28 24 L 28 26 L 25 27 L 20 29 L 12 29 L 6 27 L 4 25 Z',M)
c.line(6,24,10,26,G).line(11,26,20,27,H).line(21,26,26,24,G)
# Vertical bamboo joins and lower binding.
for x,y in [(6,26),(10,27),(15,28),(20,28),(25,26)]:
    c.line(x,y,x,y+1,D)
c.line(9,28,13,29,B).line(14,29,21,29,D).line(22,28,25,27,B)
c.set(5,25,H).set(27,25,G)
c.set(16,30,None)
print(c.stats_text())
print(c.matrix_text())
finish(result)
