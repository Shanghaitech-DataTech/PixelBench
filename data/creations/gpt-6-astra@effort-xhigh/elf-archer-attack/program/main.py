# Elf archer: original and full draw, on a shared expanded canvas.
W,H=56,54
f1=new_canvas(W,H,name='01_original')
f1.blit(input_canvas,8,3)
f2=new_canvas(W,H,name='02_full_draw')
# Original palette, including its partially transparent ground shadow.
P={d['name']:d['index'] for d in input_canvas.palette() if d['name']}
def C(n): return P['c'+str(n)]
def pix(x,y,n): f2.set(x,y,C(n))
def rect(x,y,w,h,n): f2.rect(x,y,w,h,C(n))
def line(a,b,n): f2.line(*a,*b,C(n))
def poly(points,n): f2.poly(points,C(n))
def patch(x0,y0,x1,y1,dx,dy):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            i=input_canvas.get(x,y)
            if i and i!=C(41): f2.set(x+dx,y+dy,i)
# Widened shadow, kept in the input's translucent purple.
f2.ellipse(23,48,19,2,C(41))
f2.rect(9,49,31,1,C(41))
# Sash behind the rear leg, using the original embroidered magenta cloth.
patch(2,27,10,40,6,3)
# Legs: spread from the hips into two firmly planted feet.
# Left leg, angled back and shaded on the inner edge.
poly([(19,29),(25,31),(22,36),(18,42),(16,47),(10,47),(12,40),(15,34)],24)
poly([(18,31),(22,32),(19,37),(17,41),(14,45),(12,44),(14,39)],38)
poly([(18,32),(21,32),(19,35),(15,40),(13,40),(15,35)],31)
poly([(18,32),(20,32),(17,36),(14,38),(15,35)],32)
line((20,36),(17,41),30)
line((17,39),(15,45),27)
line((13,40),(12,45),35)
line((18,43),(16,46),36)
# Front leg, pointing toward the target.
poly([(23,30),(30,30),(31,35),(34,40),(35,46),(29,48),(26,42),(24,37)],24)
poly([(25,32),(29,32),(29,36),(32,41),(33,46),(29,46),(27,40)],38)
poly([(25,32),(28,33),(29,37),(31,40),(30,43),(27,39)],31)
poly([(25,32),(27,32),(28,36),(29,38),(27,38),(25,36)],32)
line((31,40),(33,45),30)
line((29,42),(30,46),35)
# Retain the exact pixelwork of both boots, relocated outwards.
patch(1,40,10,44,7,4)
patch(18,39,26,44,9,4)
# Give the front boot a one-pixel toe extension and a grounded sole.
line((32,47),(36,47),24)
pix(36,46,36)
# Long split coat panels; their broken facets echo the original armor.
poly([(18,27),(25,28),(23,34),(22,42),(19,46),(16,45),(17,38),(16,32)],24)
poly([(18,30),(22,30),(21,35),(20,42),(18,44),(17,43),(18,37)],27)
line((18,32),(19,34),31)
line((19,36),(18,42),35)
line((18,44),(19,44),18)
poly([(24,28),(29,29),(30,35),(31,41),(28,45),(24,44),(24,37)],24)
poly([(25,30),(28,31),(28,35),(30,41),(28,43),(26,42),(26,36)],30)
poly([(25,31),(27,32),(27,36),(29,40),(28,41),(26,38)],31)
line((25,35),(25,41),35)
pix(26,43,26); pix(27,44,18)
# Rebuild the lower costume from original pixels, spreading its two halves
# progressively below the waist. This retains the original metal facets,
# split tabard, embroidery and boots while widening the support stance.
f2.clear(3,28,39,23)
f2.ellipse(23,48,21,2,C(41))
f2.rect(7,49,34,1,C(41))
for sy in range(25,45):
    for sx in range(0,24 if sy<40 else 27):
        col=input_canvas.get(sx,sy)
        if col==0 or col==C(41): continue
        # No pieces of the relaxed bow or its string.
        if sy<30 and sx>22: continue
        if sy>=30 and sy<36 and sx>22: continue
        if sy>=36 and sy<40 and sx>21: continue
        spread=max(0,sy-28)//4
        if sx<=12:
            tx=sx+7-spread
        else:
            tx=sx+7+spread
        f2.set(tx,sy+3,col)
# Fill the opening between hip plates; below this the split coat separates.
poly([(19,29),(22,29),(24,33),(21,38),(19,38)],24)
line((20,30),(22,32),35)
line((21,33),(20,36),27)
# Torso twisted into profile. Dark waist, green cloth and metal shoulder line.
poly([(20,19),(26,19),(30,24),(28,30),(19,31),(16,27),(17,23)],24)
poly([(20,20),(25,20),(28,24),(26,28),(19,28),(18,25)],23)
poly([(21,20),(25,21),(27,24),(24,27),(20,26),(19,23)],21)
poly([(21,20),(24,20),(26,23),(22,24),(19,23)],25)
line((20,26),(26,27),29)
poly([(18,26),(27,27),(28,30),(19,31),(17,29)],0)
line((18,27),(26,28),26)
line((19,28),(27,29),18)
rect(21,28,3,2,35); pix(22,28,34); pix(22,29,26)
# Original quiver, hair, face and pointed ear. The head stays steady on target.
patch(0,0,22,18,7,3)
# Back arm: elbow pulled far behind, forearm returning to the cheek.
poly([(20,23),(17,25),(10,24),(7,22),(9,19),(13,19),(19,21)],0)
poly([(19,23),(17,24),(11,23),(9,22),(10,20),(13,20)],2)
line((11,20),(16,21),11)
line((10,21),(13,22),13)
line((13,23),(17,24),1)
# Drawing forearm and bracer, upper edge rising toward the anchor.
poly([(10,19),(17,18),(23,18),(26,19),(25,22),(19,23),(12,22),(9,21)],24)
poly([(11,20),(17,19),(21,19),(22,21),(17,22),(12,21)],2)
line((12,20),(17,20),11)
poly([(17,18),(22,18),(24,20),(22,23),(17,22),(16,20)],30)
poly([(18,19),(21,19),(22,20),(21,22),(18,21)],31)
line((18,19),(21,19),32)
pix(18,20,28); pix(22,21,27)
# Extended bow arm, lower than the taut string; skin then steel bracer.
poly([(25,23),(29,22),(34,23),(39,22),(43,22),(45,24),(43,27),(37,27),(31,27),(27,28),(24,26)],24)
poly([(27,23),(31,24),(37,24),(38,26),(32,26),(28,27),(26,25)],2)
line((29,24),(36,24),11)
line((30,25),(36,25),13)
line((31,26),(36,26),1)
# Shoulder pauldron and its bright upper lip.
poly([(23,22),(27,22),(30,24),(29,27),(26,28),(23,26)],30)
poly([(24,23),(27,23),(28,24),(27,26),(25,26),(24,25)],31)
line((24,23),(27,23),32)
pix(25,24,28); pix(28,26,27)
# Wrist bracer on the bow arm, with faceted highlight.
poly([(37,22),(42,21),(44,23),(43,26),(38,27),(36,25)],30)
poly([(38,23),(41,22),(42,23),(41,25),(38,25)],31)
line((38,23),(41,22),32)
pix(39,23,28); line((42,23),(42,25),27)
# Fully flexed recurve bow. Tips sweep back toward the anchor.
# Draw the wood as paired stepped outlines and lit gold faces.
bow=[(38,6),(36,8),(37,11),(42,13),(45,16),(47,20),(48,24),(47,29),(45,34),(42,38),(37,41),(36,44),(38,45)]
for a,b in zip(bow,bow[1:]):
    f2.line(a[0]-1,a[1],b[0]-1,b[1],C(0))
    f2.line(a[0]+1,a[1],b[0]+1,b[1],C(0))
    f2.line(*a,*b,C(8))
for a,b in zip(bow,bow[1:]):
    f2.line(a[0]+1,a[1],b[0]+1,b[1],C(6))
# Top and bottom recurve tips and the signature magenta bindings.
line((38,6),(37,8),5); pix(39,6,4)
line((36,44),(38,45),5)
line((45,16),(47,20),9)
line((46,16),(48,20),7)
pix(47,17,10); pix(47,18,22)
line((45,33),(43,37),9)
line((46,33),(44,37),7)
pix(45,34,10); pix(45,35,22)
# String pulled all the way to the face; there is deliberately no arrow.
line((36,8),(28,21),12)
line((28,21),(36,44),12)
pix(34,11,13); pix(31,16,13); pix(30,27,13); pix(33,36,13)
# Bow grip behind the clasped forward hand.
line((48,22),(48,27),35)
line((49,22),(49,26),16)
# Forward hand wraps around the grip.
poly([(43,23),(46,22),(49,23),(50,24),(49,26),(45,26),(43,25)],0)
line((44,23),(47,23),11)
line((44,24),(46,24),13)
line((45,25),(48,25),2)
pix(48,23,2); pix(49,24,11); pix(48,26,1)
# Three curled drawing fingers at the jaw, closing on the bowstring.
poly([(23,18),(26,18),(28,19),(29,21),(27,23),(24,22),(23,20)],0)
rect(24,19,3,2,11)
pix(25,19,13); pix(27,20,2); pix(28,20,11)
line((25,21),(27,21),2)
pix(26,22,1); pix(28,21,13)
# Small articulated facets keep the new limbs consistent with the source.
# Back elbow and draw-arm bracer.
pix(9,21,16); pix(10,22,1); pix(12,22,2)
pix(14,21,13); pix(16,20,2); pix(17,21,30)
pix(18,21,32); pix(19,22,27); pix(20,20,32)
pix(21,21,30); pix(22,19,33); pix(23,20,31)
# Deltoid, rolled green sleeve and layered chest plates.
pix(24,23,32); pix(25,24,28); pix(26,24,31)
pix(27,25,32); pix(28,24,30); pix(28,26,31)
pix(26,26,30); pix(24,25,27)
line((20,24),(21,25),29); pix(20,24,25)
pix(22,25,21); pix(22,26,23); pix(19,26,29)
pix(18,25,23); pix(19,25,21)
pix(23,27,31); pix(24,27,30); pix(26,28,23)
# Narrow skin highlights and shadows along the extended forearm.
pix(29,24,2); pix(30,25,11); pix(32,24,13)
pix(34,25,11); pix(35,26,2); pix(36,25,16)
pix(37,24,30); pix(38,25,32); pix(39,24,31)
pix(40,24,32); pix(40,25,30); pix(41,23,28)
pix(42,24,31); pix(43,25,1)
# Segmented gilt belt and a small upper tabard fold.
pix(19,28,18); pix(20,29,26); pix(23,29,18)
pix(24,29,26); pix(25,29,0); pix(26,29,8)
line((22,30),(24,31),23); pix(23,31,21)
# A fitted steel greave replaces pixels formerly overlapped by the old bow.
poly([(27,37),(29,38),(31,41),(31,43),(29,44),(27,42)],24)
poly([(27,38),(29,39),(30,41),(29,43),(28,42)],30)
line((27,38),(29,40),31)
pix(28,39,32); pix(29,41,31); pix(30,43,39)
# Remove the old dangling quiver pixel now occluded by the drawn arm.
f2.set(9,28,None)
# Verify exact preservation of the original artwork in frame one.
for y in range(47):
    for x in range(35):
        assert f1.get(x+8,y+3)==input_canvas.get(x,y)
save('elf-archer-attack-frame-1',f1)
save('elf-archer-attack-frame-2',f2)
view(f1,scale=8,margin=0)
view(f2,scale=8,margin=0)
finish([f1,f2])
