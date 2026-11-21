c = new_canvas(64, 64, '#101b2b', name='battery-status-set')
bg = '#101b2b'
shadow = '#09121f'
rim = '#a9c2d5'
light = '#e2edf1'
inside = '#213247'
# A common silhouette and cavity for all four status icons.
for x in (3,18,33,48):
    c.rect(x+2,46,9,1,shadow)
    c.rect(x+4,15,5,4,'#526c85')
    c.rect(x+5,15,3,1,light)
    c.poly([(x+1,18),(x+11,18),(x+12,19),(x+12,43),(x+11,44),(x+1,44),(x,43),(x,19)],rim)
    c.line(x+1,19,x+10,19,light)
    c.line(x+1,20,x+1,41,light)
    c.rect(x+2,20,9,23,inside)
    c.line(x+2,42,x+10,42,'#526c85')
    c.line(x+11,20,x+11,42,'#7591ab')
# 21 usable fill rows; levels are 21, 13 and 4 rows.
for x, h, col, hi in [(3,21,'#39cd87','#8cf0b0'),(18,13,'#e4b951','#ffe291'),(33,4,'#ed6b68','#ffb09a'),(48,11,'#3b93b3','#76ccdc')]:
    y=42-h
    c.rect(x+3,y,7,h,col)
    c.line(x+3,y,x+9,y,hi)
    c.line(x+3,y+1,x+3,41,hi)
# A bright, stepped lightning bolt makes charging identifiable independently of fill.
bolt=[(55,23),(51,31),(54,31),(52,38),(58,29),(55,29),(57,23)]
c.poly([(55,22),(50,31),(50,32),(53,32),(51,39),(53,39),(59,29),(59,28),(57,28),(58,22)],shadow)
c.poly(bolt,'#ffdc64')
c.line(55,24,52,30,'#fff1ae')
# Compact bitmap labels keep every state explicit at native resolution.
glyphs={
'0':['111','101','101','101','111'],
'1':['010','110','010','010','111'],
'2':['111','001','111','100','111'],
'6':['111','100','111','101','111'],
'%':['101','001','010','100','101'],
'C':['111','100','100','100','111'],
'H':['101','101','111','101','101'],
'G':['111','100','101','101','111']}
def label(x,y,s):
    for ch in s:
        for j,row in enumerate(glyphs[ch]):
            for i,v in enumerate(row):
                if v=='1': c.set(x+i,y+j,'#a9c2d5')
        x+=4
label(2,50,'100%')
label(19,50,'60%')
label(34,50,'20%')
label(49,50,'CHG')
print(c.stats_text())
print(c.matrix_text(region=(47,14,61,44)))
save('battery-status-set',c)
finish(c)
