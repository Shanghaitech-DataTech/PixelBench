result = new_canvas(64, 64, background='#111d2e', name='battery_status_set')
# A restrained common housing makes the four states directly comparable.
ink = '#080f1d'
rim = '#7995ac'
light = '#c5dce6'
inside = '#1b2d40'
font = {
 '0':['111','101','101','101','111'],
 '1':['010','110','010','010','111'],
 '2':['111','001','111','100','111'],
 '6':['111','100','111','101','111'],
 '%':['101','001','010','100','101'],
 'C':['111','100','100','100','111'],
 'H':['101','101','111','101','101'],
 'G':['111','100','101','101','111']
}
def tiny(text, x, y, color):
    for ch in text:
        for yy,row in enumerate(font[ch]):
            for xx,p in enumerate(row):
                if p=='1': result.set(x+xx,y+yy,color)
        x+=4

for x, amount, col, hi, shade in [
    (3,20,'#53cc8c','#a0efb3','#2e946f'),
    (18,12,'#efb849','#ffe19a','#bc7e32'),
    (33,4,'#ed6e69','#ffb19a','#b34456'),
    (48,10,'#42b9ce','#8de4e3','#287b9d')]:
    result.rect(x+1,46,11,2,ink)
    # Terminal, identical in all four icons.
    result.rect(x+4,17,5,4,ink)
    result.rect(x+5,17,3,1,light)
    result.rect(x+4,18,5,2,rim)
    # Clipped corners and a cool metal rim.
    result.rect(x+1,20,11,26,ink)
    result.rect(x,21,13,24,ink)
    result.rect(x+2,21,9,24,rim)
    result.rect(x+1,22,11,22,rim)
    result.line(x+2,21,x+10,21,light)
    result.line(x+1,22,x+1,42,light)
    result.rect(x+2,22,9,22,inside)
    # Fill height: exactly 100%, 60%, 20%, and a live partial charge.
    y=43-amount+1
    result.rect(x+3,y,7,amount,col)
    result.line(x+3,y,x+9,y,hi)
    if amount>1:
        result.line(x+9,y+1,x+9,43,shade)
    result.line(x+2,44,x+10,44,'#526f88')

# High-contrast lightning symbol on the active battery.
result.poly([(54,25),(50,33),(53,33),(51,40),(58,30),(55,30),(57,25)], ink)
result.poly([(54,27),(51,32),(54,32),(53,36),(56,31),(54,31),(55,27)], '#ffe58d')
tiny('100%',2,51,'#a0efb3')
tiny('60%',19,51,'#ffe19a')
tiny('20%',34,51,'#ffb19a')
tiny('CHG',49,51,'#8de4e3')
view(result, scale=8)
save('battery-status-set',result)
finish(result)
