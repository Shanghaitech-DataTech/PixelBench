result = new_canvas(64,64,background='#10172c',name='pixel_quest')
c=result
# restrained frame and atmospheric field
c.rect(2,2,60,60,'#293751',False)
c.line(7,4,56,4,'#3e526b')
c.line(7,59,56,59,'#3e526b')
for x,y in [(5,5),(58,5),(5,58),(58,58)]:
 c.set(x,y,'#e8b867')
for x,y in [(9,11),(49,9),(56,16),(7,41),(53,44),(13,50),(47,51)]:
 c.set(x,y,'#405471')
c.line(30,7,30,11,'#7897a2'); c.line(28,9,32,9,'#7897a2'); c.set(30,9,'#fff0bc')
# custom 5x7 alphabet, doubled to ten pixels wide; compressed vertical grid
letters={
'P':['11110','10001','10001','11110','10000','10000','10000'],
'I':['11111','00100','00100','00100','00100','00100','11111'],
'X':['10001','10001','01010','00100','01010','10001','10001'],
'E':['11111','10000','10000','11110','10000','10000','11111'],
'L':['10000','10000','10000','10000','10000','10000','11111'],
'Q':['01110','10001','10001','10001','10101','10010','01101'],
'U':['10001','10001','10001','10001','10001','10001','01110'],
'S':['01111','10000','10000','01110','00001','00001','11110'],
'T':['11111','00100','00100','00100','00100','00100','00100']}
def title(word,y,colors):
 pixels=[]
 for i,ch in enumerate(word):
  for row,bits in enumerate(letters[ch]):
   for col,v in enumerate(bits):
    if v=='1':
     for dx in range(2):
      for dy in range(2): pixels.append((3+i*12+col*2+dx,y+row*2+dy))
 for x,yy in pixels:
  c.rect(x-1,yy,3,4,'#070e20')
 for x,yy in pixels: c.set(x,yy+2,'#805139' if word=='PIXEL' else '#245363')
 for x,yy in pixels: c.set(x,yy,colors[min((yy-y)//4,len(colors)-1)])
title('PIXEL',16,['#fff1b5','#ffd475','#edaa4e','#cf7e38'])
title('QUEST',34,['#e4fcdd','#a2e6ce','#62baa9','#398b93'])
# tiny invitation and dividers
c.text(17,53,'START','#e5d7b0')
c.poly([(10,54),(12,56),(10,58)],'#e8b867')
c.poly([(53,54),(51,56),(53,58)],'#e8b867')
view(c)
finish(result)
