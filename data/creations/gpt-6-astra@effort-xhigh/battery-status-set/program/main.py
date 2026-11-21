# Four small status sprites, sharing one exact casing design.
result = new_canvas(64, 64, background='#132332', name='battery-status-set')
P = {
    'shadow':'#0b1724', 'edge':'#091520',
    'case':'#a4b8c4', 'light':'#e4f3ed', 'shade':'#5a7488',
    'well':'#203546', 'empty':'#2b4354',
    'green':'#50d68b', 'green_hi':'#a4f3b1', 'green_sh':'#29956d',
    'amber':'#edbf55', 'amber_hi':'#ffe69a', 'amber_sh':'#b58338',
    'red':'#f07870', 'red_hi':'#ffb39b', 'red_sh':'#b54c5c',
    'blue':'#53bce2', 'blue_hi':'#a6e8ed', 'blue_sh':'#327baf',
    'bolt':'#fff1a3', 'bolt_sh':'#f3bc57',
}

def casing(x):
    # Small hard cast shadow, a stepped metal shell and an inset dark well.
    result.rect(x+2, 21, 11, 24, P['shadow'])
    result.rect(x+3, 14, 6, 5, P['edge'])
    result.rect(x+4, 15, 4, 3, P['case'])
    result.line(x+4, 15, x+7, 15, P['light'])
    result.rect(x+1, 18, 10, 26, P['edge'])
    result.rect(x, 19, 12, 24, P['edge'])
    result.rect(x+1, 19, 10, 24, P['case'])
    result.line(x+2, 19, x+9, 19, P['light'])
    result.line(x+1, 20, x+1, 40, P['light'])
    result.line(x+10, 20, x+10, 42, P['shade'])
    result.line(x+2, 42, x+9, 42, P['shade'])
    result.rect(x+2, 20, 8, 21, P['well'])
    for y in (21, 25, 29, 33, 37):
        result.rect(x+3, y, 6, 3, P['empty'])

def bars(x, count, hue):
    for n in range(count):
        y = 37-4*n
        result.rect(x+2, y, 8, 3, P[hue])
        result.line(x+2, y, x+2, y+2, P[hue+'_hi'])
        result.line(x+3, y, x+8, y, P[hue+'_hi'])
        result.line(x+9, y, x+9, y+2, P[hue+'_sh'])

for x,n,hue in [(2,5,'green'),(18,3,'amber'),(34,1,'red'),(50,3,'blue')]:
    casing(x)
    bars(x,n,hue)

# An unmistakable illuminated lightning bolt over the charging cell.
bolt = [(57,22),(52,31),(55,31),(53,38),(60,28),(57,28),(59,22)]
# Clip the bolt and its keyline to the inset, preserving the common casing.
charge = new_canvas(64,64,name='charging-symbol')
for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
    charge.poly([(x+dx,y+dy) for x,y in bolt], P['edge'])
charge.poly(bolt,P['bolt'])
charge.line(54,36,59,29,P['bolt_sh'])
charge.set(57,23,P['light'])
charge.select(52,20,8,21).copy_to(52,20,result,mode='over')

# Compact 3x5 numerals preserve readable percentages at native resolution.
glyphs={
 '0':['111','101','101','101','111'],
 '1':['010','110','010','010','111'],
 '2':['110','001','010','100','111'],
 '6':['011','100','111','101','111'],
 '%':['101','001','010','100','101'],
 'C':['111','100','100','100','111'],
 'H':['101','101','111','101','101'],
 'G':['111','100','101','101','111'],
}
def tiny(x,y,text,col):
    for char in text:
        for j,row in enumerate(glyphs[char]):
            for i,b in enumerate(row):
                if b=='1': result.set(x+i,y+j,col)
        x+=4

tiny(0,49,'100%',P['green_hi'])
tiny(18,49,'60%',P['amber_hi'])
tiny(34,49,'20%',P['red_hi'])
tiny(50,49,'CHG',P['blue_hi'])
view(result, scale=8, margin=0)
save('battery-status-set',result)
finish(result)
