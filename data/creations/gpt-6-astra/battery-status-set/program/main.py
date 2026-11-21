result = new_canvas(64,64,background='#111b2b',name='battery-status-set')
c=result
# A shared housing and a precise twenty-pixel charge well.
edge='#080e1b'
rim='#92adc3'
light='#d6e6ef'
well='#24354a'
for x in (2,18,34,50):
    c.rect(x+4,16,4,3,edge)
    c.rect(x+4,16,4,2,rim)
    c.line(x+4,16,x+6,16,light)
    c.rect(x+1,18,10,27,edge)
    c.rect(x,19,12,25,edge)
    c.rect(x+1,19,10,25,rim)
    c.rect(x+2,20,8,23,well)
    c.line(x+2,19,x+9,19,light)
    c.line(x+1,20,x+1,42,light)
    c.line(x+2,43,x+9,43,'#638198')
# Equal wells: 20/20, 12/20, 4/20, and a live charge indicator.
for x,amount,base,shine in [(2,20,'#40c789','#9af0b1'),(18,12,'#e9ae47','#ffe293'),(34,4,'#ed6069','#ffadb0'),(50,10,'#32b8ca','#8ee9e4')]:
    y=42-amount
    c.rect(x+3,y,6,amount,base)
    c.line(x+3,y,x+8,y,shine)
    if amount>2:
        c.line(x+3,y+1,x+3,40,shine)
# Bolt silhouette remains legible over both the filled and empty portions.
c.poly([(57,23),(52,32),(55,32),(53,39),(59,29),(57,29),(59,23)],edge)
c.poly([(57,24),(53,31),(56,31),(54,37),(59,30),(56,30),(58,24)],'#ffe187')
# Tiny, hand-pixelled labels fit their individual 16-pixel columns.
glyphs={
'0':['111','101','101','101','111'],
'1':['010','110','010','010','111'],
'2':['111','001','111','100','111'],
'6':['111','100','111','101','111'],
'%':['101','001','010','100','101'],
'C':['111','100','100','100','111'],
'H':['101','101','111','101','101'],
'G':['111','100','101','101','111']}
def label(x,s,col):
    for ch in s:
        for yy,row in enumerate(glyphs[ch]):
            for xx,v in enumerate(row):
                if v=='1': c.set(x+xx,49+yy,col)
        x+=4
label(0,'100%','#9af0b1')
label(18,'60%','#ffe293')
label(34,'20%','#ffadb0')
label(50,'CHG','#8ee9e4')
view(result)
finish(result)
