result = new_canvas(64, 64, '#101a30', name='pixel_quest')
c = result
# Quiet, stepped frame and a deep inset behind the title.
c.rect(2, 2, 60, 60, '#22324b', fill=False)
c.rect(3, 3, 58, 58, '#142139', fill=False)
for x,y,sx,sy in [(2,2,1,1),(61,2,-1,1),(2,61,1,-1),(61,61,-1,-1)]:
    c.line(x,y,x+6*sx,y,'#476078')
    c.line(x,y,x,y+6*sy,'#476078')
    c.set(x+sx,y+sy,'#72949b')
c.rect(5, 29, 54, 21, '#17243b')
# Tiny compass-star crest.
c.line(31,4,31,10,'#d9b56c')
c.line(28,7,34,7,'#d9b56c')
c.set(31,7,'#fff2c0')
c.set(30,6,'#788d8c'); c.set(32,8,'#788d8c')
c.line(20,7,25,7,'#344960'); c.line(38,7,43,7,'#344960')
# Hand-built condensed lettering for the upper word.
small={
'P':['1110','1001','1001','1110','1000','1000','1000'],
'I':['1111','0110','0110','0110','0110','0110','1111'],
'X':['1001','1001','0110','0110','0110','1001','1001'],
'E':['1111','1000','1000','1110','1000','1000','1111'],
'L':['1000','1000','1000','1000','1000','1000','1111']}
large={
'Q':['01110','11011','11011','11011','11011','01110','00011'],
'U':['11011','11011','11011','11011','11011','11011','01110'],
'E':['11111','11000','11000','11110','11000','11000','11111'],
'S':['01111','11000','11000','01110','00011','00011','11110'],
'T':['11111','00100','00100','00100','00100','00100','00100']}
def letter_pixels(word,font,x,y,scale=2,gap=2):
    points=[]
    for ch in word:
        glyph=font[ch]
        for row,bits in enumerate(glyph):
            for col,bit in enumerate(bits):
                if bit=='1':
                    for dy in range(scale):
                        for dx in range(scale): points.append((x+col*scale+dx,y+row*scale+dy))
        x+=len(glyph[0])*scale+gap
    return points

def title(word,font,x,y,colors):
    pts=letter_pixels(word,font,x,y)
    # Hard pixel extrusion and a one-pixel ink keyline.
    for px,py in pts:
        c.set(px+1,py+2,'#050e22')
    for px,py in pts:
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: c.set(px+dx,py+dy,'#080f22')
    for px,py in pts: c.set(px,py+1,colors[-1])
    for px,py in pts:
        offset=py-y
        col=colors[0] if offset<3 else colors[1] if offset<8 else colors[2] if offset<12 else colors[3]
        c.set(px,py,col)

title('PIXEL',small,8,13,['#e7f4df','#a8d8cf','#68acae','#3d747f'])
title('QUEST',large,3,33,['#fff3bc','#f5cd70','#e7a64d','#bb7038'])
# Small framing diamonds mark the pause between title lines.
for x in [16,47]:
    c.set(x,29,'#b58c58'); c.set(x-1,30,'#665446'); c.set(x+1,30,'#665446'); c.set(x,31,'#b58c58')
c.line(21,30,42,30,'#344960')
# Minimal menu prompt, in a separate five-pixel bitmap style.
mini={
'P':['110','101','110','100','100'], 'R':['110','101','110','101','101'],
'E':['111','100','110','100','111'], 'S':['111','100','111','001','111'],
'T':['111','010','010','010','010'], 'A':['010','101','111','101','101'],
' ':['0','0','0','0','0']}
x=12
for ch in 'PRESS START':
    g=mini[ch]
    for yy,row in enumerate(g):
        for xx,b in enumerate(row):
            if b=='1': c.set(x+xx,54+yy,'#8badb2')
    x+=len(g[0])+1
c.set(7,56,'#f5cd70'); c.set(8,55,'#f5cd70'); c.set(8,56,'#f5cd70'); c.set(8,57,'#f5cd70'); c.set(9,56,'#f5cd70')
view(result)
finish(result)
