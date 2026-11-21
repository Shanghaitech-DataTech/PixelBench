result = new_canvas(64,64,background='#10182d',name='Pixel Quest')
c=result
# quiet inset frame
c.rect(2,2,60,60,'#24344b',fill=False)
c.rect(4,4,56,56,'#18243a',fill=False)
for x,y in [(2,2),(59,2),(2,59),(59,59)]:
 c.rect(x,y,3,3,'#60717c')
 c.set(x+1,y+1,'#e0c78b')
# sparse stars
for x,y in [(9,10),(51,9),(7,43),(56,44),(13,52),(48,51)]:
 c.set(x,y,'#536579')
c.line(29,8,35,8,'#ac8652')
c.line(32,5,32,11,'#ac8652')
c.set(32,8,'#fff0b0')
# five-column glyphs, enlarged into substantial 2px strokes
font={
'P':['11110','10001','10001','11110','10000','10000','10000'],
'I':['111','010','010','010','010','010','111'],
'X':['10001','10001','01010','00100','01010','10001','10001'],
'E':['11111','10000','10000','11110','10000','10000','11111'],
'L':['10000','10000','10000','10000','10000','10000','11111'],
'Q':['01110','10001','10001','10001','10101','10010','01101'],
'U':['10001','10001','10001','10001','10001','10001','01110'],
'S':['01111','10000','10000','01110','00001','00001','11110'],
'T':['11111','00100','00100','00100','00100','00100','00100']}
def title(word,y):
 width=sum(len(font[a][0])*2 for a in word)+2*(len(word)-1)
 x=(64-width)//2
 pts=[]
 for a in word:
  for j,row in enumerate(font[a]):
   for i,p in enumerate(row):
    if p=='1':
     for dy in range(2):
      for dx in range(2): pts.append((x+i*2+dx,y+j*2+dy))
  x+=len(font[a][0])*2+2
 for px,py in pts:
  c.set(px+1,py+3,'#080d1c')
  c.set(px,py+2,'#8c493b')
 for px,py in pts:
  for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: c.set(px+dx,py+dy,'#080d1c')
 for px,py in pts:
  col=['#fff5bb','#fff5bb','#ffe295','#ffe295','#f9c66c','#f9c66c','#efab50','#efab50','#df8a40','#df8a40','#d87939','#d87939','#f4b759','#f4b759'][py-y]
  c.set(px,py,col)
title('PIXEL',16)
title('QUEST',34)
# understated start marker
c.line(20,55,25,55,'#526577')
c.line(39,55,44,55,'#526577')
c.poly([(30,53),(33,55),(30,58)],'#fff0b0')
view(c)
finish(result)
