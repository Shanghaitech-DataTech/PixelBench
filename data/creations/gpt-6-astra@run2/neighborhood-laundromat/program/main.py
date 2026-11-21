result = new_canvas(64,64, '#243644', name='neighborhood_laundromat')
c=result
# A shallow room, lit by cool fluorescent tubes.
c.rect(1,1,62,43,'#c6d7dc')
c.poly([(1,1),(5,5),(5,44),(1,49)], '#9db7c2')
c.poly([(59,5),(62,1),(62,49),(59,44)], '#a9c1c9')
c.poly([(1,1),(62,1),(59,6),(5,6)], '#e3edef')
c.rect(5,6,54,35,'#cbdde1')
c.rect(5,28,54,13,'#9ebcc6')
c.line(5,28,58,28,'#789ba9')
for x in range(6,59,8):
    c.line(x,30,x,40,'#b3cbd2')
c.line(5,35,58,35,'#b3cbd2')
c.rect(2,42,60,4,'#557782')
c.line(3,42,60,42,'#799aa5')
# Ceiling fixtures, dark mounts and icy light cores.
for x in (9,36):
    c.rect(x,3,19,3,'#7d99a8')
    c.rect(x+1,3,17,2,'#f5ffff')
    c.line(x+2,6,x+16,6,'#e6faff')
# Floor, with converging tile seams.
c.poly([(5,45),(58,45),(63,50),(63,63),(0,63),(0,50)], '#a6bcc5')
for a,b in [(8,-10),(21,13),(34,36),(47,59),(58,79)]:
    # Clip lines explicitly to keep the drawing inside its frame.
    x0,y0=a,46
    import math
    endx=max(0,min(63,b))
    endy=63 if 0<=b<=63 else round(46+(endx-a)*17/(b-a))
    c.line(x0,y0,endx,endy,'#7f9aa9')
c.line(1,51,62,51,'#7f9aa9')
c.line(0,59,63,59,'#7f9aa9')
c.line(1,52,62,52,'#b7cbd1')
c.line(0,60,63,60,'#b7cbd1')
# Small wall sign.
c.rect(6,9,37,8,'#496d7d')
c.text(7,10,'LAUNDRY','#e5f3f4',spacing=0)
# Clock, offset from the bank of machines.
c.circle(52,15,6,'#7795a4')
c.circle(52,14,6,'#365260')
c.circle(52,14,4,'#eef5ef')
for x,y in [(52,10),(56,14),(52,18),(48,14)]: c.set(x,y,'#819ba2')
c.line(52,14,52,11,'#2b4556')
c.line(52,14,55,15,'#2b4556')
c.set(52,14,'#587789')
# Two rows of independent front-loading washers. Dark gutters remain visible.
c.rect(4,18,40,31,'#324b5d')
def washer(x,y,variant):
    c.rect(x,y,12,14,'#658390')
    c.rect(x,y,11,13,'#dce8e9')
    c.line(x,y,x+10,y,'#f3fbf9')
    c.line(x,y+1,x,y+11,'#edf6f5')
    c.rect(x+1,y+1,9,2,'#adc3cc')
    c.rect(x+2,y+1,3,1,'#66828f')
    c.set(x+7,y+1,'#3d586d')
    c.set(x+9,y+1,'#84c9c9')
    c.circle(x+5,y+7,4,'#7d9aa7')
    c.circle(x+5,y+7,3,'#263f56')
    c.line(x+3,y+5,x+5,y+4,'#badce4')
    c.set(x+2,y+6,'#88bbc9')
    c.rect(x+3,y+7,4,2,'#365f79')
    if variant%3==0:
        c.line(x+3,y+8,x+6,y+9,'#86b7c7')
        c.set(x+6,y+8,'#c9e0dd')
    elif variant%3==1:
        c.line(x+4,y+8,x+7,y+8,'#839cad')
        c.set(x+5,y+9,'#b8c6d3')
    else:
        c.line(x+3,y+8,x+5,y+9,'#69a9b5')
        c.set(x+6,y+8,'#91cbd0')
    c.set(x+8,y+7,'#dce9e8')
    c.line(x+2,y+12,x+8,y+12,'#a5bbc4')
    c.set(x+9,y+11,'#f6fcfa')
for row,y in enumerate((19,34)):
    for col,x in enumerate((5,18,31)):
        washer(x,y,row*3+col)
# Utility shelf and detergent, on the right wall.
c.rect(47,29,12,2,'#547b89')
c.line(47,29,58,29,'#e5f0ec')
c.rect(49,24,4,5,'#5c98ab')
c.rect(50,23,2,1,'#e5f3ef')
c.rect(50,26,2,2,'#d1e5e5')
c.rect(55,26,3,3,'#ddba7e')
c.rect(55,25,2,1,'#f0d7a3')
# Folding table: slab, slim legs and folded towels.
c.poly([(44,49),(59,47),(62,51),(48,54)], '#829eaa')
c.rect(47,43,2,9,'#3b596a')
c.rect(58,42,2,9,'#3b596a')
c.line(48,44,48,50,'#b7ccd2')
c.line(59,44,59,49,'#b7ccd2')
c.poly([(47,38),(59,38),(61,42),(45,42)], '#edf3ed')
c.rect(45,42,17,2,'#74909d')
c.line(45,42,61,42,'#c4d5d8')
c.rect(49,36,8,2,'#709ba8')
c.line(49,36,56,36,'#b3d1d5')
c.rect(50,34,7,2,'#e1e7d8')
c.line(50,34,56,34,'#f5f7e8')
# Foreground basket with a rolled-over rim and open weave.
c.ellipse(19,59,10,2,'#718d9c')
c.poly([(9,51),(28,51),(26,59),(12,59)], '#ab855b')
c.poly([(11,52),(26,52),(24,58),(13,58)], '#dbb47d')
c.line(13,58,24,58,'#efd19c')
for y in (54,56):
    for x in (13,16,19,22,25):
        if x==25 and y==56: continue
        c.rect(x,y,2,1,'#8d785d')
c.ellipse(18,51,9,2,'#f1d5a1')
c.ellipse(18,51,7,1,'#786f65')
# Soft laundry peeking over the basket rim.
c.poly([(13,50),(14,47),(18,47),(20,50)], '#ecede4')
c.line(14,49,17,49,'#bfd0cf')
c.poly([(19,50),(20,48),(24,48),(25,51)], '#739faa')
c.set(23,48,'#9ec4cb')
c.line(10,52,27,52,'#f0ce95')
view(c)
save('neighborhood-laundromat',c)
finish(result)
