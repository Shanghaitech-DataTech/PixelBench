# Fruit frequencies, rendered as a compact pixel-art horizontal chart.
# Category labels are sprites; bar lengths share a six-pixel-per-unit scale.
result = new_canvas(128, 64, '#0d1725', name='fruit_chart')
c = result
P = {
    'bg':'#192938', 'edge':'#314454', 'grid':'#2a3c4d',
    'axis':'#6c8390', 'muted':'#8fa3ad', 'num':'#edf2e5',
    'out':'#0c1a25', 'stem':'#9d7950', 'green':'#65aa65', 'leaf':'#a0cc74',
    'red':'#ef5261', 'redlight':'#ff9192', 'redshade':'#b6344e',
    'banana':'#f3c950', 'bananalight':'#ffe994', 'bananashade':'#bc8f36',
    'orange':'#f3953c', 'orangelight':'#ffca77', 'orangeshade':'#bf5e31',
    'lemon':'#e6df55', 'lemonlight':'#ffffa2', 'lemonshade':'#a2aa3c',
    'grape':'#a77cd5', 'grapelight':'#d5aff2', 'grapeshade':'#6f4c9b'
}
# Stepped, one-pixel rim. No title or written category labels.
c.poly([(3,1),(124,1),(126,3),(126,60),(123,63),(4,63),(1,60),(1,3)], P['edge'])
c.poly([(4,2),(123,2),(125,4),(125,60),(123,62),(4,62),(2,60),(2,4)], P['bg'])
# Bottom row is kept open for the ruler's small pixel numerals.
c.rect(4,58,120,5,P['bg'])
c.line(4,63,123,63,P['edge'])

# Grid and shared origin. Major ticks represent 0, 5, 10, and 15.
for gx in (56,86,116):
    for gy in range(4,54,4):
        c.line(gx,gy,gx,gy+1,P['grid'])
c.line(26,4,26,55,P['axis'])
c.line(26,55,116,55,P['axis'])
for v in range(16):
    x=26+6*v
    c.set(x,56,P['axis'] if v%5==0 else P['grid'])

small_digits = {
    '0':['111','101','101','101','111'],
    '1':['010','110','010','010','111'],
    '2':['111','001','111','100','111'],
    '3':['111','001','111','001','111'],
    '4':['101','101','111','001','001'],
    '5':['111','100','111','001','111'],
    '7':['111','001','010','010','010']
}
def tiny_number(x,y,text,col):
    for i,ch in enumerate(text):
        for yy,row in enumerate(small_digits[ch]):
            for xx,z in enumerate(row):
                if z=='1': c.set(x+4*i+xx,y+yy,col)
for x,txt in [(25,'0'),(55,'5'),(83,'10'),(113,'15')]:
    tiny_number(x,58,txt,P['muted'])

rows = [(9,10,'red'), (19,5,'banana'), (29,7,'orange'), (39,14,'lemon'), (49,2,'grape')]
for cy,value,fruit in rows:
    x,y,w=27,cy-3,value*6
    end=x+w-1
    c.rect(x,y,w,7,P[fruit])
    c.line(x,y+6,end,y+6,P[fruit+'shade'])
    c.line(end,y+1,end,y+5,P[fruit+'shade'])
    c.line(x+1,y,end-1,y,P[fruit+'light'])
    # A small restrained specular mark emphasizes the pixel material.
    c.line(x+2,y+1,min(x+7,end-1),y+1,P[fruit+'light'])
    label=str(value)
    label_width=6*len(label)-1
    c.rect(end+3,cy-4,label_width+2,9,P['bg'])
    c.text(end+4,cy-3,label,P['num'],font='5x7')

# Individually authored miniature fruit sprites: 13 px wide, no text labels.
def sprite(x,y,rows,pal):
    for yy,row in enumerate(rows):
        for xx,ch in enumerate(row):
            if ch!='.': c.set(x+xx,y+yy,pal[ch])
common = {'o':P['out'],'t':P['stem'],'g':P['green'],'l':P['leaf']}

sprite(6,4,[
    '......tt.....',
    '......tglg...',
    '...ooootoo...',
    '..orRRoRRro..',
    '.orHHRRRRddo.',
    '.orHRRRRRddo.',
    '.orRRRRRRddo.',
    '..orRRRRddo..',
    '..orRRRddro..',
    '...oororoo...'
],dict(common,R=P['red'],H=P['redlight'],d=P['redshade'],r=P['redshade']))

sprite(6,15,[
    '..........tt.',
    '..........oy.',
    '.........oYyo',
    '.t......oYYyo',
    '.oyo...oYYyo.',
    '..oYYYYYYyo..',
    '...oHHYYyo...',
    '....oyyyo....',
    '.....ooo.....'
],dict(common,Y=P['banana'],H=P['bananalight'],y=P['bananashade']))

sprite(6,24,[
    '.......gg....',
    '.....tlll....',
    '....ootto....',
    '...oRRRRRo...',
    '..oRHHRRRdo..',
    '.oRHRRRRRRdo.',
    '.oRRRRRRdRdo.',
    '.oRRdRRRRddo.',
    '..oRRRRRddo..',
    '...oRddRdo...',
    '....ooooo....'
],dict(common,R=P['orange'],H=P['orangelight'],d=P['orangeshade']))

sprite(5,35,[
    '......ooo......',
    '....ooYYYoo....',
    '...oYHHYYYyo...',
    '..oYHHYYYYyyo..',
    '.oYYYYYYYYyyyto',
    '..oYYYYYYyyyo..',
    '...oyYYYyyyo...',
    '....ooyyyoo....',
    '......ooo......'
],dict(common,Y=P['lemon'],H=P['lemonlight'],y=P['lemonshade']))

sprite(6,44,[
    '......tt.....',
    '...gggtlg....',
    '...gllgg.....',
    '...oo.oo.....',
    '..oHPoHPo....',
    '..oPPoPPo....',
    '...ooHPoo....',
    '..oHPoPPo....',
    '..oPPooo.....',
    '...ooHPo.....',
    '....oPPo.....',
    '.....oo......'
],dict(common,P=P['grape'],H=P['grapelight']))

print(c.stats_text())
print(c.matrix_text(region=(4,2,21,55)))
print(c.matrix_text(region=(24,34,125,44)))
save('fruit_chart',result)
finish(result)
