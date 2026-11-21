result = new_canvas(64, 64, background='#101b2b', name='battery-status-set')
c=result
# Consistent cool-metal housings, with five equal charge units.
for x, count, fill, hi in [(2,5,'#46d68c','#9af0b0'),(18,3,'#e5b750','#ffe08b'),(34,1,'#ee6575','#ffa28e'),(50,3,'#36bccc','#8be5e9')]:
    # Small offset shadow and terminal.
    c.rect(x+1,22,12,24,'#09121f')
    c.rect(x+4,17,4,3,'#8a9faf')
    c.rect(x+4,17,4,1,'#dbe9ec')
    c.poly([(x+1,20),(x+10,20),(x+11,21),(x+11,43),(x+10,44),(x+1,44),(x,43),(x,21)],'#8a9faf')
    c.line(x+1,20,x+10,20,'#e1edf0')
    c.line(x,21,x,42,'#c3d6df')
    c.line(x+2,44,x+9,44,'#586f85')
    c.rect(x+2,22,8,21,'#091421')
    for i in range(5):
        y=39-i*4
        col=fill if i<count else '#24374a'
        c.rect(x+3,y,6,3,col)
        if i<count:
            c.line(x+3,y,x+8,y,hi)
    if x==50:
        # Dark keyline keeps the bolt distinct over both charged and empty cells.
        c.poly([(x+7,24),(x+3,31),(x+2,34),(x+5,34),(x+4,40),(x+10,31),(x+7,31),(x+9,24)],'#081723')
        c.poly([(x+7,25),(x+3,33),(x+6,33),(x+5,37),(x+9,32),(x+6,32),(x+8,25)],'#fff0a1')
# Compact hand-set 3x5 labels keep each status within its own column.
glyphs={
'0':['111','101','101','101','111'],
'1':['010','110','010','010','111'],
'2':['111','001','111','100','111'],
'6':['111','100','111','101','111'],
'%':['101','001','010','100','101'],
'C':['111','100','100','100','111'],
'H':['101','101','111','101','101'],
'G':['111','100','101','101','111']}
def small(text,x,y,color):
    for ch in text:
        for yy,row in enumerate(glyphs[ch]):
            for xx,p in enumerate(row):
                if p=='1': c.set(x+xx,y+yy,color)
        x+=4
small('100%',0,49,'#9af0b0')
small('60%',18,49,'#ffe08b')
small('20%',34,49,'#ffa28e')
small('CHG',50,49,'#8be5e9')
view(result)
finish(result)
