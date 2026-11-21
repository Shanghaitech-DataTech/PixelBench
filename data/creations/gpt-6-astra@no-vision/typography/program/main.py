c = new_canvas(64,64,background='#101626',name='Pixel Quest')
# An inset, quiet midnight frame.
c.rect(1,1,62,62,'#24354c',fill=False)
c.rect(3,3,58,58,'#131d30')
c.poly([(3,51),(12,43),(18,49),(26,40),(36,49),(45,42),(60,52),(60,61),(3,61)],'#19273c')
c.poly([(3,56),(15,50),(24,54),(40,47),(50,54),(60,50),(60,61),(3,61)],'#1d2e43')
for x,y in [(5,5),(58,5),(5,58),(58,58)]:
    c.set(x,y,'#49627a')
for x,y in [(9,10),(54,11),(4,30),(59,28),(10,49),(53,49)]:
    c.set(x,y,'#48627b')
# Small sword crest above the title.
c.line(31,4,31,10,'#d5f3df')
c.line(32,5,32,10,'#6dadae')
c.set(31,3,'#fff1c6')
c.line(28,10,35,10,'#c88b48')
c.line(30,11,33,11,'#6d4e3c')
c.line(31,11,31,12,'#e9bc70')
c.set(31,13,'#c88b48')
c.line(11,8,23,8,'#334b63')
c.line(40,8,52,8,'#334b63')
c.set(10,8,'#89aba9'); c.set(53,8,'#89aba9')
font = {
'P':['11110','10001','10001','11110','10000','10000','10000'],
'I':['111','010','010','010','010','010','111'],
'X':['10001','10001','01010','00100','01010','10001','10001'],
'E':['11111','10000','10000','11110','10000','10000','11111'],
'L':['10000','10000','10000','10000','10000','10000','11111'],
'Q':['01110','10001','10001','10001','10101','10010','01101'],
'U':['10001','10001','10001','10001','10001','10001','01110'],
'S':['01111','10000','10000','01110','00001','00001','11110'],
'T':['11111','00100','00100','00100','00100','00100','00100']}
def title(word,x,y,tones,edge):
    pixels=set()
    for letter in word:
        for yy,row in enumerate(font[letter]):
            for xx,v in enumerate(row):
                if v=='1':
                    for dy in range(2):
                        for dx in range(2): pixels.add((x+xx*2+dx,y+yy*2+dy))
        x+=len(font[letter][0])*2+2
    # Two-pixel extrusion and a crisp one-pixel keyline.
    for px,py in sorted(pixels):
        for dx,dy in [(0,2),(1,2),(0,3),(1,3)]: c.set(px+dx,py+dy,'#080d19')
    for px,py in sorted(pixels): c.set(px+1,py+2,edge)
    for px,py in pixels:
        for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
            if (px+dx,py+dy) not in pixels: c.set(px+dx,py+dy,'#080d19')
    for px,py in pixels:
        shade=tones[min((py-y)//4,len(tones)-1)]
        if (px,py-1) not in pixels: shade=tones[0]
        c.set(px,py,shade)

title('PIXEL',5,16,['#e4f5dc','#a6d6c9','#69adaf','#4b8597'],'#294258')
title('QUEST',3,34,['#fff0b1','#f4c76c','#df954a','#bb633d'],'#733e38')
# The UI line is deliberately much smaller than the title.
small={
'P':['110','101','110','100','100'],
'R':['110','101','110','101','101'],
'E':['111','100','110','100','111'],
'S':['111','100','111','001','111'],
'T':['111','010','010','010','010'],
'A':['010','101','111','101','101'],
' ':['0','0','0','0','0']}
x=11
for letter in 'PRESS START':
    for yy,row in enumerate(small[letter]):
        for xx,v in enumerate(row):
            if v=='1':c.set(x+xx,55+yy,'#a9bdc5')
    x+=len(small[letter][0])+1
# Decorative separators frame the prompt without competing with it.
c.line(23,52,28,52,'#49627a');c.line(35,52,40,52,'#49627a')
c.set(31,51,'#d6ab68');c.line(30,52,32,52,'#f4c76c');c.set(31,53,'#9f704b')
print(c.stats_text())
print(c.matrix_text(region=(0,32,63,49)))
save('pixel_quest',c)
finish(c)
